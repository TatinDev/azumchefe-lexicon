using System.ComponentModel.DataAnnotations;

namespace Azumchefe.Application
{
    public class ApplicationSettings
    {
        [Required]
        public string LexiconPath { get; set; } = String.Empty;
        [Range(1, 8760)]
        public int CacheHoursToExpire { get; set; }
    }
}
