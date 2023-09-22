# Using Puppet to create a manifest that kills a process named killmenow

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  provider    => 'shell',
  returns     => [0, '1'],
}
