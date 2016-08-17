

import glm
import DataFrames


println("Starting Julia!!!!")

data = Dataframe(X1=[1, 10, 31], X2=[2,21,22], X3=[3, 22,22], Y=[38,330,317])


OLS = glm(Y ~ X1 + X2 + X3, data, Normal(), IdentityLink())


print stderr(OLS)
print predict(OLS)



