import requests

from twilio.rest import Client

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_API = "01e49b20ed3085887630aee99b0c733d"

account_sid = "AC56ebe5a97ceb6992e777e2461e0a9975"
authentic_token = "86bff59cecef8f099df32e923370f0b1"





weather_parameters = {
    "lat": -25.8589,
    "lon": 28.1858,
    "appid": MY_API,
    "exclude": "current,minutely,daily"
}

response = requests.get(END_POINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_not_rain = True

for h_data in weather_slice:
    condition_code = h_data["weather"][0]["id"]
    if int(condition_code) > 800:
        will_not_rain = True

if will_not_rain:
    client = Client(account_sid,authentic_token)
    message = client.messages \
        .create(
        body="Clears skies for atleast the next hour",
        to="+27658742364",
        from_="+15617820426",


    )
print(message.status)




