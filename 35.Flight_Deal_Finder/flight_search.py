from datetime import datetime
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    KIWI_API = "https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021"
