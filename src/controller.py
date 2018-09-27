from flask import Response
from json import dumps

from src.logger import Logger

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


def log(post_data):
    try:
        scenario = post_data['scenario']
        service_type = post_data['service_type']
        log_data = post_data['log_data']

        logger.log(scenario, service_type, log_data)
    except Exception as err:
        return construct_error_resp(err)

    return {'status': 200, 'result': 'OK'}


def finish_logging(post_data):
    try:
        scenario_id = post_data['scenario_id']

        logger.finish_scenario(scenario_id)
    except Exception as err:
        return construct_error_resp(err)

    return {'status': 200, 'result': 'OK'}
