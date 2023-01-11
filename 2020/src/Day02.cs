using _2020.Utilities;

namespace _2020.src
{
    public class Day02 : BaseDay
    {
        private string[] data;

        public Day02() : base()
        {
            data = Utils.ToStringArray(RawData);
        }

        public override ValueTask<string> Solve1()
        {
            int res = 0;

            foreach (string s in data)
            {
                var a = s.Split(": ");
                var pass = a[1];
                var b = a[0].Split(" ");
                var ch = b[1][0];
                var c = b[0].Split("-");
                var min = int.Parse(c[0]);
                var max = int.Parse(c[1]);

                var count = pass.Count(x => x == ch);
                if (count >= min && count <= max)
                    res++;
            }

            return new ValueTask<string>(res.ToString());
        }

        public override ValueTask<string> Solve2()
        {
            
            int res = 0;

            foreach (string s in data)
            {
                var a = s.Split(": ");
                var pass = a[1];
                var b = a[0].Split(" ");
                var ch = b[1][0];
                var c = b[0].Split("-");
                var left = int.Parse(c[0]);
                var right = int.Parse(c[1]);

                if (pass[left-1] == ch ^ pass[right-1] == ch)
                    res++;
            }

            return new ValueTask<string>(res.ToString());
        }
    }
}