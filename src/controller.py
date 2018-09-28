from json import dumps

from flask import Response

from src.logger import Logger
from src.settings import Tracers

logger = Logger()


def construct_error_resp(error):
    result = {
        'status': 500,
        "errors": [{
            "code": 1,
            "message": str(error)
        }]
    }
    return Response(dumps(result), status=500, content_type='application/json; charset=utf-8')


def construct_ok_resp():
    return dumps({'status': 200, 'result': 'OK'})


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@run_once
def init_tracers():
    Tracers.init_tracers()


def log(post_data):
    init_tracers()

    try:
        scenario = post_data['scenario']
        service_type = post_data['service_type']
        log_data = post_data['log_data']

        logger.log(scenario, service_type, log_data)
    except Exception as err:
        return construct_error_resp(err)

    return construct_ok_resp()


def finish_logging(post_data):
    try:
        scenario_id = post_data['scenario_id']

        logger.finish_scenario(scenario_id)
    except Exception as err:
        return construct_error_resp(err)

    return construct_ok_resp()
