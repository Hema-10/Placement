import java.util.Scanner;

public class LoginSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String username = "admin", password = "1234";

        System.out.print("Enter username: ");
        String user = sc.nextLine();
        System.out.print("Enter password: ");
        String pass = sc.nextLine();

        if (user.equals(username) && pass.equals(password))
            System.out.println("Login Successful");
        else
            System.out.println("Invalid Credentials");
    }
}
