from MySQLdb import connect

import manage
from minicms.settings import DATABASES

dbinfo = DATABASES['default']
dbname = dbinfo['NAME']

while True:
    try:
        conn = connect(
            host=dbinfo['HOST'],
            user=dbinfo['USER'],
            password=dbinfo['PASSWORD']
        )
        break
    except Exception as e:
        print(e)

cs = conn.cursor()
try:
    cs.execute(r"CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" % dbname)
    manage.main(["manage.py", "makemigrations"])
    manage.main(["manage.py", "migrate"])
except Exception as e:
    print(e)
finally:
    manage.main(["manage.py", "runserver", "0.0.0.0:8000"])
