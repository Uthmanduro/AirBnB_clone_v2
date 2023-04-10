#!/usr/bin/python3
"""A script that distributes an archive to my web servers and decompress it"""

from fabric.api import run, put, env
import os


env.hosts = ['54.237.35.136', '18.209.224.238']


def do_deploy(archive_path):
    """the function that distributes the archivei and decompress it"""

    if os.path.isfile(archive_path):
        """get the filename from the path"""
        file_path = os.path.basename(archive_path)
        file_name = file_path.split(".")[0]
        remote_temp_path = f"/tmp/{file_path}"
        remote_path = "/data/web_static/releases/{}".format(file_name)

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xzf {} -C {}".format(remote_temp_path, remote_path))
        run(f"sudo rm -rf {}".format(remote_temp_path))
        run(f"sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        run(f"sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {} /data/web_static/current".format(remote_path))
        return True
    else:
        return False
