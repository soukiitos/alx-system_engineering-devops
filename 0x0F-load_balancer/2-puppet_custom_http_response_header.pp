#!/usr/bin/env bash
# Install nginx
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

package { 'nginx':
  ensure => 'installed',
}

# Create nginx custom configuration file
file { '/etc/nginx/sites-enabled':
  ensure => directory,
}

file {'etc/nginx/sites-enabled/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html;
      location /redirect_me {
        return https://www.github.com/soukiitos permanent;
}
      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
}
}
',
}
file { '/var/www/html':
  ensure => directory,
}

file { 'var/www/html/index.html':
  ensure  => present,
    content => 'Hello World!',
}
service { 'nginx':
  ensure  => running,
  enablr  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
