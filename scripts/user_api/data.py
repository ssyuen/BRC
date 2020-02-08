import requestsA
import json
import pandas as pd

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'SURFX~3.67|IPDN~17|PNGYX~15.17|TCBK~17.17|DMPI~5.21|VPOIX~1.81|MTN~15.51|FCOR~10.62|MWCIX~8.64|9637~5.2|','calculatePerformance':True,'calculateRisk':True})

data = portfolioAnalysisRequest.json()


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

    print('-'*15)
    print(tbl[col])
    print('-'*15)


    annualized_returns[col]= tbl[col]['sinceStartDateAnnualized']

    
    print('\n'*2)




for date in annualized_returns.keys():
    print('Date: ', date, '\nAnnualized Return Since Start: ', annualized_returns[date])
    print('\n')

#tbl
print('Total Risk of Portfolio: ', total_risk_val)
#print(totalRisk)

#print(type(data))




def application(env,start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'SURFX~3.67|IPDN~17|PNGYX~15.17|TCBK~17.17|DMPI~5.21|VPOIX~1.81|MTN~15.51|FCOR~10.62|MWCIX~8.64|9637~5.2|','calculatePerformance':True,'calculateRisk':True})
    
    data = portfolioAnalysisRequest.json()


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

        print('-'*15)
        print(tbl[col])
        print('-'*15)


        annualized_returns[col]= tbl[col]['sinceStartDateAnnualized']

    
        print('\n'*2)




    for date in annualized_returns.keys():
        print('Date: ', date, '\nAnnualized Return Since Start: ', annualized_returns[date])
        print('\n')

        #tbl
        print('Total Risk of Portfolio: ', total_risk_val)
        #print(totalRisk)

    return json.dumps({'arr':annualized_returns[annualized_returns.keys()[-1],'risk':annualized_returns[annualized_returns.keys()[-1]})
