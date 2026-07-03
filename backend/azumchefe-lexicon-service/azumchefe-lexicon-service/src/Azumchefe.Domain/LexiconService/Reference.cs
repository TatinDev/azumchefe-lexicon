using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class Reference
    {
        [XmlAttribute(XmlAttributeName.ReferenceIsExternal)]
        public string? IsExternal { get; set; }

        [XmlAttribute(XmlAttributeName.ReferenceEditorialNote)]
        public string? EditorialNote { get; set; }

        [XmlAttribute(XmlAttributeName.ReferenceText)]
        public required string Text { get; set; }
    }
}
