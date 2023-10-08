#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A pytest plugin for managing processes across test runs
Summary(pl.UTF-8):	Wtyczka pytesta do zarządzania procesami między uruchomieniami testów
Name:		python-pytest-xprocess
# keep 0.14.x here for python2 support
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-xprocess/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-xprocess/pytest-xprocess-%{version}.tar.gz
# Source0-md5:	e9557702d10022fd39fd9d5bee56bc80
URL:		https://pypi.org/project/pytest-xprocess/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-xprocess provides a "xprocess" fixture which helps you to
ensure that one or more longer-running processes are present for your
tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).

%description -l pl.UTF-8
pytest-xprocess udostępnia wyposarzenie "xprocess", pomagający
zapewnić, że istnieje jeden lub więcej dłużej działających procesów w
trakcie testów. Można ich użyć do uruchomienia i wstępnej konfiguracji
bez danych specyficznych dla testów (Postgres, Couchdb...).

%package -n python3-pytest-xprocess
Summary:	A pytest plugin for managing processes across test runs
Summary(pl.UTF-8):	Wtyczka pytesta do zarządzania procesami między uruchomieniami testów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pytest-xprocess
pytest-xprocess provides a "xprocess" fixture which helps you to
ensure that one or more longer-running processes are present for your
tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).

%description -n python3-pytest-xprocess -l pl.UTF-8
pytest-xprocess udostępnia wyposarzenie "xprocess", pomagający
zapewnić, że istnieje jeden lub więcej dłużej działających procesów w
trakcie testów. Można ich użyć do uruchomienia i wstępnej konfiguracji
bez danych specyficznych dla testów (Postgres, Couchdb...).

%prep
%setup -q -n pytest-xprocess-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-pytest-xprocess-%{version}
cp -p example/*.py $RPM_BUILD_ROOT%{_examplesdir}/python-pytest-xprocess-%{version}
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-pytest-xprocess-%{version}
cp -p example/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-pytest-xprocess-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_xprocess.py[co]
%{py_sitescriptdir}/xprocess.py[co]
%{py_sitescriptdir}/pytest_xprocess-%{version}-py*.egg-info
%{_examplesdir}/python-pytest-xprocess-%{version}
%endif

%if %{with python3}
%files -n python3-pytest-xprocess
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_xprocess.py
%{py3_sitescriptdir}/xprocess.py
%{py3_sitescriptdir}/__pycache__/pytest_xprocess.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/xprocess.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_xprocess-%{version}-py*.egg-info
%{_examplesdir}/python3-pytest-xprocess-%{version}
%endif
