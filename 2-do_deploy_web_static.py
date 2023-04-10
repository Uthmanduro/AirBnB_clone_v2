#!/usr/bin/python3
"""distributes an archive to my web servers"""

from fabric.api import run, put, env
import os


env.hosts = ['54.237.35.136', '18.209.224.238']


def do_deploy(archive_path):
    """the function that distributes the archive"""

    if os.path.isfile(archive_path):
        """"get the filename from the path"""
        file_path = os.path.basename(archive_path)
        file_name = file_path.split(".")[0]
        remote_temp_path = f"/tmp/{file_path}"
        remote_path = "/data/web_static/releases/{}".format(file_name)

        """upload the file to my server"""
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(remote_path))

        """uncompress the file"""
        run(f"tar -xzf {remote_temp_path} -C {remote_path}")

        """delete the archive from th web_server"""
        run(f"rm -rf {remote_temp_path}")
        run(f"mv {remote_path}/web_static/* {remote_path}")
        run(f"rm -rf {remote_path}/web_static")

        """delete the symbolic link"""
        run("rm -rf /data/web_static/current")

        """create a new symbolic link"""
        run(f"ln -s {remote_path} /data/web_static/current")

        return "True"

    else:
        return "False"
