public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int a = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Division by zero error.");
        } finally {
            System.out.println("End of program.");
        }
    }
}
