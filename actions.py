from rasa_sdk import Action
from rasa_sdk.events import SlotSet

# Sample action showing interactions between the script and the bot

#class ActionName(Action):
#	def name(self):
#		return 'action_name' <-- This must match an action in the domain

#	def run(self, dispatcher, tracker, domain):
#		variable = tracker.get_slot('SLOT_NAME') <-- Get a value from a slot
#		dispatcher.utter_message('STRING TO PRINT') <-- Have bot utter message
#		return [SlotSet('SLOT_NAME', 'WHAT TO SET SLOT TO')] <-- Set a value to a slot
