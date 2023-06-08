
"""
If the weather is cloudy today and it rained yesterday, it will rain today".
Generate the logical operation for the statement above and evaluate the weather forecast for today.
"""
weather_cloudy_today = True
weather_cloudy_yesterday = True
it_will_rain_today = weather_cloudy_today and weather_cloudy_yesterday
if it_will_rain_today:
    print("it will rain today")
else:
    print("it will not rain today")

# -----------------------------

weather_cloudy_today = False
weather_cloudy_yesterday = False
it_will_rain_today = weather_cloudy_today and weather_cloudy_yesterday
if it_will_rain_today:
    print("it will not rain today")
else:
    print("it will  rain today")