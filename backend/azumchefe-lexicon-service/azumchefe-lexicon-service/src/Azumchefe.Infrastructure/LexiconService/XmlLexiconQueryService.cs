using Azumchefe.Application.Interfaces.LexiconService;
using Azumchefe.Domain.LexiconService;
using Azumchefe.Domain.LexiconService.Constants.Xml;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Infrastructure.LexiconService
{
    public class XmlLexiconQueryService : ILexiconQueryService
    {
        private readonly ILogger<XmlLexiconQueryService> _logger;

        private static readonly XmlReaderSettings _settings = XmlReaderSettingsManager.CreateIgnoreValidation();

        private static readonly XmlSerializer _entrySerializer = new(typeof(Entry));

        public XmlLexiconQueryService(ILogger<XmlLexiconQueryService> logger)
        {
            _logger = logger;
        }

        //<inheritdoc>
        public async Task<List<Lexicon>?> GetAllLexiconsEntriesByLemmasAsync(string path, HashSet<string> lemmas)
        {
            List<Lexicon> lexicons = [];

            _logger.LogDebug("GetAllLexiconsEntriesByLemmasAsync(): Read {_path}", path);
            Stopwatch? sw = Stopwatch.StartNew();

            foreach (var file in Directory.GetFiles(path, "*.alex"))
            {
                var lexicon = await GetAllLexiconEntriesByLemmasAsync(file, lemmas);

                _logger.LogDebug("GetAllLexiconsEntriesByLemmasAsync(): Read {file}", file);

                if (lexicon != null) lexicons.Add(lexicon);
            }

            sw.Stop();
            _logger.LogDebug("GetAllLexiconsEntriesByLemmasAsync(): Execution time: {ElapsedMilliseconds} ms.", sw.ElapsedMilliseconds);

            return lexicons;
        }

        /// <summary>
        /// Asynchronously gets all lexical entries at the specified URI that match any lemma from the specified 
        /// <see cref="HashSet{T}"/> lemmas.
        /// </summary>
        /// <returns>
        /// A <see cref="Domain.LexiconService.Lexicon"/> instance containing all matching <see cref="Entry"/>.
        /// If none are found, then returns <see langword="null"/>.
        /// </returns>
        private static async Task<Lexicon?> GetAllLexiconEntriesByLemmasAsync(string path, HashSet<string> lemmas)
        {
            await using FileStream stream = new(
                path,
                FileMode.Open,
                FileAccess.Read,
                FileShare.Read,
                bufferSize: 65536,
                useAsync: true);

            using XmlReader reader = XmlReader.Create(stream, _settings);

            await reader.MoveToContentAsync();

            Lexicon lexicon = new()
            {
                Label = reader.GetAttribute(XmlAttributeName.LexiconLabel)!,
                SourceLanguage = reader.GetAttribute(XmlAttributeName.LexiconSourceLanguage)!,
                TargetLanguage = reader.GetAttribute(XmlAttributeName.LexiconTargetLanguage)
            };

            while (await reader.ReadAsync())
            {
                if (reader.NodeType != XmlNodeType.Element)
                    continue;

                if (reader.LocalName != XmlElementLocalName.Entry)
                    continue;

                var lemma = reader.GetAttribute(XmlAttributeName.EntryLemma);

                if (lemma is null || !lemmas.Contains(lemma))
                    continue;

                using var subtreeReader = reader.ReadSubtree();

                subtreeReader.MoveToContent();

                if (_entrySerializer.Deserialize(subtreeReader) is Entry entry)
                {
                    lexicon.Entries.Add(entry);
                }
            }

            // If found nothing, discard.
            return lexicon.Entries.Count > 0 ? lexicon : null;
        }
    }
}
