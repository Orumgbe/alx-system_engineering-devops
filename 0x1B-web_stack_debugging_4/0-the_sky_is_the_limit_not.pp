# change nginx open file limits
exec { 'change limit':
  command => 'sudo sed -i "s/15/4096/g" /etc/default/nginx',
}

exec { 'restart nginx':
  command    => 'sudo service nginx restart',
}
