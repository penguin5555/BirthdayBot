import requests as rq
import datetime as dt
import time as t

webhookUrl = 'https://discord.com/api/webhooks/1158867763620753551/c1BYtEOYVxGV5tiTnj7KPdT0KxX1_pvKjnOCPh3cwThU-cNPqtQc8N_KZzvUN1hBjzop'
nextBirthdayWebhookUrl = 'https://discord.com/api/webhooks/1193010830841741383/TV1iCUsYTWL7KC8TnXXIJn_Fj0fYfJKNLfXgMn6ShwdLjK75KQiWmvyg51VtpLz_YyZy'

BIRTHDAYS = {
  '02/28':'Aarav',
  '01/03':'Mama',
  '03/23':'Baba',
  '03/24':'Aarohi',
  '10/09':'Jacob',
  '04/29':'Shruti',
  '09/09':'Anjani',
  '07/27':'Nannu',
  '04/30':'Ria',
  '09/26':'Arushi',
  '12/03':'Aarya',
  '07/17':'Rucha Tai and Ruta Tai',
  '11/14':'Rama Tai',
  '08/13':'Riddhi Tai',
}

def getNextBirthday(birthdays):
  todayDate = dt.datetime.now().strftime('%m/%d')
  todayDate = dt.datetime.strptime(f'{todayDate}/{dt.datetime.now().year}', '%m/%d/%Y')

  birthdayDists = []

  for date in birthdays:
    curBirthdayDateCheck = dt.datetime.strptime(f'{date}/{dt.datetime.now().year}', '%m/%d/%Y')
    dateDistanceInDays = (curBirthdayDateCheck-todayDate).days
    if dateDistanceInDays > 0:
      birthdayDists.append((dateDistanceInDays, date))
  birthdayDists.sort(key=lambda x: x[0])

  if not birthdayDists:
    return sorted(birthdays)[0]
  
  return birthdayDists[0][1]


def postBirthday(name, webhookUrl, today=True):
  if today:
    payload = {
      'content' : f"@everyone Birthday Reminder!\n\nIt is {name}'s Birthday Today!"
    }
  else:
    payload = {
      'content' : f"@everyone Upcoming Birthday Reminder!\n\nIt is {name}'s Birthday Tomorrow!"
    }
    
  rq.post(webhookUrl, json=payload)

def postTomorrowBirthday(name, webhookUrl):
  postBirthday(name, webhookUrl, today=False)

rq.post(webhookUrl, json={'content':'server starting'})

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

  # loop waiting for 60 seconds each up until 24 hrs have passed
  for heartbeat in range(1440):
    # would print the heartbeat but it takes up log storage (bad)
    rq.post(nextBirthdayWebhookUrl, json={'content':getNextBirthday(birthdays=BIRTHDAYS)})
    t.sleep(60)