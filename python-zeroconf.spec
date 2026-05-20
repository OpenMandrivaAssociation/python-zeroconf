%global debug_package %{nil}
%define module zeroconf

Name:		python-zeroconf
Summary:	Multicast DNS Service Discovery for Python
Version:	0.149.9
Release:	1
Group:		Development/Python
License:	LGPL-2.1-or-later
URL:		https://github.com/python-zeroconf/python-zeroconf
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(ifaddr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Multicast DNS Service Discovery for Python

%prep -a
# no coverage checks
sed -Ei 's/--cov(-|=)[^ "]+//g' pyproject.toml

%build -p
export REQUIRE_CYTHON=1
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc README.rst
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
