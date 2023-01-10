using _2020.Utilities;

namespace _2020.src
{
    public class BlankDay : BaseDay
    {
        public BlankDay() : base()
        {
        }

        public override ValueTask<string> Solve1()
        {
            return new ValueTask<string>("");
        }

        public override ValueTask<string> Solve2()
        {
            return new ValueTask<string>("");
        }
    }
}