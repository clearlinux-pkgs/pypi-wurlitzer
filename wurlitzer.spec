#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wurlitzer
Version  : 2.0.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/02/2e/56d35781ef9ca92e26ff1fb3f351615a70083a95085d56d47451860925c5/wurlitzer-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/02/2e/56d35781ef9ca92e26ff1fb3f351615a70083a95085d56d47451860925c5/wurlitzer-2.0.1.tar.gz
Summary  : Capture C-level output in context managers
Group    : Development/Tools
License  : MIT
Requires: wurlitzer-license = %{version}-%{release}
Requires: wurlitzer-python = %{version}-%{release}
Requires: wurlitzer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Capture C-level stdout/stderr pipes in Python via `os.dup2`.

%package license
Summary: license components for the wurlitzer package.
Group: Default

%description license
license components for the wurlitzer package.


%package python
Summary: python components for the wurlitzer package.
Group: Default
Requires: wurlitzer-python3 = %{version}-%{release}

%description python
python components for the wurlitzer package.


%package python3
Summary: python3 components for the wurlitzer package.
Group: Default
Requires: python3-core
Provides: pypi(wurlitzer)

%description python3
python3 components for the wurlitzer package.


%prep
%setup -q -n wurlitzer-2.0.1
cd %{_builddir}/wurlitzer-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605725687
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wurlitzer
cp %{_builddir}/wurlitzer-2.0.1/LICENSE %{buildroot}/usr/share/package-licenses/wurlitzer/360b2fe584a00d26d9643bf330bf0d36a49257b8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wurlitzer/360b2fe584a00d26d9643bf330bf0d36a49257b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
