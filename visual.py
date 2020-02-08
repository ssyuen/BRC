import requests
import json
import pandas as pd

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'BLK~100|','calculatePerformance':True,})

data = portfolioAnalysisRequest.json()


#print(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['latestPerf'])


returnsMap = json.dumps(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['returnsMap']) 

# print(returnsMap)

f = open('returnsMap.json','w')
f.write(returnsMap)

#tbl = pd.read_json(returnsMap,typ='series')
tbl = pd.read_json(returnsMap)
print(tbl)

#tbl
