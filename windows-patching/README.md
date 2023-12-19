# Ansible for patching Windows Server updates

## Description

There are 2 playbooks that patch Windows (win-security-update.yml) this playbook will install Windows updates by the category which are SecurityUpdates, CriticalUpdates and UpdateRollups.

The playbook (win-update-all.yml) this playbook will update Windows with all available updates.

## Getting Started

### Dependencies

* Setting up Ansible to talk to Windows is a little different than talking to Linux hosts.
* On the Windows host open a Powershell window enter Get-ExecutionPolicy.
* Change the execution policy from restricted to unrestricted, by default won't be able to execute any scripts.  
* Set-ExecutionPolicy Unrestricted.
* Copy the script located in the Scripts directory ConfigureRemoteForAnsible.ps1 to the Downloads directory.
* Go back to the Powershell Window and run it .\ConfigureRemoteForAnsible.ps1
* The script checks some basic conditions like if the correct version of PowerShell is installed and if WinRM is listening.

* Ansible collections install on Linux where Ansible is installed
```
ansible-galaxy collection install ansible.windows
```

### Installing

* Configure your inventory files and variables, unlike managing Linux servers your be connecting over WinRM not SSH.
* group_vars, this is where you place your inventory variables.
* Note group vars is where you can store the Adninstrator password, for prodction evviroments and storing on Git, use ansible vault to store secrets. 

### Executing the playbooks

* Step-by-step
```
ansible-playbook win-update-all.yml -e "admin_password=your_password" (passing in the password with extra vars)
ansible-playbook win-update-all.yml (With password stored in group_vars)
Optional switches -C for dry-run -v for verbosity

```

## Help Troubleshooting

Advise for common problems or issues.
```
"msg": "winrm or requests is not installed: No module named winrm"
Ubuntu # sudo apt install python3-winrm
CentOS # dnf or yum install python3-winrm

```

## Authors

[Joey Allen](https://www.linkedin.com/in/joey-allen)

## Version History

* 0.1
    * Initial Release

## License
GPLv3 licensed project

# Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

[SSL Certificates Strong Encryption](https://cloudhosting.comptek.systems/affordable-ssl-certificates)