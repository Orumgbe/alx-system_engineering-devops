# change all limits
exec { 'soft limit change':
  command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf'
}

exec { 'hard limit change':
  command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf'
}
