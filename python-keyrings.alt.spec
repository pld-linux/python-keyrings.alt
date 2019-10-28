#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# py.test tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Alternate keyring backend implementations for use with the keyring module
Summary(pl.UTF-8):	Alternatywne implementacje backendów dla modułu keyring
Name:		python-keyrings.alt
Version:	2.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/keyrings.alt
Source0:	https://files.pythonhosted.org/packages/source/k/keyrings.alt/keyrings.alt-%{version}.tar.gz
# Source0-md5:	f7354b203095cf557fce94b4b818366b
Patch0:		%{name}-fs.patch
URL:		https://pypi.python.org/pypi/keyrings.alt
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:28.2
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-Crypto
BuildRequires:	python-backports.unittest_mock
BuildRequires:	python-fs >= 2.0
BuildRequires:	python-gdata
BuildRequires:	python-keyczar
BuildRequires:	python-keyring >= 10.3.1
BuildRequires:	python-pytest >= 2.8
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 1:28.2
BuildRequires:	python3-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python3-Crypto
BuildRequires:	python3-fs >= 2.0
BuildRequires:	python3-keyring >= 10.3.1
BuildRequires:	python3-pytest >= 2.8
%endif
%endif
%if %{with doc}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-rst.linker
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternate keyring backend implementations for use with the keyring
module.

%description -l pl.UTF-8
Alternatywne implementacje backendów dla modułu keyring.

%package -n python3-keyrings.alt
Summary:	Alternate keyring backend implementations for use with the keyring module
Summary(pl.UTF-8):	Alternatywne implementacje backendów dla modułu keyring
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-keyrings.alt
Alternate keyring backend implementations for use with the keyring
module.

%description -n python3-keyrings.alt -l pl.UTF-8
Alternatywne implementacje backendów dla modułu keyring.

%package apidocs
Summary:	API documentation for Python keyrings.alt library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Pythona keyrings.alt
Group:		Documentation

%description apidocs
API documentation for Python keyrings.alt library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Pythona keyrings.alt.

%prep
%setup -q -n keyrings.alt-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%{?with_tests:PYTHONDIR=$(pwd) %{__python} -m pytest tests}
%endif

%if %{with python3}
%py3_build %{?with_doc:build_sphinx}

%{?with_tests:PYTHONDIR=$(pwd) %{__python3} -m pytest tests}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%dir %{py_sitescriptdir}/keyrings
%{py_sitescriptdir}/keyrings/alt
%{py_sitescriptdir}/keyrings.alt-%{version}-py*-nspkg.pth
%{py_sitescriptdir}/keyrings.alt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-keyrings.alt
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%dir %{py3_sitescriptdir}/keyrings
%{py3_sitescriptdir}/keyrings/alt
%{py3_sitescriptdir}/keyrings.alt-%{version}-py*-nspkg.pth
%{py3_sitescriptdir}/keyrings.alt-%{version}-py*.egg-info
%endif

%if %{with python3} && %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc build-3/sphinx/html/{_static,*.html,*.js}
%endif
