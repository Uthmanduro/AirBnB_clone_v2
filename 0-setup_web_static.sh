#!/usr/bin/env bash
#sets up my web server for the deployment of web-static
#installs nginx if not already installed
sudo apt-get update
sudo apt-get install nginx -y
#create the necessary folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo '<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>
      <p>This is my fake html file</p>
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
#create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#change ownership of the data folder
sudo chown -R ubuntu:ubuntu /data/
#update the nginx configuration
sudo sed -i '/server_name _;/a \    location /hbnb_static {\n        \talias /data/web_static/current/;\n    }' /etc/nginx/sites-enabled/default
sudo service nginx restart
