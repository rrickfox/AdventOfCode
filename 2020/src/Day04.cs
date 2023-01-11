using System.Text.RegularExpressions;
using _2020.Utilities;

namespace _2020.src
{
    public class Day04 : BaseDay
    {
        private string[] data;
        private List<Dictionary<string, string>> fields = new();
        public Day04() : base()
        {
            data = Utils.ToStringArray(RawData, "\n\n");
            for (int i = 0; i < data.Length; i++)
                data[i] = data[i].Replace("\n", " ");

            foreach (string s in data)
            {
                var dict = new Dictionary<string, string>();

                var l = s.Split(" ");
                foreach (string elem in l)
                {
                    var temp = elem.Split(":");
                    dict.Add(temp[0], temp[1]);
                }

                fields.Add(dict);
            }
        }

        public override ValueTask<string> Solve1()
        {
            int res = 0;

            foreach (var dict in fields)
            {
                if (dict.Keys.Count == (dict.Keys.Contains("cid") ? 8 : 7))
                    res += 1;
            }

            return new ValueTask<string>(res.ToString());
        }

        public override ValueTask<string> Solve2()
        {
            int res = 0;

            var fourDigits = new Regex(@"^[0-9]{4}$");
            var height = new Regex(@"^([0-9]+)(cm|in)$");
            var hair = new Regex(@"^#[0-9a-f]{6}$");
            var eye = new Regex(@"^(amb|blu|brn|gry|grn|hzl|oth)$");
            var pid = new Regex(@"^[0-9]{9}$");

            foreach (var (dict, index) in fields.WithIndex())
            {
                if (!dict.ContainsKey("byr") || !fourDigits.IsMatch(dict["byr"]) || !(int.Parse(dict["byr"]) >= 1920) || !(int.Parse(dict["byr"]) <= 2002))
                    continue;

                if (!dict.ContainsKey("iyr") || !fourDigits.IsMatch(dict["iyr"]) || !(int.Parse(dict["iyr"]) >= 2010) || !(int.Parse(dict["iyr"]) <= 2020))
                    continue;

                if (!dict.ContainsKey("eyr") || !fourDigits.IsMatch(dict["eyr"]) || !(int.Parse(dict["eyr"]) >= 2020) || !(int.Parse(dict["eyr"]) <= 2030))
                    continue;

                if (!dict.ContainsKey("hgt") || !height.IsMatch(dict["hgt"]))
                    continue;
                else
                {
                    var matches = height.Match(dict["hgt"]).Groups;
                    if (matches[2].Value == "cm" && !(int.Parse(matches[1].Value) >= 150 && int.Parse(matches[1].Value) <= 193))
                        continue;
                    if (matches[2].Value == "in" && !(int.Parse(matches[1].Value) >= 59 && int.Parse(matches[1].Value) <= 76))
                        continue;
                }

                if (!dict.ContainsKey("hcl") || !hair.IsMatch(dict["hcl"]))
                    continue;

                if (!dict.ContainsKey("ecl") || !eye.IsMatch(dict["ecl"]))
                    continue;

                if (!dict.ContainsKey("pid") || !pid.IsMatch(dict["pid"]))
                    continue;

                res++;
            }

            return new ValueTask<string>(res.ToString());
        }
    }
}