# Ansible Playbook that fully automates the "manual" patching of CentOS/RHEL and Debian/Ubuntu, using all known official patches.

Tested on CentOS 7/8/9 Stream, RHEL 7/8, Debian Ubuntu 18.04 and 20.04.

## Installation

ansible-playbook update-by-group.yml -v

Optional, check for updates before running, ansible-playbook update-by-group.yml -C -vv

ansible-playbook update-by-group.yml --list-tags

Using tags example update RHEL8-9 only: ansible-playbook update-by-group.yml --tags=update-rhel8-9 -C -v

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
GNU General Public License

## Author Information
Joey Allen