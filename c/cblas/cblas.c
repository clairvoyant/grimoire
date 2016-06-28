#include <cblas.h>
#include <stdio.h>

  /***
   * gemm multiplies matrix 
   *
   *     C = C := alpha*op(A)*op(B) + beta*C
   *
   *
   *  cblas_dgemm (const CBLAS_LAYOUT Layout, 
   *               const CBLAS_TRANSPOSE transa, 
   *               const CBLAS_TRANSPOSE transb, 
   *                     const MKL_INT m,
   *                     const MKL_INT n,
   *                     const MKL_INT k,
   *                     const double alpha,
   *                     const double *a,
   *                     const MKL_INT lda,
   *                     const double *b,
   *                     const MKL_INT ldb,
   *                     const double beta,
   *                     double *c,
   *                     const MKL_INT ldc); 
   *
   *    Layout:         CblasRowMajor or CblasColMajor
   *    transa, transb: If the matrix shall be transpose before.
   *    op(A) is an m-by-k matrix,
   *    op(B) is a k-by-n matrix,
   *    C is an m-by-n matrix. 
   *
   *    lda: lenght of the row in row order and column in column order.
   *    ldb: lenght of the row in row order and column in column order.
   *    ldc: lenght of the row in row order and column in column order.
   *
   *    Take care that 
   *        - Fortran: memory layout is usually column order. 
   *        - C:       memory layout is usually row  order.
   */
 
/* 
 * This code is an example of blas a*b multiply.
 *      a =
 *
 *         1   2
 *         3   4
 *         5   6
 *
 *      b =
 *
 *         1   2   3
 *         4   5   6
 *
 *      a*b =
 *
 *          9   12   15
 *         19   26   33
 *         29   40   51
 *
 */


void print_matrix(double* M, int rows, int columns)
{
    int     i = 0;
    int     j = 0;
    double* p;

    for(i=0; i<rows; i++) {
        for(j=0; j<columns; j++) {
            p = M + i*columns+j;
            printf(" %.3lf ", *p);
        }
        printf("\n");
    }
    printf("\n");
}


int main(int argc, char* argv[])
{
  int m = 3;
  int n = 3;
  int k = 2;

  /* 3x2 matrix */
  double A[6] = {  1.0, 2.0 , 
                   3.0, 4.0 , 
                   5.0, 6.0  
  };         

  /* 2x3 matrix */
  double B[6] = { 1.0,  2.0, 3.0, 
                  4.0,  5.0, 6.0};  

  double C[9] = { .1, .2, .3,
                  .4, .5, .6,
                  .7, .8, .9  }; 


 
  printf("matrix A = \n");
  print_matrix(A, m, k);
  printf("matrix B = \n");
  print_matrix(B, k, n);
  printf("matrix C = \n");
  print_matrix(C, m, n);

  cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
              3,3,2,  /* m, n, k */
              1, 
                A, 2,  
                B, 3,
              1,
                C,3
             );


  print_matrix(C, m, n);

  return 0;
}
