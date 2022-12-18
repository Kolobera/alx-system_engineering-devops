#!/usr/bin/env bash
# Client configuration file (w/ Puppet)

file_line { 'Turn off passwd auth':
  line => ' PasswordAuthentication no',
  path => '/etc/ssh/ssh_config'
}

file_line { 'Declare identity file':
  line => ' IdentityFile ~/.ssh/holberton',
  path => '/etc/ssh/ssh_config'
}