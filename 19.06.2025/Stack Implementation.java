import java.util.Stack;

public class StackDemo {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(10); s.push(20); s.pop();
        System.out.println(s.peek());
    }
}
