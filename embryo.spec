Summary:	Enlightenment Fundation Libraries - embryo
Name:		embryo
Version:	0.9.1
%define	_snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	f92d19c71263a9b5560206966357a6b6
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embryo is a tiny library designed as a virtual machine to interpret a
limited set of small compiled programs.

%package devel
Summary:	Embryo headers, documentation and test programs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers, test programs and documentation for Embryo.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_libdir}/libembryo.so.*
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_bindir}/embryo

%files devel
%defattr(644,root,root,755)
%{_libdir}/libembryo.la
%attr(755,root,root) %{_libdir}/libembryo.so
%attr(755,root,root) %{_bindir}/embryo-config
%{_datadir}/%{name}
%{_pkgconfigdir}/embryo.pc
%{_includedir}/Embryo*


%files static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
