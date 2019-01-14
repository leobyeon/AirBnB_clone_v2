#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""


def do_pack():
    """ creates a tarball """
    from fabric.api import local
    from datetime import datetime

    thetime = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "/versions/web_static_{}.tgz".format(thetime)

    local("mkdir -p versions")
    process = local("tar -cvzf {} ./web_static".format(filename))

    if process.succeeded:
        return filename
    else:
        return None
