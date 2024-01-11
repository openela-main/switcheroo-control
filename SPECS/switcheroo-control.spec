Name:           switcheroo-control
Version:        1.1
Release:        5%{?dist}
Summary:        D-Bus service to check the availability of dual-GPU

License:        GPLv3
URL:            https://github.com/hadess/switcheroo-control
Source0:        https://github.com/hadess/switcheroo-control/releases/download/%{version}/switcheroo-control-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  systemd

%{?systemd_requires}

%description
D-Bus service to check the availability of dual-GPU.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%post
%systemd_post switcheroo-control.service

%preun
%systemd_preun switcheroo-control.service

%postun
%systemd_postun_with_restart switcheroo-control.service


%files
%license COPYING
%doc NEWS README.md
%{_sysconfdir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf
%{_unitdir}/switcheroo-control.service
%{_sbindir}/switcheroo-control


%changelog
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
