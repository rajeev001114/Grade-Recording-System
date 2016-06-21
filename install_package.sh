#!/bin/bash


tar -zxvf project.tar.gz

#### install python pip
sudo apt-get install python-pip

#### Uninstall old version of Django
sudo pip uninstall Django

#### Install required packages
sudo pip install -r requirement.txt

#### Install MySQL server
export DEBIAN_FRONTEND=noninteractive 
debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password password '$MySQL_PASSWORD''
debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password_again password '$MySQL_PASSWORD''
apt-get -y install mysql-server-5.6

echo "----------------------------------------------------------------"
echo " All the software package and database installation is DONE !!!!"
echo "----------------------------------------------------------------"
#sudo apt-get update


