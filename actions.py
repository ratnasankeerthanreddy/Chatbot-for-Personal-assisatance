from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from utils import convert_timestamp
from rasa_sdk.events import AllSlotsReset
import datetime
from datetime import timedelta, date
import dateutil.parser
import boto3
from boto3.dynamodb.conditions import Key

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Hello World!")
#         return []

def get_doc(date):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('sensor_daily_summary')
	doc = table.get_item(Key={'farmId':'demo_farm_1','date': date})
	return doc['Item']

# class ActionSearchRestaurant(Action):
# 	def name(self) -> Text:
# 		return "action_search_restaurant"
# 	def run(self, dispatcher: CollectingDispatcher, 
# 		tracker: Tracker,
# 		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# 		entities = tracker.latest_message['entities']
# 		print(entities)
# 		for e in entities:
# 			if e['entity'] == 'type':
# 				name = e['value']
# 			if name == 'indian':
# 				message = "Items: Indian1, Indian2, Indian3, Indian4"
# 		dispatcher.utter_message(text=message)
# 		return []

param_arr = ["salinity", "solarRad", "airTemp", "aeration", "potassium", "moisture", "soilTemp", "respiration", "pressure", "phosphorus", "pH", "humidity", "nitrogen", "evapotranspiration(ET)"]

class ActionGetDate(Action):

	def name(self):
		return 'action_date' #****This is used in the story!****

	def run(self, dispatcher, tracker, domain):

		try:
			slots = tracker.current_slot_values()
			slot_time = slots['time']
			f_date = convert_timestamp(slot_time)
			date_s = f_date.strftime("%Y-%m-%d")
			str_date = f_date.strftime('%B %d, %Y')
		except:
			f_date = date.today()
			date_s = f_date.strftime("%Y-%m-%d")
			str_date = f_date.strftime('%B %d, %Y')
			# dispatcher.utter_message(text='Please enter the date properly')
			# return [AllSlotsReset()]

		try:
			doc = get_doc(date_s)
			# st = f"""DATE: {date}\nAir Temparature: {doc['airTemp']}\nSoil Temparature: {doc['soilTemp']}\nMoisture: {doc['moisture']}\nPressure: {doc['pressure']}\nHumidity: {doc['humidity']}\nPhosphorus: {doc['phosphorus']}\nNitrogen: {doc['nitrogen']}\nPotassium: {doc['potassium']}\nSolar Radiation: {doc['solarRad']}\nSalinity: {doc['salinity']}\nPH: {doc['pH']}"""
			st = f'Sensor data on {str_date}'
			for key in param_arr:
				st += '\n{:<12}: {:.2f}'.format(key, float(doc[key]))
			dispatcher.utter_message(text=st)
		except:
			dispatcher.utter_message(text='No data recorded on '+str_date)

		return [AllSlotsReset()] 

