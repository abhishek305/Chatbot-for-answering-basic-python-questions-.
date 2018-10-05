from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

def bot():
    

    bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.2,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],trainers='chatterbot.trainers.ListTrainers')
    bot.set_trainer(ListTrainer)

 
    x=pyttsx3.init()
    x.setProperty('rate',130)
    x.setProperty('volume',8)
    while (True):
        msg = input('Human: ')
        if msg.strip() != 'Bye':
            x.say(msg)
            reply = bot.get_response(msg)
            print('Bot : ',reply)
            x.say(reply)
        if msg.strip() == 'Bye':
            print('Bot : Bye & have a nice day !!')
            x.say(msg)
            break
        x.runAndWait()
bot()        
        
