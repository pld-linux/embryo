Summary:	Enlightenment Fundation Libraries - Embryo
Summary(pl):	Podstawowe biblioteki Enlightenmenta - Embryo
Name:		embryo
Version:	0.9.1.013
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	e1140446f243445ad8b987becb975d3d
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embryo is a tiny library designed as a virtual machine to interpret a
limited set of small compiled programs.

%description -l pl
Embryo to ma³a biblioteka zaprojektowana jako maszyna wirtualna do
interpretowania ograniczonego zbioru ma³ych skompilowanych programów.

%package devel
Summary:	Embryo header files
Summary(pl):	Pliki nag³ówkowe Embryo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Embryo.

%description devel -l pl
Pliki nag³ówkowe Embryo.

%package static
Summary:	Static Embryo library
Summary(pl):	Statyczna biblioteka Embryo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Embryo library.

%description static -l pl
Statyczna biblioteka Embryo.

%prep
%setup -q

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
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_bindir}/embryo
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/embryo-config
%attr(755,root,root) %{_libdir}/libembryo.so
%{_libdir}/libembryo.la
%{_includedir}/Embryo*
%{_datadir}/%{name}
%{_pkgconfigdir}/embryo.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
