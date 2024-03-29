#
# TODO: - pass LDFLAGS
#	- BRs, bconds, package files
#	- separate packages for tutorials/docs
#	- xrootd is disabled because of errors - re-enable it in future
#	- files
#	- check and set proper groups for subpackages if needed
#	- create script for package generation
#
# NOTE: The upstream source is modified to exclude proprietary fonts, fix it by doing:
#
# wget -N ftp://root.cern.ch/root/root_v%{version}.source.tar.gz
# tar -z -x -f root_v%{version}.source.tar.gz
# rm -rf root/fonts
# mv root root-%{version}
# tar -z -c -f root-%{version}.tar.gz root-%{version}
#
#Conditional build:
%bcond_with	krb5	# build with MIT kerberos
#
Summary:	An object-oriented data analysis environment
Summary(pl.UTF-8):	Obiektowo zorientowane środowisko do analizowania danych
Name:		root
Version:	5.28.00c
Release:	0.1
License:	LGPL v2.1+
Group:		Applications/Engineering
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1fb410a231fd95d1325e6f4199ba71e5
# Script to extract the list of include files in a subpackage
Source1:	%{name}-includelist
Patch0:		%{name}-docs.patch
Patch1:		%{name}-namespaces.patch
Patch2:		%{name}-make_version.patch
Patch3:		%{name}-krb5_functions.patch
Patch4:		%{name}-fontconfig.patch
URL:		http://root.cern.ch/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	fontconfig-devel
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
BuildRequires:	pkgconfig
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
The ROOT system provides a set of object oriented frameworks with all
the functionality needed to handle and analyze large amounts of data
in a very efficient way. Having the data defined as a set of objects,
specialized storage methods are used to get direct access to the
separate attributes of the selected objects, without having to touch
the bulk of the data. Included are histogramming methods in 1, 2 and 3
dimensions, curve fitting, function evaluation, minimization, graphics
and visualization classes to allow the easy setup of an analysis
system that can query and process the data interactively or in batch
mode.

Thanks to the built in CINT C++ interpreter the command language, the
scripting, or macro, language and the programming language are all
C++. The interpreter allows for fast prototyping of the macros since
it removes the time consuming compile/link cycle. It also provides a
good environment to learn C++. If more performance is needed the
interactively developed macros can be compiled using a C++ compiler.

The system has been designed in such a way that it can query its
databases in parallel on MPP machines or on clusters of workstations
or high-end PCs. ROOT is an open system that can be dynamically
extended by linking external libraries. This makes ROOT a premier
platform on which to build data acquisition, simulation and data
analysis systems.

%description -l pl.UTF-8
System ROOT udostępnia zestaw obiektowo zorientowanych frameworków
wraz z całą funkcjonalnością potrzebną do obróbki i analizy dużych
ilości danych w bardzo efektywny sposób. Posiadając dane zdefiniowane
jako zbiór obiektów, specjalistyczne metody magazynowania są używane w
celu otrzymania dostępu do osobnych atrybutów wybranych objektów bez
konieczności ruszania większości danych. Załączone są również metody
histogramiczne w 1, 2 i 3 wymiarach, dopasowania krzywej, oceny
funkcji, minimalizacji oraz klasy do grafiki i wizualizacji, które
umożliwiają łatwe ustawienie systemu analiz umożliwiającego
odpytywanie i przetwarzanie danych interaktywnie lub w trybie
wsadowym.

Dzięki wbudowanemu interpretorowi CINT C++, język komend, skrypty,
makra, język oraz język programowania są stworzone w C++. Dzięki
ominięciu czasu niezbędnego do kompilacji/linkowania interpreter
umożliwia szybkie prototypowanie makr. Przy okazji udostępniane jest
dobre środowisko do nauki C++. Jeżeli potrzebna jest lepsza wydajność,
interaktywnie stworzone makra mogą zostać zbudowane używając
kompilatora C++.

System został zaprojektowany w sposób umożliwiający równoległe
odpytywanie jego baz danych na maszynach MPP, na klastrach stacji
roboczych lub końcowych PC-tach. ROOT jest otwartym systemem, który
może być dynamicznie rozszerzany poprzez linkowanie zewnętrznych
bibliotek. To czyni ROOT podstawową platformą do budowy akwizycji
danych, symulacji oraz systemów analizy danych.

%package icons
Summary:	ROOT icon collection
Summary(pl.UTF-8):	Zbiór icon dla ROOT
Group:		Applications/Engineering
Requires:	%{name}-core = %{version}-%{release}

%description icons
This package contains icons used by the ROOT GUI.

