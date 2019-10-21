from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.knowledge_base.utils import (
	SLOT_OBJECT_TYPE,
	SLOT_LAST_OBJECT_TYPE,
	SLOT_ATTRIBUTE,
	SLOT_MENTION,
	SLOT_LAST_OBJECT,
	SLOT_LISTED_OBJECTS,
	reset_attribute_slots,
	get_attribute_slots,
	get_object_name
)
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from typing import Text, Callable, Dict, List, Any, Optional

# Sample action showing interactions between the script and the bot

#class ActionName(Action):
#	def name(self):
#		return 'action_name' <-- This must match an action in the domain

#	def run(self, dispatcher, tracker, domain):
#		variable = tracker.get_slot('SLOT_NAME') <-- Get a value from a slot
#		dispatcher.utter_message('STRING TO PRINT') <-- Have bot utter message
#		return [SlotSet('SLOT_NAME', 'WHAT TO SET SLOT TO')] <-- Set a value to a slot

class ActionMyKB(ActionQueryKnowledgeBase):
	def __init__(self):
		knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
	
		super().__init__(knowledge_base)

	def get_attribute_text(self, attributes):
		if attributes is None:
			return
		response = ''
		for a in attributes:
			response += a.get('value') + ', '

		return response[:-2] + ' '

	def utter_objects(self, dispatcher: CollectingDispatcher, object_type: Text, objects: List[Dict[Text, Any]], attributes) -> None:
		if objects:
			if object_type == 'network':
				dispatcher.utter_message('The following ' + self.get_attribute_text(attributes) + 'networks are available:')
				repr_function = self.knowledge_base.get_representation_function_of_object(object_type)
				for i, obj in enumerate(objects, 1):
					dispatcher.utter_message("{}: {}".format(i, repr_function(obj)))
		else:
			dispatcher.utter_message("Sorry, I couldn't find any \"{}\" in our knowledge base.".format(object_type))

	def utter_attribute_value(self, dispatcher: CollectingDispatcher, object_name: Text, attribute_name: Text, attribute_value: Text) -> None:
		if attribute_value:
			if attribute_name == 'about':
				dispatcher.utter_message(attribute_value)
			else:
				dispatcher.utter_message("\"{}\" has the value \"{}\" for attribute \"{}\"".format(object_name, attribute_value, attribute_name))
		else:
			dispatcher.utter_message("I could not find a valid value for attribute \"{}\" for object \"{}\"".format(attribute_name, object_name))

	def _query_objects(self, dispatcher: CollectingDispatcher, tracker: Tracker) -> List[Dict]:
		object_type = tracker.get_slot(SLOT_OBJECT_TYPE)
		object_attributes = self.knowledge_base.get_attributes_of_object(object_type)

		attributes = get_attribute_slots(tracker, object_attributes)
		
		objects = self.knowledge_base.get_objects(object_type, attributes)

		self.utter_objects(dispatcher, object_type, objects, attributes)

		if not objects:
			return reset_attribute_slots(tracker, object_attributes)

		key_attribute = self.knowledge_base.get_key_attribute_of_object(object_type)

		last_object = None if len(objects) > 1 else objects[0][key_attribute]

		slots = [
			SlotSet(SLOT_OBJECT_TYPE, object_type),
			SlotSet(SLOT_MENTION, None),
			SlotSet(SLOT_LAST_OBJECT, last_object),
			SlotSet(SLOT_LAST_OBJECT_TYPE, object_type),
			SlotSet(SLOT_LISTED_OBJECTS, list(map(lambda e: e[key_attribute], objects)))
		]

		return slots + reset_attribute_slots(tracker, object_attributes)

