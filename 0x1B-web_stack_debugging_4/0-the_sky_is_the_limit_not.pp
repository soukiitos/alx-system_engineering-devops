# increase the amount of traffic

exec { 'fix-fr-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/usr/sbin',
}
