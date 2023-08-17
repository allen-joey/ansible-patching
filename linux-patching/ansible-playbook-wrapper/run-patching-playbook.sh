#!/bin/bash

ANSIBLE_PLAYBOOK=`which ansible-playbook`
$ANSIBLE_PLAYBOOK update-by-group.yml --limit your:inventory:groups

exit 0