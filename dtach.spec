Summary:	A program that emulates the detach feature of screen
Name:		dtach
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/dtach/%{name}-%{version}.tar.gz
# Source0-md5:	3ed45d8a52539c25302302a419e1358e
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dtach is a program that emulates the detach feature of screen, with
less overhead.  It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%prep
%setup -q

%build
%configure \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
