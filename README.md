## API Usage

### List API
- Endpoint : `/api/videos/`
- Sample Response:
```json
[
  {
    "title": "MOST EFL CUP/CARABAO CUP VICTORY MANAGERS.",
    "description": "In This Video Show Most English Football League Cup/Carabao Cup Victory Managers. DON'T CLICK THIS ...",
    "link": "https://www.youtube.com/watch?v=1da1Wm3F0TU",
    "thumbnail_url": "https://i.ytimg.com/vi/1da1Wm3F0TU/mqdefault.jpg",
    "published_on": "2022-02-28T18:35:00Z"
  },
  {
    "title": "Afghanistan vs Bangladesh 1st t20 toss &amp; match prediction analysis",
    "description": "Afghanistan vs Bangladesh 1st t20 toss & match prediction analysis Sidra gaming cricket prediction share story in this video 1st ...",
    "link": "https://www.youtube.com/watch?v=ga9Ex6X2nI4",
    "thumbnail_url": "https://i.ytimg.com/vi/ga9Ex6X2nI4/mqdefault.jpg",
    "published_on": "2022-02-28T17:23:42Z"
  }
]
```


### Search API
- Endpoint : `/api/videos/?q=toss`
- Sample Response:
```json
[
  {
    "title": "Afghanistan vs Bangladesh 1st t20 toss &amp; match prediction analysis",
    "description": "Afghanistan vs Bangladesh 1st t20 toss & match prediction analysis Sidra gaming cricket prediction share story in this video 1st ...",
    "link": "https://www.youtube.com/watch?v=ga9Ex6X2nI4",
    "thumbnail_url": "https://i.ytimg.com/vi/ga9Ex6X2nI4/mqdefault.jpg",
    "published_on": "2022-02-28T17:23:42Z"
  }
]
```

## Enviroment Variables
You need to create a .env file based of the example included in the repository by running the following command:
```
cp youtube_search/.env.example youtube_search/.env
```

Update the value of the secret `YOUTUBE_API_KEY` with a valid YouTube API credentials
