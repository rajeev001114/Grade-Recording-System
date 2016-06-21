#!/bin/bash

#### Read value from config file

source ./admin_info.conf

db="create database $MySQL_DATABASE_NAME;GRANT ALL PRIVILEGES ON $MySQL_DATABASE_NAME.* TO $MySQL_USER_NAME@localhost IDENTIFIED BY '$MySQL_PASSWORD';FLUSH PRIVILEGES;"
mysql -u root -p$MySQL_PASSWORD -e "$db"
 
if [ $? != "0" ]; then
 echo "[Error]: Database creation failed"
 exit 1
else
 echo "------------------------------------------"
 echo " Database has been created successfully "
 echo "------------------------------------------"
 echo " DB Info: "
 echo ""
 echo " DB Name: $MySQL_DATABASE_NAME"
 echo " DB Username: $MySQL_USER_NAME"
 echo " DB Password: $MySQL_PASSWORD"
 echo ""
 echo "------------------------------------------"
fi


#####  Restore sql dump into database    

mysql -u root -p$MySQL_PASSWORD $MySQL_DATABASE_NAME < project_dump.sql

if [ $? -ne 0 ]; then
	echo "Enter correct password or database name in admin_info.conf "
	exit
else
	echo "..."
	echo "..."
	echo "Installing tables into database........"
	echo "It will take some time........"
	echo "-----------------------------------------------------------"
	echo "Tables creation into database is successfully done !!! "
	echo "-----------------------------------------------------------"
fi


#### copy settings.py to project settings
sudo cp -rf settings.py ./project/project/

##### copy college name
sudo cp -rf collegename.txt ./project/ADM/


### create dir
sudo mkdir -p /opt/project
sudo cp -rf runserver.sh /opt/project

##### copy command into rc.local
sudo sed --in-place '/^exit 0/i\cd /opt/project\nbash runserver.sh' /etc/rc.local


