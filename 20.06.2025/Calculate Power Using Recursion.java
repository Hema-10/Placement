public class Power {
    public static int power(int base, int exp) {
        return (exp == 0) ? 1 : base * power(base, exp - 1);
    }
    public static void main(String[] args) {
        System.out.println(power(2, 5)); // Output: 32
    }
}
