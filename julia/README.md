
Julia cheat sheet
=================

Cheat sheet written while studing Julia.


Fancy commands
--------------
```julia
;                   # Escape to shell
?                   # Help
apropos("commmand") # search for coma
whos()
cd("c:/")
pwd()
include("file.jl")
workspace()   # Clear workspace
push!(LOAD_PATH, "/path/to/modules/")

```


Variables and matrix
--------------------

```julia
A = [1 2 3 4; 5 6 7 8; 9 10 11 12]
A[2,1] = 0  # Set A row=2, column=1

A[3, 2:end] # Slice
A[3, :]     # Get 3 row.
A'          # Transpose A
A .* B      # Element multiplication
A \  b      # Solution to A*x = b
lambda, V = eig(A)
```

Dictionary
----------
```julia
dict = Dict("a" => 1, "b" => 2, "c" => 3)
dict2 = Dict{String,Int64}()
files = ["a.txt", "b.txt", "c.txt"]
fvars = Dict()
for (n, f) in enumerate(files)
   fvars["x_$(n)"] = f
end
dict["a"]
get(dict, "c", -1)
haskey(dict, "dd") # false
delete!(dict, "a")
[uppercase(key) for key in keys(dict)]
map(uppercase, keys(dict))
```

List and Queue
--------------
```julia

v = zeros(10)
append!(v, rand(10))
isempty(v)
empty!(v)
length(v)
reduce(+, v)
```

Strings
-------
```julia
s = "Test"
s2 = "This is a $s"
search(s2, "Test")
replace(s2, "Test", "Fact")
split(s2)
[trim(t) for t in split(s2)]

```
Math functions
--------------
```julia
sqrt(-5+0im)
rand(12,4)         # Random matrix 12 rows, 4 cols.
randn(12)          # Gaussian random
eye(5)
linspace(10)
diagm([1;2;3;4])   # Diagonal matrix with 1 2 3 4 in the diagonal.
t = linspace(0, 2*pi, 1000)
```

Type definition
---------------
```julia
type TScore
  id::Int
  name::String
  rating::Float
end
score = TScore(1, "match12", 21)

c = Complex(1, 2)
println(c.re, c.im)
typeof(score)
isa(Complex, c)

```
Type definition
---------------
```julia
type Point{T}
   x::T
   y::T
end

```

Function definition
-------------------

```julia
function ex(n::Int, m::Int64=0)
    m = ones(Bool, n) # n-element vector of true-s
    tmp = 0
    for i in 2:round(Int, sqrt(n))
        for j in (i*i):i:n    # See iteration with step.
                m[j] = false
        end
    end
    if n < 0
       println("n lt 0")
    elseif n == 0
       println("n eq 0")
    else
       println("n gt 0")
    end

    # While example
    while n>0
       tmp += 1
       n   -= 1
       println(tmp,";", n)
    end
    return filter(x -> m[x], 1:n) # filter using anonymous function
end

fib(n) = n < 2 ? n : fib(n - 1) + fib(n - 2)
```

Modules
-------
```julia
module example
using Gadfly

using GLM, RDatasets
import Base.show

importall SemiringAlgebra

export ExType, exfun

type ExType
    x
    y
end

privatefun(x) = 2*x
exfun(a::ExType) = privatefun(a.x) + 1

show(io, a::ExType) = print(io, "ExType $(a.x)")
end
```

Profiling
---------
```julia
@elapsed fib(25)
start <- Sys.time()
end <- Sys.time()
end - start
```



Package Management
------------------
```julia
Pkg.installed()
Pkg.status()
Pkg.add("package")
Pkg.rm("package")
Pkg.update()
Pkg.clone("git-repo")
Pkg.checkout("package", branch="branch") # Packages are "Git repos".
```

Plot
----
```julia
using PyPlot
plot(x,sin(x), color="red", linewidth=2.0, linestyle="--")

using Gadfly
draw(SVG("output.svg", 6inch, 3inch), plot(x=x, y=sin(x)))


```
