# Set up doc for Project D Ansible demo


## Requirements
* Nexus Repository http://download.sonatype.com/nexus/3/latest-unix.tar.gz
* Download `jboss-eap-7.0.0.zip` under `deploy-app-playbook/roles/jboss-standalone/files/`
* 1 or 2 more RHEL/CentOS VM with a ssh account with sudo privelege. 

## Nexus Repository

The Nexus repository will host the application, config files and the IPs of the VMs. 

  * Create a new raw(hosted) reciepe Nexus repository called 'demo'. (https://books.sonatype.com/nexus-book/reference3/raw.html#raw-hosted) 
  * Edit `repo_artifacts/config/sit.yml` to add VM IPs
  * Edit `bin/upload.sh` for the NEXUS Host IP and upload the artifacts by running `bin/upload-repo.sh`.

## Setup the VMs

Run `setup.yml` to install the necessary packages on the VM. This will install JBOSS EAP and MariaDB.

Pass the following extra-vars to ansible-playbook:

* `-e stage=sit`
* `-e nexus_repo_url=http://<NEXUS IP>:8081/repository/demo`
* `- u <SSH_USER`

```
$ ansible-playbook -i hosts -e stage=sit \
-e nexus_repo_url=http://<NEXUS_IP>:8081/repository/demo \
-u <SSH_USER> setup.yml
```
 
##  Install the sample app

Run `site.yml` to deploy the EAP Application and setup the database.

* `-e stage=sit`
* `-e nexus_repo_url=http://<NEXUS_IP>:8081/repository/demo`
* `-u <SSH_USER>` 

```
$ ansible-playbook -i hosts -e stage=sit \
-e nexus_repo_url=http://<NEXUS_IP>:8081/repository/demo \
-u <SSH_USER> site.yml
```
