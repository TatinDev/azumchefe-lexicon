using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class Quote
    {
        [XmlAttribute(XmlAttributeName.ExampleTargetLanguageText)]
        public string? TargetLanguageText { get; set; }

        [XmlAttribute(XmlAttributeName.ExampleAuthor)]
        public string? Author { get; set; }

        [XmlAttribute(XmlAttributeName.ExampleText)]
        public required string Text { get; set; }
    }
}