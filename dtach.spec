Summary:	A program that emulates the detach feature of screen
Summary(pl):	Program emuluj±cy funkcjê detach ze screena
Name:		dtach
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/dtach/%{name}-%{version}.tar.gz
# Source0-md5:	9aa11433d5a5b4b9fed271f10102cf6f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dtach is a program that emulates the detach feature of screen, with
less overhead.  It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%description -l pl
dtach to program emuluj±cy funkcjê detach ze screena z mniejszym
narzutem. Zosta³ zaprojektowany tak, by byæ przezroczysty i
nieinwazyjny; zapobiega interpretowaniu wej¶cia i wyj¶cia pomiêdzy
pod³±czonymi terminalami a kontrolowanym programem. Konsekwentnie,
dzia³a najlepiej z aplikacjami pe³noekranowymi takimi jak emacs.

%prep
%setup -q

%build
%configure

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
