#!/usr/bin/python3

import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# This function grabs our credentials
# It is easily recycled from our previous script
def returncreds():
    ## First, I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## Remove any newline characters from the api_key
    nasacreds = nasacreds.strip("\n")
    return nasacreds

# This is our main function
def main():
    ## First, grab credentials
    nasacreds = returncreds()

    ## Prompt the user to enter a start date
    startdate = input("Enter the start date (YYYY-MM-DD): ")

    ## Prompt the user to enter an end date (optional)
    enddate = input("Enter the end date (YYYY-MM-DD) [optional]: ")

    ## Build the request URL based on user input
    neourl = NEOURL + "start_date=" + startdate
    if enddate:
        neourl += "&end_date=" + enddate
    neourl += "&api_key=" + nasacreds

    # Make a request with the requests library
    neowrequest = requests.get(neourl)

    # Extract the JSON data from the response
    neodata = neowrequest.json()

    ## Display NASA's NEOW data without printing the API key
    if 'code' not in neodata:
        print(neodata)
    else:
        print("Error:", neodata['error_message'])

if __name__ == "__main__":
    main()

