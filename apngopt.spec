Summary:	APNG Optimizer
Summary(pl.UTF-8):	Optymalizator plików APNG
Name:		apngopt
Version:	1.4
Release:	2
License:	Zlib (BSD-like)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/apng/%{name}-%{version}-src.zip
# Source0-md5:	cb214b0b30b9b89ac25f41fb84ca5559
URL:		https://sourceforge.net/projects/apng/
BuildRequires:	advancecomp-7z-devel
BuildRequires:	libpng-devel >= 2:1.6.17
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel >= 1.2.8
BuildRequires:	zopfli-devel
Requires:	libpng >= 2:1.6.17
Requires:	zlib >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APNG Optimizer makes APNG files smaller.

%description -l pl.UTF-8
APNG Optimizer zmniejsza pliki APNG.

%prep
%setup -q -c

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -Wall -o apngopt apngopt.cpp \
	-I/usr/include/adv7z \
	-lpng -ladv7z -lzopfli -lz -lm

%install
rm -rf $RPM_BUILD_ROOT

install -D apngopt $RPM_BUILD_ROOT%{_bindir}/apngopt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/apngopt
