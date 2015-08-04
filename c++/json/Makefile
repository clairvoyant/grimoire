#
# 'make depend' uses makedepend to automatically generate dependencies 
#               (dependencies are added to end of Makefile)
# 'make'        build executable file 'mycc'
# 'make clean'  removes all .o and executable files
#

CC = c++
CFLAGS = -Wall -g
INCLUDES = 
LFLAGS = -ljson
LIBS =  -lm

SRCS = main.cc
OBJS = $(SRCS:.c=.o)

MAIN = json-reader

.PHONY: depend clean

all:    $(MAIN)
	@echo $(MAIN) has been build.

$(MAIN): $(OBJS) 
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS) $(LFLAGS) $(LIBS)

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o *~ $(MAIN)

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# DO NOT DELETE THIS LINE -- make depend needs it
