using Azumchefe.Application.Interfaces.LexiconService;
using Azumchefe.Domain.LexiconService.Constants.Xml;
using Azumchefe.Infrastructure.LexiconService;
using Microsoft.Extensions.Logging;
using System.Diagnostics;
using System.Xml;

namespace Azumchefe.Infrastructure.LexiconServiceService
{
    public class XmlLexiconIndexService : ILexiconIndexService
    {
        private readonly ILogger<XmlLexiconIndexService> _logger;

        private SortedList<string, HashSet<string>> _index = [];

        private static readonly XmlReaderSettings _settings = XmlReaderSettingsManager.Create();

        public IReadOnlyDictionary<string, HashSet<string>> Index => _index;

        public XmlLexiconIndexService(ILogger<XmlLexiconIndexService> logger)
        {
            _logger = logger;
        }

        // <inheritdoc>
        public async Task UpdateIndexAsync(string path)
        {
            SortedList<string, HashSet<string>> index = [];

            Stopwatch? sw = Stopwatch.StartNew();

            foreach (var file in Directory.GetFiles(path, "*.alex"))
            {
                index = await BuildIndexAsync(file, index);
            }

            _logger.LogInformation("Indexed {index.Count} lexical items", index.Count);

            sw.Stop();
            _logger.LogDebug("UpdateIndexAsync(): Execution time: {ElapsedMilliseconds} ms.", sw.ElapsedMilliseconds);

            _index = index;
        }

        /// <summary>
        /// Asynchronously builds an index upon the specified index, using the specified URI.
        /// </summary>
        /// <returns>A <see cref="SortedList{TKey, TValue}"/> containing the built index.</returns>
        private static async Task<SortedList<string, HashSet<string>>> BuildIndexAsync(
            string path,
            SortedList<string, HashSet<string>> index)
        {
            await using FileStream stream = new(
                path,
                FileMode.Open,
                FileAccess.Read,
                FileShare.Read,
                bufferSize: 65536,
                useAsync: true);

            using XmlReader reader = XmlReader.Create(stream, _settings);

            while (await reader.ReadAsync())
            {
                if (reader.NodeType == XmlNodeType.Element && reader.LocalName == XmlElementLocalName.Entry)
                {
                    var lemma = reader.GetAttribute(XmlAttributeName.EntryLemma)!;

                    // Checks if lemma is already key in index, if it is then creates a HashSet<String> and adds
                    // it to the lemma key's Value to prevent overriding the previous indexation.
                    (index.TryGetValue(lemma, out var cl) ? cl : index[lemma] = []).Add(lemma);

                    while (await reader.ReadAsync())
                    {
                        if (reader.NodeType == XmlNodeType.Element && reader.LocalName == XmlElementLocalName.Form)
                        {
                            if (!bool.Parse(reader.GetAttribute(XmlAttributeName.FormDoNotIndex) ?? "false"))
                            {
                                string form = reader.GetAttribute(XmlAttributeName.FormText)!;

                                // Checks if form is already key in index, if it is then creates a HashSet<String> and adds
                                // it to the form key's Value to prevent overriding the previous indexation.
                                (index.TryGetValue(form, out var fl) ? fl : index[form] = []).Add(lemma);
                            }
                        }
                        if (reader.NodeType == XmlNodeType.EndElement && reader.LocalName == XmlElementLocalName.Entry)
                            break;
                    }
                }
            }

            return index;
        }
    }
}
