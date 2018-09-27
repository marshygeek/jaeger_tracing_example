import os
import configparser
from typing import Dict

from jaeger_client import Tracer, Config

from src.const import service_names

config = configparser.ConfigParser(inline_comment_prefixes=(';',))
config.read([os.getcwd() + '/conf.ini',
             os.getcwd() + '/conf.override.ini'])


def get_guni_conf():
    return {
        'bind': config.get('GUNI', 'bind'),
        'workers': config.get('GUNI', 'workers'),
        'log_file': config.get('LOG', 'file'),
        'log_level': config.get('LOG', 'level'),
    }


def get_host_port():
    return {
        'host': config.get('API', 'interface'),
        'port': config.getint('API', 'port'),
    }


def create_tracer(service_type):
    tracer_config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': config.get('JAEGER_API', 'host'),
            },
            'logging': True,
        },
        service_name=service_names[service_type],
    )

    return tracer_config.new_tracer()


tracers = {service_type: create_tracer(service_type) for service_type in service_names}  # type: Dict[int, Tracer]
