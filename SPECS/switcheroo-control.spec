Name:           switcheroo-control
Version:        2.4
Release:        4%{?dist}
Summary:        D-Bus service to check the availability of dual-GPU

License:        GPLv3
URL:            https://gitlab.freedesktop.org/hadess/switcheroo-control/
# URL from https://gitlab.freedesktop.org/hadess/switcheroo-control/-/releases
Source0:        https://gitlab.freedesktop.org/hadess/switcheroo-control/uploads/accd4a9492979bfd91b587ae7e18d3a2/switcheroo-control-2.4.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  systemd

%{?systemd_requires}

%description
D-Bus service to check the availability of dual-GPU.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs

This package contains the documentation for %{name}.

%prep
%autosetup


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%post
if [ $1 -eq 2 ] && [ -x /usr/bin/systemctl ] ; then
	/usr/bin/systemctl daemon-reload
fi
%systemd_post switcheroo-control.service
%udev_hwdb_update

%preun
%systemd_preun switcheroo-control.service

%postun
%systemd_postun_with_restart switcheroo-control.service
%udev_hwdb_update

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/switcherooctl
%{_sysconfdir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf
%{_unitdir}/switcheroo-control.service
%{_libexecdir}/switcheroo-control
%{_udevhwdbdir}/30-pci-intel-gpu.hwdb
%{_mandir}/man1/switcherooctl.1*

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.4-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.4-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Bastien Nocera <bnocera@redhat.com> - 2.4-1
+ switcheroo-control-2.4-1
- Update to 2.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Bastien Nocera <bnocera@redhat.com> - 2.2-1
+ switcheroo-control-2.2-1
- Update to 2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Bastien Nocera <bnocera@redhat.com> - 2.1-1
+ switcheroo-control-2.1-1
- Update to 2.1
- Fix crasher on startup (#1786846)

* Thu Nov 21 2019 Bastien Nocera <bnocera@redhat.com> - 2.0-2
+ switcheroo-control-2.0-2
- Fix post scripts not reloading service file

* Tue Nov 05 2019 Bastien Nocera <bnocera@redhat.com> - 2.0-1
+ switcheroo-control-2.0-1
- Update to 2.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Bastien Nocera <bnocera@redhat.com> - 1.3.1-1
+ switcheroo-control-1.3.1-1
- Fix Secure Boot work-around

* Wed Jun 12 2019 Bastien Nocera <bnocera@redhat.com> - 1.3-1
+ switcheroo-control-1.3-1
- Update to 1.3
- Fix operation with SecureBoot enabled

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Bastien Nocera <bnocera@redhat.com> - 1.1-1
+ switcheroo-control-1.1-1
- Update to 1.1
- Don't throw errors when the machine doesn't have dual-GPU (#1391212)

* Fri Oct 21 2016 Kalev Lember <klember@redhat.com> - 1.0-1
- Initial Fedora packaging
