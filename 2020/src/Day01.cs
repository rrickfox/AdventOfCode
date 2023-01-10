using _2020.Utilities;

namespace _2020.src
{
    public class Day01 : BaseDay
    {
        private int[] data;
        public Day01() : base()
        {
            data = Utils.ToIntArray(this.RawData);
        }

        public override ValueTask<string> Solve1()
        {
            foreach (var v in data)
            {
                var l = data.Where(x => v + x == 2020);
                if (l.Count() > 0)
                    return new ValueTask<string>((v * l.First()).ToString());
            }
            return new ValueTask<string>("");
        }

        public override ValueTask<string> Solve2()
        {
            foreach (var v in data)
            {
                foreach (var w in data)
                {
                    var l = data.Where(x => v + w + x == 2020);
                    if (l.Count() > 0)
                        return new ValueTask<string>((v * w * l.First()).ToString());
                }
            }
            return new ValueTask<string>("");
        }
    }
}