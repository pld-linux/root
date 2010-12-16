#
# TODO: - pass LDFLAGS
#	- BRs, bconds, package files
#	- separate packages for tutorials/docs
#	- xrootd is disabled because of errors - re-enable it in future
#	- files
#	- dosn't build on 64 bits
#
#Conditional build:
%bcond_with	krb5	# build with MIT kerberos
#
Summary:	An object-oriented data analysis environment
Summary(pl.UTF-8):	Obiektowo zorientowane środowisko do analizowania danych
Name:		root
Version:	5.28.00
Release:	0.1
License:	LGPL v2.1+
Group:		Applications/Engineering
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
%if %{with krb5}
BuildRequires:	krb5-devel
%else
BuildRequires:	heimdal-devel
%endif
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

%package icons
Summary:	ROOT icon collection
Summary(pl.UTF-8):	Zbiór icon dla ROOT
Group:		Applications/Engineering
Requires:	%{name}-core = %{version}-%{release}
BuildArch:	noarch

%description icons
This package contains icons used by the ROOT GUI.

%description icons -l pl.UTF-8
Ten pakiet zawiera ikony używane przez GUI ROOT.

%package doc
Summary:	Documentation for the ROOT system
Summary(pl.UTF-8):	Dokumentacja dla systemu ROOT
License:	LGPLv2+ and GPLv2+ and BSD
Requires:	%{name}-cint = %{version}-%{release}
BuildArch:	noarch

%description doc
This package contains the automatically generated ROOT class
documentation.

%description doc -l pl.UTF-8
Ten pakiet zawiera automatycznie wygenerowaną klasę dokumentacji dla
ROOT.

%package core
Summary:	ROOT core libraries
Summary(pl.UTF-8):	Biblioteki główne ROOT
License:	LGPL v2+ and BSD
Group:		Libraries
Requires:	%{name}-graf-asimage = %{version}-%{release}
Requires:	%{name}-icons = %{version}-%{release}
Requires:	fonts-TTF-RedHat-liberation
Requires:	xorg-font-font-misc-misc-ISO8859-1

%description core
This package contains the core libraries used by ROOT: libCore,
libNew, libRint, libRIO and libThread.

%description core -l pl.UTF-8
Ten pakiet zawiera główne biblioteki używane przez ROOT: libCore,
libNew, libRint, libRIO oraz libThread.

%package graf-asimage
Summary:	AfterImage graphics renderer for ROOT
Summary(pl.UTF-8):	Grafinczy renderer AfterImage dla ROOT
Group:		Libraries
Requires:	%{name}-core = %{version}-%{release}

%description graf-asimage
This package contains the AfterImage renderer for ROOT, which allows
you to store output graphics in many formats, including JPEG, PNG and
TIFF.

%description graf-asimage -l pl.UTF-8
Ten pakiet zawiera renderer AfterImage dla ROOT, który umożliwia
użytkownikowi przechowywanie wyjściowych plików graficznych w wielu
formatach, między innymi JPEG, PNG oraz TIFF.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if %{with krb5}
%patch3 -p1
%endif

%{__sed} -i '/check_library/s@ \\$@ %{_libdir} \\@' configure

%build
./configure %{config_target} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}/%{name} \
	--docdir=%{_docdir}/%{name}-%{version} \
	--disable-builtin-afterimage \
	--disable-builtin-ftgl \
	--disable-builtin-freetype \
	--disable-builtin-pcre \
	--disable-builtin-zlib \
	--disable-xrootd \
	%{!?with_krb5:--disable-krb5} \
	--enable-gsl-shared \
	--with-cc="%{__cc} %{rpmcflags}" \
	--with-cxx="%{__cxx} %{rpmcxxflags}" \
	--with-x11-libdir=%{_libdir} \
	--with-xpm-libdir=%{_libdir}
# TODO: no way to pass xft,xext libdir

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# Remove some junk
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/BUILDSYSTEM
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/ChangeLog-2-24
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/INSTALL
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.ALIEN
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.MONALISA

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hadd
%attr(755,root,root) %{_bindir}/root
%attr(755,root,root) %{_bindir}/root.exe
%attr(755,root,root) %{_bindir}/rootn.exe
%attr(755,root,root) %{_bindir}/roots
%attr(755,root,root) %{_bindir}/roots.exe
%attr(755,root,root) %{_bindir}/ssh2rpd
%{_mandir}/man1/hadd.1*
%{_mandir}/man1/root.1*
%{_mandir}/man1/root.exe.1*
%{_mandir}/man1/rootn.exe.1*
%{_mandir}/man1/roots.exe.1*
%{_mandir}/man1/ssh2rpd.1*

%files icons
%defattr(644,root,root,755)
%{_datadir}/%{name}/icons

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/html

%files core
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/CREDITS
%doc %{_docdir}/%{name}-%{version}/README
%attr(755,root,root) %{_bindir}/memprobe
%attr(755,root,root) %{_bindir}/rlibmap
%attr(755,root,root) %{_bindir}/rmkdepend
%attr(755,root,root) %{_bindir}/root-config
%{_mandir}/man1/memprobe.1*
%{_mandir}/man1/rmkdepend.1*
%{_mandir}/man1/rlibmap.1*
%{_mandir}/man1/root-config.1*
%{_libdir}/%{name}/libCore.*
%{_libdir}/%{name}/libNew.*
%{_libdir}/%{name}/libRint.*
%{_libdir}/%{name}/libRIO.*
%{_libdir}/%{name}/libThread.*
%{_libdir}/%{name}/lib[^R]*Dict.*
%{_includedir}/%{name}/RConfigOptions.h
%{_includedir}/%{name}/RConfigure.h
%{_includedir}/%{name}/compiledata.h
%{_includedir}/%{name}/rmain.cxx
%dir %{_includedir}/%{name}/Math
%{_aclocaldir}/root.m4

%files graf-asimage
%defattr(644,root,root,755)
%{_libdir}/%{name}/libASImage.*
%{_libdir}/%{name}/libASImageGui.*
