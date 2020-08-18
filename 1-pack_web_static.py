#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
...web_static folder of your AirBnB Clone repo, using the function do_pack"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """return the archive path if the archive has been correctly generated
    Otherwise, it should return None"""
    name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    try:
        local("mkdir -p versions")
        path = "versions/{}".format(name)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
