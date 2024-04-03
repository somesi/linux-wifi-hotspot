%global debug_package %{nil}

Name:           linux-wifi-hotspot
Version:        4.7.1
Release:        1%{?dist}
Summary:        Feature-rich wifi hotspot creator for Linux which provides both GUI and command-line interface
License:        BSD-2-Clause
URL:            https://github.com/lakinduakash/linux-wifi-hotspot
Source:         https://github.com/lakinduakash/linux-wifi-hotspot/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gtk3-devel gcc gcc-c++ kernel-devel pkg-config make hostapd qrencode-devel libpng-devel
Requires:       procps-ng hostapd

%description
Feature-rich wifi hotspot creator for Linux which provides both GUI and command-line interface. It is also able to create a hotspot using the same wifi card which is connected to an AP already.

%prep
%autosetup -n %{name}-%{version} -p1

%build
make

%install
make install PREFIX=%{buildroot}%{_prefix}

%check

%files
%license LICENSE*
%doc README.md


%changelog
