## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## builder
* ask_builder
  - utter_builder

## thanks for ask
* ask_howdoing
  - utter_nice_asking

## who are you
* ask_whoisit
  - utter_imbot

## handle insult
* handleinsult
  - utter_handle_insult

## nicetomeetyou
* nicetomeetyou
  - utter_nicemeet

## ask_whatspossible
* ask_whatspossible
  - utter_whatspossible


## are you bot
* ask_isbot
  - utter_imbot

## date data
* sensor_data
 - action_date