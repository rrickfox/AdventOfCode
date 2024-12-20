using System.Text;

namespace _2020.Utilities
{
    public static partial class Utils
    {
        public static (List<TSource> TruthyValues, List<TSource> FalsyValues) Bifurcate<TSource>(this IEnumerable<TSource> source, Func<TSource, bool> fn)
        {
            if (source == null)
                throw new ArgumentNullException(nameof(source));
            if (fn == null)
                throw new ArgumentNullException(nameof(fn));

            List<TSource> truthyValues = new();
            List<TSource> falsyValues = new();

            foreach (var element in source)
            {
                if (fn(element))
                    truthyValues.Add(element);
                else
                    falsyValues.Add(element);
            }

            return (truthyValues, falsyValues);
        }

        public static string MostCommon(string[] sequence)
            => sequence.GroupBy(v => v)
                    .OrderByDescending(g => g.Count())
                    .First()
                    .Key;

        public static IEnumerable<int> Sequence(int start, int stop)
            => Sequence(start, stop, start < stop ? 1 : -1);

        public static IEnumerable<int> Sequence(int start, int stop, int step)
        {
            int current = start;

            while (step >= 0 ? stop >= current
                             : stop <= current)
            {
                yield return current;
                current += step;
            }
        }

        public static string ToLiteral(this string input)
        {
            StringBuilder literal = new StringBuilder(input.Length + 2);
            literal.Append("\"");
            foreach (var c in input) {
                switch (c) {
                    case '\"': literal.Append("\\\""); break;
                    case '\\': literal.Append(@"\\"); break;
                    case '\0': literal.Append(@"\0"); break;
                    case '\a': literal.Append(@"\a"); break;
                    case '\b': literal.Append(@"\b"); break;
                    case '\f': literal.Append(@"\f"); break;
                    case '\n': literal.Append(@"\n"); break;
                    case '\r': literal.Append(@"\r"); break;
                    case '\t': literal.Append(@"\t"); break;
                    case '\v': literal.Append(@"\v"); break;
                    default:
                        // ASCII printable character
                        if (c >= 0x20 && c <= 0x7e) {
                            literal.Append(c);
                        // As UTF16 escaped character
                        } else {
                            literal.Append(@"\u");
                            literal.Append(((int)c).ToString("x4"));
                        }
                        break;
                }
            }
            literal.Append("\"");
            return literal.ToString();
        }

        public static IEnumerable<(T item, int index)> WithIndex<T>(this IEnumerable<T> source)
        {
            return source.Select((item, index) => (item, index));
        }
    }
}