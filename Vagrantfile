# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

REL_DIR = File.dirname(__FILE__)
HOST_SHARE_FOLDER = REL_DIR + "/" + "src"
HOST_BACKUPS_SHARE_FOLDER = REL_DIR + "/" + "backups"
GUEST_SHARE_FOLDER = "/home/vagrant/src"
GUEST_SHARE_FOLDER_PROVISION = "/home/vagrant/provision"

BACKUPS_SHARE_FOLDER = "/home/vagrant/backups"

Vagrant.configure("2") do |config|
	config.vm.synced_folder HOST_BACKUPS_SHARE_FOLDER, BACKUPS_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder HOST_SHARE_FOLDER, GUEST_SHARE_FOLDER, owner: "vagrant", group: "vagrant", create: true
	config.vm.synced_folder 'provision', GUEST_SHARE_FOLDER_PROVISION, owner: "vagrant", group: "vagrant", create: true
	config.vm.box = "geerlingguy/centos7"

	config.vm.define 'elastic', primary: true do |m|
		m.vm.host_name = "elastic"
		config.vm.network "forwarded_port", guest: 9200, host: 9200
		m.vm.provider "virtualbox" do |vb|
			vb.name = "elastic"
			vb.memory = 1024
			vb.cpus = 1
		end
		m.vm.provision :shell, path: REL_DIR + "/" + "provision/update_centos.sh"
		m.vm.provision :shell, path: REL_DIR + "/" + "provision/install_elastic.sh"
	end

	config.vm.define 'postgres', primary: true do |m|
		m.vm.host_name = "postgres"
		config.vm.network "forwarded_port", guest: 5432, host: 5432
		m.vm.provider "virtualbox" do |vb|
			vb.name = "postgres"
			vb.memory = 512
			vb.cpus = 1
		end
		m.vm.provision :shell, path: REL_DIR + "/" + "provision/update_centos.sh"
		m.vm.provision :shell, path: REL_DIR + "/" + "provision/install_prostgresql.sh"
	end
end
