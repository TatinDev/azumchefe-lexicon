using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class Definition
    {
        [XmlAttribute(XmlAttributeName.DefinitionEditorialNote)]
        public string? EditorialNote { get; set; }

        [XmlAttribute(XmlAttributeName.DefinitionText)]
        public string? Text { get; set; }

        [XmlElement(XmlElementLocalName.Reference)]
        public List<Reference>? References { get; set; }

        [XmlElement(XmlElementLocalName.Example)]
        public List<Quote>? Quotes { get; set; }
    }
}