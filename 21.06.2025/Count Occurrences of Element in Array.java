public class CountOccurrence {
    public static void main(String[] args) {
        int[] arr = {1, 3, 3, 3, 5, 7};
        int target = 3, count = 0;
        for (int n : arr)
            if (n == target) count++;
        System.out.println("Count: " + count);
    }
}
