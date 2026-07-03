using Azumchefe.Application.Interfaces;
using Microsoft.Extensions.Caching.Memory;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace Azumchefe.Infrastructure
{
    public class MemoryCacheService : ICacheService
    {
        private readonly ILogger<MemoryCacheService> _logger;

        private readonly IMemoryCache _cache;

        public MemoryCacheService(IMemoryCache cache, ILogger<MemoryCacheService> logger)
        {
            _cache = cache;
            _logger = logger ?? NullLogger<MemoryCacheService>.Instance;
        }

        //<inheritdoc>
        public Task<T?> GetAsync<T>(string key)
        {
            if (_cache.TryGetValue(key, out T? value))
            {
                _logger.LogDebug("GetAsync(): Retrieved {key} in cache", key);
            }

            return Task.FromResult(value);
        }

        //<inheritdoc>
        public Task SetAsync<T>(string key, T value, TimeSpan? expiration = null)
        {
            var options = new MemoryCacheEntryOptions();

            if (expiration.HasValue)
                options.SetAbsoluteExpiration(expiration.Value);

            _cache.Set(key, value, options);

            _logger.LogDebug("SetAsync(): Cached {key} until {expiration}", key, expiration.ToString());

            return Task.CompletedTask;
        }
    }
}
