#!/bin/bash

if systemctl is-active --quiet firewalld.service; then
    sudo firewall-cmd --zone=FedoraWorkstation --add-masquerade --permanent
    sudo firewall-cmd --zone=trusted --add-masquerade --permanent
    sudo firewall-cmd --zone=trusted --add-interface=ap0 --permanent
else
    true
fi
