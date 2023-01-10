using _2020.Utilities.Bots;

namespace _2020.Utilities
{
    public abstract class BaseDay
    {
        protected virtual string ClassPrefix { get; } = "Day";
        protected string InputFileDirPath { get; } = "Data/";
        protected int Year { get; set; } = 2020;
        public string RawData { get; set; }

        protected BaseDay()
        { 
            RawData = DataBot.LoadData((int)GetIndex(), Year, InputFileDirPath);
        }

        public virtual uint GetIndex()
        {
            var typeName = GetType().Name;

            return uint.TryParse(typeName[(typeName.IndexOf(ClassPrefix) + ClassPrefix.Length)..].TrimStart('_'), out var index)
                ? index
                : default;
        }

        public abstract ValueTask<string> Solve1();
        public abstract ValueTask<string> Solve2();
    }
}
