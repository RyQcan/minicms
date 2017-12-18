import logging
import os
import subprocess
import time

from MySQLdb import connect

import manage
from minicms.settings import DATABASES

logger = logging.getLogger(__name__)
try:
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
            logger.error(e)
            time.sleep(2)
    try:
        cs = conn.cursor()
        cs.execute(r"CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci" % dbname)
    except Exception as e:
        logger.error(e)
    if subprocess.run(["python", "manage.py", "sqldiff", "-a"]).returncode != 0:
        manage.main(["manage.py", "makemigrations", "--check"])
        manage.main(["manage.py", "migrate"])
except Exception as e:
    logger.error(e)
finally:
    listen_addr = os.getenv('LISTEN_ADDR', '0.0.0.0')
    listen_port = os.getenv('LISTEN_PORT', '8000')

    manage.main(["manage.py", "runserver", "%s:%s" % (listen_addr, listen_port)])
