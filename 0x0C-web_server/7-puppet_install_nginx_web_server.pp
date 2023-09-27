# Install Nginx web server (w/ Puppet)

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World !',
  require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "9i\      rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
