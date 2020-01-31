%global sname proj

Name:		%{sname}
Version:	6.3.2
Release:	1
Epoch:		0
Summary:	Cartographic projection software (PROJ)

License:	MIT
URL:		https://proj.org
Source0:	%{sname}-%{version}.tar.gz

BuildRequires:	sqlite3
BuildRequires:	sqlite3-devel >= 3.7
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

Requires:	sqlite3
Requires:	%{name}-data = %{version}-%{release}

%package devel
Summary:	Development files for PROJ
Requires:	%{name} = %{version}-%{release}

%package utils
Summary:	Utilities for PROJ
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package data
Summary:	Data files for PROJ

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions. Proj docs: http://www.remotesensing.org/dl/new_docs/

%description devel
This package contains libproj and the appropriate header files and man pages.

%description utils
This package contains libproj utilities.

%description data
This package contains libproj data library.

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

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{_prefix}/share/doc/*
%{_datadir}/proj/*
%{_libdir}/libproj.so.15*

%files data
%defattr(-,root,root,-)
%{_datadir}/proj/*

%files devel
%defattr(-,root,root,-)
%{_mandir}/man3/*.3.gz
%{_includedir}/*.h
%{_includedir}/proj/*
%{_includedir}/proj_json_streaming_writer.hpp
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%attr(0755,root,root) %{_libdir}/pkgconfig/*.pc
%{_includedir}/proj/util.hpp

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*.1.gz

%changelog
* Fri Jan 31 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 0:6.3.2-1
- Fresh packaging onto upstream git tag
