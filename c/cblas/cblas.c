#include <cblas.h>
#include <stdio.h>


/* 
 * This code is an example of blas a*b multiply.
 *   a =
 *       1   2
 *       4   5
 *       7   8
 *
 *  b =
 *
 *       1   2   3
 *       3   4   5
 *
 *  a*b =
 *
 *       7   10   13
 *       19   28   37
 *       31   46   61
 *
 */


void print_matrix(double* M, int rows, int columns)
{
    int i=0;
    int j=0;

    for(i=0; i<rows; i++) {
        for(j=0; j<columns; j++) {
            printf(" %lf ", *M+i*rows+j);
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
                   4.0, 5.0 , 
                   7.0, 8.0  
  };         

  /* 2x3 matrix */
  double B[6] = { 1.0,  2.0, 3.0, 
                  3.0,  4.0, 5.0};  

  double C[9] = { .5, .5, .5,
                  .5, .5, .5,
                  .5, .5, .5  }; 


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
   */
  
  print_matrix(A, m, k);
  print_matrix(B, k, n);

  cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasTrans,
              3,3,2,  /* m, n, k */
              1, 
                A, 3, 
                B, 3,
              2,
                C,3
             );


  print_matrix(C, m, n);

  return 0;
}
