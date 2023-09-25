import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
stock_key=os.getenv("stock_api_key")
news_key=os.getenv("news_api_key")
twilio_key=os.getenv("twilio_auth")
twilio_sid=os.getenv('twilio_id')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
def stock_price():
    values=[]
    params={"function":"TIME_SERIES_DAILY","symbol":STOCK,"apikey":stock_key}
    url="https://www.alphavantage.co/query?"
    response=requests.get(url,params=params)
    print(response.status_code)
    data=response.json()
    first_two_values = dict(list(data["Time Series (Daily)"].items())[:2])
    for key in first_two_values:
        values.append((first_two_values[key]['4. close']))
    change=(float(values[1])-float(values[0]))/float(values[0])
    change*=100
    mod_change=abs(change)
    if mod_change<5:
        get_news(change=change)
def get_news(change):
        count=0
        news=[]
        params={"q":COMPANY_NAME,"from":"2023-09-22","sortBy":"popularity","pageSize":"3","searchIn":
                "description","apiKey":news_key}
        url="https://newsapi.org/v2/everything?"
        response=requests.get(url,params=params)
        data=response.json()
        articles=data['articles']
        for article in articles:
            news.append(article['title'])
            news.append(article['description'])
            news.append(article['url']+'\n')
            count+=1 
            if count==1:
                 break
        message(info=news, mod_change=change)
def message(info,mod_change):
    body=''
    text=''
    for i in info:
         text=text+i
    if mod_change<0:
        body=f'{COMPANY_NAME}:🔻{mod_change}'
    else:
        body=f'{COMPANY_NAME}:🔺{mod_change}'
    client = Client(twilio_sid,twilio_key)
    message = client.messages.create(
    from_='+16186994410',
    body=body+f'\n{text}',
    to='+919620635660'
    )
    print(message.sid)
stock_price()
