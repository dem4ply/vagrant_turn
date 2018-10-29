FOLDER_PROVISION="/home/vagrant/provision"

while [ $( curl -I localhost:9200 2> /dev/null | grep -q -v "200 OK" ) ]
do
	sleep 10
done

sleep 2

curl -v localhost:9200/ 2> /dev/null

curl -v localhost:9200/_template/turn_api__partner_worker -XPUT \
	-d@"$FOLDER_PROVISION/partner_worker_template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__log -XPUT \
	-d@"$FOLDER_PROVISION/log.template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__resource_event -XPUT \
	-d@"$FOLDER_PROVISION/resource_event.template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__partner -XPUT \
	-d@"$FOLDER_PROVISION/partner.template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__county -XPUT \
	-d@"$FOLDER_PROVISION/county.template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__state -XPUT \
	-d@"$FOLDER_PROVISION/state.template.json" \
	-H 'content-type: application/json' 2> /dev/null

curl -v localhost:9200/_template/turn_api__background_checks -XPUT \
	-d@"$FOLDER_PROVISION/background_check.template.json" \
	-H 'content-type: application/json' 2> /dev/null
