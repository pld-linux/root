Summary:	root dot files
Summary(pl):	Pliki w katalogu domowym super u¿ytkownika (root)
Name:		root
Version:	1.0
Release:	2
Copyright:	public domain
Group:		Base
Group(pl):	Podstawowe
Source:		root.tar.bz2
Obsoletes:	rootfiles
BuildRoot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
This package contains all the startup files for the root super-user.

%description -l pl
W pakiecie tym znajduj± siê podstawowe pliki z katalogu domowego 
super u¿ytkownika (root-a).

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

cp -a root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(600,root,root,700)
%config(noreplace) %verify(not mtime size md5) /root

%changelog
* Thu Jul 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.5-4d]
- build for PLD Tornado
