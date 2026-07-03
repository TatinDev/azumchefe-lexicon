namespace Azumchefe.Domain.LexiconService
{
    public class Lexicon
    {
        public string? Id { get; set; }
        public required string Label { get; set; }
        public required string SourceLanguage { get; set; }
        public string? TargetLanguage { get; set; }
        public List<Entry> Entries { get; set; } = [];
    }
}
