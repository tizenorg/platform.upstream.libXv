lib_LTLIBRARIES = libXv.la

libXv_la_SOURCES = \
         Xv.c \
         Xvlibint.h

libXv_la_LIBADD = @XV_LIBS@
AM_CFLAGS = @XV_CFLAGS@ -I$(top_srcdir)/include

libXv_la_LDFLAGS = -version-number 1:0:0 -no-undefined
