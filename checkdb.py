from MySQLdb import connect

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
    cs.execute(r"USE %s" % dbname)
except Exception as e:
    cs.execute(r"CREATE DATABASE IF NOT EXISTS `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" % dbname)
    from django.core.management import call_command

    call_command("makemigrations", interactive=False)
    call_command("migrate", interactive=False)
