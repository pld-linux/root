#
# TODO: - pass LDFLAGS
#	- BRs, bconds, package files
#	- separate packages for tutorials/docs
#	- xrootd is disabled because of errors - re-enable it in future
#	- files
#
Summary:	An object-oriented data analysis environment
Summary(pl.UTF-8):	Obiektowo zorientowane środowisko do analizowania danych
Name:		root
Version:	5.28.00
Release:	0.1
License:	LGPL v2.1+
Group:		Applications
Source0:	ftp://root.cern.ch/root/%{name}_v%{version}.source.tar.gz
# Source0-md5:	fc30b6410295ae2df9e74064fc84539d
Patch0:		%{name}-docs.patch
Patch1:		%{name}-namespaces.patch
Patch2:		%{name}-make_version.patch
Patch3:		%{name}-krb5_functions.patch
URL:		http://root.cern.ch/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	fftw3-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	ftgl-devel >= 2.1.3-0.rc5.1
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	gsl-devel >= 1.8
BuildRequires:	heimdal-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 1:2.4
BuildRequires:	make >= 3.80
BuildRequires:	mysql-devel >= 3.23
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	postgresql-devel
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRequires:	unixODBC-devel
BuildRequires:	which
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
# TODO???: oracle, rfio, shift, gfal, G4Navigator, apmon, pythia, dcap, chirp, glite, gapi, afterimage, srp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	config_target	linux
%ifarch %{x8664}
%define	config_target	linuxx8664gcc
%endif
%ifarch ppc
%define	config_target	linuxppcgcc
%endif
%ifarch ppc64
%define	config_target	linuxppc64gcc
%endif

%description
An object-oriented data analysis environment.

%description -l pl.UTF-8
Obiektowo zorientowane środowisko do analizowania danych.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{__sed} -i '/check_library/s@ \\$@ %{_libdir} \\@' configure

%build
./configure %{config_target} \
	--prefix="%{_prefix}" \
	--disable-builtin-afterimage \
	--disable-builtin-ftgl \
	--disable-builtin-freetype \
	--disable-builtin-pcre \
	--disable-builtin-zlib \
	--disable-xrootd \
	--disable-krb5 \
	--enable-gsl-shared \
	--with-cc="%{__cc} %{rpmcflags}" \
	--with-cxx="%{__cxx} %{rpmcxxflags}" \
	--with-x11-libdir=%{_libdir} \
	--with-xpm-libdir=%{_libdir}
# TODO: no way to pass xft,xext libdir

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README/{CREDITS,ChangeLog-*,README*} doc tutorials
%attr(755,root,root) %{_bindir}/root
%attr(755,root,root) %{_bindir}/root.exe
%{_datadir}/%{name}
%dir %{_libdir}/root
%attr(755,root,root) %{_libdir}/root/*.so
%{_mandir}/man1/*.1*
