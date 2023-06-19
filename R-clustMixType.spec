#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clustMixType
Version  : 0.3.9
Release  : 59
URL      : https://cran.r-project.org/src/contrib/clustMixType_0.3-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clustMixType_0.3-9.tar.gz
Summary  : k-Prototypes Clustering for Mixed Variable-Type Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-tibble
BuildRequires : R-RColorBrewer
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
# Development version of the R Package clustMixType
k-Prototypes Clustering for Mixed Variable-Type Data. For details cf. [R Journal paper](https://journal.r-project.org/archive/2018/RJ-2018-048/index.html).

%prep
%setup -q -n clustMixType
cd %{_builddir}/clustMixType

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671054721

%install
export SOURCE_DATE_EPOCH=1671054721
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/clustMixType/NEWS
/usr/lib64/R/library/clustMixType/R/clustMixType
/usr/lib64/R/library/clustMixType/R/clustMixType.rdb
/usr/lib64/R/library/clustMixType/R/clustMixType.rdx
/usr/lib64/R/library/clustMixType/help/AnIndex
/usr/lib64/R/library/clustMixType/help/aliases.rds
/usr/lib64/R/library/clustMixType/help/clustMixType.rdb
/usr/lib64/R/library/clustMixType/help/clustMixType.rdx
/usr/lib64/R/library/clustMixType/help/figures/logo.png
/usr/lib64/R/library/clustMixType/help/paths.rds
/usr/lib64/R/library/clustMixType/html/00Index.html
/usr/lib64/R/library/clustMixType/html/R.css
/usr/lib64/R/library/clustMixType/tests/testthat.R
/usr/lib64/R/library/clustMixType/tests/testthat/test_basics.R
/usr/lib64/R/library/clustMixType/tests/testthat/test_clustervalidation.R
