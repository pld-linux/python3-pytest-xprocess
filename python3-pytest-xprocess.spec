#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A pytest plugin for managing processes across test runs
Summary(pl.UTF-8):	Wtyczka pytesta do zarządzania procesami między uruchomieniami testów
Name:		python3-pytest-xprocess
Version:	1.0.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-xprocess/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-xprocess/pytest-xprocess-%{version}.tar.gz
# Source0-md5:	697f056ebf13d37cdbb2244f504702c4
# docs missing in sdist, get them from git archive (which isn't usable alone for packaging because of no PKG-INFO and git metadata)
Source1:	https://github.com/pytest-dev/pytest-xprocess/archive/%{version}/pytest-xprocess-%{version}-git.tar.gz
# Source1-md5:	747b07ccca14ca79d9bef6a7a56200e9
URL:		https://pypi.org/project/pytest-xprocess/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:45.0
BuildRequires:	python3-setuptools_scm >= 6.2.3
%if %{with tests}
BuildRequires:	python3-psutil
BuildRequires:	python3-pytest >= 2.8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
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

%package apidocs
Summary:	API documentation for Python pytest_xprocess module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pytest_xprocess
Group:		Documentation

%description apidocs
API documentation for Python pytest_xprocess module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pytest_xprocess.

%prep
%setup -q -n pytest-xprocess-%{version} -a1

%{__mv} pytest-xprocess-%{version}/{docs,CHANGELOG.rst} .
%{__rm} -r pytest-xprocess-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="xprocess.pytest_xprocess" \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/xprocess
%{py3_sitescriptdir}/pytest_xprocess-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
