import requests
import json
import pandas as pd

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'BLK~25|AAPL~25|IXN~25|MALOX~25'})


f = open('out.json','a')
f.write(json.dumps(portfolioAnalysisRequest.json()))




