using Azumchefe.Domain.LexiconService.Constants.Xml;
using System.Xml.Serialization;

namespace Azumchefe.Domain.LexiconService
{
    [XmlRoot(XmlElementLocalName.Entry, Namespace = "")]
    public class Entry
    {
        [XmlAttribute(XmlAttributeName.EntryLemma)]
        public required string Lemma { get; set; }

        [XmlElement(XmlElementLocalName.Form)]
        public List<Form>? Forms { get; set; }

        [XmlElement(XmlElementLocalName.Sense)]
        public List<Sense>? Senses { get; set; }

        [XmlElement(XmlElementLocalName.SublevelEntry)]
        public List<Entry>? SublevelEntries { get; set; }
    }
}
