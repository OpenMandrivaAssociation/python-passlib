%define module passlib
%define oname libpass

Name:		python-passlib
Summary:	Comprehensive password hashing framework supporting over 30 schemes
Version:	1.9.3
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
# Use the maintained fork
URL:		https://github.com/notypecheck/passlib
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem: python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# Optional runtime dependencies
Recommends:	python%{pyver}dist(argon2-cffi)
Recommends:	python%{pyver}dist(bcrypt)
Recommends:	python%{pyver}dist(cryptography)

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It is
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%build -a
# This package was renamed from passlib to libpass when it was forked and we
# need to provide the old distinfo for packages that still require it.
%global old_distinfo %{module}-%{version}.dist-info
mkdir %{old_distinfo}
cat > %{old_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: passlib
Version: %{version}
EOF
echo rpm > %{old_distinfo}/INSTALLER

%install -a
install -Dpm755 %{old_distinfo}/* -t %{buildroot}%{python_sitelib}/%{old_distinfo}

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{old_distinfo}
%{python_sitelib}/%{oname}-%{version}.dist-info
