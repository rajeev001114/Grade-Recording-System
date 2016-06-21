=========================================================================================================================================
Grade Recording System

=========================================================================================================================================
This system will help teachers of engineering colleges for assessment of blended MOOCs. The teachers from various institutes participating in the blended MOOCs, will be able to generate a composite mark sheet for the particular course by giving certain weightage to online assessment along with their regular university assessment. This system can also be used to store students regular university assessment without using MOOC assessment i.e. for their local use.
Copyright (C) 2015  Rajeev 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses>.

For more information:
Email to: rk31278@gmail.com

=========================================================================================================================================
Prerequisities:

To install the software following are the requirements:
Operating System: Ubuntu 12.04 and upper version
Software Required:
1) Django 1.8.2
2) MySQL-python 1.2.5
3) beautifulsoup4
4) Pillow 1.7.8

Database Required:
1)mysql-server-5.6

=========================================================================================================================================
Installing and running on your local machine:-

1)Enter college name in collegename.txt

2)Edit admin_info.conf and settings.py:

admin_info.conf (Enter value between double quotes) :
---------------
MySQL_PASSWORD (Default password:- MySQL_PASSWORD="123456")


settings.py (Enter value between double quotes) :
-----------
MySQL password at line no. 126 (Example:- 'PASSWORD': '123456' (same as MySQL_PASSWORD))

If use Moodle as LMS:
Moodle Database name at line no. 115 ('NAME': '')
MySQL password at line no. 117 ('PASSWORD': '')

3)Enter the full path in runserver.sh where you have setup the system.

4)Open terminal (Alt+Clt+t)

5)Now run following commands in the terminal:
-----------------------------------------
make
-----------------------------------------

6)Now go url in web browser:
-----------------------------------------
0.0.0.0:8181
-----------------------------------------

=========================================================================================================================================
Author:

    Rajeev Kumar Gautam 

=========================================================================================================================================



