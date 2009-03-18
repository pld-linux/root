#
# TODO: pass LDFLAGS
#
Summary:	An object-oriented data analysis environment
Summary(pl.UTF-8):	Obiektowo zorientowane środowisko do analizowania danych
Name:		root
Version:	5.22.00
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	ftp://root.cern.ch/root/%{name}_v%{version}.source.tar.gz
# Source0-md5:	0d621315cf82abb02b2db951461be6f3
URL:		http://root.cern.ch/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An object-oriented data analysis environment.

%description -l pl.UTF-8
Obiektowo zorientowane środowisko do analizowania danych.

%prep
%setup -q -n %{name}

%build
./configure linux \
	--prefix="%{_prefix}" \
	--with-cc="%{__cc} %{rpmcflags}" \
	--with-cxx="%{__cxx} %{rpmcxxflags}"
#	--with-ld="%{__cxx} %{rpmldflags}"
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
