import requests
import json
import sys
import time

from datetime import datetime

class WebClient(object):
    base_url = "n/a"

    def __init__(self):
        self.base_url = "https://localhost:44333"

    def show_api_result_details(self, result):
        print (f"Result code: {result.status_code}")
        if result.status_code == 200:
            print (self.get_json_text(result.json()))
        print (result.headers)
        print ("==================================================================")
        print()

    def get_json_text(self, obj):
        # create a formatted string of the Python JSON object
        return json.dumps(obj, sort_keys=True, indent=4)

    def get_json_object(self, obj):
        # create a json object that can be traversed
        return json.loads(self.get_json_text(obj))

    def transform_sensor_data(self, sensor_list):
        timestamp = datetime.now()

        data = [
            {
                "name": "Water Level",
                "type": 1,
                "stringValue": "0",
                "readTime": timestamp,
            }
        ]

        return data
    
    def upload_sensor_readings(self, sensor_data, node_id):
        url = f"{self.base_url}/api/node/UpdateNodeSensors/{node_id}"
        data = self.transform_sensor_data(sensor_data)

        username = "hydriot@test.com"
        password = "3!WRVhEWsqaxFBrCyP6V"

        success = False

        try:
            # TODO: Remove verify=False before deploying to production (Local Testing Only)
            response = requests.put(url, json=data, auth=(username, password), verify=False)

            if response.status_code == 200:
                success = True

        except:
            e = sys.exc_info()[0]
            print(f"Failed to update sensor reading. Error details >> {e}")
            # Sleep for 2s so that message is visible
            time.sleep(2)

        # finally:
             # client.show_result_details(response)

        return success




client = WebClient()

client.upload_sensor_readings({},'508728DE-F6AC-48C9-9D12-F18E0674A70A')