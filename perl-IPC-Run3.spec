Name:           perl-IPC-Run3
Version:        0.043
Release:        3%{?dist}
Summary:        Run a subprocess in batch mode
License:        (GPL+ or Artistic) or BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Run3/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# For improved tests
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%prep
%setup -q -n IPC-Run3-%{version}
# Perms in tarballs are broken 
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.043-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 0.043-1
- Upstream update.
- Reflect upstream URL having changed.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.042-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.042-3
- Change %summary.

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.042-2
- fix license tag (technically, it was correct before, but this keeps rpmlint from
  flagging this package as a false positive)

* Mon Aug 25 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.042-1
- Upstream update.

* Fri Aug 08 2008 Ralf Corsépius <rc040203@freenet.de> 0.041-1
- Upstream update.

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.040-5
- reorder license tag so it doesn't flag as a false positive

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.040-4
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.040-3
- Rebuild for perl 5.10 (again), disable tests for first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.040-2
- rebuild normally, second pass

* Sat Jan 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.040-1.1
- rebuild for new perl, disable tests and TPC for first pass

* Fri Dec 28 2007 Ralf Corsépius <rc040203@freenet.de> 0.040-1
- Upstream update.
- chmod -x files from source tarball.

* Tue Nov 27 2007 Ralf Corsépius <rc040203@freenet.de> 0.039-2
- Bump release to please koji suckage.

* Tue Nov 27 2007 Ralf Corsépius <rc040203@freenet.de> 0.039-1
- Upstream update.

* Fri Sep 07 2007 Ralf Corsépius <rc040203@freenet.de> 0.037-2
- Initial import.
- Update license tag.

* Tue Aug 07 2007 Ralf Corsépius <rc040203@freenet.de> 0.037-1
- Initial submission.
