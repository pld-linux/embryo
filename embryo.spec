#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightenment Fundation Libraries - Embryo
Summary(pl.UTF-8):	Podstawowe biblioteki Enlightenmenta - Embryo
Name:		embryo
Version:	1.7.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	d66a0e91dfc37eeb4c362b2c46bd91ab
URL:		http://trac.enlightenment.org/e/wiki/Embryo
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
Requires:	eina >= 1.7.0
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
Requires:	eina-devel >= 1.7.0

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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libembryo.so.1
# for embryo_cc
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libembryo.so
%{_libdir}/libembryo.la
%{_includedir}/embryo-1
%{_pkgconfigdir}/embryo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
%endif