%description icons -l pl.UTF-8
Ten pakiet zawiera ikony używane przez GUI ROOT.

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

%package cint
Summary:	CINT C++ interpreter
Summary(pl.UTF-8):	Interpreter CINT C++
License:	MIT
Group:		Applications/Engineering

%description cint
This package contains the CINT C++ interpreter version 5.

%description cint -l pl.UTF-8
Ten pakiet zawiera interpreter CINT C++ w wersji 5.

%package reflex
Summary:	Reflex dictionary generator
Summary(pl.UTF-8):	Generator słownika reflex
Group:		Libraries

%description reflex
This package contains the reflex dictionary generator for ROOT.

%description reflex -l pl.UTF-8
Ten pakiet zawiera generator słownika reflex dla ROOT.

%package doc
Summary:	Documentation for the ROOT system
Summary(pl.UTF-8):	Dokumentacja dla systemu ROOT
License:	LGPL v2+ and GPL v2+ and BSD
Group:		Documentation
Requires:	%{name}-cint = %{version}-%{release}

%description doc
This package contains the automatically generated ROOT class
documentation.

%description doc -l pl.UTF-8
Ten pakiet zawiera automatycznie wygenerowaną klasę dokumentacji dla
ROOT.

%package geom
Summary:	Geometry library for ROOT
Summary(pl.UTF-8):	Biblioteka geometryczna dla ROOT
Group:		Libraries

%description geom
This package contains a library for defining geometries in ROOT.

%description geom -l pl.UTF-8
Ten pakiet zawiera bibliotekę do definiowania geomterii w ROOT.

%package graf
Summary:	2D graphics library for ROOT
Summary(pl.UTF-8):	Biblioteka graficzna 2D dla ROOT
Group:		Libraries

%description graf
This package contains the 2-dimensional graphics library for ROOT.

%description graf -l pl.UTF-8
Ten pakiet zawiera dwuwymiarową bibliotekę graficzną dla ROOT.

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

%package graf-gpad
Summary:	Canvas and pad library for ROOT
Summary(pl.UTF-8):	Biblioteka canvas i pad dla ROOT
Group:		Libraries
Requires:	%{name}-graf-postscript = %{version}-%{release}

%description graf-gpad
This package contains a library for canvas and pad manipulations.

%description graf-gpad -l pl.UTF-8
Ten pakiet zawiera bibliotekę canvas i pad do manipulacji.

%package graf-postscript
Summary:	Postscript/PDF renderer library for ROOT
Summary(pl.UTF-8):	Biblioteka renderująca Postscript/PDF dla ROOT
Group:		Libraries

%description graf-postscript
This package contains a library for ROOT, which allows rendering
postscript and PDF output.

%description graf-postscript -l pl.UTF-8
Ten pakiet zawiera bibliotekę dla ROOT, która umożliwia renderowanie
postscript i zapis do PDF.

%package graf3d
Summary:	Basic 3D shapes library for ROOT
Summary(pl.UTF-8):	Podstawowe kształty 3D dla ROOT
Group:		Libraries

%description graf3d
This library contains the basic 3D shapes and classes for ROOT. For a
more full-blown geometry library, see the root-geom package.

%description graf3d -l pl.UTF-8
Ta biblioteka zawiera podstawowe kształty 3D oraz klasy dla ROOT.
Biblioteka zawierająca bardziej rozwinięte kształty znajduje się w
pakiecie root-geom.

%package hbook
Summary:	Hbook library for ROOT
Summary(pl.UTF-8):	Biblioteka Hbook dla ROOT
Group:		Libraries

%description hbook
This package contains the Hbook library for ROOT, allowing you to
access legacy Hbook files (NTuples and Histograms from PAW).

%description hbook -l pl.UTF-8
Ten pakiet zawiera bibliotekę Hbook dla ROOT, umożliwiającą dostęp do
starszych plików Hbooka (NTuples i Histograms z PAW).

%package hist
Summary:	Histogram library for ROOT
Summary(pl.UTF-8):	Biblioteka histogramu dla ROOT
Group:		Libraries
Requires:	%{name}-hist-painter = %{version}-%{release}

%description hist
This package contains a library for histogramming in ROOT.

%description hist -l pl.UTF-8
Ten pakiet zawiera bibliotekę do tworzenia histogramów w ROOT.

%package hist-painter
Summary:	Histogram painter plugin for ROOT
Summary(pl.UTF-8):	Wtyczka rysownika histogramów dla ROOT
Group:		Libraries

%description hist-painter
This package contains a painter of histograms for ROOT.

%description hist-painter -l pl.UTF-8
Ten pakiet zawiera rysownik histogramów dla ROOT.

