from MySQLdb import connect

import manage
from minicms.settings import DATABASES

dbname = DATABASES['default']['NAME']

conn = connect(
    host=DATABASES['default']['HOST'],
    # host="nist.lee-service.com",
    user=DATABASES['default']['USER'],
    password=DATABASES['default']['PASSWORD']
)

cs = conn.cursor()
try:
    cs.execute(r"CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" % dbname)
    manage.main(["manage.py", "makemigrations"])
    manage.main(["manage.py", "migrate"])
except Exception as e:
    print(e)

    # from django.core.management import call_command
    #
    # if not settings.configured:
    #     settings.configure(myappsettings)
    # django.setup()
    # call_command("makemigrations", interactive=False)
    # call_command("migrate", interactive=False)
