#!/bin/bash

if systemctl is-active --quiet firewalld.service; then
    firewall-cmd --zone=FedoraWorkstation --add-masquerade --permanent
    firewall-cmd --zone=trusted --add-masquerade --permanent
    firewall-cmd --zone=trusted --add-interface=ap0 --permanent
else
    true
fi
