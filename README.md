## Xpresso Assignment

### Build
- `docker-compose build`

### Run
- Run the following command:
    - `.\autostart.bat` => to start the elasticseach instance and web service
- After running the above command, go to [http://localhost:5000/search?q=Space]("http://localhost:5000/search?q=Space") url
- You can provide different *keywords* to the query like *SpaceNews, NASA, Tesla, etc* to get JSON list of data
- `docker-compose down` -> to delete the elasticseach instance and web service containers

### Assumptions
- None

> **Note: When the elastic search instance runs, wait for 10sec to run python script. Otherwise the script will show that its not connected**