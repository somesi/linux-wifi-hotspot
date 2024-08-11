%global debug_package %{nil}

Name:           linux-wifi-hotspot
Version:        4.7.2
Release:        1%{?dist}
Summary:        Share your wifi
License:        BSD-2-Clause
URL:            https://github.com/lakinduakash/linux-wifi-hotspot
Source:         https://github.com/lakinduakash/linux-wifi-hotspot/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gtk3-devel gcc gcc-c++ kernel-devel pkg-config make hostapd qrencode-devel libpng-devel
Requires:       procps-ng hostapd

%description
Share your wifi as a hotspot using a GUI or from the terminal.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build

%install
%make_install

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/create_ap
%{_bindir}/wihotspot
%{_bindir}/wihotspot-gui
%{_prefix}/lib/systemd/system/create_ap.service
%{_datadir}/applications/wihotspot.desktop
%{_datadir}/bash-completion/completions/create_ap
%{_datadir}/doc/create_ap/README.md
%{_datadir}/icons/hicolor/256x256/apps/wihotspot.png
%{_datadir}/icons/hicolor/48x48/apps/wihotspot.png
%{_datadir}/icons/hicolor/512x512/apps/wihotspot.png
%{_datadir}/icons/hicolor/64x64/apps/wihotspot.png
%{_datadir}/icons/hicolor/scalable/apps/wihotspot.svg
%{_datadir}/pixmaps/wihotspot.png
%{_datadir}/polkit-1/actions/org.opensuse.policykit.wihotspot.policy
%{_datadir}/polkit-1/rules.d/90-org.opensuse.policykit.wihotspot.rules
%{_sysconfdir}/create_ap.conf

%post
firewall-cmd --zone=FedoraWorkstation --add-masquerade --permanent --quiet || true
firewall-cmd --zone=trusted --add-masquerade --permanent --quiet || true
firewall-cmd --zone=trusted --add-interface=ap0 --permanent --quiet || true
firewall-cmd --reload --quiet || true

%changelog
* Sun Aug 11 2024 Sidney <sidneypro@proton.me> - 4.7.2-1
- updated to upstream version v4.7.2

* Sun Apr 07 2024 Sidney <sidneypro@proton.me> - 4.7.1-2
- the required firewalld changes are now made automatically on install

* Sat Apr 06 2024 Sidney <sidneypro@proton.me> - 4.7.1-1
- initial build
