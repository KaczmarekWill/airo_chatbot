## say hello
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## query knowledge base
* query_knowledge_base
  - action_query_knowledge_base

## query path 1
* greet
  - utter_greet
* query_knowledge_base
  - action_query_knowledge_base
* goodbye
  - utter_goodbye

## query path 2
* greet
  - utter_greet
* query_knowledge_base
  - action_query_knowledge_base
* query_knowledge_base
  - action_query_knowledge_base
* goodbye
  - utter_goodbye

## connect_to_mainwifi
* connect_to_mainwifi
  - utter_connect_to_mainwifi

## connect_to_guestwifi
* connect_to_guestwifi
	- utter_connect_to_guestwifi

## connect_to_dormwifi
* connect_to_dormwifi
	- utter_connect_to_dormwifi

## unfwireless_update
* unfwireless_update
	- utter_unfwireless_update

## antivirus_choice
* antivirus_choice
	- utter_antivirus_choice

## policy_key_info
* policy_key_info
	- utter_policy_key_info

## policy_key_install
* policy_key_install
	- utter_policy_key_install

## ospreynet
* ospreynet
	- utter_ospreynet
