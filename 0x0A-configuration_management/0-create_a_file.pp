# Create the directory if it doesn't exist
file { '/tmp':
  ensure => 'directory',
}

# Create the file with the specified requirements
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

