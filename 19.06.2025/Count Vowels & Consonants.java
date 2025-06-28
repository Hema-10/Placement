public class CountVowels {
    public static void main(String[] args) {
        String s = "Programming";
        int v = 0, c = 0;
        for (char ch : s.toLowerCase().toCharArray()) {
            if ("aeiou".indexOf(ch) >= 0) v++;
            else if (Character.isLetter(ch)) c++;
        }
        System.out.println("Vowels: " + v + ", Consonants: " + c);
    }
}
