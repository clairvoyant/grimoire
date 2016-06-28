#
# Recipe extracted from 
# examples at http://dan.iel.fm/emcee/current/user/line/
#
import numpy as np
import matplotlib.pyplot as plt


# Choose the "true" parameters.
m_true = -0.9594
b_true = 4.294
f_true = 0.534

#
# Generate some synthetic data from the model.
#
N = 50
x = np.sort(10*np.random.rand(N))
yerr = 0.1+0.5*np.random.rand(N)
# Original Y
y_true = m_true*x+b_true
# Gausian Error based on the absolute value of the result 
y_tmp  = y_true + np.abs(f_true*y_true) * np.random.randn(N)
# Gausian Constant error added 
y     = y_tmp + yerr * np.random.randn(N)


plt.plot(x, y_true, label="True value")
plt.plot(x, y_tmp, label="Gaussian proportional")
plt.plot(x, y, label="Gaussian constant")


#
# Least Squares Linear regresion used to compare with MCMC method
#

A = np.vstack((np.ones_like(x), x)).T
C = np.diag(yerr * yerr)
cov = np.linalg.inv(np.dot(A.T, np.linalg.solve(C, A)))
b_ls, m_ls = np.dot(cov, np.dot(A.T, np.linalg.solve(C, y)))

y_reg = m_ls*x + b_ls
plt.plot(x, y_reg, label="Regression")


#
# Define the usual log likelihood and maximize it!!!
#
def lnlike(theta, x, y, yerr):
    m, b, lnf = theta
    model = m * x + b
    inv_sigma2 = 1.0/(yerr**2 + model**2*np.exp(2*lnf))
    return -0.5*(np.sum((y-model)**2*inv_sigma2 - np.log(inv_sigma2)))

import scipy.optimize as op
nll = lambda *args: -lnlike(*args) # Note the minus because the function minimizes!!!
result = op.minimize(nll, [m_true, b_true, np.log(f_true)], args=(x, y, yerr))
m_ml, b_ml, lnf_ml = result["x"]

y_opt = m_ml*x + b_ml
plt.plot(x, y_opt, label="Likelihood optimized")

plt.legend()
plt.show()

#
# Lets do MCMC
#

# define the prior, conservative value.
def lnprior(theta):
    m, b, lnf = theta
    if -5.0 < m < 0.5 and 0.0 < b < 10.0 and -10.0 < lnf < 1.0:
        return 0.0
    return -np.inf
# Define the probability taking into account 
def lnprob(theta, x, y, yerr):
    lp = lnprior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + lnlike(theta, x, y, yerr)

# initialize the values using the "maximum" likelihood results
# result["x"] contains the m,b and lnf
ndim, nwalkers = 3, 100
pos = [result["x"] + 1e-4*np.random.randn(ndim) for i in range(nwalkers)]
import emcee
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x, y, yerr))
sampler.run_mcmc(pos, 500)

# altmost there, 
plt.figure(1)
plt.subplot(311)
plt.plot(sampler.chain[:, :,0])
plt.subplot(312)
plt.plot(sampler.chain[:, :,1])
plt.subplot(313)
plt.plot(sampler.chain[:, :,2])

plt.show()
# Display all posible results
#   - use the alpha to show the "density" of the result.
#   - use the samples after the 50 inital to let the algorithm converge
plt.figure(1)
plt.subplot(111)
xl = np.array([0, 10])

samples = sampler.chain[:, 50:, :].reshape((-1, ndim))
for m, b, lnf in samples[np.random.randint(len(samples), size=100)]:
    plt.plot(xl, m*xl+b, color="k", alpha=0.1)
plt.plot(xl, m_true*xl+b_true, color="r", lw=2, alpha=0.8)
plt.errorbar(x, y, yerr=yerr, fmt=".k")

plt.show()
