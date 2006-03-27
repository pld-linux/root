#
Summary:	An object-oriented data analysis environment
Name:		root
Version:	5.10.00
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	ftp://root.cern.ch/%{name}/%{name}_v%{version}.source.tar.gz
# Source0-md5:	158009f95202abaa06ab008add29f86b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n root

%build
./configure linux --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
