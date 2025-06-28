public class MatrixTranspose {
    public static void main(String[] args) {
        int[][] mat = { {1, 2, 3}, {4, 5, 6} };
        int rows = mat.length, cols = mat[0].length;

        for (int i = 0; i < cols; i++) {
            for (int j = 0; j < rows; j++)
                System.out.print(mat[j][i] + " ");
            System.out.println();
        }
    }
}
