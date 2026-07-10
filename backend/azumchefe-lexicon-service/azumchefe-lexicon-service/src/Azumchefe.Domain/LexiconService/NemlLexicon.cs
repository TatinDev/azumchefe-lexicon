using System.Text.Json.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class NemlLexicon
    {
        [JsonPropertyName("lexicon")]
        public required NemlLexiconData Lexicon { get; set; }
    }

    public class NemlLexiconData
    {
        [JsonPropertyName("language_index")]
        public string? LanguageIndex { get; set; }

        [JsonPropertyName("language_content")]
        public string? LanguageContent { get; set; }

        [JsonPropertyName("article_index")]
        public Dictionary<string, NemlEntry>? ArticleIndex { get; set; }
    }

    public class NemlEntry
    {
        [JsonPropertyName("writtenForm")]
        public string? WrittenForm { get; set; }

        [JsonPropertyName("variants")]
        public List<string>? Variants { get; set; }

        [JsonPropertyName("senses")]
        public List<NemlSense>? Senses { get; set; }
    }

    public class NemlSense
    {
        [JsonPropertyName("partOfSpeech")]
        public string? PartOfSpeech { get; set; }

        [JsonPropertyName("definitions")]
        public List<NemlDefinition>? Definitions { get; set; }

        [JsonPropertyName("examples")]
        public List<NemlExample>? Examples { get; set; }
    }

    public class NemlDefinition
    {
        [JsonPropertyName("definition")]
        public string? Definition { get; set; }
    }

    public class NemlExample
    {
        [JsonPropertyName("example")]
        public string? Example { get; set; }
    }
}
