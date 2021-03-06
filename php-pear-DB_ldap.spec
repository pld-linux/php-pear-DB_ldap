%define		status		stable
%define		pearname	DB_ldap
Summary:	%{pearname} - DB interface to LDAP server
Summary(pl.UTF-8):	%{pearname} - interfejs DB do serwerów LDAP
Name:		php-pear-%{pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	590f37e1ec0fef3ca6c9cca29c47889f
URL:		http://pear.php.net/package/DB_ldap/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-DB
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::DB_ldap class provides a DB compliant interface to LDAP
servers.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa PEAR::DB_ldap dostarcza zgodny z DB interfejs do serwerów LDAP.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/DB_ldap/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/DB/*.php
