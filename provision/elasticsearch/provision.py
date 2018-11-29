#!/usr/bin/env python3
import requests
import time
from chibi.command import systemctl
import pprint


FOLDER_PROVISION="/home/vagrant/provision/elasticsearch/provision/templates"
url = 'http://localhost:9200'

while True:
    status = (
        systemctl.status( 'elasticsearch' )
            .properties.get( 'active_state', 'No' ) )
    try:
        response = requests.get( url )
    except:
        time.sleep( 10 )
        continue


    if ( status == 'active' and str( response.status_code ) == '200' ):
        break
    time.sleep( 10 )
    print( status )
    print( response.status_code, response.text )


print( requests.get( url ).text )
