#
# 'make depend' uses makedepend to automatically generate dependencies 
#               (dependencies are added to end of Makefile)
# 'make'        build executable file 'mycc'
# 'make clean'  removes all .o and executable files
#

CC = mkoctfile 
CFLAGS = 
INCLUDES = 
LFLAGS = --link-stand-alone
LIBS =  

SRCS = main.cc
OBJS = $(SRCS:.c=.o)

MAIN = exec

.PHONY: depend clean

all:    $(MAIN)
	@echo $(MAIN) has been build.

$(MAIN): $(SRCS) 
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(LFLAGS) $(LIBS) $(SRCS)

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o *~ $(MAIN)

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# DO NOT DELETE THIS LINE -- make depend needs it
