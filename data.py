import requests
import json
import pandas as pd


def call(args):
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : args,'calculatePerformance':True,'calculateRisk':True})

    print(args)
    data = portfolioAnalysisRequest.json()
    #return json.dumps(data)
    
    #print(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['latestPerf'])
    
    
    returnsMap = json.dumps(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['returnsMap']) 
    portfolio = json.dumps(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0])
    totalRisk = json.dumps(data['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['riskData'])

    f = open('portfolio.json','w')
    f.write(portfolio)


    f = open('totalRisk.json','w')
    f.write(totalRisk)

    f = open('returnsMap.json','w')
    f.write(returnsMap)



    total_risk_val = eval(totalRisk)['totalRisk']
    annualized_returns = {}

    #tbl = pd.read_json(returnsMap,typ='series')
    tbl = pd.read_json(returnsMap)

    for col in tbl.columns:
        #print('-'*15)
        #print(tbl[col])
        #print('-'*15)
        annualized_returns[col]= tbl[col]['sinceStartDateAnnualized']
        #print('\n'*2)
        
    # for date in annualized_returns.keys():
        
        # print('Date: ', date, '\nAnnualized Return Since Start: ', annualized_returns[date])
        # print('\n')

        # print('Total Risk of Portfolio: ', total_risk_val)
    #print(totalRisk)
    
    #print(type(data))
    
    pair = {'arr':annualized_returns[sorted(annualized_returns.keys())[-1]],'risk':total_risk_val}
    print(pair)
    return json.dumps(pair)
