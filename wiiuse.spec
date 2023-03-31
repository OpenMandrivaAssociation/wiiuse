%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Library to access wiimotes and its various accessories
Name:		wiiuse
Version:	0.15.5
Release:	3
License:	GPLv3+
Group:		System/Libraries
URL:		https://github.com/wiiuse/wiiuse
Source0:	https://github.com/wiiuse/wiiuse/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		wiiuse-soname.patch
BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(bluez)
# for the example
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(sdl2)

%description
Wiiuse is a library written in C that connects with several Nintendo Wii 
wiimotes. It supports motion sensing, IR tracking, nunchuk, classic 
controller, and the Guitar Hero 3 controller.

Single threaded and nonblocking makes a light weight and clean API.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	libwiiuse = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files from %{name}
Group:		Development/C
Requires:	libwiiuse = %{version}
Requires:	bluez-devel
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Includes files for developing programs based on %{name}.

%prep
%autosetup -p1

dos2unix CHANGELOG.mkd README.mkd

%build
%cmake \
  -DBUILD_EXAMPLE=NO \
  -DBUILD_EXAMPLE_SDL=NO \
  -DINSTALL_EXAMPLES=NO

%make_build

%install
%make_install -C build

# Handle in %%files
rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%doc CHANGELOG.mkd README.mkd
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
