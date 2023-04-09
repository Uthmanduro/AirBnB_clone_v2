#!/usr/bin/python3
"""distributes an archive to my web servers"""

from fabric.api import *
from fabric import Connection
from datetime import datetime
import os


env.hosts = ['54.237.35.136', '18.209.224.238']
con = Connection()


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


def do_deploy(archive_path):
    """the function that distributes the archive"""
    if os.path.isfile(archive_path):
        """"get the filename from the path"""
        file_path = os.path.basename(archive_path)
        file_name = file_path.split(".")[0]
        remote_temp_path = f"/tmp/{file_path}"
        remote_path = "/data/web_static/releases/{}".format(file_name)

        """upload the file to my server"""
        local(f"put {archive_path} /tmp/")

        """uncompress the file"""
        con.run(f"tar -xzf {remote_temp_path} -C {remote_path}")

        """delete the archive from th web_server"""
        con.run(f"rm -rf {remote_temp_path}")

        """delete the symbolic link"""
        con.run(f"rm -rf /data/web_static/current")

        """create a new symbolic link"""
        con.run(f"ln -s {remote_path} /data/web_static/current")

        return "True"

    else:
        return "False"
