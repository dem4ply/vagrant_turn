Creation of the virtual environment with Vagrant
===========================================

Vagrant_ is a command line tool whose main objective is the creation of virtual machines, quickly, flexibly and reproducibly. It is developed in Ruby, it is open source and cross platform. Vagrant allows us to easily create an environment with the configuration we need (operating system, libraries, applications, etc).

In addition, we must install a virtualization tool. In our case we use VirtualBox_, since it is free and available on the most important platforms.

============
Dependencies
============

Install `vagrant <https://www.vagrantup.com/>`_
and `virtualbox <https://www.virtualbox.org/>`_

==========
How to use
==========

The initial configuration of the virtual machine that we are going to create will be defined in the Vagrantfile file of this repository. For start the virtual machine you put in the root of the repository and execute the command:

.. code-block:: bash

	vagrant up 
...

Or you can install element by the element with the next commands:

.. code-block:: bash

	vagrant up elastic
	vagrant up postgres
	vagrant up redis

... 

And you going to have a new virtual machine provide with all nesesary for use
elastic, postgres and redis without production settings

==========
Testing
==========

For tests is running you can use

- Elastic
.. code-block:: bash

	curl http://localhost:9200
...

- Postgres
To test Postgres it is necessary to make a connection with a database client with the data provided in the 
file [provision.py](https://github.com/turnhq/vagrant_turn/blob/master/provision/postgresql/provision.py).

- Redis	
.. code-block:: bash

	curl http://localhost:6379
...
