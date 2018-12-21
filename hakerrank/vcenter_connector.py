from __future__ import print_function
from vconnector.core import VConnector
from pyVim import connect
import pyVmomi


import json

def test_vcenter_connection():
    client = VConnector(
        user='rbade@vmware.com',
        pwd='Ark1nc0113ct0R',
        host='10.197.17.51'
    )
    print(client.connect())
    vms = client.get_vm_view()
    #hosts = client.get_host_view()
    hosts = get_host_details(client)
    print (vms.view)

    print ("success")

def get_host_details(client):
    host = client.get_object_by_property(
        property_name='name',
        property_value='10.196.7.63',
        obj_type = pyVmomi.vim.HostSystem
    )

    return  host