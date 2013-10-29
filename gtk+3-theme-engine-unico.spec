%define		bzr_rev	r150

Summary:	Unico Gtk+3 theming engine
Name:		gtk+3-theme-engine-unico
Version:	1.0.3
Release:	0.%{bzr_rev}.1
License:	LGPL 3.0
Group:		Libraries
#Source0:	https://launchpad.net/unico/1.0/1.0.2/+download/unico-%{version}.tar.gz
#
# bzr branch lp:unico
# cd unico
# bzr export ../unico-1.0.3-r150.tar
# xz -9 unico-1.0.3-r150.tar
Source0:	unico-%{version}-%{bzr_rev}.tar.xz
# Source0-md5:	d84a01d142dd871d9ac3011f06dd5d0a
Patch0:		%{name}-bug999277.patch
URL:		https://launchpad.net/unico
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful
theming engine for Gtk+3 and newer. It's the first Gtk+ engine
written with Gtk+ style context APIs in mind, using CSS as first class
citizen.

%prep
%setup -qn unico-%{version}-%{bzr_rev}
#%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
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

