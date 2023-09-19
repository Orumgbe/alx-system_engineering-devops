# Change file limits
exec { 'replace':
  command => '/bin/sed -ie \'s/-n 15/-n 4096/\' /etc/default/nginx'
}

# Restart nginx
exec { 'restart':
  command    => '/etc/init.d/nginx restart'
}
