Linux Wifi Hotspot rpm builds for Fedora (https://github.com/lakinduakash/linux-wifi-hotspot)
repo for the copr: https://copr.fedorainfracloud.org/coprs/zinix01/linux-wifi-hotspot/

# Install
Add this repo and install linux-wifi-hotspot:
```
dnf copr enable zinix01/linux-wifi-hotspot
sudo dnf install linux-wifi-hotspot
```
Add firewalld support (see https://github.com/somesi/linux-wifi-hotspot/issues/2):
```
sudo firewall-cmd --zone=FedoraWorkstation --add-masquerade --permanent
sudo firewall-cmd --zone=trusted --add-masquerade --permanent
sudo firewall-cmd --zone=trusted --add-interface=ap0 --permanent
```
Then launch 'Wifi Hotspot' from your apps menu to start using the app.

Todo:
- apply firewalld rules at install time
- auto tag release

# Credits
felix for the original spec file (https://copr.fedorainfracloud.org/coprs/felix/fedora-copr/package/linux-wifi-hotspot/)
