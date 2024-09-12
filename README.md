# reservamos_challenge
Reservamos code challenge in Python
=======================================================
Caso práctico - EN - Python

Code Challenge Description
In Reservamos we're always looking for ways to help our users have the best
experience when looking for travel options so that they can make the best decision
when reserving a bus or flight ticket. To accomplish this, we have to make a REST API
which can be consumed by a client app to check the weather forecast for the
destinations available in Reservamos. The API's functionality is to be able to compare
the weather forecast for the next 7 days, by day, of different destinations offered by
Reservamos. The client app must be able to send the name of a city and fetch the
maximum and minimum temperature for these places.
For this challenge you will be using OpenWeather's API to look up the temperature
using geographic coordinates, and show the results in metric units.
● Docs: https://openweathermap.org/api/one-call-api
● API key: a5a47c18197737e8eeca634cd6acb581
To find the coordinates of a given city, you will use an endpoint from the Reservamos
API where we can get data for different places by name.
● Docs: https://documenter.getpostman.com/view/6904537/TzRRCo6f
● No API key required
Expected output:
● An endpoint that receives a city name and return a list of cities with it’s
weather forecast:
● Params

● Results

● Partial or total name of any city in
Mexico, e.g:
Mon or Monterrey
● List of cities that match the given
param including the maximum and
minimum temperature for the next 7
days (include only cities into results)

Scope
● We are happy to see anything that's working so we can build on top of it
during the coding interview step of the interview process.

● It is not required to persist data in a data base, we're only interested in
showing them while using the API.
● User login is not required, anybody can look up weather forecasts.
● This challenge must be built in Django.
Deliverables
● Code repo in Github, Gitlab, Bitbucket, etc.
● Instructions to run the API locally, or a link where we can see and test the
API.

If you have any question you can contact us at challenge@reservamos.mx
