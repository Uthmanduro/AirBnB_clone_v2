#!/usr/bin/python3
"""A fabric script that henerates a .tgz archive from web_static"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """the function that generates the .tgz archive"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path_to_file = "versions/web_static_" + time + ".tgz"
    result = local("tar -czvf {} web_static".format(path_to_file))
    if result.return_code == 0:
        return path_to_file
    else:
        return None
