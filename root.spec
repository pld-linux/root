#
# TODO: - pass LDFLAGS
#	- BRs, bconds, package files
#	- separate packages for tutorials/docs
#	- fix krb5_net_read function redeclaration
#
Summary:	An object-oriented data analysis environment
Summary(pl.UTF-8):	Obiektowo zorientowane środowisko do analizowania danych
Name:		root
Version:	5.24.00
Release:	0.1
License:	LGPL v2.1+
Group:		Applications
Source0:	ftp://root.cern.ch/root/%{name}_v%{version}.source.tar.gz
# Source0-md5:	249c414bf34ed1e6660d2d829c2db964
Patch0:		%{name}-docs.patch
URL:		http://root.cern.ch/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	fftw3-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	ftgl-devel >= 2.1.3~rc5
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	gsl-devel >= 1.8
BuildRequires:	heimdal-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 1:2.4
BuildRequires:	make >= 3.79.1
BuildRequires:	mysql-devel >= 3.23
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	postgresql-devel
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	unixODBC-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
# TODO???: oracle, rfio, shift, gfal, G4Navigator, apmon, pythia, dcap, chirp, glite, gapi, afterimage, srp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An object-oriented data analysis environment.

%description -l pl.UTF-8
Obiektowo zorientowane środowisko do analizowania danych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
./configure linux \
	--prefix="%{_prefix}" \
	--disable-builtin-afterimage \
	--disable-builtin-ftgl \
	--disable-builtin-freetype \
	--disable-builtin-pcre \
	--disable-builtin-zlib \
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
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
