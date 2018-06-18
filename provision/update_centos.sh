FILE_CHECK=".update_centos"
if [ ! -f ~/$FILE_CHECK ]
then
	yum install epel-release -y
	yum update -y
	yum groupinstall development -y
	yum groupinstall "Development Tools" -y
	yum install zlib-devel -y
	yum install -y install https://centos7.iuscommunity.org/ius-release.rpm
	yum -y install python36u python36u-pip python36u-devel git

	ln -s /usr/bin/python3.6 /usr/bin/python3

	yum install fortune-mod git vim ruby texinfo kernel-headers kernel-devel -y
	yum install -y bash-completion bash-completion-extras vim htop
	git clone https://github.com/erkin/ponysay.git
	cd ponysay
	sudo ./setup.py  install --freedom=partial
	cd

	sudo yum -y localinstall ~/tmp/cowsay.rpm
	wget --progress=bar:force \
		-O ~/tmp/cowsay.rpm \
		"http://www.melvilletheatre.com/articles/el7/cowsay-3.03-14.el7.centos.noarch.rpm"

	ponysay "end update centos
you should run this after restart the virtual machine
'/opt/VBoxGuestAdditions-5.1.10/init/vboxadd setup'"
	touch ~/$FILE_CHECK
fi
