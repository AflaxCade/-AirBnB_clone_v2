#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric import task
from fabric import Connection
import os


env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.hosts = ['34.224.16.126', '54.237.34.32']


@task
def do_deploy(c, archive_path):
        """
        return the archive path if archive has generated correctly.
    """
        
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    archive_folder = "/data/web_static/releases/{}".format(
        archive_filename.split(".")[0]
    )

    try:
        c.put(archive_path, "/tmp/")
        c.run("mkdir -p {}".format(archive_folder))
        c.run("tar -xzf /tmp/{} -C {}".format(archive_filename, archive_folder))
        c.run("rm /tmp/{}".format(archive_filename))
        c.run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
        c.run("rm -rf {}/web_static".format(archive_folder))
        c.run("rm -rf /data/web_static/current")
        c.run("ln -s {} /data/web_static/current".format(archive_folder))

        return True

    except Exception:
        return False
