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
    def __init__(self, tb_host, access_token, logger):
        self.tb_host = tb_host
        self.access_token = access_token
        self.logger = logger

    def start(self):
        # Main loop
        print("Starting agent...")
        while True:
            start_time = time.time()
            poll_period_seconds = 5 # add to config.json later
            self.read_and_send_telemetry()
            self.logger.info("Agent tick...")
            end_time = time.time()
            elapsed = end_time - start_time
            delay = max(0, int(poll_period_seconds - elapsed))
            time.sleep(delay)

    def read_and_send_telemetry(self):
        self.logger.info("Reading and sending telemetry... (stub)")