%package io
Summary:	Input/output of ROOT objects
Summary(pl.UTF-8):	Wejście/wyjście dla obiektów ROOT
Group:		Libraries

%description io
This package provides I/O routines for ROOT objects.

%description io -l pl.UTF-8
Ten pakiet zawiera procedury wejścia/wyjścia dla obiektów ROOT.

%package mathcore
Summary:	Core mathematics library for ROOT
Summary(pl.UTF-8):	Główna biblioteka matematyczna dla ROOT
Group:		Libraries
Requires:	%{name}-minuit = %{version}-%{release}

%description mathcore
This package contains the MathCore library for ROOT.

%description mathcore -l pl.UTF-8
Ten pakiet zawiera bibliotekę MathCore dla ROOT.

%package matrix
Summary:	Matrix library for ROOT
Summary(pl.UTF-8):	Biblioteka matrix dla ROOT
Group:		Libraries

%description matrix
This package contains the Matrix library for ROOT.

%description matrix -l pl.UTF-8
Ten pakiet zawiera bibliotekę Matrix dla ROOT.

%package minuit
Summary:	Minuit library for ROOT
Summary(pl.UTF-8):	Biblioteka minuit dla ROOT
Group:		Libraries

%description minuit
This package contains the MINUIT library for ROOT. This provides a
fitting algorithm for ROOT.

%description minuit -l pl.UTF-8
Ten pakiet zawiera bibliotekę MINUIT dla ROOT. Udostępnia ona algorytm
dopasowania dla ROOT.

%package net
Summary:	Net library for ROOT
Summary(pl.UTF-8):	Biblioteka net dla ROOT
Group:		Libraries

%description net
This package contains the ROOT networking library.

%description net -l pl.UTF-8
Ten pakiet zawiera bibliotekę sieciową dla ROOT.

%package proof-pq2
Summary:	PROOF Quick Query (pq2)
Summary(pl.UTF-8):	Szybkie Zapytanie PROFF (PROOF Quick Query - pq2)
Group:		Libraries

%description proof-pq2
Shell-based interface to the PROOF dataset handling.

%description proof-pq2 -l pl.UTF-8
Konsolowy interfejs do obsługi zestawów danych PROFF.

%package tree
Summary:	Tree library for ROOT
Summary(pl.UTF-8):	Biblioteka tree dla ROOT
Group:		Applications/Engineering

%description tree
This package contains the Tree library for ROOT.

%description tree -l pl.UTF-8
Ten pakiet zawiera bibliotekę Tree dla ROOT.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if %{with krb5}
%patch3 -p1
%endif
%patch4 -p1

%{__sed} -i '/check_library/s@ \\$@ %{_libdir} \\@' configure

# Remove embedded sources in order to be sure they are not used
#  * ftgl
%{__rm} -r graf3d/ftgl/src graf3d/ftgl/inc

%build
./configure %{config_target} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}/%{name} \
	--etcdir=%{_datadir}/%{name} \
	--docdir=%{_docdir}/%{name}-%{version} \
	--disable-builtin-afterimage \
	--disable-builtin-ftgl \
	--disable-builtin-freetype \
	--disable-builtin-pcre \
	--disable-builtin-zlib \
	--disable-rpath \
	--disable-xrootd \
	%{!?with_krb5:--disable-krb5} \
	--enable-explicitlink \
	--enable-gsl-shared \
	--enable-minuit2 \
	--enable-reflex \
	--enable-soversion \
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

# Remove some junk
%{__rm} $RPM_BUILD_ROOT%{_bindir}/drop_from_path
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/cint.1

# Remove cintdll sources - keep the prec_stl directory
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/cint/cint/lib/{[^p],p[^r]}*

# Create includelist files ...
RPM_BUILD_DIR=$(pwd)
for module in `find * -name Module.mk` ; do
	module=`dirname $module`
	make -f %{SOURCE1} includelist MODULE=$module ROOT_SRCDIR=$RPM_BUILD_DIR
done

# ... and merge some of them
cat includelist-core-[^we]* > includelist-core
cat includelist-io-io >> includelist-core
cat includelist-geom-geom* > includelist-geom
cat includelist-roofit-* > includelist-roofit
cat includelist-gui-qt* > includelist-guiqt
cat includelist-graf2d-x11ttf >> includelist-graf2d-x11
cat includelist-gui-guihtml >> includelist-gui-gui
cat includelist-io-xmlparser >> includelist-io-xml
cat includelist-proof-proofplayer >> includelist-proof-proof

