FILE_CHECK=".install_elastic"
FOLDER_PROVISION="/home/vagrant/provision"
if [ ! -f ~/$FILE_CHECK ]
then
	sudo cp -v $FOLDER_PROVISION/elasticsearch.repo /etc/yum.repos.d/
	yum install -y java-1.8.0-openjdk.x86_64
	java -version 2>&1 >/dev/null | ponysay
	rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
	yum install -y elasticsearch
	sudo cp -v $FOLDER_PROVISION/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
	chown elasticsearch:elasticsearch /etc/elasticsearch/elasticsearch.yml
	systemctl enable elasticsearch.service
	systemctl start elasticsearch.service
	touch ~/$FILE_CHECK
fi
