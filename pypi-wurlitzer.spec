#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wurlitzer
Version  : 3.0.2
Release  : 27
URL      : https://files.pythonhosted.org/packages/e8/2c/3e57755689fcf75aa25f6afba064d3891e9864ef43a24745575c86b12ad4/wurlitzer-3.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/2c/3e57755689fcf75aa25f6afba064d3891e9864ef43a24745575c86b12ad4/wurlitzer-3.0.2.tar.gz
Summary  : Capture C-level output in context managers
Group    : Development/Tools
License  : MIT
Requires: pypi-wurlitzer-license = %{version}-%{release}
Requires: pypi-wurlitzer-python = %{version}-%{release}
Requires: pypi-wurlitzer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Wurlitzer
Capture C-level stdout/stderr pipes in Python via `os.dup2`.
For more details on why this is needed, please read [this blog post](https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/).

%package license
Summary: license components for the pypi-wurlitzer package.
Group: Default

%description license
license components for the pypi-wurlitzer package.


%package python
Summary: python components for the pypi-wurlitzer package.
Group: Default
Requires: pypi-wurlitzer-python3 = %{version}-%{release}

%description python
python components for the pypi-wurlitzer package.


%package python3
Summary: python3 components for the pypi-wurlitzer package.
Group: Default
Requires: python3-core
Provides: pypi(wurlitzer)

%description python3
python3 components for the pypi-wurlitzer package.


%prep
%setup -q -n wurlitzer-3.0.2
cd %{_builddir}/wurlitzer-3.0.2
pushd ..
cp -a wurlitzer-3.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361093
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wurlitzer
cp %{_builddir}/wurlitzer-3.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-wurlitzer/360b2fe584a00d26d9643bf330bf0d36a49257b8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wurlitzer/360b2fe584a00d26d9643bf330bf0d36a49257b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
