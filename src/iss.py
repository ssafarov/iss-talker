from datetime import datetime, timedelta

from src import service
from src.api import Api
from src.service import to_float

"""Station Class - API interaction and formatting&handling responses"""


class Iss:

    def __init__(self):
        self.Api = Api()
        self.helpers = service
        self.status = True
        self.message = ''

    """Request and return crew onboard"""

    def get_people(self, args=None):
        self.status = True
        people_result = Api.get_people_onboard(self.Api)
        if ('status' in people_result) and (people_result['status'] == True):
            craft = people_result['people'][0]["craft"]
            crew = ''
            for p in people_result['people']:
                crew = crew + ', ' + p["name"]
            self.message = "There are " + str(people_result["number"]) + " people aboard the " + str(
                craft) + ":" + crew[1:]
        else:
            self.status = False
            self.message = "There are error during API interaction. Unable to get a valid response from third party " \
                           "API, error message: " + people_result['reason']

    """Request and return current location"""

    def get_loc(self, args=None):
        self.status = True
        location_result = Api.get_location(self.Api)
        if ('status' in location_result) and (location_result['status'] == True):
            position = location_result["iss_position"]
            lat = position["latitude"]
            lon = position["longitude"]
            dto_local = datetime.fromtimestamp(location_result["timestamp"])
            self.message = "The ISS current location_result at " + str(dto_local) + " is " + lat + ", " + lon
        else:
            self.status = False
            self.message = "There are error during API interaction. Unable to get a valid response from third party " \
                           "API, error message: " + location_result['message']

    """Request and return passes over the point"""

    def get_pass(self, args=None):
        self.status = False
        self.message = "Wrong amount of arguments provided. Current latitude and longitude should be provided: [" \
                       "python main.py pass 45 -80] "

        if len(args) == 2:
            secs_total = 0
            raises = ''
            latitude = to_float(args[0])
            longitude = to_float(args[1])
            if isinstance(latitude, (int, float)) and isinstance(longitude, (int, float)):
                pass_result = Api.get_pass_details(self.Api, str(latitude), str(longitude))
                if pass_result['status']:
                    for p in pass_result['response']:
                        secs_total = secs_total + int(p["duration"])
                        moments = "{:0>8}".format(str(timedelta(seconds=p["duration"])))
                        raises = raises + str(
                            datetime.fromtimestamp(p["risetime"])) + " for the " + moments + " (" + str(
                            p["duration"]) + " secs)\n"

                    secs = "{:0>8}".format(str(timedelta(seconds=secs_total)))
                    self.status = True
                    self.message = "The ISS will be overhead of " + str(latitude) + ", " + str(
                        longitude) + " for the total time of " + secs + " (" + str(
                        secs_total) + " secs) in the following moments: \n" + raises
                else:
                    self.message = "Invalid arguments provided: " + pass_result["reason"] + "Please be noted to avoid " \
                                                                                            "0 in latitude and " \
                                                                                            "longitude and latitudes " \
                                                                                            "greater than 71.73 " \
                                                                                            "degrees due to core API " \
                                                                                            "limitations "
            else:
                self.message = "Wrong arguments provided. Latitude and longitude should be provided as a valid " \
                               "numbers: [python main.py pass 45 -80]. Please be noted to avoid 0 in latitude and " \
                               "longitude and latitudes greater than 71.73 due to core API limitations "
