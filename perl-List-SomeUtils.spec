#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	List
%define		pnam	SomeUtils
%include	/usr/lib/rpm/macros.perl
Summary:	List::SomeUtils - Provide the stuff missing in List::Util
Summary(pl.UTF-8):	List::SomeUtils - funkcje brakujące w List::Util
Name:		perl-List-SomeUtils
Version:	0.53
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bde33a340a9644368ac2d47d2cac8bb5
URL:		http://search.cpan.org/dist/List-SomeUtils/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Implementation
BuildRequires:	perl-Test-LeakTrace
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::SomeUtils provides some trivial but commonly needed
functionality on lists which is not going to go into List::Util.

%description -l pl.UTF-8
Moduł List::SomeUtils dostarcza kilka trywialnych, ale często
potrzebnych funkcji operujących na listach, a nie dodawanych do
List::Util.

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
%doc Changes
%{perl_vendorlib}/List/SomeUtils.pm
%{perl_vendorlib}/List/SomeUtils
%{_mandir}/man3/List::SomeUtils*.3pm*
