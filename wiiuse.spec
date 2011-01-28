Name:			wiiuse
Version:		0.12
Release:		%mkrel 1.1

%define	major		0
%define	libname		%mklibname %{name} %major
%define develname	%mklibname %{name} -d

Summary:	Library to access wiimotes and its various accessories
#LGPLv3+?
License:	GPLv3+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/wiiuse
Source0:	http://sourceforge.net/projects/wiiuse/files/wiiuse/v0.12/wiiuse_v0.12_src.tar.gz
Patch0:		wiiuse.memset.patch
BuildRequires:	bluez-devel
# for the example
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	mesaglut-devel
BuildRequires:	SDL-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Wiiuse is a library written in C that connects with several Nintendo Wii 
wiimotes. It supports motion sensing, IR tracking, nunchuk, classic 
controller, and the Guitar Hero 3 controller.

Single threaded and nonblocking makes a light weight and clean API.

%package -n %{develname}
Summary:	Header files from %{name}
Group:		Development/C
Requires:	libwiiuse = %{version}
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
perl -pi -e "s|\r\n|\n|g" CHANGELOG README

%build
%make

%install
rm -rf %{buildroot}
install -D -m 644 src/release*/libwiiuse.so %{buildroot}%{_libdir}/libwiiuse.so
install -D -m 644 src/wiiuse.h %{buildroot}%{_includedir}/wiiuse.h
install -D -m 755 example/release*/wiiuse-example %{buildroot}%{_bindir}/wiiuse-example
install -D -m 755 example-sdl/release*/wiiuse-sdl %{buildroot}%{_bindir}/wiiuse-example-sdl
%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGELOG README
%attr(0755,root,root) %{_bindir}/*

%files -n %{develname}
%defattr(0644,root,root,0755)
%{_includedir}/*

%files -n %{libname}
%defattr(0644,root,root,0755)
%{_libdir}/*.so
