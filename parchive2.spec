%define tarname par2cmdline-%{version}

Name:		parchive2
Version:	1.0.0
Release:	1
Summary:	Parchive: par2cmdline is a PAR 2.0 compatible file verification and repair tool.
Group:		Archiving/Other
License:	GPL-2.0-or-later
URL:        https://github.com/Parchive/par2cmdline
# project was formerly maintained at https://parchive.sourceforge.net/
# they have moved development to github
Source: 	https://github.com/Parchive/par2cmdline/archive/v%{version}/%{tarname}.tar.gz

BuildRequires:	gcc-c++

%description
%{name} / par2cmdline is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary.

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
%{_bindir}/par2*
%{_mandir}/man1/par2.1.*
%doc AUTHORS COPYING README.md ROADMAP
