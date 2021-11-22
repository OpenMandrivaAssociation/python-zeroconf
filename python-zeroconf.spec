Summary:	Multicast DNS Service Discovery for Python
Name:		python-zeroconf
Version:	0.37.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://pypi.org/project/zeroconf/
Source0:	https://files.pythonhosted.org/packages/5e/82/791c22d47f4622ce83553756461b682a0a1be1cbc0251201c6cf58a3fd66/zeroconf-0.37.0.tar.gz
BuildRequires:	python3dist(setuptools)
BuildArch:	noarch

%description
Multicast DNS Service Discovery for Python

%files
%{py_puresitedir}/zeroconf
%{py_puresitedir}/zeroconf*.egg-info

#------------------------------------------------------------
%prep
%autosetup -p1 -n zeroconf-%{version}

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1

%check
%{__python} setup.py \
	check
