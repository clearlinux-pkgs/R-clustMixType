#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clustMixType
Version  : 0.2.1
Release  : 18
URL      : https://cran.r-project.org/src/contrib/clustMixType_0.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clustMixType_0.2-1.tar.gz
Summary  : k-Prototypes Clustering for Mixed Variable-Type Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-assertthat
BuildRequires : R-RColorBrewer
BuildRequires : R-assertthat
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n clustMixType

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552793061

%install
export SOURCE_DATE_EPOCH=1552793061
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clustMixType
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clustMixType
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clustMixType
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  clustMixType || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clustMixType/CITATION
/usr/lib64/R/library/clustMixType/DESCRIPTION
/usr/lib64/R/library/clustMixType/INDEX
/usr/lib64/R/library/clustMixType/Meta/Rd.rds
/usr/lib64/R/library/clustMixType/Meta/features.rds
/usr/lib64/R/library/clustMixType/Meta/hsearch.rds
/usr/lib64/R/library/clustMixType/Meta/links.rds
/usr/lib64/R/library/clustMixType/Meta/nsInfo.rds
/usr/lib64/R/library/clustMixType/Meta/package.rds
/usr/lib64/R/library/clustMixType/NAMESPACE
/usr/lib64/R/library/clustMixType/R/clustMixType
/usr/lib64/R/library/clustMixType/R/clustMixType.rdb
/usr/lib64/R/library/clustMixType/R/clustMixType.rdx
/usr/lib64/R/library/clustMixType/help/AnIndex
/usr/lib64/R/library/clustMixType/help/aliases.rds
/usr/lib64/R/library/clustMixType/help/clustMixType.rdb
/usr/lib64/R/library/clustMixType/help/clustMixType.rdx
/usr/lib64/R/library/clustMixType/help/paths.rds
/usr/lib64/R/library/clustMixType/html/00Index.html
/usr/lib64/R/library/clustMixType/html/R.css
/usr/lib64/R/library/clustMixType/tests/testthat.R
/usr/lib64/R/library/clustMixType/tests/testthat/test_basics.R
/usr/lib64/R/library/clustMixType/tests/testthat/test_clustervalidation.R
