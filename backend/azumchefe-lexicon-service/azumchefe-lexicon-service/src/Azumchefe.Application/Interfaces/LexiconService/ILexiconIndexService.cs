namespace Azumchefe.Application.Interfaces.LexiconService
{
    public interface ILexiconIndexService
    {
        IReadOnlyDictionary<string, HashSet<string>> Index { get; }

        /// <summary>
        /// Asynchronously updates <see cref="Index"/>.
        /// </summary>
        /// <returns>
        /// A task that represents the completion of the update operation.
        /// </returns>
        Task UpdateIndexAsync(string path);
    }
}
