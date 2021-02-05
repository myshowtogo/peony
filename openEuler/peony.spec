%define debug_package %{nil}

Name:           peony
Version:        3.0.6
Release:        1
Summary:       file Manager for the UKUI desktop
License:        GPL-2.0+ GPL-3.0+ Expat LGPL-3.0+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: libudisks2-devel
BuildRequires: libnotify-devel
BuildRequires: gtk2-devel
BuildRequires: pkg-config
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qtchooser
BuildRequires: glib2-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: gsettings-qt-devel
BuildRequires: poppler-devel
BuildRequires: poppler-qt5-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libcanberra-devel

Requires: peony-common
Requires: libpeony3
Requires: gvfs

%description
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.

%package common
Summary:     file manager for the UKUI desktop (common files)
License:     LGPLv2+

BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel, gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel


%description common
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the architecture independent files.

%package -n libpeony3
Summary:     libraries for Peony components
License:     LGPLv2+

BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel, gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel
Provides: libpeony

%description -n libpeony3
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions

%package -n libpeony-dev
Summary:     libraries for Peony components (development files)
License:     LGPLv2+

Provides: libpeony

%description -n libpeony-dev
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the development files for the libraries needed
 by Peony's extensions.


%prep
%setup -q

%build
qmake-qt5 
make


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

#peony-common
install -D %{_builddir}/%{name}-%{version}/peony-qt-desktop/freedesktop-dbus-interfaces.xml %{buildroot}/usr/share/dbus-1/interfaces
install -D %{_builddir}/%{name}-%{version}/peony-qt-desktop/org.ukui.freedesktop.FileManager1.service %{buildroot}/usr/share/dbus-1/services
install -D %{_builddir}/%{name}-%{version}/translations/peony-qt/* %{buildroot}/usr/share/peony-qt
install -D %{_builddir}/%{name}-%{version}/translations/peony-qt-desktop/* %{buildroot}/usr/share/peony-qt-desktop

#libpeony3
install -D %{_builddir}/%{name}-%{version}/translations/libpeony-qt/* %{buildroot}/usr/share/libpeony-qt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_prefix}/bin/*
%{_datadir}/applications/*

%files common
%doc debian/copyright debian/changelog
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/dbus-1/services/*
%{_datadir}/peony-qt/*
%{_datadir}/peony-qt-desktop/*

%files -n libpeony3
%{_prefix}/%{_lib}/*.so.*
%{_datadir}/libpeony-qt/*

%files -n libpeony-dev
%{_prefix}/include/peony-qt/*
%{_prefix}/%{_lib}/pkgconfig/*.pc
%{_prefix}/%{_lib}/*.so

%changelog
* Wed Feb 3 2021 lvhan <lvhan@kylinos.cn> - 3.0.6-1
- update to upstream version 3.0.6-1

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.4-1
- update to upstream version 3.0.4

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.1.2-1
- Init package for openEuler
