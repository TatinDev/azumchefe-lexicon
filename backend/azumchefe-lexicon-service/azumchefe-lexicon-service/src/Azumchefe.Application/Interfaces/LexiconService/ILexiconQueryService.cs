using Azumchefe.Domain.LexiconService;

namespace Azumchefe.Application.Interfaces.LexiconService
{
    public interface ILexiconQueryService
    {
        /// <summary>
        /// Asynchronously gets all lexical entries from all lexicons that match any lemma from the specified
        /// <see cref="HashSet{T}"/> lemmas.
        /// </summary>
        /// <param name="lemmas">Set of lemmas to retrieve from lexical entries in all lexicons.</param>
        /// <returns>A <see cref="List{T}"/> of <see cref="Lexicon"/> instances containing all matching 
        /// <see cref="Entry"/>. If none are found, then returns <see langword="null"/>.</returns>
        Task<List<Domain.LexiconService.Lexicon>?> GetAllLexiconsEntriesByLemmasAsync(string path, HashSet<string> lemmas);
    }
}
