#include <cblas.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
  int i=0;
  double A[6] = {1.0,2.0,1.0,-3.0,4.0,-1.0};         
  double B[6] = {1.0,2.0,1.0,-3.0,4.0,-1.0};  
  double C[9] = {.5,.5,.5,.5,.5,.5,.5,.5,.5}; 


  /***
   * gemm multiplies matrix 
   *
   *     C = C := alpha*op(A)*op(B) + beta*C
   *
   *
   *  cblas_dgemm (const CBLAS_LAYOUT Layout, 
   *               const CBLAS_TRANSPOSE transa, 
   *               const CBLAS_TRANSPOSE transb, 
   *                    const MKL_INT m,
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
  
  cblas_dgemm(CblasColMajor, CblasNoTrans, CblasTrans,
              3,3,2,
              1, 
                A, 3, 
                B, 3,
              2,
                C,3
             );

  for(i=0; i<9; i++)
    printf("%lf ", C[i]);
  printf("\n");


  return 0;
}
