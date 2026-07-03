using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class Form
    {
        [XmlAttribute(XmlAttributeName.FormDoNotIndex)]
        public string? DoNotIndex { get; set; }

        [XmlAttribute(XmlAttributeName.FormEditorialNote)]
        public string? EditorialNote { get; set; }

        [XmlAttribute(XmlAttributeName.FormText)]
        public required string Text { get; set; }
    }
}