#!/bin/bash
mv /home/user/python/backup/* /home/user/python/backup_old/
python3 /home/user/python/backup3.py
ansible-playbook /home/user/python/remove1.yml
ansible-playbook /home/user/python/remove2.yml
