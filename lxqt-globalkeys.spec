#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : lxqt-globalkeys
Version  : 0.14.1
Release  : 2
URL      : https://downloads.lxqt.org/downloads/lxqt-globalkeys/0.14.1/lxqt-globalkeys-0.14.1.tar.xz
Source0  : https://downloads.lxqt.org/downloads/lxqt-globalkeys/0.14.1/lxqt-globalkeys-0.14.1.tar.xz
Source99 : https://downloads.lxqt.org/downloads/lxqt-globalkeys/0.14.1/lxqt-globalkeys-0.14.1.tar.xz.asc
Summary  : LXQt daemon and library for global keyboard shortcuts registration.
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-globalkeys-bin = %{version}-%{release}
Requires: lxqt-globalkeys-data = %{version}-%{release}
Requires: lxqt-globalkeys-lib = %{version}-%{release}
Requires: lxqt-globalkeys-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : qttools-dev

%description
# lxqt-globalkeys
## Overview
This repository is providing tools to set global keyboard shortcuts in LXQt
sessions, that is shortcuts which apply to the LXQt session as a whole and are
not limited to distinct applications.

%package bin
Summary: bin components for the lxqt-globalkeys package.
Group: Binaries
Requires: lxqt-globalkeys-data = %{version}-%{release}
Requires: lxqt-globalkeys-license = %{version}-%{release}

%description bin
bin components for the lxqt-globalkeys package.


%package data
Summary: data components for the lxqt-globalkeys package.
Group: Data

%description data
data components for the lxqt-globalkeys package.


%package dev
Summary: dev components for the lxqt-globalkeys package.
Group: Development
Requires: lxqt-globalkeys-lib = %{version}-%{release}
Requires: lxqt-globalkeys-bin = %{version}-%{release}
Requires: lxqt-globalkeys-data = %{version}-%{release}
Provides: lxqt-globalkeys-devel = %{version}-%{release}
Requires: lxqt-globalkeys = %{version}-%{release}

%description dev
dev components for the lxqt-globalkeys package.


%package lib
Summary: lib components for the lxqt-globalkeys package.
Group: Libraries
Requires: lxqt-globalkeys-data = %{version}-%{release}
Requires: lxqt-globalkeys-license = %{version}-%{release}

%description lib
lib components for the lxqt-globalkeys package.


%package license
Summary: license components for the lxqt-globalkeys package.
Group: Default

%description license
license components for the lxqt-globalkeys package.


%prep
%setup -q -n lxqt-globalkeys-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551233075
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1551233075
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-globalkeys
cp LICENSE %{buildroot}/usr/share/package-licenses/lxqt-globalkeys/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-config-globalkeyshortcuts
/usr/bin/lxqt-globalkeysd

%files data
%defattr(-,root,root,-)
/usr/share/applications/lxqt-config-globalkeyshortcuts.desktop
/usr/share/cmake/*
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ar.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ca.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_cs.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_cy.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_da.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_de.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_el.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_eo.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_es.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_es_VE.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_eu.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_fi.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_fr.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_gl.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_he.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_hu.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_id.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_it.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ja.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_lt.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_lv.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_nl.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pl.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pt.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ro_RO.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ru.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_sl.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_th_TH.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_tr.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_uk.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_zh_TW.qm

%files dev
%defattr(-,root,root,-)
/usr/include/lxqt-globalkeys-ui/LXQtGlobalKeysUi/ShortcutSelector
/usr/include/lxqt-globalkeys-ui/shortcut_selector.h
/usr/include/lxqt-globalkeys-ui/shortcutselector.h
/usr/include/lxqt-globalkeys/LXQtGlobalKeys/Action
/usr/include/lxqt-globalkeys/LXQtGlobalKeys/Client
/usr/include/lxqt-globalkeys/LXQtGlobalKeys/LXQtGlobalKeys
/usr/include/lxqt-globalkeys/action.h
/usr/include/lxqt-globalkeys/client.h
/usr/include/lxqt-globalkeys/lxqt-globalkeys.h
/usr/include/lxqt-globalkeys/lxqtglobalkeys.h
/usr/lib64/liblxqt-globalkeys-ui.so
/usr/lib64/liblxqt-globalkeys.so
/usr/lib64/pkgconfig/lxqt-globalkeys-ui.pc
/usr/lib64/pkgconfig/lxqt-globalkeys.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblxqt-globalkeys-ui.so.0
/usr/lib64/liblxqt-globalkeys-ui.so.0.14.1
/usr/lib64/liblxqt-globalkeys.so.0
/usr/lib64/liblxqt-globalkeys.so.0.14.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-globalkeys/LICENSE
