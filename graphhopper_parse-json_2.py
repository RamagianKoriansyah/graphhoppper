import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "washington, D.C"
loc2 = "Baltimore, Maryland"
key = "1a48a927-20ec-463a-b97c-dd79c05fb27f"  ### Replace with your API key

def geocoding (location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?" 
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    # print("Geocoding API URL for " + location + ":\n" + url)
    if json_status == 200:
        json_data = requests.get(url).json()
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["country"]

        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""
        
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""
        
        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)

    else:
        lat="null"
        lng="null"
        new_loc=location
    return json_status,lat,lng,new_loc

orig = geocoding(loc1, key)
print(orig)
dest = geocoding(loc2, key)
print(dest)
