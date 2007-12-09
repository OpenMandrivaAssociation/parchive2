%define name parchive2
%define version 0.4
%define release %mkrel 3
%define tarname par2cmdline-%{version}

Summary:	Parchive: Parity Archive Volume Set
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Archiving/Other
License:	GPL
URL: 		http://parchive.sourceforge.net/
# http://prdownloads.sourceforge.net/parchive/%{tarname}.tar.gz?download
Source: 	http://prdownloads.sourceforge.net/parchive/%{tarname}.tar.bz2
Patch0:		par2cmdline-gcc4.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description

The idea behind this project is to provide a tool to apply the data-
recovery capability concepts of RAID-like systems to the posting and
recovery of multi-part archives on Usenet. With a parity archive, this
tool, and all but one part of a multi-part set you can recover the
missing part.

The key to this mission is a clean file format specification which
provides all the necessary capabilities for programs to easily verify
and regenerate single missing parts out of a set of archives.

We might just be able to make binary posting and downloading on Usenet a
little easier. That's a pretty cool goal!

par2 is complete rewrite of parchive with much additional advantages.
Read all about them on this page:
  http://www.pbclements.co.uk/QuickPar/AboutPAR2.htm

Tip of the day: alias par='par2 r *.((p|P)??|par2)'


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %tarname

%patch0 -p1

%build
%configure
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc AUTHORS COPYING README ROADMAP
%{_bindir}/*

