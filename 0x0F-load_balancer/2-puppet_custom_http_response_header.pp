# Using Puppet

exec { 'Install nginx':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && echo "Hello World!" >> /var/www/html/index.html && sudo sed -i "60 i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => 'shell',
}