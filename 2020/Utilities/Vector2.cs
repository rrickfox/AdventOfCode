namespace _2020.Utilities
{
    public class Vector2
    {
        public int x;
        public int y;

        public Vector2(int x = 0, int y = 0)
        {
            this.x = x;
            this.y = y;
        }

        public static Vector2 operator +(Vector2 a) => a;
        public static Vector2 operator -(Vector2 a) => new Vector2(-a.x, -a.y);
        public static Vector2 operator +(Vector2 a, Vector2 b) => new Vector2(a.x + b.x, a.y + b.y);
        public static Vector2 operator -(Vector2 a, Vector2 b) => a + (-b);

        public double Length() => Math.Sqrt(x*x + y*y);
    }
}