using Microsoft.Extensions.Configuration;
using System.ComponentModel.DataAnnotations;

namespace Azumchefe.Infrastructure
{
    public static class ConfigurationExtensions
    {
        /// <summary>
        /// Gets a configuration section to a strongly-typed annotated object of type <typeparamref name="T"/> and validates it.
        /// </summary>
        /// <returns>An instance of <typeparamref name="T"/> populated with values from the configuration section.</returns>
        public static T GetValidatedAnnotatedSection<T>(this IConfiguration configuration, string sectionName) where T : class
        {
            var settings = configuration.GetSection(sectionName).Get<T>()
                ?? throw new InvalidOperationException();

            Validator.ValidateObject(settings, new ValidationContext(settings), validateAllProperties: true);

            return settings;
        }
    }
}
