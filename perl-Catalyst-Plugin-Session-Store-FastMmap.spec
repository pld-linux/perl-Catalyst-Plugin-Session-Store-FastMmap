#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-Store-FastMmap
Summary:	Catalyst::Plugin::Session::FastMmap - FastMmap sessions for Catalyst
Summary(pl):	Catalyst::Plugin::Session::FastMmap - sesje FastMmap dla Catalysta
Name:		perl-Catalyst-Plugin-Session-Store-FastMmap
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4bb42dc7c9c4300240b1d0a3e88f37cd
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

%description -l pl
Catalyst::Plugin::Session::Store::FastMmap to wtyczka szybkiego
przechowywania danych sesji dla Catalysta u¿ywaj±ca mmapowanego pliku
jako pamiêci podrêcznej wspó³dzielonej miêdzy procesami. Jest oparta
na Cache::FastMmap.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/*.pm
%{_mandir}/man3/*
