if DEBUG
  AM_CFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -g -O3
else
  AM_CFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -O3
endif

AM_CFLAGS += $(GLIB_CFLAGS)
AM_CFLAGS += $(SQLITE3_CFLAGS)

bin_PROGRAMS = project
project_SOURCES = main.c

project_LDADD = $(top_builddir)/src/lib/libproject-base.a $(AM_LDFLAGS)
project_LDADD += $(GLIB_LIBS)
project_LDADD += $(SQLITE3_LIBS)
