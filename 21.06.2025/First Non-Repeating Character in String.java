public class FirstUniqueChar {
    public static void main(String[] args) {
        String s = "swiss";
        for (int i = 0; i < s.length(); i++) {
            if (s.indexOf(s.charAt(i)) == s.lastIndexOf(s.charAt(i))) {
                System.out.println("First Unique: " + s.charAt(i));
                break;
            }
        }
    }
}
