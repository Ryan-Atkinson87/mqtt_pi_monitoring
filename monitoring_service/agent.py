"""
agent.py

Defines the MonitoringAgent class, which manages telemetry and attribute
reporting to ThingsBoard. This class owns the lifecycle of the monitoring
process, including connecting to the MQTT broker, scheduling telemetry updates,
and handling incoming server-side RPC or attribute updates.

Classes:
    MonitoringAgent

Usage:
    Instantiate MonitoringAgent and call .start() to begin the monitoring loop.
"""
import time


class MonitoringAgent:
    def __init__(self,
                 tb_host,
                 access_token,
                 logger,
                 telemetry_collector,
                 poll_period=60
                 ):
        self.tb_host = tb_host
        self.access_token = access_token
        self.logger = logger
        self.collector = telemetry_collector
        self.poll_period = poll_period
        # TODO: add poll_period to config.json when created

    def start(self):
        self.logger.info("MonitoringAgent started.")
        # Main loop
        while True:
            start_time = time.time()
            self.read_and_send_telemetry()
            self.logger.info("Agent test tick...")
            end_time = time.time()
            elapsed = end_time - start_time
            delay = max(0, int(self.poll_period - elapsed))
            time.sleep(delay)

    def read_and_send_telemetry(self):
        self.logger.info("Reading telemetry... (stub)")

        telemetry, errors = self.collector.get_telemetry()
        self.logger.info(f"Collected telemetry: {telemetry}")
        for err in errors:
            self.logger.error(f"Telemetry error: {err}")
