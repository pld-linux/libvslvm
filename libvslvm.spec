#
# Conditional build:
%bcond_without	python	# Python (3) bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20230108
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfvalue_ver		20200711
%define		libuna_ver		20230702
Summary:	Library to access the Linux Logical Volume Manager (LVM) volume system
Summary(pl.UTF-8):	Biblioteka dostępu do systemu wolumenów Linux Logical Volume Manager (LVM)
Name:		libvslvm
Version:	20240504
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libvslvm/releases
Source0:	https://github.com/libyal/libvslvm/releases/download/%{version}/%{name}-experimental-%{version}.tar.gz
# Source0-md5:	7491d52be8ccf0d853678a51cad10d87
URL:		https://github.com/libyal/libvslvm/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
# or libfuse >= 2.6
BuildRequires:	libfuse3-devel >= 3.0
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
Requires:	libfdata >= %{libfdata_ver}
Requires:	libfvalue >= %{libfvalue_ver}
Requires:	libuna >= %{libuna_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvslvm is a library to access the VMware Virtual Disk (VMDK) image
format.

Read supported formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
* delta links
* grain compression (as of version 20131209)
* data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse))
 / change tracking file

Work in progress:
- Dokan library support
- Thread-safety in handle API functions

%description -l pl.UTF-8
libvslvm to biblioteka służąca do dostępu do formatu obrazów VMware
Virtual Disk (VMDK).

Obsługuje odczyt formatów:
- RAW (płaski)
- COWD w wersji 1 (rzadki)
- VMDK w wersji 1, 2 i 3 (rzadki)

Obsługiwana funkcjonalność obrazów:
- dowiązania różnic
- kompresja ziarnista (w wersji 20131209)
- znaczniki danych (w wersji 20140416)

Funkcjonalność formatu VMDK obecnie nie obsługiwana:
- obrazy wykorzystujące urządzenia fizyczne
- śledzenie zmienionych bloków (CBT) (obsługiwane przez rzadkie VMDK w
  wersji 3) / pliki śledzenia zmian

W trakcie implementacji:
- obsługa biblioteki Dokan
- obsługa wątków w funkcjach API uchwytów

%package devel
Summary:	Header files for libvslvm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvslvm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}
Requires:	libfdata-devel >= %{libfdata_ver}
Requires:	libfvalue-devel >= %{libfvalue_ver}
Requires:	libuna-devel >= %{libuna_ver}

%description devel
Header files for libvslvm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvslvm.

%package static
Summary:	Static libvslvm library
Summary(pl.UTF-8):	Statyczna biblioteka libvslvm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvslvm library.

%description static -l pl.UTF-8
Statyczna biblioteka libvslvm.

%package tools
Summary:	Tools to support the Linux Logical Volume Manager (LVM) volume system
Summary(pl.UTF-8):	Narzędzia obsługujące system wolumenów Linux Logical Volume Manager (LVM)
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	libfuse3 >= 3.0

%description tools
Tools to support the Linux Logical Volume Manager (LVM) volume system.

%description tools -l pl.UTF-8
Narzędzia obsługujące system wolumenów Linux Logical Volume Manager
(LVM).

%package -n python3-pyvslvm
Summary:	Python 3 bindings for libvslvm library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libvslvm
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pyvslvm
Python 3 bindings for libvslvm library.

%description -n python3-pyvslvm -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libvslvm.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON_VERSION=3 \
	%{?with_python3:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvslvm.la

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pyvslvm.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libvslvm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvslvm.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvslvm.so
%{_includedir}/libvslvm
%{_includedir}/libvslvm.h
%{_pkgconfigdir}/libvslvm.pc
%{_mandir}/man3/libvslvm.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libvslvm.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vslvminfo
%attr(755,root,root) %{_bindir}/vslvmmount
%{_mandir}/man1/vslvminfo.1*

%if %{with python3}
%files -n python3-pyvslvm
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pyvslvm.so
%endif
