from minicms.settings import DATABASES

from MySQLdb import connect

conn = connect(
    host=DATABASES['default']['HOST'],
    # host="nist.lee-service.com",
    db=DATABASES['default']['NAME'],
    user=DATABASES['default']['USER'],
    password=DATABASES['default']['PASSWORD']
)

cs = conn.cursor()
cs.execute(r"CREATE DATABASE IF NOT EXISTS `djangodb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
