
from APIClient import  APIClient,
    endpoint,
    paginated,
    retry_request,
    HeaderAuthentication,
    JsonResponseHandler,
    JsonRequestFormatter,
)

class HydriotClient(APIClient):
    _baseURL = "https://localhost:44333/api"

    def GetNodeSensorData(self):
        url = f"{_baseURL}/GetNodeSensorData"
        return self.get(url)

    def UpdateNodeSensors(self, sensor_data):
        url = f"{_baseURL}/UpdateNodeSensors"
        return self.post(url, data=sensor_data)

#client = ClientImplementation(
#    authentication_method=BasicAuthentication(username="foo", password="secret_value"),
#    response_handler=...,
#    request_formatter=...,
#)