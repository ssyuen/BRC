import requests
import json
import pandas as pd

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'BLK~25|AAPL~25|IXN~25|MALOX~25'})

data = portfolioAnalysisRequest.json()


f = open('out.json','a')
f.write(json.dumps(data))

print(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['latestPerf'])


latest_perf = json.dumps(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['latestPerf']) 


f = open('latest_perf.json','a')
f.write(latest_perf)

tbl = pd.read_json(latest_perf,typ='series')
print(tbl.head())
