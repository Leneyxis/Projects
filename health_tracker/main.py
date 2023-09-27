import requests
from dotenv import load_dotenv
load_dotenv()
import os
import datetime
import time
nutri_id=os.getenv("nutri_id")
nutri_key=os.getenv("nutri_key")
sheety_key=os.getenv("sheety_key")
def exercise():
    Query=input('What did you do today?\n') 
    Url="https://trackapi.nutritionix.com/v2/natural/exercise"
    Params={'query':Query,'gender':'male'}
    Headers={'x-app-id':nutri_id,'x-app-key':nutri_key,"Content-Type": "application/json"}
    response=requests.post(url=Url,json=Params,headers=Headers) # type: ignore 
    res=response.json()
    result=(res['exercises'])
    exc=[]
    duration=[]
    calories=[]
    for i in result:
        exc.append(i['name'])
        duration.append(i['duration_min'])
        calories.append(i['nf_calories'])
    sheet(exercise=exc,time_spent=duration,calories_burnt=calories)
def sheet(exercise,time_spent,calories_burnt):
    date=datetime.date.isoformat(datetime.date.today())
    time_now=time.strftime("%H:%M:%S")
    Url='https://api.sheety.co/f74bfb5f79504a2ecdec7d5b2b0ffab1/myWorkouts/workouts'
    print(exercise)
    print(time_spent)
    print(calories_burnt)
    for i in exercise:
        Params={'workout':{'date':date,'time':time_now,'exercise':i,'duration':time_spent[exercise.index(i)],'calories':calories_burnt[exercise.index(i)]}}
        response=requests.post(url=Url,json=Params)
    print(response.text) #type: ignore


exercise()
