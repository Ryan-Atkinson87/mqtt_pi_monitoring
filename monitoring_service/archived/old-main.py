"""
old-main.py
"""

import time
import os
from monitoring_service.archived.connection import attribute_callback, rpc_callback, sync_state
from telemetry import get_telemetry
from monitoring_service.archived.attributes import get_attributes
from dotenv import load_dotenv
from monitoring_service.archived.error_logging import setup_logging
from tb_gateway_mqtt import TBDeviceMqttClient

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN") or "ENTER_TOKEN"
THINGSBOARD_SERVER = os.getenv("THINGSBOARD_SERVER") or "IP Not Set"
   
client = None
logger = setup_logging()
   
# default blinking period
period = 1.0

def main():
    global client
    client = TBDeviceMqttClient(THINGSBOARD_SERVER, username=ACCESS_TOKEN)
    client.connect()
    client.request_attributes(shared_keys=['blinkingPeriod'], callback=sync_state)
    
    # now attribute_callback will process shared attribute request from server
    sub_id_1 = client.subscribe_to_attribute("blinkingPeriod", attribute_callback)
    sub_id_2 = client.subscribe_to_all_attributes(attribute_callback)

    # now rpc_callback will process rpc requests from server
    client.set_server_side_rpc_request_handler(rpc_callback)

    while not client.stopped:
        # Get attributes, log errors
        try:
            attributes, errors = get_attributes()
            
            for err in errors:
                logger.error(f"Attributes error: {err}")
        except Exception as e:
            logger.error(f"Attributes error: {e}")

        # Get telemetry, log errors
        try:
            telemetry, errors = get_telemetry()

            for err in errors:
                logger.error(f"Telemetry error: {err}")
        except Exception as e:
            logger.error(f"Unexpected error while getting telemetry data: {e}")
        
        client.send_attributes(attributes)
        client.send_telemetry(telemetry)
        time.sleep(60)
   
if __name__=='__main__':
    if ACCESS_TOKEN != "ENTER_TOKEN":
        main()
    else:
        print("Please change the ACCESS_TOKEN variable to match your device access token and run script again.")