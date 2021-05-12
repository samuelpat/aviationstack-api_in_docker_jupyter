import json
import pandas as pd


def fecthApiResponseFile(file_name):
    with open(file_name) as json_file:
        api_response = json.load(json_file)
    return api_response

 
def trasformFlightData(flights_data):
    """Taken the json data and keep just the fields that we're interested in.
    Also, replace '/' for ' - ' on departureTimezone and arrivalTerminal
    Parameters: 
    flights_data: json to transform. 

    Returns:
    list: list of flights data. 

   """
    flight_list = []
    for flight in flights_data['data']:
        row = []
        row.append(flight['flight_date'])
        row.append(flight['flight_status'])
        row.append(flight['departure']['airport'])
        if (flight['departure']['timezone'] == None):
            row.append(flight['departure']['timezone'])
        else:
            row.append(flight['departure']['timezone'].replace('/',' - '))
        row.append(flight['arrival']['airport'])
        row.append(flight['arrival']['timezone'])
        if (flight['arrival']['terminal'] == None):
            row.append(flight['arrival']['terminal'])
        else:
            row.append(flight['arrival']['terminal'].replace('/',' - '))
        row.append(flight['airline']['name'])
        row.append(flight['flight']['number'])
        flight_list.append(row)
    return flight_list


def saveDataCsv(flights_filtered_list, columns, file_name):
    """Save the trasnformed flight's data in a csv file in workdir.

    Parameters: 
    flights_filtered_list: data transformed list. 
    columns: name of the columns.
    file_name: name of the csv file.

    Returns:
    Has no return value.

   """
    df = pd.DataFrame(flights_filtered_list, columns=columns)
    
    #print for the logs.
    print('**************** FLIGHT DATA TRANSFORMED - CSV *******************')
    print(df)
    print('******************************************************************')
    
    df.to_csv(file_name)

def flow_transformApiData():
    json_data = fecthApiResponseFile('data.json')
    transformed_list = trasformFlightData(json_data)

    columns = ['flightDate','flightStatus','departureAirport','departureTimezone','arrivalAirport','arrivalTimezone','arrivalTerminal','airlineName','flightNumber']
    saveDataCsv(transformed_list, columns=columns, file_name='data.csv')

if __name__ == "__main__":
    flow_transform()

 