Name:		wiiuse
Version:		0.12
Release:		4

%define	major		0
%define	libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Library to access wiimotes and its various accessories
#LGPLv3+?
License:	GPLv3+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/wiiuse
Source0:	http://sourceforge.net/projects/wiiuse/files/wiiuse/v0.12/wiiuse_v0.12_src.tar.gz
Patch0:		wiiuse.memset.patch
Patch1:		wiiuse_cflags.patch
Patch2:		wiiuse_fix_linking.patch
BuildRequires:	pkgconfig(bluez)
# for the example
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(sdl)


%description
Wiiuse is a library written in C that connects with several Nintendo Wii 
wiimotes. It supports motion sensing, IR tracking, nunchuk, classic 
controller, and the Guitar Hero 3 controller.

Single threaded and nonblocking makes a light weight and clean API.

%package -n %{develname}
Summary:	Header files from %{name}
Group:		Development/C
Requires:	libwiiuse = %{version}
Requires:	bluez-devel
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Includes files for developing programs based on %{name}.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	libwiiuse = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.


%prep
%setup -q -n %{name}_v%{version}
%patch0 -p0
%patch1 -p1 
%patch2 -p1 


perl -pi -e "s|\r\n|\n|g" CHANGELOG README

%build
CFLAGS='%optflags' make

%install
install -D -m 644 src/release*/libwiiuse.so %{buildroot}%{_libdir}/libwiiuse.so
install -D -m 644 src/wiiuse.h %{buildroot}%{_includedir}/wiiuse.h
install -D -m 755 example/release*/wiiuse-example %{buildroot}%{_bindir}/wiiuse-example
install -D -m 755 example-sdl/release*/wiiuse-sdl %{buildroot}%{_bindir}/wiiuse-example-sdl

%files
%doc CHANGELOG README
%attr(0755,root,root) %{_bindir}/*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libwiiuse.so

%files -n %{libname}
%{_libdir}/libwiiuse.so.%{major}*

%ifarch ix86
%exclude %{_libdir}/debug
%endif

%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.12-3mdv2011.0
+ Revision: 640874
- rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.12-2
+ Revision: 635055
- requires bluez-devel for headers

* Fri Jan 28 2011 Zombie Ryushu <ryushu@mandriva.org> 0.12-1.1
+ Revision: 633643
- Fix memset bug in wiiuse

* Wed Oct 14 2009 Guillaume Bedot <littletux@mandriva.org> 0.12-1mdv2010.0
+ Revision: 457314
- import wiiuse


* Mon Sep 21 2009 Guillaume Bedot <littletux@mandriva.org> 0.12-1mdv2010.0
- First package of wiiuse for Mandriva
