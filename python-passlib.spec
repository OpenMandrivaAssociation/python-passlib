Summary:	comprehensive password hashing framework supporting over 30 schemes
Name:		python-passlib
Version:	1.7.4
Release:	2
License:	BSD
Group:		Development/Python
URL:		https://pypi.org/project/passlib/
Source0:	https://files.pythonhosted.org/packages/source/p/passlib/passlib-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
Passlib is a password hashing library for Python 2 & 3, which provides
cross-platform implementations of over 20 password hashing algorithms,
as well as a framework for managing existing password hashes. It is
designed to be useful for a wide range of tasks, from verifying a hash
found in /etc/shadow, to providing full-strength password hashing for
multi-user application.

%files
%{py_sitedir}/passlib
%{py_sitedir}/passlib-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n passlib-%{version}

%build
%py_build

%install
%py_install

