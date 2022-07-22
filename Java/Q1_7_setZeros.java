/* #########################################################################################
* Author  : Hong
* Created : 7/20/2022
* Modified: 7/20/2022
* Notes   : [1.7] Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
*                column are set to 0.
 ######################################################################################### */
public class Q1_7_setZeros {
    int[][] sampleMatrix(int m, int n){
        int[][] A = new int[m][n];
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                A[i][j] = (int) (Math.random()*10);
            }
        }
        return A;
    }
    void setZeros(int[][] matrix){
        if (matrix == null || matrix.length < 1) return;
        int m = matrix.length;
        int n = matrix[0].length;

        boolean[] rowBuffer = new boolean[m];
        boolean[] columnBuffer = new boolean[n];

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (matrix[i][j] == 0){
                    rowBuffer[i] = true;
                    columnBuffer[j] = true;
                }
            }
        }
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (rowBuffer[i] || columnBuffer[j]) matrix[i][j] = 0;
            }
        }
    }

    void setZeros2(int[][] matrix){ // Bitwise operation
        if (matrix == null || matrix.length <1) return;
        int m = matrix.length;
        int n = matrix[0].length;

        long checkerRow = 0;
        long checkerColumn = 0;

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (matrix[i][j] == 0 ){
                    checkerRow |= (1 << i);
                    checkerColumn |= (1 << j);
                }
            }
        }
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < m; ++j){
                if ((checkerRow & (1 << i)) > 0 || (checkerColumn & (1 << j)) > 0){
                    matrix[i][j] = 0;
                }
            }

        }
    }
}
/*
import java.util.Arrays;
Q1_7_setZeros q1_7_setZeros = new Q1_7_setZeros();
int[][] A = q1_7_setZeros.sampleMatrix(4,4);
System.out.println(Arrays.deepToString(A));
//q1_7_setZeros.setZeros(A);
q1_7_setZeros.setZeros2(A);
System.out.println(Arrays.deepToString(A));
 */