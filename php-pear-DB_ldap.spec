%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       ldap
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - DB interface to LDAP server
Summary(pl):	%{_pearname} - interfejs DB do serwer�w LDAP
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::DB_ldap class provides a DB compliant interface to LDAP
servers.

%description -l pl
Klasa PEAR::DB_ldap dostarcza zgodny z DB interfejs do serwer�w LDAP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
