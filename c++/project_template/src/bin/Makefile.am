if DEBUG
  AM_CXXFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -g -O3
else
  AM_CXXFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -O3
endif

AM_CXXFLAGS += $(GLIB_CFLAGS)
AM_CXXFLAGS += $(SQLITE3_CFLAGS)

bin_PROGRAMS = project
project_SOURCES = main.cc

project_LDADD = $(top_builddir)/src/lib/libproject-base.a $(AM_LDFLAGS)
project_LDADD += $(GLIB_LIBS)
project_LDADD += $(SQLITE3_LIBS)
