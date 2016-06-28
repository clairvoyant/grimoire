#
# 'make depend' uses makedepend to automatically generate dependencies 
#               (dependencies are added to end of Makefile)
# 'make'        build executable file 'mycc'
# 'make clean'  removes all .o and executable files
#

CC = gcc
CFLAGS = -Wall -g
INCLUDES = -I/usr/local/include  
LFLAGS = -L/usr/local/lib  
LIBS =  -lm  -lblas -lpthread -lgfortran

SRCS = cblas.c
OBJS = $(SRCS:.c=.o)

MAIN = cblas

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
