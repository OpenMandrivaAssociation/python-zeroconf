Summary:	Multicast DNS Service Discovery for Python
Name:		python-zeroconf
Version:	0.38.1
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://pypi.org/project/zeroconf/
Source0:	https://files.pythonhosted.org/packages/9c/74/74a032f5841fd4ca24e89aa4b0b35f62321b96dda3c8e7d73665324e0984/zeroconf-0.38.1.tar.gz
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
