# reservamos_challenge
Reservamos code challenge in Python
=================================================================================

System requirements:
- Docker

Installation:
- On the command line, go to your repo clone folder
- Execute: 
  - docker compose up 
- Wait until the container is built and running
- Test on your browser:
  - http://localhost:3000

Usage:
- GET http://localhost:3000/<city>
  - Parameters:
    - city: The partial or full name of a city
  - Output:
    - (JSON) The list of matching cities and their 7 days weather forecast
  
