%define upstream_name    App-Nopaste
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Easy access to any pastebin
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WWW::Mechanize)
BuildRequires:	perl(Config::INI::Reader)
BuildRequires:	perl(WWW::Pastebin::PastebinCom::Create)
BuildRequires:	perl(Browser::Open)
BuildRequires:	perl(Clipboard)
BuildRequires:	perl(Config::GitLike)
BuildArch:	noarch

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the name
nopaste).

Each pastebin is slightly different. When one pastebin goes down (I'm
looking at you, the http://paste.husk.org manpage), then you have to find a
new one. And if you usually use a script to publish text, then it's too
much hassle.

This module aims to smooth out the differences between pastebins, and
provides redundancy: if one site doesn't work, it just tries a different
one.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/App
%{_bindir}/nopaste
%{_mandir}/man1/nopaste.1*
%{_mandir}/man3/*

%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 648056
- update to new version 0.28

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.270.0-1
+ Revision: 646399
- update to new version 0.27

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1
+ Revision: 641315
- update to new version 0.26

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 628696
- update to new version 0.25

* Thu Dec 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 624069
- update to new version 0.24

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 601859
- update to new version 0.23

* Wed Jul 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 562708
- import perl-App-Nopaste


* Fri Feb 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 512125
- new version

* Sat Jan 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 485155
- new version

* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 474524
- new version
- import perl-App-Nopaste


* Fri Jan 09 2009 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist

