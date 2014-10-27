library("plyr")
library("ggplot2")


#setwd("counters")


# Multiple plot function
#
# ggplot objects can be passed in ..., or to plotlist (as a list of ggplot objects)
# - cols:   Number of columns in layout
# - layout: A matrix specifying the layout. If present, 'cols' is ignored.
#
# If the layout is something like matrix(c(1,2,3,3), nrow=2, byrow=TRUE),
# then plot 1 will go in the upper left, 2 will go in the upper right, and
# 3 will go all the way across the bottom.
#
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}

###################################

get_servers <- function (path, p) {
  files = dir(path, pattern=p)
  #files <- list.files(path, pattern=p)
  parts = strsplit(files, "-")
  return (sapply(parts, function (l) l[2]))
}

#
# Use a file stat that appear only in probes to get the name of the probes.
#
get_mediations <- function (path) {
  get_servers(path, "*xdr*")

}

#
# Use a file stat that appear only in mediations to get the name of the probes.
#
get_probes <- function (path) {
  get_servers(path, "*rx_*")
}

ts2date2 <- function(x) {
    as.POSIXlt(x, origin="1970-01-01")
}

# 
# Load hosts
#
probes         <- get_probes("counters")
mediations     <- get_mediations("counters")
bps            <- data.frame(ts=integer(0), bps=numeric(0),     date=numeric(0), probe=character(0))
cpu            <- data.frame(ts=integer(0), cpu=numeric(0),     date=numeric(0), probe=character(0))

xdrs_mediation <- data.frame(ts=integer(0), probe=character(0), date=numeric(0), mediation=character(0))

#
# Create data frames for probes.
#

# TODO refactor
for (i in 1:length(probes)) {
  
  # throughput 
  probe         <-  probes[i]
  # read BPS
  bps_one_probe <- read.csv(paste("counters/", "rx_bps.rrd-",probe, sep=""), sep=",", skip=1, col.names = c("ts", "bps"), header=FALSE)
  # add a date time column
  bps_one_probe        <- transform(bps_one_probe, date=as.POSIXct(ts, origin="1970-01-01", "America/Lima"))
  
  # find a way to make it better, is appending to itself, but is copying over an over
  bps_one_probe$probe  <-  rep(probe, dim(bps_one_probe)[1])
  bps                  <- rbind(bps, bps_one_probe)
  
  # CPU
  
  # throughput 
  # read BPS
  cpu_one_probe <- read.csv(paste("counters/", "cpu_user.rrd-",probe, sep=""), sep=":", skip=1, col.names = c("ts", "cpu"), header=FALSE)
  # add a date time column
  cpu_one_probe        <- transform(cpu_one_probe, date=as.POSIXct(ts, origin="1970-01-01", "America/Lima"))
  
  # find a way to make it better, is appending to itself, but is copying over an over
  cpu_one_probe$probe  <-  rep(probe, dim(cpu_one_probe)[1])
  cpu                  <- rbind(cpu, cpu_one_probe)
}

#dirty trick make it a warning!!! this map shall be before the data is retrieved
cpu[cpu$probe=="applevel.telefonica.com.ec", "probe"] <- "applevel"
cpu[cpu$probe=="lav1.telefonica.com.pe","probe"]     <- "lav1.pe"
cpu[cpu$probe=="sis1.telefonica.com.pe","probe"]     <- "sis1.pe"

bps[bps$probe=="applevel.telefonica.com.ec", "probe"] <- "applevel"
bps[bps$probe=="lav1.telefonica.com.pe","probe"]     <- "lav1.pe"
bps[bps$probe=="sis1.telefonica.com.pe","probe"]     <- "sis1.pe"

for (i in 1:length(mediations)) {
  mediation         <-  mediations[i]
  # read BPS
  fname <- paste("counters/", "xdrs-",mediation, sep="")
  fname
  xdrs_one_mediation           <- read.csv(fname, sep=",", skip=1, col.names = c("ts", "probe", "xdrs"), colClasses=c("character", "factor", "numeric"), header=FALSE)
  xdrs_one_mediation$date      <- as.POSIXct(strptime(xdrs_one_mediation$ts, format="%Y%m%d.%H%M"), tz="America/Lima")
  xdrs_one_mediation$mediation <- rep(mediation, dim(xdrs_one_mediation)[1])
  # add a date time column
  ## find a way to make it better, is appending to itself, but is copying over an over
  
  xdrs_mediation  <- rbind(xdrs_mediation, xdrs_one_mediation)
}



# Necessary to do a grouping of the xdrs_mediation, one probe can happend more than 1 time
xdrs_probe <- ddply(xdrs_mediation, .(date, probe), summarize, xdrs = sum(xdrs))
# compute only before 15:00, TODO dirty trick
xdrs_probe <- xdrs_probe[xdrs_probe$date < as.POSIXct(strptime("2014-02-23 15:00", format="%Y-%m-%d %H:%M" )),]


# merge both xdrs by date and probe generator. 
all <- merge(bps, xdrs_probe, by=c("date", "probe"))
all <- merge(all, cpu, by=c("date", "probe"))


p1<- ggplot(all, aes(x=date, y=xdrs , color=probe, group=probe)) + geom_point(shape=1) + scale_colour_hue(l=50) + ggtitle("Time vs XDRs") + ylab("xdrs") + xlab("Date")
p2<- ggplot(all, aes(x=cpu, y=bps , color=probe, group=probe)) + geom_point(shape=1) + scale_colour_hue(l=50) + ggtitle("CPU vs Throughput") + ylab("Bps") + xlab("%CPU")
p3<- ggplot(all, aes(x=bps, y=xdrs , color=probe, group=probe)) + geom_point(shape=1) + scale_colour_hue(l=50) + ggtitle("XDRs vs Bps") + ylab("xdrs") + xlab("Bps")
p4<- ggplot(xdrs_mediation, aes(x=date, y=xdrs , color=probe, group=probe)) + geom_point(shape=1) + scale_colour_hue(l=50) + ggtitle("mediation: Time vs XDRs") + ylab("xdrs") + xlab("Date")
multiplot(p1, p2, p3, p4, cols=2)


all$cpu24 <- all$cpu*2

ggplot(cpu, aes(x=ts, y=cpu24 , color=probe, group=probe)) + geom_point(shape=1) + scale_colour_hue(l=50) + ggtitle("mediation: CPU vs time") + ylab("CPU") + xlab("Date")
#library(xts)

#xTemps <- align.time(xts(temps[,2],as.POSIXct(temps[,1])), n=600)
#xGas <- align.time(xts(gas[,2],as.POSIXct(gas[,1])), n=600)
#merge(xTemps,xGas)