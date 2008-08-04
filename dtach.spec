Summary:	A program that emulates the detach feature of screen
Summary(pl.UTF-8):	Program emulujący funkcję detach ze screena
Name:		dtach
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/dtach/%{name}-%{version}.tar.gz
# Source0-md5:	ec5999f3b6bb67da19754fcb2e5221f3
URL:		http://dtach.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dtach is a program that emulates the detach feature of screen, with
less overhead.  It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%description -l pl.UTF-8
dtach to program emulujący funkcję detach ze screena z mniejszym
narzutem. Został zaprojektowany tak, by być przezroczysty i
nieinwazyjny; zapobiega interpretowaniu wejścia i wyjścia pomiędzy
podłączonymi terminalami a kontrolowanym programem. Konsekwentnie,
działa najlepiej z aplikacjami pełnoekranowymi takimi jak emacs.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name}	$RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
