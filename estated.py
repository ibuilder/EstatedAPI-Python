import requests
import json


class Estated():
    def __init__(self, address, city, state, zip):
        self.address = str.replace(address, ' ', '+')
        self.city = str.replace(city, ' ', '+')
        self.state = state
        self.zip = zip
        self.estated = "https://apis.estated.com/v4/property"
        self.token = "XXXX"  # Enter API Key here
        self.url = self.estated + "?token=" + self.token + "&combined_address=" + \
            self.address + "+" + self.city + "+" + self.state + "+" + self.zip

    def __str__(self):
        return str(self.__dict__)


# Ask for property info
street = input("What is the Street Address? ")
city = input("What is the City? ")
state = input("What is the State? ")
zipcode = input("What is the Zip code? ")

# create class and variables
url = Estated(street, city, state, zipcode)

property = vars(url)
prop_address = property['address']
prop_city = property['city']
prop_state = property['state']
prop_zip = property['zip']
prop_url = property['url']
response = requests.get(prop_url)
items = response.json()

# write JSON
with open('output.json', 'w') as outfile:
    json.dump(items, outfile, ensure_ascii=False, indent=4)

# Opening JSON file
with open('output.json') as json_file:
    data = json.load(json_file)

# pull address data
longitude = data['data']['address']['longitude']
latitude = data['data']['address']['latitude']
print("Longitude:", longitude)
print("Latitude:", latitude)

# pul parcel data
frontage_ft = data['data']['parcel']['frontage_ft']
depth_ft = data['data']['parcel']['depth_ft']
print("Frontage:", frontage_ft)
print("Depth:", depth_ft)

# market_assessments
if data['data']['market_assessments'][0]['land_value'] != 'null':
    land_value = data['data']['market_assessments'][0]['land_value']
    print("Land Value:", land_value)
if data['data']['market_assessments'][0]['improvement_value'] != 'null':
    improvement_value = data['data']['market_assessments'][0]['improvement_value']
    print("Impovements:", improvement_value)
assessed_year = data['data']['market_assessments'][0]['year']
assessed_value = data['data']['market_assessments'][0]['total_value']
print("Year Assessed:", assessed_year)
print("Total Value:", assessed_value)

# owner info
owner = data['data']['owner']['name']
print("Owner:", owner)

# deed info
loan_amount = data['data']['deeds'][0]['loan_amount']
print("Loan Amount:", loan_amount)
