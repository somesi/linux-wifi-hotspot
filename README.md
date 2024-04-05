Add this repo and install linux-wifi-hotspot:
```
dnf copr enable zinix01/linux-wifi-hotspot
sudo dnf install linux-wifi-hotspot
```
Add firewalld support:
```
sudo firewall-cmd --zone=FedoraWorkstation --add-masquerade
sudo firewall-cmd --zone=trusted --add-masquerade
sudo firewall-cmd --zone=trusted --add-interface=ap0
```
Then launch 'Wifi Hotspot' from your apps menu to start using the app.
