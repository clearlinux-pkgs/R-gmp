#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gmp
Version  : 0.5.13.1
Release  : 8
URL      : https://cran.r-project.org/src/contrib/gmp_0.5-13.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gmp_0.5-13.1.tar.gz
Summary  : Multiple Precision Arithmetic
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gmp-lib
BuildRequires : R-Rmpfr
BuildRequires : clr-R-helpers
BuildRequires : gmp-dev
BuildRequires : mpfr-dev

%description
prime number tests, matrix computation), "arithmetic without limitations"
 using the C library GMP (GNU Multiple Precision Arithmetic).

%package lib
Summary: lib components for the R-gmp package.
Group: Libraries

%description lib
lib components for the R-gmp package.


%prep
%setup -q -c -n gmp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521244152

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521244152
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gmp|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gmp/DESCRIPTION
/usr/lib64/R/library/gmp/INDEX
/usr/lib64/R/library/gmp/Meta/Rd.rds
/usr/lib64/R/library/gmp/Meta/data.rds
/usr/lib64/R/library/gmp/Meta/features.rds
/usr/lib64/R/library/gmp/Meta/hsearch.rds
/usr/lib64/R/library/gmp/Meta/links.rds
/usr/lib64/R/library/gmp/Meta/nsInfo.rds
/usr/lib64/R/library/gmp/Meta/package.rds
/usr/lib64/R/library/gmp/NAMESPACE
/usr/lib64/R/library/gmp/R/gmp
/usr/lib64/R/library/gmp/R/gmp.rdb
/usr/lib64/R/library/gmp/R/gmp.rdx
/usr/lib64/R/library/gmp/data/Oakley1.R
/usr/lib64/R/library/gmp/data/Oakley2.R
/usr/lib64/R/library/gmp/help/AnIndex
/usr/lib64/R/library/gmp/help/aliases.rds
/usr/lib64/R/library/gmp/help/gmp.rdb
/usr/lib64/R/library/gmp/help/gmp.rdx
/usr/lib64/R/library/gmp/help/paths.rds
/usr/lib64/R/library/gmp/html/00Index.html
/usr/lib64/R/library/gmp/html/R.css
/usr/lib64/R/library/gmp/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gmp/libs/gmp.so
/usr/lib64/R/library/gmp/libs/gmp.so.avx2
/usr/lib64/R/library/gmp/libs/gmp.so.avx512
