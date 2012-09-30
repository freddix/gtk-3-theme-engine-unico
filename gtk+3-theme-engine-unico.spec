Summary:	Unico Gtk+3 theming engine
Name:		gtk+3-theme-engine-unico
Version:	1.0.2
Release:	4
License:	LGPL 3.0
Group:		Libraries
Source0:	https://launchpad.net/unico/1.0/1.0.2/+download/unico-%{version}.tar.gz
# Source0-md5:	1#9fb3ecc36d4d13b4a76e26a4ebd6412
Patch0:		%{name}-bug999277.patch
URL:		https://launchpad.net/unico
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	pkg-config
Requires:	gtk+3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful
theming engine for Gtk+3 and newer. It's the first Gtk+ engine
written with Gtk+ style context APIs in mind, using CSS as first class
citizen.

%prep
%setup -qn unico-%{version}
%patch0 -p0

%build
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/libunico.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libunico.so

