#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-prompt_toolkit
Version  : 3.0.29
Release  : 85
URL      : https://files.pythonhosted.org/packages/59/68/4d80f22e889ea34f20483ae3d4ca3f8d15f15264bcfb75e52b90fb5aefa5/prompt_toolkit-3.0.29.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/68/4d80f22e889ea34f20483ae3d4ca3f8d15f15264bcfb75e52b90fb5aefa5/prompt_toolkit-3.0.29.tar.gz
Summary  : Library for building powerful interactive command lines in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-prompt_toolkit-license = %{version}-%{release}
Requires: pypi-prompt_toolkit-python = %{version}-%{release}
Requires: pypi-prompt_toolkit-python3 = %{version}-%{release}
Requires: pypi(pygments)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pygments)
BuildRequires : pypi(wcwidth)

%description
Python Prompt Toolkit
=====================
|Build Status|  |AppVeyor|  |PyPI|  |RTD|  |License|  |Codecov|

%package license
Summary: license components for the pypi-prompt_toolkit package.
Group: Default

%description license
license components for the pypi-prompt_toolkit package.


%package python
Summary: python components for the pypi-prompt_toolkit package.
Group: Default
Requires: pypi-prompt_toolkit-python3 = %{version}-%{release}

%description python
python components for the pypi-prompt_toolkit package.


%package python3
Summary: python3 components for the pypi-prompt_toolkit package.
Group: Default
Requires: python3-core
Provides: pypi(prompt_toolkit)
Requires: pypi(wcwidth)

%description python3
python3 components for the pypi-prompt_toolkit package.


%prep
%setup -q -n prompt_toolkit-3.0.29
cd %{_builddir}/prompt_toolkit-3.0.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649100838
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-prompt_toolkit
cp %{_builddir}/prompt_toolkit-3.0.29/LICENSE %{buildroot}/usr/share/package-licenses/pypi-prompt_toolkit/3f9fcc5a3e1595282b9841f8258755e753f26461
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-prompt_toolkit/3f9fcc5a3e1595282b9841f8258755e753f26461

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
