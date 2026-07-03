using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    public class Sense
    {
        [XmlAttribute(XmlAttributeName.SensePartOfSpeech)]
        public string? PartOfSpeech { get; set; }

        [XmlAttribute(XmlAttributeName.SenseGeographicalMark)]
        public string? GeographicalMark { get; set; }

        [XmlAttribute(XmlAttributeName.SenseRestrictionMark)]
        public string? RestrictionMark { get; set; }

        [XmlAttribute(XmlAttributeName.SenseEditorialNote)]
        public string? EditorialNote { get; set; }

        [XmlElement(XmlElementLocalName.Reference)]
        public List<Reference>? References { get; set; }

        [XmlElement(XmlElementLocalName.Definition)]
        public List<Definition>? Definitions { get; set; }
    }
}