%define tarname par2cmdline-%{version}

Name:		parchive2
Version:	1.1.1
Release:	1
Summary:	Parchive: par2cmdline is a PAR 2.0 compatible file verification and repair tool.
Group:		Archiving/Other
License:	GPL-2.0-or-later
URL:		https://github.com/Parchive/par2cmdline
# project was formerly maintained at https://parchive.sourceforge.net/
# they have moved development to github
Source:		https://github.com/Parchive/par2cmdline/archive/v%{version}/%{tarname}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	gcc-c++

%description
%{name} / par2cmdline is a PAR 2.0 compatible file verification and repair tool.

par2cmdline is a program for creating and using PAR2 files to detect damage
in data files and repair them if necessary.

It can be used with any kind of file.

%prep
%autosetup -n %{tarname} -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/par2{,create,repair,verify}
%{_mandir}/man1/par2{,create,repair,verify}.1*
