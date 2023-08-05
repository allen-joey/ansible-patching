# Ansible Playbook that fully automates the "manual" patching of CentOS/RHEL and Debian/Ubuntu, using all known official patches.

Patches CentOS 7/8/9 Stream, RHEL 7/8/9, Debian Ubuntu 18.04 and 20.04.

## Installation

ansible-playbook update-by-group.yml -v

Optional, check for updates before running, ansible-playbook update.yml -C -v

Optional, run the playbook with the wrapper scripts, update if needed the --limit with your own inventory groups.

./run-patching-playbook-check.sh Check the patches needed before applying

./run-patching-playbook.sh

Example inventory file included called inventory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author Information

Joey Allen
linkedin.com/in/joey-allen