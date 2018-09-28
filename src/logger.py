from src.const import scenario_names
from src.logger_engine import LoggerEngine


class Logger:
    def __init__(self):
        self._engine = LoggerEngine()

    def log(self):
        # Data for testing
        scenario = {'id': '123', 'type': 1}
        service_type = 1
        log_data = {'ev': 'testing'}

        scenario_id = scenario['id']
        if not self._engine.is_exists(scenario_id):
            scenario_name = scenario_names[scenario['type']]
            self._engine.start_scenario(scenario_name, scenario_id, service_type, scenario.get('child_of'))

        self._engine.log(scenario_id, log_data)

    def finish_scenario(self):
        # Data for testing
        scenario_id = '123'

        self._engine.finish_scenario(scenario_id)
