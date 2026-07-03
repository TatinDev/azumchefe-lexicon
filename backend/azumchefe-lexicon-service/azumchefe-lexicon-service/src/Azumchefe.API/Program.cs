using Azumchefe.Application;
using Azumchefe.Domain.LexiconService;
using Azumchefe.Infrastructure;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);

var applicationSettings = builder.Configuration
    .GetValidatedAnnotatedSection<ApplicationSettings>("Azumchefe");

builder.Services.AddSingleton(applicationSettings);

builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.SetIsOriginAllowed(origin => origin.StartsWith("http://localhost"))
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.DefaultIgnoreCondition =
        System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull;
    options.SerializerOptions.PropertyNameCaseInsensitive = true;
});

var app = builder.Build();

app.UseCors();

var lexiconJsonOptions = new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true,
};

string dictionariesPath = Path.Combine(applicationSettings.LexiconPath, "diccionarios");

app.MapGet("/dictionaries", () =>
{
    var summaries = LoadLexicons(dictionariesPath, lexiconJsonOptions)
        .Select(lexicon => new
        {
            lexicon.Id,
            lexicon.Label,
            lexicon.SourceLanguage,
            lexicon.TargetLanguage,
            EntryCount = lexicon.Entries.Count,
        });

    return Results.Ok(summaries);
});

app.MapGet("/dictionaries/{id}", (string id) =>
{
    var lexicon = LoadLexicons(dictionariesPath, lexiconJsonOptions)
        .FirstOrDefault(lexicon => lexicon.Id == id);

    return lexicon is null
        ? Results.NotFound($"The dictionary '{id}' was not found")
        : Results.Ok(lexicon);
});

app.MapGet("/index", () =>
{
    var index = LoadLexicons(dictionariesPath, lexiconJsonOptions)
        .SelectMany(lexicon => lexicon.Entries)
        .SelectMany(GetEntryForms)
        .Distinct(StringComparer.OrdinalIgnoreCase)
        .Order(StringComparer.OrdinalIgnoreCase);

    return Results.Ok(index);
});

app.MapGet("/entries/{form}", (string form) =>
{
    var lexicons = LoadLexicons(dictionariesPath, lexiconJsonOptions)
        .Select(lexicon => new Lexicon
        {
            Id = lexicon.Id,
            Label = lexicon.Label,
            SourceLanguage = lexicon.SourceLanguage,
            TargetLanguage = lexicon.TargetLanguage,
            Entries = lexicon.Entries.Where(entry => EntryMatches(entry, form)).ToList(),
        })
        .Where(lexicon => lexicon.Entries.Count > 0)
        .ToList();

    return lexicons.Count == 0
        ? Results.NotFound($"The given form '{form}' was not present in any lexicon")
        : Results.Ok(lexicons);
});

app.Run();

static IEnumerable<Lexicon> LoadLexicons(string path, JsonSerializerOptions options)
{
    if (!Directory.Exists(path))
        return [];

    return Directory.GetFiles(path, "*.json")
        .Order(StringComparer.OrdinalIgnoreCase)
        .Select(file =>
        {
            var lexicon = JsonSerializer.Deserialize<Lexicon>(File.ReadAllText(file), options)
                ?? throw new InvalidOperationException($"Could not deserialize '{file}'");

            lexicon.Id ??= Path.GetFileNameWithoutExtension(file);

            return lexicon;
        });
}

static IEnumerable<string> GetEntryForms(Entry entry)
{
    yield return entry.Lemma;

    foreach (var form in entry.Forms ?? [])
    {
        if (form.DoNotIndex != "true")
            yield return form.Text;
    }

    foreach (var sublevelEntry in entry.SublevelEntries ?? [])
    {
        foreach (var form in GetEntryForms(sublevelEntry))
            yield return form;
    }
}

static bool EntryMatches(Entry entry, string form) =>
    GetEntryForms(entry).Any(entryForm => entryForm.Equals(form, StringComparison.OrdinalIgnoreCase));