%clean
rm -rf $RPM_BUILD_ROOT

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig
%post cint -p /sbin/ldconfig
%postun cint -p /sbin/ldconfig
%post geom -p /sbin/ldconfig
%postun geom -p /sbin/ldconfig
%post graf -p /sbin/ldconfig
%postun graf -p /sbin/ldconfig
%post graf-asimage -p /sbin/ldconfig
%postun graf-asimage -p /sbin/ldconfig
%post graf-gpad -p /sbin/ldconfig
%postun graf-gpad -p /sbin/ldconfig
%post graf-postscript -p /sbin/ldconfig
%postun graf-postscript -p /sbin/ldconfig
%post graf3d -p /sbin/ldconfig
%postun graf3d -p /sbin/ldconfig
%post hbook -p /sbin/ldconfig
%postun hbook -p /sbin/ldconfig
%post hist -p /sbin/ldconfig
%postun hist -p /sbin/ldconfig
%post hist-painter -p /sbin/ldconfig
%postun hist-painter -p /sbin/ldconfig
%post io -p /sbin/ldconfig
%postun io -p /sbin/ldconfig
%post mathcore -p /sbin/ldconfig
%postun mathcore -p /sbin/ldconfig
%post matrix -p /sbin/ldconfig
%postun matrix -p /sbin/ldconfig
%post minuit -p /sbin/ldconfig
%postun minuit -p /sbin/ldconfig
%post net -p /sbin/ldconfig
%postun net -p /sbin/ldconfig
%post reflex -p /sbin/ldconfig
%postun reflex -p /sbin/ldconfig
%post tree -p /sbin/ldconfig
%postun tree -p /sbin/ldconfig

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

