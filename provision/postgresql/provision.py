#!/usr/bin/env python3
from chibi.command import command, systemctl
from chibi.command.echo import cowsay
from chibi.file.snippets import join, copy, chown


list_of_user_to_create = [ 'vagrant', "root" ]
databases = [
    "vagrant", "root", "turning_db_dev", "turning_db_test", "turn_profiling" ]


FOLDER_PROVISION="/home/vagrant/provision/postgresql/provision"

cowsay( "provision posrgresql" )

copy(
    join( FOLDER_PROVISION, "pg_hba.conf" ),
    "/var/lib/pgsql/9.6/data/pg_hba.conf", verbose=True )

chown(
    "/var/lib/pgsql/9.6/data/pg_hba.conf",
    user_name='postgres', group_name='postgres' )

copy(
    join( FOLDER_PROVISION, "postgresql.conf" ),
    "/var/lib/pgsql/9.6/data/postgresql.conf", verbose=True )

chown(
    "/var/lib/pgsql/9.6/data/postgresql.conf",
    user_name='postgres', group_name='postgres' )


for database in databases:
    command( "su", "postgres", "-c", "createdb {}".format( database ) )
    command(
        "su", "postgres", "-c",
        "psql -d {} -c "
        "\"CREATE EXTENSION IF NOT EXISTS postgis;\"".format( database) )

for user in list_of_user_to_create:
    command( "su", "postgres", "-c", "createuser -d -s -r {}".format( user ) )
    command(
        "su", "postgres", "-c",
        "psql -c \"ALTER USER {} WITH PASSWORD 'asdf';\"".format( user ) )


systemctl.restart( "postgresql-9.6" )

cowsay( "finish provision posrgresql" )
