Linux Wifi Hotspot rpm builds for Fedora (https://github.com/lakinduakash/linux-wifi-hotspot), repo for the copr: https://copr.fedorainfracloud.org/coprs/zinix01/linux-wifi-hotspot/

# Install
Add this repo and install linux-wifi-hotspot:
```
dnf copr enable zinix01/linux-wifi-hotspot
sudo dnf install linux-wifi-hotspot
```
~Add firewalld support:~ Since 4.7.1-2, these are applied automatically on install, but you can also apply them manaully if you are facing any connection issues:
```
sudo firewall-cmd --zone=FedoraWorkstation --add-masquerade --permanent
sudo firewall-cmd --zone=trusted --add-masquerade --permanent
sudo firewall-cmd --zone=trusted --add-interface=ap0 --permanent
sudo firewall-cmd --reload
```
Then launch 'Wifi Hotspot' from your apps menu to start using the app.

Todo:
- auto tag releases

# Credits
felix for the original spec file (https://copr.fedorainfracloud.org/coprs/felix/fedora-copr/package/linux-wifi-hotspot/)
