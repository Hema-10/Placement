class Bank {
    private String name;
    private double balance;

    public Bank(String name, double balance) {
        this.name = name; this.balance = balance;
    }

    public void deposit(double amt) { balance += amt; }
    public void withdraw(double amt) {
        if (amt <= balance) balance -= amt;
        else System.out.println("Insufficient funds");
    }
    public void display() { System.out.println(name + ": ₹" + balance); }
}

public class BankMain {
    public static void main(String[] args) {
        Bank b = new Bank("Hema", 1000);
        b.deposit(500); b.withdraw(300); b.display();
    }
}
