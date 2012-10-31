Name:           libXv
Version:        1.0.7
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXv runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxv-devel

%description devel
X.Org X11 libXv development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install

%make_install
%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0

%files devel
%defattr(-,root,root,-)
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
