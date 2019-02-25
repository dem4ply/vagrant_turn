#!/usr/bin/env python3
from chibi.command import systemctl
from chibi.command.echo import cowsay
from chibi.file.snippets import join, copy, chown


FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision"

if __name__ == "__main__":

    cowsay( "config of elasticsearch" )

    copy(
        join( FOLDER_PROVISION, 'elasticsearch.yml' ),
        '/etc/elasticsearch/elasticsearch.yml' )

    chown(
        '/etc/elasticsearch/elasticsearch.yml',
        user_name='elasticsearch', group_name='elasticsearch' )

    systemctl.restart( 'elasticsearch.service' )

    cowsay( "end config of elasticsearch" )
