#!/bin/bash

ANSIBLE_PLAYBOOK=`which ansible-playbook`
cd /home/user1/CodeCommit/ansible_repo/Ansible_Updates/Linux_Updates/
$ANSIBLE_PLAYBOOK update-by-group.yml --limit local:servers:kvm

exit 0