# Team-Granite-Backend
### A Web Crawler Parser
=========================


## Installation 

- Run the App:
- Fork this repository
- Clone to your local machine
- cd into the repository and create a virtual environment with pipenv library
- activate the environmment with 
``` shell
pipenv shell
```

- Then run 
``` shell
pipenv install -r requirements.txt
```

This will download all the dependencies for this application.


## Using the service
- We have BeautifulSoup as part of the dependencies.
- We have Requests as part of the dependencies.
- We have Pandas as part of the dependencies.
- Make sure you import pandas. You can import pandas as pd.


# Error Codes
```
404, 400, 401
```

## Base Url
https://fgn-web-crawler.herokuapp.com/


## GET: 2018/

- Example
- This gets the download links for each year 
```
[
    {
        "31/12/2018": "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/DECEMBER/31-12-2018.xlsx"
    }
]
```

## GET: 2018/month/1

- Example
- This gets the download links for each Month 
```

[
    {
        "January": [
            {

            01/1/2018,
            "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/01-01-2018.xlsx"
            
            },
            {
             01/1/2018,
            "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/02-01-2018.xlsx"
            }

        ]
        
    }
]
```


## GET: 2018/month/1/day/1

- Example
- This gets the download links for each day 
```
[
    {
            "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/01-01-2018.xlsx",
            
            "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/02-01-2018.xlsx",

            "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/03-01-2018.xlsx"
        
    }
]
```



## GET: cron

- Example
- This get requests initiates 9AM every day
```
{
   "https://opentreasury.gov.ng/images/dailypaymentFGN/2018/JANUARY/01-01-2018.xlsx",
}
```


## Contribute guide
If you're in team-granite-backend:

- Add the main repository as an upstream git remote add upstream https://github.com/hngi/webpage-crawler.git
- Pull the latest version of the repo git fetch upstream
- follow this guide https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a if lost.
- Create a feature branch with your feature name, e.g: <user-pagination>
- Create the your feature locally and commit
- Send a PR after you have test your feature locally with Postman
- Tell us in your PR in bullet points what you have added
- Add yourself as a user to the database mongodb(this will eventually count for contribution points)
