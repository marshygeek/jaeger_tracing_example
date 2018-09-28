from flask import Flask

app = Flask(__name__)

from src import routes
import threading
from time import sleep

logger = threading.current_thread().logger

logger.log()
logger.finish_scenario()

"""
scenario = {'id': '1a31200d-eb46-420f-a60f-8742be848aa3', 'type': 1}
service_type = 1
log_data = {'ev': 'workwork', 'data': None}

logger = threading.current_thread().logger

logger.log(scenario, service_type, {'event': 'ringing', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})

logger.log(scenario, service_type, {'event': 'start_write_to_pipe', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})

logger.log(scenario, service_type, {'event': 'entered _onNewCall', 'call_id': 'c053759a-c301-11e8-a82c-21260f79071a', 'speech_pipe': '/tmp/speech/YVqxDm', 'integration_address': 'demo_novokuibishevsk', 'partner_call_id': 'tCFLs-xOPI', 'partner_user_id': '89020412147', 'partner_user_phone_number': None, 'dialog_record': 'c053759a-c301-11e8-a82c-21260f79071a.wav'})

logger.log(scenario, service_type, {'event': 'start dialogApp', 'call_id': 'c053759a-c301-11e8-a82c-21260f79071a'})

logger.log(scenario, service_type, {'event': 'fs cmd: "pickup"', 'data': 'None'})
sleep(1)
logger.log(scenario, service_type, {'event': 'answered', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})

logger.log(scenario, service_type, {'event': 'fs cmd: "play_file"', 'data': '/tmp/dialog/tts/crt/Анна/audio/419f89e1-f116-4093-938e-27e1e685663d_no_silence.wav'})

logger.log(scenario, service_type, {'event': 'playback_finished', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})
sleep(2)
logger.log(scenario, service_type, {'event': 'fs cmd: "play_file"', 'data': '/tmp/dialog/tts/crt/Анна/audio/04cd082e-67f4-4dbc-9fd4-b053307cd0fd_no_silence.wav'})
sleep(10)
logger.log(scenario, service_type, {'event': 'playback_finished', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})
sleep(2)
logger.log(scenario, service_type, {'event': 'fs cmd: "play_file"', 'data': '/tmp/dialog/tts/crt/Анна/audio/bf053e56-13f3-4d8b-895d-8431d315c8e3_no_silence.wav'})

logger.log(scenario, service_type, {'event': 'playback_finished', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})
sleep(1)
logger.log(scenario, service_type, {'event': 'fs cmd: "play_file"', 'data': '/tmp/dialog/tts/crt/Анна/audio/04cd082e-67f4-4dbc-9fd4-b053307cd0fd_no_silence.wav'})
sleep(10)
logger.log(scenario, service_type, {'event': 'playback_finished', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})
sleep(2)
logger.log(scenario, service_type, {'event': 'fs cmd: "play_file"', 'data': '/tmp/dialog/tts/crt/Анна/audio/22caf1ca-cac6-48ba-a1d9-8b2d5d3f9e1f_no_silence.wav'})

logger.log(scenario, service_type, {'event': 'playback_finished', 'uuid': 'c053759a-c301-11e8-a82c-21260f79071a'})
sleep(4)
logger.log(scenario, service_type, {'event': 'fs cmd: "hangup"', 'data': 'None'})

logger.finish_scenario(scenario['id'])

"""
