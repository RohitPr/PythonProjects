from datetime import datetime
import requests

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    
    # API KEY Declaration
    KIWI_API = "https://tequila-api.kiwi.com/v2/search" 
    KIWI_API_KEY = "M_SjAkzFGq67IT8j-30dmjlGs5-SFnB5"

    response = requests.get(KIWI_API)