%files core -f includelist-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/memprobe
%attr(755,root,root) %{_bindir}/rlibmap
%attr(755,root,root) %{_bindir}/rmkdepend
%attr(755,root,root) %{_bindir}/root-config
%attr(755,root,root) %{_libdir}/%{name}/libCore.so
%{_libdir}/%{name}/libCore.rootmap
%attr(755,root,root) %{_libdir}/%{name}/libNew.so
%attr(755,root,root) %{_libdir}/%{name}/libRint.so
%{_libdir}/%{name}/libRint.rootmap
%attr(755,root,root) %{_libdir}/%{name}/libThread.so
%{_libdir}/%{name}/libThread.rootmap
%attr(755,root,root) %{_libdir}/%{name}/lib[^R]*Dict.so
%{_libdir}/%{name}/lib[^R]*Dict.rootmap
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/class.rules
%{_datadir}/%{name}/gdb-backtrace.sh
%{_datadir}/%{name}/root.mimes
%{_datadir}/%{name}/system.rootauthrc
%{_datadir}/%{name}/system.rootdaemonrc
%{_datadir}/%{name}/system.rootrc
%dir %{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/plugins/*
%{_includedir}/%{name}/RConfigOptions.h
%{_includedir}/%{name}/RConfigure.h
%{_includedir}/%{name}/compiledata.h
%{_includedir}/%{name}/rmain.cxx
%dir %{_includedir}/%{name}/Math
%{_aclocaldir}/root.m4
%{_mandir}/man1/memprobe.1*
%{_mandir}/man1/rmkdepend.1*
%{_mandir}/man1/rlibmap.1*
%{_mandir}/man1/root-config.1*
%{_mandir}/man1/system.rootdaemonrc.1*

%files cint -f includelist-cint-cint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rootcint
%{_mandir}/man1/rootcint.1*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libCint.so
%attr(755,root,root) %{_libdir}/%{name}/cint
%dir %{_includedir}/%{name}

%files reflex -f includelist-cint-reflex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/genmap
%attr(755,root,root) %{_bindir}/genreflex
%attr(755,root,root) %{_bindir}/genreflex-rootcint
%{_mandir}/man1/genmap.1*
%{_mandir}/man1/genreflex.1*
%{_mandir}/man1/genreflex-rootcint.1*
%attr(755,root,root) %{_libdir}/%{name}/libReflex.so
%attr(755,root,root) %{_libdir}/%{name}/libReflexDict.so
%{_libdir}/%{name}/libReflexDict.rootmap
%attr(755,root,root) %{_libdir}/%{name}/python
%dir %{_includedir}/%{name}/Reflex
%dir %{_includedir}/%{name}/Reflex/Builder
%dir %{_includedir}/%{name}/Reflex/internal

%files doc
%defattr(644,root,root,755)
#%%doc %{_docdir}/%{name}-%{version}/html

%files geom -f includelist-geom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libGeom.so
%{_libdir}/%{name}/libGeom.rootmap
%attr(755,root,root) %{_libdir}/%{name}/libGeomBuilder.so
%{_libdir}/%{name}/libGeomBuilder.rootmap
%attr(755,root,root) %{_libdir}/%{name}/libGeomPainter.so
%{_libdir}/%{name}/libGeomPainter.rootmap
%{_datadir}/%{name}/plugins/TGeoManagerEditor/P010_TGeoManagerEditor.C
%{_datadir}/%{name}/plugins/TVirtualGeoPainter/P010_TGeoPainter.C
%{_datadir}/%{name}/RadioNuclides.txt

%files graf -f includelist-graf2d-graf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libGraf.so
%{_libdir}/%{name}/libGraf.rootmap
%{_datadir}/%{name}/plugins/TMinuitGraph/P010_TGraph.C

%files graf-asimage -f includelist-graf2d-asimage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libASImage.so
%attr(755,root,root) %{_libdir}/%{name}/libASImageGui.so

%files graf-gpad -f includelist-graf2d-gpad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libGpad.so
%{_libdir}/%{name}/libGpad.rootmap
%dir %{_datadir}/%{name}/plugins/TVirtualPad
%{_datadir}/%{name}/plugins/TVirtualPad/P010_TPad.C

%files graf-postscript -f includelist-graf2d-postscript
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libPostscript.so
%{_libdir}/%{name}/libPostscript.rootmap
%dir %{_datadir}/%{name}/plugins/TVirtualPS
%{_datadir}/%{name}/plugins/TVirtualPS/P010_TPostScript.C
%{_datadir}/%{name}/plugins/TVirtualPS/P020_TSVG.C
%{_datadir}/%{name}/plugins/TVirtualPS/P030_TPDF.C
%{_datadir}/%{name}/plugins/TVirtualPS/P040_TImageDump.C

%files graf3d -f includelist-graf3d-g3d
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libGraf3d.so
%{_libdir}/%{name}/libGraf3d.rootmap
%dir %{_datadir}/%{name}/plugins/TView
%{_datadir}/%{name}/plugins/TView/P010_TView3D.C

%files hbook -f includelist-hist-hbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g2root
%attr(755,root,root) %{_bindir}/h2root
%{_mandir}/man1/g2root.1*
%{_mandir}/man1/h2root.1*
%attr(755,root,root) %{_libdir}/%{name}/libminicern.so
%attr(755,root,root) %{_libdir}/%{name}/libHbook.so
%{_libdir}/%{name}/libHbook.rootmap

%files hist -f includelist-hist-hist
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libHist.so
%{_libdir}/%{name}/libHist.rootmap

%files hist-painter -f includelist-hist-histpainter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libHistPainter.so
%{_libdir}/%{name}/libHistPainter.rootmap
%{_datadir}/%{name}/plugins/TVirtualHistPainter/P010_THistPainter.C
%{_datadir}/%{name}/plugins/TVirtualGraphPainter/P010_TGraphPainter.C

%files io -f includelist-io-io
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libRIO.so
%{_libdir}/%{name}/libRIO.rootmap
%{_datadir}/%{name}/plugins/TArchiveFile/P010_TZIPFile.C
%{_datadir}/%{name}/plugins/TVirtualStreamerInfo/P010_TStreamerInfo.C

%files mathcore -f includelist-math-mathcore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libMathCore.so
%{_libdir}/%{name}/libMathCore.rootmap
%dir %{_includedir}/%{name}/Fit

%files matrix -f includelist-math-matrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libMatrix.so
%{_libdir}/%{name}/libMatrix.rootmap

%files minuit -f includelist-math-minuit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libMinuit.so
%{_libdir}/%{name}/libMinuit.rootmap
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P020_TMinuitMinimizer.C
%{_datadir}/%{name}/plugins/ROOT@@Math@@Minimizer/P060_TLinearMinimizer.C
%{_datadir}/%{name}/plugins/TVirtualFitter/P010_TFitter.C

%files net -f includelist-net-net
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libNet.so
%{_libdir}/%{name}/libNet.rootmap
%{_datadir}/%{name}/plugins/TApplication/P010_TApplicationRemote.C
%{_datadir}/%{name}/plugins/TApplication/P020_TApplicationServer.C
%{_datadir}/%{name}/plugins/TFile/P010_TWebFile.C
%{_datadir}/%{name}/plugins/TSystem/P050_TWebSystem.C
%{_datadir}/%{name}/plugins/TVirtualMonitoringWriter/P020_TSQLMonitoringWriter.C

%files proof-pq2 -f includelist-proof-pq2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pq2*
%{_mandir}/man1/pq2*.1*

%files tree -f includelist-tree-tree
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libTree.so
%{_libdir}/%{name}/libTree.rootmap
