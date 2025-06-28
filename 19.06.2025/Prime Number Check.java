public class Prime {
    public static void main(String[] args) {
        int n = 29;
        boolean prime = n > 1;
        for (int i = 2; i <= Math.sqrt(n); i++)
            if (n % i == 0) prime = false;
        System.out.println(prime);
    }
}
