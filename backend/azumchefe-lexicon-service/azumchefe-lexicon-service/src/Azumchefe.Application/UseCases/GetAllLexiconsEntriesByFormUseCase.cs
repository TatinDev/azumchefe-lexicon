using Azumchefe.Application.Interfaces;
using Azumchefe.Application.Interfaces.LexiconService;
using Azumchefe.Domain.LexiconService;

namespace Azumchefe.Application.UseCases
{
    public class GetAllLexiconsEntriesByFormUseCase
    {
        private readonly ILexiconIndexService _lexiconIndex;
        private readonly ILexiconQueryService _lexiconQuery;
        private readonly ICacheService _cache;
        private readonly ApplicationSettings _settings;

        public GetAllLexiconsEntriesByFormUseCase(
            ILexiconIndexService lexiconIndex,
            ILexiconQueryService lexiconQuery,
            ICacheService cache,
            ApplicationSettings settings)
        {
            _lexiconIndex = lexiconIndex;
            _lexiconQuery = lexiconQuery;
            _cache = cache;
            _settings = settings;
        }

        /// <summary>
        /// Asynchronously gets all <see cref="Lexicon"/> that have the specified form.
        /// </summary>
        /// <returns>A <see cref="List{T}"/> of <see cref="Lexicon"/> instances containing all matching 
        /// <see cref="Entry"/>. If none are found, then returns <see langword="null"/>.</returns>
        public async Task<List<Lexicon>?> ExecuteAsync(string form)
        {
            // Check if it's in index.
            if (!_lexiconIndex.Index.TryGetValue(form, out var lemmas))
                throw new KeyNotFoundException();

            // Assign cache key to queried form.
            string cacheKey = $"form:{form}";

            // Check if it's in cache.
            var cached = await _cache.GetAsync<List<Lexicon>?>(cacheKey);

            if (cached != null)
                return cached;

            // If cached is null.
            var lexicons = await _lexiconQuery.GetAllLexiconsEntriesByLemmasAsync(_settings.LexiconPath, lemmas);

            await _cache.SetAsync(cacheKey, lexicons, TimeSpan.FromHours(_settings.CacheHoursToExpire));

            return lexicons;
        }
    }
}
