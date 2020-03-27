#!/usr/local/bin/python3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from datetime import datetime
import json, random

# class Factory(ABC):
#     @abstractmethod
#     def create(self):
#         pass
#     def operate(self, request):
#         result = self.create(request)
#         return result

# class ContextFactory(Factory):
#     def create(self) -> Context:
#         return Context()

@dataclass(order=True, frozen=True)
class History:
    time: str = field() # datetime.now()
    sender: str = field()
    message: str = field() # default_factory=list, compare=True)

    # def update(self, message):
    #     self.message.append((message, datetime.now()))

@dataclass(order=True, frozen=True)
class Answer:
    keyword: str = field()
    response: str = field()

@dataclass(order=True, frozen=True)
class Context:
    keyword: list = field()
    text: list = field() # default_factory=list, compare=False)

class Nlp(object):
    'process messages'
    def __init__(self):
        # self.history = []
        self.context = []
        self.context_lib = []
        self.answers = {}
        self.noise = ['o', 'a', 'the']
        self.load_answers()
        self.load_context()
    
    def process(self, sender, message):
        'process message and send response'
        self.insert_update(sender, message)
        filtered = self.filter_noise()
        self.proc_context(filtered)
        return self.proc_answer()

    def insert_update(self, sender, message):
        'update message history'
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.history == None:
            self.history = History(now, sender, message)
        else:
            self.history.append(History(now, sender, message))

    def proc_context(self, message):
        'analize to understand message type and context'
        for k, context in self.context_lib:
            if context in message:
                self.context.append(k)
        else:   
            self.context.append('neutral')

    def proc_answer(self):
        'find answer using context'
        if 'question' in self.context:
            # random reorder message words
            answer = self.answers['question'] + self.history.sample() + '.'

        elif 'neutral' in self.context:
            # random reorder message words
            answer = self.answers['joint'] + self.history.sample() + '.'

        elif 'cry' in self.context:
            # appologise and ask what happend
            answer = self.answers['disapointed'] + '.'

        elif 'hello' in self.context:
            # say hi
            answer = self.answers['hello'] + ':)'
        
        elif 'bye' in self.context:
            # say bye
            answer = self.answers['bye'] + ':)'
        
        else:
            # say i cant understand
            answer = self.answers['unknown']
        
        return answer

    def filter_noise(self, message):
        'split message into list & filter out noise'
        no_characters = message.replace(",", "")
        splited = no_characters.split()
        filtered = [x for x in splited if x not in self.noise]
        return filtered
    
    def load_context(self):
        'read context.json to nlp context ojbect dict'
        with open('context.json') as json_file:
            f =json.load(json_file)
            for k, context in f.items():
                self.context_lib.append(Context(k, context))

    def load_answers(self):
        'read answers.json to dict'
        with open('answers.json') as json_file:
            f = json.load(json_file)
            for k, answer in f.items():
                # self.answers.append(Answer(k, answer))
                self.answers.update({k: answer})


nlp = Nlp()
# nlp.insert_update('me', 'hello wa po ioi i')
# nlp.insert_update('you', 'hey')
# print(nlp.filter_noise('hello wa, a po ioi the i'))
print(nlp.answers['bye'])