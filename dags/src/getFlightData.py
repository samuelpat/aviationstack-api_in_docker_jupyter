import requests
import json
import os

#Parameters for the connection. This should be in a external and secure source.
params = {
  'access_key': 'ae1009e333ffb85534024de33722fae6',
  'limit': '100',
  'flight_status': 'active'
}

def getApiResponse():
    """Get Flights API's Data Response. Please visit the official web page for more information.
    API Documentation --> [ https://aviationstack.com/documentation ]

    Parameters: It takes no parameters.

    Returns:
    json:Returning the API's response. This looks like this --> {'pagination: {some pagination info}, 'data': [{flight data 1},{flight data 2}]}

    """
    try:
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
        api_response = api_result.json()
    except:
        print("ERROR GETTING API DATA: An exception occurred while Flights API was been requested")
    
    return api_response
    

def saveJson(api_response, file_name):
    """Save a json in the workdir.

    Parameters: 
    api_reponse: json that comes from the API.
    file_name: name of the file that 

    Returns:
    Has no return value.

   """
    with open(file_name, 'w') as outfile:
        json.dump(api_response, outfile)


def flow_getApiData():
    """Director. It does the same that  main() function.

    Parameters: 
    It takes no parameters.

    Returns:
    Has no return value.

   """
    flight_api_response = getApiResponse()
    
    #print for the logs.
    print('************************* FLIGHT API RESPONSE ***********************')
    print(flight_api_response)
    print('*********************************************************************')
    
    #saving the data that has been downloaded. Now, it's available for other consumers.
    #file_name should be chosen by parameters.
    saveJson(api_response=flight_api_response, file_name='data.json')

if __name__ == "__main__":
    flow()
