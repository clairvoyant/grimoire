

%
% Some data to fill the example
% X*b = y 
%

X = [ 1 2 3; 4 5 6; 7 8 9; 121 22 89; 1 3 45; 46 7 98; 987 101 22; 76 5 43; 105 22 66; 13 253 843 ];
b = [ 31; 47; 101];

% add some white noise to make the least square data more real
%y=X*b + randn(size(X,1), 1);

% Compute y to use as a test check in ols.
y=X*b 



% ordinary least square
disp('*** ols ****')
[beta, sigma, r] = ols(y,X)

%disp('*** gls ****')
%[beta, v, r] = gls(y,X)

size(X, 1)
size(X, 2)
