#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
echo "<html><head>Test</head></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '41i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart