import django
from MySQLdb import connect
from django.conf import settings
import manage
from minicms import settings as myappsettings

DATABASES = myappsettings.DATABASES

dbname = DATABASES['default']['NAME']

conn = connect(
    host=DATABASES['default']['HOST'],
    # host="nist.lee-service.com",
    user=DATABASES['default']['USER'],
    password=DATABASES['default']['PASSWORD']
)

cs = conn.cursor()
try:
    cs.execute(r"USE %s" % dbname)
except Exception as e:
    cs.execute(r"CREATE DATABASE IF NOT EXISTS `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" % dbname)
    manage.main(["manage.py", "makemigrations"])
    manage.main(["manage.py", "migrate"])

    # from django.core.management import call_command
    #
    # if not settings.configured:
    #     settings.configure(myappsettings)
    # django.setup()
    # call_command("makemigrations", interactive=False)
    # call_command("migrate", interactive=False)
