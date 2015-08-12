# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "debian/wheezy64"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y streamer imagemagick python-dev python-pip libffi-dev
    sudo pip install pyasn1 --upgrade
    sudo pip install crossbar
  SHELL
end
