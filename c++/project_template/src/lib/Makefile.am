if DEBUG
  AM_CFLAGS =-I$(top_srcdir)/src/lib -Wall -g -O3
else
  AM_CFLAGS =-I$(top_srcdir)/src/lib -Wall
endif


# The libraries to build
noinst_LIBRARIES = libproject-base.a

# The files to add to the library and to the source distribution
libproject_base_a_SOURCES = \
						$(libproject_base_a_HEADERS) \
						libproject.cc
