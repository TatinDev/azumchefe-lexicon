using Azumchefe.Application.Interfaces.LexiconService;
using Azumchefe.Infrastructure.LexiconServiceService;
using Microsoft.Extensions.DependencyInjection;

namespace Azumchefe.Infrastructure.LexiconService
{
    public static class XmlLexiconServiceCollectionExtensions
    {
        /// <summary>
        /// Adds an XML-based implementation of <see cref="ILexiconIndexService"/> and <see cref="ILexiconQueryService"/> to the 
        /// <see cref="IServiceCollection"/>.
        /// </summary>
        /// <returns>The <see cref="IServiceCollection"/> so that additional calls can be chained.</returns>
        public static IServiceCollection AddXmlLexiconServices(this IServiceCollection services)
        {
            services.AddSingleton<ILexiconIndexService, XmlLexiconIndexService>();
            services.AddScoped<ILexiconQueryService, XmlLexiconQueryService>();

            return services;
        }
    }
}
