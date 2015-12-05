# Digital Ocean deployment

The following script sets everything up so that the application can be deployed on a [Digital Ocean](https://www.digitalocean.com/) droplet with Ubuntu 14.04 and the Apache web server. Of course you should go through it and modify the parts that are unique to your application (the username and the application GitHub URL/folder). You will also have to change the ``app.wsgi`` and the ``Flask-Boilerplate.conf`` files, just open the files and replace the obvious stuff.

```sh
# Login and change password
ssh root@<IP>

# Add a new user "MAX" and give him a password
adduser MAX
# Give "MAX" sudo rights
gpasswd -a MAX sudo

# Change "PermitRootLogin yes" to "PermitRootLogin no"
nano /etc/ssh/sshd_config

# Restart SSH
service ssh restart

# Switch to user "MAX"
sudo su MAX

# Configure the timezone
sudo dpkg-reconfigure tzdata
# Configure NTP Synchronization
sudo apt-get update
sudo apt-get install ntp
# Create a Swap File
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sh -c 'echo "/swapfile none swap sw 0 0" >> /etc/fstab'

# Setup Python and Apache
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install python3-pip python3-dev libapache2-mod-wsgi-py3

# Clone the repository containing the code
cd /var/www
sudo apt-get install git
sudo git clone https://github.com/MaxHalford/Flask-Boilerplate
sudo chmod -R 777 Flask-Boilerplate
cd Flask-Boilerplate

# Install the necessary Python libraries (takes some time)
sudo pip3 install -r setup/requirements.txt

# Configure and enable a virtual host
sudo cp deployment/Flask-Boilerplate.conf /etc/apache2/sites-available/
sudo a2ensite Flask-Boilerplate
sudo service apache2 reload
sudo service apache2 restart

# Reboot the server and you should be done!
sudo reboot
```