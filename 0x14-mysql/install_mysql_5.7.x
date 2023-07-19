#port 3306
sudo apt update
sudo apt install mysql-server-8.0
sudo systemctl start mysql

#for distribution package 5.7
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
ubuntu bionic > Mysql server & cluster > mysql 5.7 > ok
sudo apt-get update
if:
GPG error: http://repo.mysql.com/apt/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29
then:
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29

try:
sudo apt install -f mysql-client mysql-community-server mysql-server
except Error:
then:
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

Done
