## Xpresso Assignment

### Build
- `docker-compose up build`

### Run
- Run the following two commnds:
    - `.\autostart.bat` => to start the elasticseach instance
    - `python web/app.py` => to start the web service
- After running the above command, go to [http://localhost:5000/search?q=Space]("http://localhost:5000/search?q=Space") url
- You can provide different *keywords* to the query like *SpaceNews, NASA, Tesla, etc* to get JSON list of data
- `docker-ccompose down` -> to stop the elasticseach instance

### Assumptions
- The elastic search instance and service are running independently

> **Note: When the elastic search instance runs, wait for 10sec to run python script. Otherwise the script will show that its not connected**