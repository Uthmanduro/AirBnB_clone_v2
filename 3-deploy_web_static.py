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
    """the function that distributes the archive"""

    if os.path.isfile(archive_path):
        """get the filename from the path"""
        file_path = os.path.basename(archive_path)
        file_name = file_path.split(".")[0]
        remote_temp_path = f"/tmp/{file_path}"
        remote_path = "/data/web_static/releases/{}".format(file_name)

        """upload the file to my server"""
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))

        """uncompress the file"""
        run(f"sudo tar -xzf {remote_temp_path} -C {remote_path}")

        """delete the archive from th web_server"""
        run(f"sudo rm -rf {remote_temp_path}")
        run(f"sudo mv {remote_path}/web_static/* {remote_path}")
        run(f"sudo rm -rf {remote_path}/web_static")

        """delete the symbolic link"""
        run("sudo rm -rf /data/web_static/current")

        """create a new symbolic link"""
        run(f"sudo ln -s {remote_path} /data/web_static/current")

        return "True"

    else:
        return "False"


def deploy():
    """creates and distributes archive to my web servers"""
    file_path = do_pack()
    result = do_deploy(file_path)
    return (result)
