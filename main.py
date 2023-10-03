import requests as rq
import os
import subprocess
import datetime as dt
import time as t

webhookUrl = 'https://discord.com/api/webhooks/1158867763620753551/c1BYtEOYVxGV5tiTnj7KPdT0KxX1_pvKjnOCPh3cwThU-cNPqtQc8N_KZzvUN1hBjzop'

BIRTHDAYS = {
  '02/28':'Aarav',
  '01/03':"Mama",
  '03/23':'Baba',
  '03/24':'Aarohi',
  '10/09':'Jacob',
  '04/29':'Shruti',
  '10/03':'BdayBot'
}

def postBirthday(name, webhookUrl, today=True):
  if today:
    payload = {
      'content' : f"@everyone Birthday Reminder!\n\nIt is {name}'s Birthday Today!"
    }
  else:
    payload = {
      'content' : f"@everyone Upcoming Birthday Reminder!\n\nIt is {name}'s Birthday Tomorrow!"
    }
    
  response = rq.post(webhookUrl, json=payload)
  
  if response.status_code == 204:
    print("Success!")
  else:
    print("Error Sending Message!")

def postTomorrowBirthday(name, webhookUrl):
  postBirthday(name, webhookUrl, today=False)
  
print("Started.")
while True:
  currentDate = dt.datetime.now().strftime('%m/%d')
  
  tomorrowDate = dt.date.today() + dt.timedelta(days=1)
  tomorrowDate = tomorrowDate.strftime("%m/%d")
  
  if currentDate in BIRTHDAYS:
    name = BIRTHDAYS[currentDate]
    postBirthday(name, webhookUrl, today=True)
    
  elif tomorrowDate in BIRTHDAYS:
    name = BIRTHDAYS[tomorrowDate]
    postTomorrowBirthday(name, webhookUrl)
    
  t.sleep(60)