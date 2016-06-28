/*****************************************************************************
* File:  main.c
* 
* Description: Example of solving a  linear square system.
*
* 
*
*****************************************************************************/


/*
y=X*b + randn(size(X,1), 1);
% add some white noise to make the least square data more real



% ordinary least square
disp('*** ols ****')
[beta, sigma, r] = ols(y,X)

disp('*** gls ****')
[beta, v, r] = ols(y,X)
*/


#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;

int main(int argc, char** argv)
{
    mat X = "1 2 3; 4 5 6; 7 8 9; 121 22 89; 1 3 45; 46 7 98; 987 101 22; 76 5 43; 105 22 66; 13 253 843";
    vec b = "31 47 101"; // this is the one we are looking for.

    vec y = X*b;

    // solve the system using least squares.
    mat B = solve(X,y);


    // report and analysis. 
    mat beta = pinv(X)*y;

    cout << "reference:" << endl;
    cout << B << endl;
    cout << "solve:" << endl;
    cout << b << endl;
    cout << "residuals:" << endl;
    vec r = y - X * beta;
    cout << r << endl;
    cout << "sigma:" << endl;
    cout << (r.t() * r) / ( y.n_rows -rank(X)) << endl;

    return 0;
}
