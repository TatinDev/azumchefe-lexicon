using System.Reflection;
using System.Xml;
using System.Xml.Schema;

namespace Azumchefe.Infrastructure.LexiconService
{
    internal static class XmlReaderSettingsManager
    {
        private const string _xsdPath = "Azumchefe.Infrastructure.LexiconService.Schemas.lexicon.xsd";
        private static readonly XmlSchemaSet Schemas;

        static XmlReaderSettingsManager()
        {
            Schemas = new XmlSchemaSet();
            var assembly = Assembly.GetExecutingAssembly();

            using var stream = assembly.GetManifestResourceStream(_xsdPath)
                ?? throw new InvalidOperationException($"The schema '{_xsdPath}' was not found.");
            using var reader = XmlReader.Create(stream);
            Schemas.Add(null, reader);
        }

        public static XmlReaderSettings Create()
        {
            var settings = new XmlReaderSettings
            {
                Async = true,
                IgnoreComments = true,
                IgnoreWhitespace = true,
                DtdProcessing = DtdProcessing.Ignore,
                Schemas = Schemas,
                ValidationType = ValidationType.Schema
            };

            settings.ValidationEventHandler += (sender, exception) =>
            {
                if (exception.Severity == XmlSeverityType.Error)
                    throw new XmlSchemaValidationException(exception.Message);
            };

            return settings;
        }

        public static XmlReaderSettings CreateIgnoreValidation()
        {
            return new XmlReaderSettings
            {
                Async = true,
                IgnoreComments = true,
                IgnoreWhitespace = true,
                DtdProcessing = DtdProcessing.Ignore
            };
        }
    }
}