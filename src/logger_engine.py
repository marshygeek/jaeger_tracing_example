from typing import Dict

from jaeger_client import Span

from src.settings import tracers


class LoggerEngine:
    def __init__(self):
        self._active_spans = {}  # type: Dict[str, Span]

    def is_exists(self, scenario_id):
        return scenario_id in self._active_spans

    def start_scenario(self, scenario_name, scenario_id, service_type, child_of=None):
        if scenario_id not in self._active_spans:
            tracer = tracers[service_type]

            parent = self._active_spans.get(child_of) if child_of else None
            span = tracer.start_span(scenario_name, child_of=parent)
            self._active_spans[scenario_id] = span

    def log(self, scenario_id, log_data):
        span = self._active_spans[scenario_id]
        span.log_kv(log_data)

    def finish_scenario(self, scenario_id):
        if scenario_id in self._active_spans:
            span = self._active_spans[scenario_id]
            span.finish()
