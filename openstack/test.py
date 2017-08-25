#!/usr/bin/env python

from auth import neutron_client
from auth import nova_client

#for flavor in nova_client.flavors.list():
#	print flavor.name

#for ava in nova_client.availability_zones.list():
#	print ava.hosts.keys()[0]

#for image in nova_client.images.list():
#	print image.name

#for net in nova_client.networks.list():
#	print net.human_id, net.id
