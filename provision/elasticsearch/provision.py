#!/usr/bin/env python3
import time
import requests

from chibi.command import systemctl
from chibi.file import Chibi_file
from chibi.file.snippets import join


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


f = Chibi_file( join( FOLDER_PROVISION, "resource_event.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__api_event".format( url ),
    data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "background_check.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__background_checks".format( url ),
    data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "county.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__county".format( url ), data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "log.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__logs".format( url ), data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "partner_worker_template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__partner_worker".format( url ),
    data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "resource_event.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__resource_event".format( url ),
    data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "state.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__state".format( url ), data=j )
print( r.text )


f = Chibi_file( join( FOLDER_PROVISION, "laniidae_profiles.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/laniidae_profile_data".format( url ), data=j )
print( r.text )

f = Chibi_file( join( FOLDER_PROVISION, "laniidae_sub_profiles.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/laniidae_sub_profile_data".format( url ), data=j )
print( r.text )


f = Chibi_file( join( FOLDER_PROVISION, "placement.template.json" ) )
j = f.read_json()
r = requests.put(
    "{}/_template/turn_api__placement".format( url ), data=j )
print( r.text )
