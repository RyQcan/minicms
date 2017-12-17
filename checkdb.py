from MySQLdb import connect

import manage
from minicms.settings import DATABASES

dbname = DATABASES['default']['NAME']

# conn = None

while True:
    try:
        conn = connect(
            host=DATABASES['default']['HOST'],
            # host="nist.lee-service.com",
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD']
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
