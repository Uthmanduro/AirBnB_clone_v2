#!/usr/bin/python3
"""distributes an archive to my web servers"""

from fabric.api import local, put


def do_deploy(archive_path):
    """the function that distributes the archive"""
    with open(archive_path, "r") as file_path:
        if file_path.read() = [] or file_path.read() is None:
            return "False"
    file_path = "versions/web_static_20230406163820.tgz"
    remote_path = "/tmp/versions/web_static_20230406163820.tgz"

    """upload the file to my server"""
    local("put(file_path, remote_path)")

    """uncompress the file"""
   local(tar -xzf file_path)
