library("stringr")
library("ggplot2")
library("plyr")

# Rationale:
#    reads a csv file and print columns. 
#    selector is based on the host volumen columns
#    it's also possible to aggregate by the site column, note the ddply
# 
# Example:
#    2014-01-01 10:10,host1,brazil,100,200
#    2014-01-01 10:10,host2,brazil,130,400
#    2014-01-01 10:10,host3,brazil,301,20
#
# Filtering can be performed using
# the array primitives
#    stat <- stat[stat$rat!="",]
#    stat[stat$rat=="1", "rat"]  <- "UTRAN"
#    stat[stat$rat=="2", "rat"]  <- "GERAN"
#    stat[stat$rat=="99", "rat"] <- "MIXED"

#
# CSV readingand adaptation
#  
stat <- read.csv("counter/daily.csv", colClasses=c("character", "character", "character", "numeric", "numeric" ))
names(stat)   <- c("timestamp","host","site","counterdown","counterup")
stat$time    <- strptime(stat$timestamp, format="%Y-%m-%d %H:%M")
 
#
# grouping based on ddply
# one of the most powerfull concepts
# to process data, 
#
countersite <- ddply(stat, .(time, site), summarize, 
                 counterdown = sum(counterdown), 
                 counterup   = sum(counterup))
				 
				 
#
# Plot
#
ggplot(stat, aes(x=time, y=counterdown, color=host, group=host)) + geom_line(shape=1) + scale_colour_hue(l=50) + ggtitle("counter down") + ylab("Bytes") + xlab("Time")

ggplot(stat, aes(x=time, y=counterup, color=host, group=host)) + geom_line(shape=1) + scale_colour_hue(l=50) + ggtitle("counter  up") + ylab("Bytes") + xlab("Time")
