import threading
from json import dumps

from flask import Response

from src.logger import Logger

threading.current_thread().logger = Logger()


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


def log(post_data):
    if not hasattr(log, 'i'):
        log.i = 1

        logger = threading.current_thread().logger

        logger.log()
        logger.finish_scenario()

    return construct_ok_resp()

    # try:
    #     scenario = post_data['scenario']
    #     service_type = post_data['service_type']
    #     log_data = post_data['log_data']
    #
    #     threading.current_thread().logger.log(scenario, service_type, log_data)
    # except Exception as err:
    #     return construct_error_resp(err)
    #
    # return construct_ok_resp()


def finish_logging(post_data):
    return construct_ok_resp()

    # try:
    #     scenario_id = post_data['scenario_id']
    #
    #     threading.current_thread().logger.finish_scenario(scenario_id)
    # except Exception as err:
    #     return construct_error_resp(err)
    #
    # return construct_ok_resp()
