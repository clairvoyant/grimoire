set term postscript eps color blacktext "Helvetica" 24
set output "sin.eps"
set ylabel "sin(x)"
set xlabel "x"
plot sin(x)
set output
quit

