# increase the amount of traffic

# Increase the ULIMIT
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

# Restart nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d',
}
