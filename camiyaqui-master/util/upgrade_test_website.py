# """
#     .. warning:: This file is work in progress and doesn't work as it is.
# """
# import getpass
# from fabric import Connection, Config
#
# project_name = 'dev_camiyaqui'
#
# sudo_pass = getpass.getpass("What's your sudo remote password? ")
#
# config = Config(overrides={'sudo': {'password': sudo_pass}})
#
# c = Connection('digital', config=config)
# with c.cd(f'/webapps/{project_name}/camiyaqui'):
#     c.run('git pull')
#     c.run('../venv/bin/pip install -r requirements.txt')
#     c.run('../venv/bin/python manage.py migrate --settings=camiyaqui.settings.production --noinput')
#     c.run('../venv/bin/python manage.py collectstatic --settings=camiyaqui.settings.production --noinput')
#
# c.sudo('supervisorctl restart Camiyaqui_dev')
# c.sudo('systemctl reload nginx')
