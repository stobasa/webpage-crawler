##Team-Granite-Backend
### A Web Crawler Parser
=========================

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


##Using the service
- We have Scraper as part of the dependencies.
- We have BeautifulSoup as part of the dependencies.
- We have Pandas as part of the dependencies.
- Make sure you import pandas. You can import pandas as pd.
- To read the excel run, use this function
``` shell
 pd.read_excel('name of file.xlsx')
```

Please make sure you read the file into a variable, acceptable variable names include d_frame, df, data_frame, etc.
To read the data frame into another another file, use this function d_frame.to_json(name of file.csv)
For more information on how to manipulate data using pandas visit https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

##Contribute guide
If you're in team-granite-backend:

- Add the main repository as an upstream git remote add upstream https://github.com/hngi/webpage-crawler.git
- Pull the latest version of the repo git fetch upstream
- follow this guide https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a if lost.
- Create a feature branch with your feature name, e.g: <user-pagination>
- Create the your feature locally and commit
- Send a PR after you have test your feature locally with Postman
- Tell us in your PR in bullet points what you have added
- Add yourself as a user to the database mongodb(this will eventually count for contribution points)
