# Ansible playbook to install K0S

Set of tasks to install k0s as single node or cluster.

## Installation
```
$ ansible all -m ping -i nodes.ini
$ ansible-playbook -i nodes.ini single.yaml -K
$ ansible-playbook -i nodes.ini cluster.yaml -K
```

## Troubleshooting
In case of error on SSH connection add the ssh key with teh following command:
```
$ ssh-copy-id <USERNAME>@<IP>
```