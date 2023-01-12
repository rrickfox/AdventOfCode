using _2020.Utilities;

namespace _2020.src
{
    public class Day05 : BaseDay
    {
        private HashSet<Tuple<int, int>> data = new();
        public Day05() : base()
        {
            var t = Utils.ToStringArray(RawData);

            foreach (var elem in t)
            {
                int left = 1;
                int right = 128;

                foreach (var c in elem.Take(7))
                {
                    if (c == 'F')
                        right -= (right - left + 1)/2;
                    if (c == 'B')
                        left += (right - left + 1)/2;
                }
                var row = right - 1;

                left = 1;
                right = 8;

                foreach (var c in elem.Skip(7))
                {
                    if (c == 'L')
                        right -= (right - left + 1)/2;
                    if (c == 'R')
                        left += (right - left + 1)/2;
                }
                var col = right - 1;

                data.Add(new Tuple<int, int>(row, col));
            }
        }

        public override ValueTask<string> Solve1()
        {
            int max = 0;

            foreach (var elem in data)
            {
                var val = elem.Item1 * 8 + elem.Item2;
                if (val > max)
                    max = val;
            }

            return new ValueTask<string>(max.ToString());
        }

        public override ValueTask<string> Solve2()
        {
            int ret = 0;

            foreach (var y in Utils.Sequence(0, 127))
                foreach (var x in Utils.Sequence(0, 7))
                    if (!data.Contains(new Tuple<int, int>(y, x)) && data.Contains(new Tuple<int, int>(y-1, x)) && data.Contains(new Tuple<int, int>(y+1, x)) && data.Contains(new Tuple<int, int>(y, x-1)) && data.Contains(new Tuple<int, int>(y, x+1)))
                        ret = y * 8 + x;

            return new ValueTask<string>(ret.ToString());
        }
    }
}