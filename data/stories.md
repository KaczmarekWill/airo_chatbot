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
