#!/usr/bin/env python3
from chibi.command.echo import cowsay
from chibi.file.snippets import copy


directory_of_repos = '/home/vagrant/provision/repos/*.repo'
destiny_of_repos = '/etc/yum.repos.d/'

cowsay( "starting to copy repos" )
copy( directory_of_repos, destiny_of_repos, verbose=True )
cowsay( "ending to copy repos" )
