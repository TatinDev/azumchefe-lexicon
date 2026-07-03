namespace Azumchefe.Application.Interfaces
{
    public interface ICacheService
    {
        /// <summary>
        /// Asynchronously gets the cached object at the specified key.
        /// </summary>
        /// <returns>
        /// The cached object at the specified key. If it was not found, then returns <see langword="null"/>.
        /// </returns>
        Task<T?> GetAsync<T>(string key);

        /// <summary>
        /// Asynchronously caches the specified value at the specified key, with an optional <see cref="TimeSpan"/>
        /// expiration.
        /// </summary>
        /// <returns>
        /// A task that represents the completion of the caching operation.
        /// </returns>
        Task SetAsync<T>(string key, T value, TimeSpan? expiration = null);
    }
}
