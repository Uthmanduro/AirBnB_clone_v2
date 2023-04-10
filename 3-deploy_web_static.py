#!/usr/bin/python3
"""A fabric script that henerates a .tgz archive from web_static"""


from datetime import datetime
from fabric.api import env, local, run, put
import os


env.hosts = ['54.237.35.136', '18.209.224.238']


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
        run("sudo rm -rf {}".format(remote_temp_path))
        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(remote_path))
        return True
    else:
        return False


def deploy():
    """creates and distributes archive to my web servers"""
    file_path = do_pack()
    result = do_deploy(file_path)
    return (result)
