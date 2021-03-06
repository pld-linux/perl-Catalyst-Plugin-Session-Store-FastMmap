#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Catalyst
%define	pnam	Plugin-Session-Store-FastMmap
Summary:	Catalyst::Plugin::Session::FastMmap - FastMmap sessions for Catalyst
Summary(pl.UTF-8):	Catalyst::Plugin::Session::FastMmap - sesje FastMmap dla Catalysta
Name:		perl-Catalyst-Plugin-Session-Store-FastMmap
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	75c545a9b1cd92b294aa950677bb631a
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-FastMmap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-FastMmap
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.01
BuildRequires:	perl-Path-Class
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage
plugin for Catalyst that uses an mmap'ed file to act as a shared
memory interprocess cache. It is based on Cache::FastMmap.

%description -l pl.UTF-8
Catalyst::Plugin::Session::Store::FastMmap to wtyczka szybkiego
przechowywania danych sesji dla Catalysta używająca mmapowanego pliku
jako pamięci podręcznej współdzielonej między procesami. Jest oparta
na Cache::FastMmap.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/*.pm
%{_mandir}/man3/*
