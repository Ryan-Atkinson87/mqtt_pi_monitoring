# callback function that will call when we will change value of our Shared Attribute
def attribute_callback(result, _):
     print(result)
     # make sure that you paste YOUR shared attribute name
     period = result.get('blinkingPeriod', 1.0)

# callback function that will call when we will send RPC
def rpc_callback(id, request_body):
    # request body contains method and other parameters
    print(request_body)
    method = request_body.get('method')
    if method == 'getTelemetry':
        attributes, telemetry = get_data()
        client.send_attributes(attributes)
        client.send_telemetry(telemetry)
    else:
        print('Unknown method: ' + method)
   
# request attribute callback
def sync_state(result, exception=None):
     global period
     if exception is not None:
         print("Exception: " + str(exception))
     else:
         period = result.get('shared', {'blinkingPeriod': 1.0})['blinkingPeriod']
