%define manbo_vendor manbo
%define manbo_platform %{_target_cpu}-%{manbo_vendor}-%{_target_os}%{?_gnu}

%define gcc_libdir		%{_prefix}/lib/gcc

Name:		manbo-files-gcc
Summary:	Supplemental files for Manbo GCC
Version:	4.2.3
Release:	%{manbo_mkrel 6}
License:	GPLv3+
Group:		Development/C
URL:		http://manbo-labs.mandriva.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Supplemental files for Manbo GCC which is built with the vendor-name
"manbo".

%package -n manbo-%{_real_vendor}-files-gcc
Summary:	Supplemental files for Manbo GCC
Provides:	manbo-files-gcc = %{version}-%{release}
Group:		Development/C
Conflicts:	gcc < 4.2.3

%description -n manbo-%{_real_vendor}-files-gcc
Supplemental files for Manbo GCC which is built with the vendor-name
"manbo".

%package -n manbo-%{_real_vendor}-files-gcc-c++
Summary:	Supplemental files for Manbo GCC C++
Provides:	manbo-files-gcc-c++ = %{version}-%{release}
Group:		Development/C++
Conflicts:	gcc-c++ < 4.2.3

%description -n manbo-%{_real_vendor}-files-gcc-c++
Supplemental files for Manbo GCC C++ which is built with the vendor-name
"manbo".

%package -n manbo-%{_real_vendor}-files-gcc-gfortran
Summary:	Supplemental files for Manbo GCC Fortran
Provides:	manbo-files-gcc-gfortran = %{version}-%{release}
Group:		Development/Other
Conflicts:	gcc-gfortran < 4.2.3

%description -n manbo-%{_real_vendor}-files-gcc-gfortran
Supplemental files for Manbo GCC Fortran which is built with the vendor-name
"manbo".

%package -n manbo-%{_real_vendor}-files-gcc-java
Summary:	Supplemental files for Manbo GCC Java
Provides:	manbo-files-gcc-java = %{version}-%{release}
Group:		Development/Other
Conflicts:	gcj-tools < 4.2.3
Conflicts:	gcc-java < 4.2.3

%description -n manbo-%{_real_vendor}-files-gcc-java
Supplemental files for Manbo GCC Java which is built with the vendor-name
"manbo".

%prep
test "%{_real_vendor}" = "%{manbo_vendor}" && /bin/false

%build

mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
for i in c++ g++ gcj gcc gcc-%{version} gfortran gcjh; do
   ln -sf %{manbo_platform}-$i $RPM_BUILD_ROOT/%{_bindir}/%{_target_platform}-$i
done

mkdir -p $RPM_BUILD_ROOT/%{gcc_libdir}/%{_target_platform}
ln -sf ../%{manbo_platform}/%{version} \
 $RPM_BUILD_ROOT/%{gcc_libdir}/%{_target_platform}/%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n manbo-%{_real_vendor}-files-gcc
%{_bindir}/%{_target_platform}-gcc
%{_bindir}/%{_target_platform}-gcc-%{version}
%{gcc_libdir}/%{_target_platform}/*

%files -n manbo-%{_real_vendor}-files-gcc-c++
%{_bindir}/%{_target_platform}-c++
%{_bindir}/%{_target_platform}-g++

%files -n manbo-%{_real_vendor}-files-gcc-gfortran
%{_bindir}/%{_target_platform}-gfortran

%files -n manbo-%{_real_vendor}-files-gcc-java
%{_bindir}/%{_target_platform}-gcj
%{_bindir}/%{_target_platform}-gcjh
