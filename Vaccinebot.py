import time
import json 
import requests
from datetime import datetime, date, timedelta
from telegram import *
from telegram.ext import *

#PARAMETERS
listdis = [] #List of Districts you want to search
bot = Bot('')
chat_id = 
url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="
url2 = "&date="
vaccine_list = ['COVAXIN', 'SPUTNIK V'] #List of Vaccines you want to search
notification_history = []


#helper functions
def clear_history():
    i = 0
    while i < len(notification_history):
        #comparing year
        if notification_history[i][1][-4:] < today.strftime("%d-%m-%Y")[-4:]:
            del notification_history[i]
        elif notification_history[i][1][3:5] < today.strftime("%d-%m-%Y")[3:5]:
            del notification_history[i]
        elif notification_history[i][1][0:2] < today.strftime("%d-%m-%Y")[0:2]:
            del notification_history[i]
        else:
            i += 1

def send_message(json_data, place, vaccine):
    if place == 0:
        st = "SLOT filled and less than 10 for {} dose 1 ".format(vaccine)
    else:
        st = "SLOT available for {} dose 1 ".format(vaccine)
    bot.send_message(chat_id=chat_id, 
                     text=st+
                     "\nDate: "+json_data['centers'][k]['sessions'][j]['date']+
                     "\nDistrict: "+json_data['centers'][k]['district_name']+
                     "\nCenter Name: "+json_data['centers'][k]['name']+
                     "\nAddress: "+json_data['centers'][k]['address']+
                     "\nSlots: "+ json.dumps(json_data['centers'][k]['sessions'][j]["slots"])+
                     "\nAvailable doses: "+str(json_data['centers'][k]['sessions'][j]["available_capacity_dose1"]))
    time.sleep(5)


while 1>0:
    for district in listdis:
        today = datetime.today()
        
        json_data = requests.get(url1 + str(district) + url2 + today.strftime("%d-%m-%Y")).json()
        
        for k in range(len(json_data['centers'])):
            for j in range(len(json_data['centers'][k]['sessions'])):
                if json_data['centers'][k]['sessions'][j]['vaccine'] in vaccine_list and int(json_data['centers'][k]['sessions'][j]['available_capacity_dose1']) > 0:
                    counter = 0
                    for notification in notification_history:
                        if notification[0] == json_data['centers'][k]['center_id'] and notification[1] == json_data['centers'][k]['sessions'][j]['date']:
                            counter = 1
                            if (notification[2] != today.strftime("%d-%m-%Y") and today.strftime("%H")=="06") or (notification[3] > 10 and json_data['centers'][k]['sessions'][j]['available_capacity_dose1'] <= 10):
                                notification[2] = today.strftime("%d-%m-%Y")
                                notification[3] = json_data['centers'][k]['sessions'][j]['available_capacity_dose1']
                                send_message(json_data, 0, json_data['centers'][k]['sessions'][j]['vaccine'])
                                
                    #counter is 0 if notification has not been sent previously
                    if counter == 0:
                        #adding this notification to the notification history
                        notification_history.append([json_data['centers'][k]['center_id'], json_data['centers'][k]['sessions'][j]['date'],
                                                    today.strftime("%d-%m-%Y"), json_data['centers'][k]['sessions'][j]['available_capacity_dose1']])
                        send_message(json_data, 1, json_data['centers'][k]['sessions'][j]['vaccine'])

    clear_history()
    time.sleep(300)