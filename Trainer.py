from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('F:/Bottt/ChatBot/chatterbot_corpus/data/Python/'):
        convData = open('F:/Bottt/ChatBot/chatterbot_corpus/data/Python/'+ file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        print("Training Completed")
    

setup()
