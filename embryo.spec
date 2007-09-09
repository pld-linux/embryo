#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightenment Fundation Libraries - Embryo
Summary(pl.UTF-8):	Podstawowe biblioteki Enlightenmenta - Embryo
Name:		embryo
Version:	0.9.1.038
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	f044bf2bc2e668784528a705aa290e4a
URL:		http://enlightenment.org/p.php?p=about/libs/embryo
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Embryo is a tiny library designed as a virtual machine to interpret a
limited set of small compiled programs.

%description -l pl.UTF-8
Embryo to mała biblioteka zaprojektowana jako maszyna wirtualna do
interpretowania ograniczonego zbioru małych skompilowanych programów.

%package devel
Summary:	Embryo header files
Summary(pl.UTF-8):	Pliki nagłówkowe Embryo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Embryo.

%description devel -l pl.UTF-8
Pliki nagłówkowe Embryo.

%package static
Summary:	Static Embryo library
Summary(pl.UTF-8):	Statyczna biblioteka Embryo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Embryo library.

%description static -l pl.UTF-8
Statyczna biblioteka Embryo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
# for embryo_cc
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/embryo-config
%attr(755,root,root) %{_libdir}/libembryo.so
%{_libdir}/libembryo.la
%{_includedir}/Embryo.h
%{_pkgconfigdir}/embryo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
%endif
