#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """ creates a tarball """
    thetime = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(thetime)

    local("mkdir -p versions")
    process = local("tar -cvzf {} web_static".format(filename))
    
    thepath = local("readlink -f {}".format(filename))

    return thepath
