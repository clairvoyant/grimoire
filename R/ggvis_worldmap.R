
require(googleVis)
Country <- c("Spain", "France", "Australia", "Argentina")
Cases  <- c(43, 20, 3, 5 )
x       <- data.frame(Country, Cases)
p <- gvisGeoMap(x, locationvar="Country", numvar="Cases", options=list(width="720", height="570"))
plot(p)

