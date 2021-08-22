## Xpresso Assignment

### Build
- `docker-compose up build`

### Run
- `docker-compose up -d`
- After running the above command, go to "http://localhost:5010/search?q=Space" url
- You can provide different *keywords* to the query like *SpaceNews, NASA, Tesla, etc* to get JSON list of data
- To test the query => `curl -X 'GET' "http://localhost:5010/search?q=Space"`

### Assumptions
- The method to search query is done in the service pi itlself
- Seperate function for search is not provided