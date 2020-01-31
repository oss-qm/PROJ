%global sname proj

%global pkg_libs	libproj15
%global pkg_devel	proj-devel
%global pkg_utils	proj-utils
%global pkg_data	proj-data

Name:		%{sname}
Version:	6.2.1
Release:	mtx.3
Epoch:		0
Summary:	Cartographic projection software (PROJ)
License:	MIT
URL:		https://proj.org
Source0:	%{sname}-%{version}.tar.gz

BuildRequires:	sqlite3-devel >= 3.7
BuildRequires:	sqlite3 >= 3.7
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/

%package -n %pkg_libs
Summary:	Cartographic projection software (PROJ)
Requires:	%pkg_data = %{version}-%{release}

%description -n %pkg_libs
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/

%post -n %pkg_libs
/sbin/ldconfig

%postun -n %pkg_libs
/sbin/ldconfig

%files -n %pkg_libs
%defattr(-,root,root,-)
%doc %{_prefix}/share/doc/*
%{_libdir}/libproj.so.15*

%package -n %pkg_devel
Summary:	Development files for PROJ
Requires:	%pkg_libs = %{version}-%{release}
Requires:	sqlite3-devel >= 3.7

%description -n %pkg_devel
This package contains libproj and the appropriate header files and man pages.

%files -n %pkg_devel
%defattr(-,root,root,-)
%{_mandir}/man3/*.3.gz
%{_includedir}/*.h
%{_includedir}/proj/*
%{_includedir}/proj_json_streaming_writer.hpp
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%attr(0755,root,root) %{_libdir}/pkgconfig/*.pc

%package -n %pkg_utils
Summary:	Utilities for PROJ
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n %pkg_utils
This package contains libproj utilities.

%files -n %pkg_utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*.1.gz

%package -n %pkg_data
Summary:	Data files for PROJ

%description -n %pkg_data
This package contains libproj data library.

%files -n %pkg_data
%defattr(-,root,root,-)
%{_datadir}/proj/*

%prep
%setup -q -n %{sname}-%{version}
./autogen.sh
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--libdir=%{_libdir} \
	--bindir=%{_bindir} \
	--without-jni

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install
%{__install} -d %{buildroot}%{_datadir}/%{sname}
%{__install} -d %{buildroot}%{_docdir}
%{__install} -p -m 0644 NEWS AUTHORS COPYING README.md ChangeLog %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Jun 04 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 0:6.2.1-3
- Fresh packaging onto upstream git tag
