Name:           libXv
Version:        1.0.7
Release:        1
License:        MIT
Summary:        Xvideo extension library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXv runtime library

%package devel
Summary:        Xvideo extension library - Development
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXv development package

%prep
%setup -q

%build
%reconfigure --disable-static 
make %{?_smp_mflags}

%install

%make_install
%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING 
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0

%files devel
%defattr(-,root,root,-)
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
