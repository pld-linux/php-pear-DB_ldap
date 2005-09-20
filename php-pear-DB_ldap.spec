%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	ldap
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DB interface to LDAP server
Summary(pl):	%{_pearname} - interfejs DB do serwerów LDAP
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	18455feab68bc0cd4ebada001f2e6717
URL:		http://pear.php.net/package/DB_ldap/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::DB_ldap class provides a DB compliant interface to LDAP
servers.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::DB_ldap dostarcza zgodny z DB interfejs do serwerów LDAP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
