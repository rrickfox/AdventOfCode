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

        public override bool Equals(object? obj) => this.Equals(obj as Vector2);
        public override int GetHashCode() => (x, y).GetHashCode();

        public bool Equals(Vector2? p)
        {
            if (p is null)
            {
                return false;
            }

            // Optimization for a common success case.
            if (Object.ReferenceEquals(this, p))
            {
                return true;
            }

            // If run-time types are not exactly the same, return false.
            if (this.GetType() != p.GetType())
            {
                return false;
            }

            // Return true if the fields match.
            // Note that the base class is not invoked because it is
            // System.Object, which defines Equals as reference equality.
            return (x == p.x) && (x == p.x);
        }

        public static bool operator ==(Vector2? lhs, Vector2? rhs)
        {
            if (lhs is null)
            {
                if (rhs is null)
                {
                    return true;
                }

                // Only the left side is null.
                return false;
            }
            // Equals handles case of null on right side.
            return lhs.Equals(rhs);
        }
        public static bool operator !=(Vector2? lhs, Vector2? rhs) => !(lhs == rhs);

        public override string ToString()
        {
            return $"({x}, {y})";
        }

        public double Length() => Math.Sqrt(x*x + y*y);
    }
}