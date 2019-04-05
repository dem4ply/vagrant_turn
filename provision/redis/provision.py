#!/usr/bin/env python3
from chibi.command import systemctl
from chibi.command.echo import cowsay
from chibi.file.snippets import join, copy


FOLDER_PROVISION="/home/vagrant/provision/redis/provision"

cowsay( "provisionado redis" )

copy( join( FOLDER_PROVISION, "redis.conf" ), "/etc/redis.conf", verbose=True )

systemctl.restart( "redis" )

cowsay( "termino de provisionado redis" )
