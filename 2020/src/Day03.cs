using _2020.Utilities;

namespace _2020.src
{
    public class Day03 : BaseDay
    {
        private string[] data;
        private HashSet<Vector2> trees = new HashSet<Vector2>();
        public Day03() : base()
        {
            data = Utils.ToStringArray(RawData);
            for (int y = 0; y < data.Length; y++)
            {
                for (int x = 0; x < data[y].Length; x++)
                {
                    if (data[y][x] == '#')
                        trees.Add(new Vector2(x, y));
                }
            }
            // Console.WriteLine(String.Join(",", trees));
        }

        public override ValueTask<string> Solve1()
        {
            Vector2 pos = new();
            Vector2 move = new Vector2(3, 1);
            int res = 0;

            while (pos.y < data.Length - 1)
            {
                pos += move;
                pos.x %= data[0].Length-1;

                if (trees.Contains(pos))
                    res += 1;
            }

            return new ValueTask<string>(res.ToString());
        }

        public override ValueTask<string> Solve2()
        {
            Vector2[] moves = {new Vector2(1, 1), new Vector2(3, 1), new Vector2(5, 1), new Vector2(7, 1), new Vector2(1, 2)};
            long res = 1;

            foreach (Vector2 move in moves)
            {
                Vector2 pos = new();
                int temp = 0;

                while (pos.y < data.Length - 1)
                {
                    pos += move;
                    pos.x %= data[0].Length-1;

                    if (trees.Contains(pos))
                        temp += 1;
                }

                res *= temp;
            }

            return new ValueTask<string>(res.ToString());
        }
    }
}