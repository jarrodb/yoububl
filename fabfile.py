#
# Used to easily deploy code to the production server
#
# INSTALL fabric ON YOUR LOCAL MACHINE
# i.e. sudo easy_install fabric
#
from fabric.api import *

env.hosts=['65.183.54.4']

def deploy():
    project_dir = '/data/www/yoububl.com'
    with cd(project_dir):
        run("sudo git pull origin master")

