# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'installi':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/coxy-code permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
