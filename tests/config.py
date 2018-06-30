from sqlalchemy.dialects import registry

from clickhouse_sqlalchemy.util import compat

from tests import log

if compat.PY3:
    import configparser
else:
    import ConfigParser as configparser


registry.register(
    "clickhouse", "clickhouse_sqlalchemy.drivers.http.base", "dialect"
)
registry.register(
    "clickhouse.native", "clickhouse_sqlalchemy.drivers.native.base", "dialect"
)

# Http protocol is obsolete.
uri = 'clickhouse://default:@localhost:8123/default'

file_config = configparser.ConfigParser()
file_config.read(['setup.cfg'])

log.configure(file_config.get('log', 'level'))

host = file_config.get('db', 'host')
port = file_config.getint('db', 'port')
database = file_config.get('db', 'database')
user = file_config.get('db', 'user')
password = file_config.get('db', 'password')

uri_template = '{schema}://{user}:{password}@{host}:{port}/{database}'
native_uri = uri_template.format(
    schema='clickhouse+native', user=user, password=password, host=host,
    port=port, database=database
)

system_native_uri = uri_template.format(
    schema='clickhouse+native', user=user, password=password, host=host,
    port=port, database='system'
)
