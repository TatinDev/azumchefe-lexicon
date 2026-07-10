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

var jsonOptions = new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true,
};

string dictionariesPath = Path.Combine(applicationSettings.LexiconPath, "diccionarios");

app.MapGet("/dictionaries", () =>
{
    var summaries = LoadNemlFiles(dictionariesPath)
        .Select(item => new
        {
            item.Id,
            LanguageIndex = item.Data.Lexicon?.LanguageIndex,
            LanguageContent = item.Data.Lexicon?.LanguageContent,
            EntryCount = item.Data.Lexicon?.ArticleIndex?.Count ?? 0
        });

    return Results.Ok(summaries);
});

app.MapGet("/dictionaries/{id}", (string id) =>
{
    var item = LoadNemlFiles(dictionariesPath)
        .FirstOrDefault(item => item.Id == id);

    if (item.Id is null)
        return Results.NotFound($"The dictionary '{id}' was not found");

    var entries = item.Data.Lexicon?.ArticleIndex?
        .Select(kvp => new
        {
            kvp.Value.WrittenForm,
            Variants = kvp.Value.Variants ?? [],
            Senses = kvp.Value.Senses
        })
        .ToList() ?? [];

    return Results.Ok(new
    {
        item.Id,
        item.Data.Lexicon?.LanguageIndex,
        item.Data.Lexicon?.LanguageContent,
        Entries = entries
    });
});

app.MapGet("/index", () =>
{
    var index = LoadNemlFiles(dictionariesPath)
        .SelectMany(item => item.Data.Lexicon?.ArticleIndex?.Values ?? Enumerable.Empty<NemlEntry>())
        .SelectMany(GetNemlEntryForms)
        .Distinct(StringComparer.OrdinalIgnoreCase)
        .Order(StringComparer.OrdinalIgnoreCase);

    return Results.Ok(index);
});

app.MapGet("/entries/{form}", (string form) =>
{
    var lexicons = LoadNemlFiles(dictionariesPath)
        .Select(item =>
        {
            var matchingEntries = (item.Data.Lexicon?.ArticleIndex ?? [])
                .Where(kvp => EntryMatches(kvp.Value, form))
                .Select(kvp => new
                {
                    kvp.Value.WrittenForm,
                    Variants = kvp.Value.Variants ?? [],
                    Senses = kvp.Value.Senses
                })
                .ToList();

            return new
            {
                item.Id,
                item.Data.Lexicon?.LanguageIndex,
                item.Data.Lexicon?.LanguageContent,
                Entries = matchingEntries
            };
        })
        .Where(item => item.Entries.Count > 0)
        .ToList();

    return lexicons.Count == 0
        ? Results.NotFound($"The given form '{form}' was not present in any lexicon")
        : Results.Ok(lexicons);
});

app.Run();

static IEnumerable<(string Id, NemlLexicon Data)> LoadNemlFiles(string path)
{
    if (!Directory.Exists(path))
        return Enumerable.Empty<(string Id, NemlLexicon Data)>();

    var files = Directory.GetFiles(path, "*.json")
        .Concat(Directory.GetFiles(path, "*.neml"))
        .Order(StringComparer.OrdinalIgnoreCase)
        .ToArray();

    return files.Select(file =>
    {
        var data = JsonSerializer.Deserialize<NemlLexicon>(File.ReadAllText(file), new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        }) ?? throw new InvalidOperationException($"Could not deserialize '{file}'");

        var id = Path.GetFileNameWithoutExtension(file);
        return (Id: id, Data: data);
    });
}

static IEnumerable<string> GetNemlEntryForms(NemlEntry entry)
{
    if (!string.IsNullOrEmpty(entry.WrittenForm))
        yield return entry.WrittenForm;

    foreach (var variant in entry.Variants ?? [])
    {
        if (!string.IsNullOrEmpty(variant))
            yield return variant;
    }
}

static bool EntryMatches(NemlEntry entry, string form)
{
    return GetNemlEntryForms(entry).Any(f => f.Equals(form, StringComparison.OrdinalIgnoreCase));
}
