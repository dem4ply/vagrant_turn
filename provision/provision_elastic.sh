FOLDER_PROVISION="/home/vagrant/provision"

sleep 10

curl localhost:9200/
curl localhost:9200/_template/turn_api__partner_worker -XPUT -d@"$FOLDER_PROVISION/partner_worker_template.json" -H 'content-type: application/json'
curl localhost:9200/_template/turn_api__log -XPUT -d@"$FOLDER_PROVISION/log.template.json" -H 'content-type: application/json'
curl localhost:9200/_template/turn_api__resource_event -XPUT -d@"$FOLDER_PROVISION/resource_event.template.json" -H 'content-type: application/json'
