#!/usr/bin/python3
""" distributes an archive to web servers """
from fabric.api import *
env.hosts = ['35.243.251.251', '34.73.23.24']


def do_deploy(archive_path):
    """ deploys the archive """

    if not archive_path:
        return False
    try:
        filename = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        no_ext = filename.split(".")[0]
        datapath = "/data/web_static/"
        run("mkdir -p {}releases/{}/".format(datapath, no_ext))
        run("tar -xzf /tmp/{} -C {}releases/{}/".format(
            filename, datapath, no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}releases/{}/web_static/* {}releases/{}".format(
            datapath, no_ext, datapath, no_ext))
        run("rm -rf {}releases/{}/web_static".format(datapath, no_ext))
        run("rm -rf {}current".format(datapath))
        run("ln -s {}releases/{}/ {}current".format(
            datapath, no_ext, datapath))
        return True
    except:
        return False
