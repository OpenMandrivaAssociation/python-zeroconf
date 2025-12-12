%global debug_package %{nil}
%define module zeroconf

Name:		python-zeroconf
Summary:	Multicast DNS Service Discovery for Python
Version:	0.148.0
Release:	1
Group:		Development/Python
License:	LGPL-2.1-or-later
URL:		https://github.com/python-zeroconf/python-zeroconf
Source0:	https://files.pythonhosted.org/packages/source/z/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(ifaddr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


%description
Multicast DNS Service Discovery for Python

%prep
%autosetup -n %{module}-%{version} -p1
# no coverage checks
sed -Ei 's/--cov(-|=)[^ "]+//g' pyproject.toml

%build
export REQUIRE_CYTHON=1
export LDFLAGS="%{ldflags} -lpython%{pyver}"
%py_build

%install
%py_install

%files
%doc README.rst
%license COPYING
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
