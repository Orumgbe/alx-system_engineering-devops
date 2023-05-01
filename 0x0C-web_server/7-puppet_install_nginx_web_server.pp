# configure nginx

package { 'nginx':
    ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
    require => Package['nginx'],
    content => 'Hello World!',
}

file_line { 'add-rewrite':
    ensure  => 'present',
    require => Package['nginx'],
    path    => '/etc/nginx/sites-enabled/default',
    after   => 'root /var/www/html;',
    line    => 'rewrite ^/redirect_me sitesurf.tech permanent;',
    notify  => Service['nginx'],
}

service { 'nginx':
    ensure  => running,
    require => File_line['add-rewrite'],
}
