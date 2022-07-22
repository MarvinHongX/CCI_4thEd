/* #########################################################################################
* Author  : Hong
* Created : 7/20/2022
* Modified: 7/20/2022
* Notes   : [1.6] Given an image represented by an NxN matrix, where each pixel in the image is 4
*                bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
 ######################################################################################### */
public class Q1_6_rotate {
    int[][] sampleMatrix(int m, int n){
        int maxLen = (m > n) ? m : n;
        int[][] A = new int[maxLen][maxLen];
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                A[i][j] = (int) (Math.random() * 100);
            }
        }
        return A;
    }

    int axialSymmetryIndex(int len, int index){
        return len - 1 - index;
    }
    int[][] rotate90(int[][] matrix){ // Clockwise 90
        if (matrix == null || matrix.length < 1) return matrix;

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] result = new int[n][m]; // n by m matrix
        for (int i = 0; i < m; ++i){
            int sym_i = axialSymmetryIndex(m, i);
            for (int j = 0; j < n; ++j){
                result[j][sym_i] = matrix[i][j];
            }
        }
        return result;
    }

    int[][] rotate180(int[][] matrix){  // Clockwise 180
        if (matrix == null || matrix.length < 1) return matrix;

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] result = new int[m][n]; // m by n matrix
        for (int i = 0; i < m; ++i){
            int sym_i = axialSymmetryIndex(m, i);
            for (int j = 0; j < n; ++j){
                int sym_j = axialSymmetryIndex(n, j);
                result[sym_i][sym_j] = matrix[i][j];
            }
        }
        return result;
    }

    int[][] rotate270(int[][] matrix){  // Clockwise 270
        if (matrix == null || matrix.length < 1) return matrix;

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] result = new int[n][m]; // n by m matrix
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                int sym_j = axialSymmetryIndex(n, j);
                result[sym_j][i] = matrix[i][j];
            }
        }
        return result;
    }

    void rotateInPlace90(int[][] matrix){  // In place, clockwise 90
        if (matrix == null || matrix.length < 1) return;
        int m = matrix.length;
        int n = matrix[0].length;
        if (m != n) return; // only n by n matrix

        for (int i = 0; i < m/2; ++i) {
            int sym_i = axialSymmetryIndex(m, i);
            for (int j = i; j < sym_i; ++j) {
                int sym_j = axialSymmetryIndex(n, j);
                int buffer = matrix[i][j]; // 0 degree -> buffer
                matrix[i][j] = matrix[sym_j][i]; // -90 degree -> 0 degree
                matrix[sym_j][i] = matrix[sym_i][sym_j]; // -180 degree -> -90 degree
                matrix[sym_i][sym_j] = matrix[j][sym_i]; // -270 degree -> -180 degree
                matrix[j][sym_i] = buffer; // buffer -> -270degree
            }
        }
    }
}
/*
import java.util.Arrays;
Q1_6_rotate q1_6_rotate = new Q1_6_rotate();
int[][] A = q1_6_rotate.sampleMatrix(3,2);
System.out.println(Arrays.deepToString(A));

System.out.println(Arrays.deepToString(q1_6_rotate.rotate90(A)));
System.out.println(Arrays.deepToString(q1_6_rotate.rotate180(A)));
System.out.println(Arrays.deepToString(q1_6_rotate.rotate270(A)));
q1_6_rotate.rotateInPlace90(A);
System.out.println(Arrays.deepToString(A));
 */
