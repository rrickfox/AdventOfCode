using System.Xml;
using _2020.src;
using _2020.Utilities.Bots;

using Spectre.Console;

namespace _2020
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What day to run? (leave empty for all days):");
            string? day = Console.ReadLine();
            if (day == null || day == "")
                RunAll();
            else
                RunSpecific(int.Parse(day));
        }

        public static async void RunAll()
        {
            await Solver.SolveAll();
        }

        public static async void RunSpecific(int day)
        {
            await Solver.SolveSpecific(day);
        }
    }
}