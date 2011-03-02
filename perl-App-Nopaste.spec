%define upstream_name    App-Nopaste
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Easy access to any pastebin
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Mechanize)
BuildRequires: perl(Config::INI::Reader)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/App
%{_bindir}/nopaste
%{_mandir}/man1/nopaste.1*
%{_mandir}/man3/*


