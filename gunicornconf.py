from src.settings import get_guni_conf


guni_conf = get_guni_conf()

bind = guni_conf['bind']
workers = guni_conf['workers']

errorlog = guni_conf['log_file']
loglevel = guni_conf['log_level']
accesslog = guni_conf['log_file']

capture_output = True
