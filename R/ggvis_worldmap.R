
require(googleVis)

# reads a csv will following format and display a map based on the values
#
#  country     : string
#  measurement : numerick
# Example:
#    Italy,10
#    Germany,2000
#    Span,20
#

stat <- read.csv("country.csv", header = FALSE, sep=",", colClasses=c("character", "numeric"))
names(stat)   <- c("Country","Measurement")
           

p <- gvisGeoMap(stat, locationvar="Country", numvar="Measurement", options=list(width="720", height="570"))
plot(p)