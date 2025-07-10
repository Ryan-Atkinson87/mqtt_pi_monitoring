"""
main.py

Runs the monitoring service by setting up configuration, logging, telemetry collection,
and ThingsBoard connectivity. Loads `.env` and `config.json`, establishes the MQTT connection,
and starts the MonitoringAgent loop.

This script is the main entry point for the monitoring application.
"""
import logging
from config_loader import ConfigLoader
from telemetry import TelemetryCollector
from TBClientWrapper import TBClientWrapper
from agent import MonitoringAgent


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    config_loader = ConfigLoader(logger)
    config = config_loader.as_dict()

    collector = TelemetryCollector()

    server = config["server"]
    token = config["token"]
    poll_period = config["poll_period"]

    client = TBClientWrapper(server,
                             token,
                             logger)

    agent = MonitoringAgent(server,
                            token,
                            logger,
                            collector,
                            client,
                            poll_period)

    client.connect()
    agent.start()
    client.disconnect()


if __name__ == "__main__":
    main()
