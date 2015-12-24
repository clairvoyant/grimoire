if DEBUG
  AM_CXXFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -g -O3
else
  AM_CXXFLAGS =-I$(top_srcdir)/src/bin -I$(top_srcdir)/src/lib -Wall -O3
endif

AM_CXXFLAGS += $(GLIB_CFLAGS)
AM_CXXFLAGS += $(SQLITE3_CFLAGS)

bin_PROGRAMS = test
test_SOURCES = test.cc

test_LDADD = $(top_builddir)/src/lib/libproject-base.a $(AM_LDFLAGS)
test_LDADD += $(GLIB_LIBS)
test_LDADD += $(SQLITE3_LIBS)
test_LDADD += -lboost_unit_test_framework
