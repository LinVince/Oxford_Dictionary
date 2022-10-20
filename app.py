#@title Activate the Dict Engine
import requests
import re
from bs4 import BeautifulSoup


app_id = 'YOUR OXFORD DICTIONARY APP ID'
app_key = 'YOUR OXFORD DICTIONARY APP KEY'
language = 'en'
oxford_url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/'

    
          
def search_s(word_id):
          
    #Define data structure
    Entries = [] #the list item comes from Entry

    Entry = {
        'PoS':'',
        'Pronunciation':'',
        'definitions':[], #the list item comes from definitionDicList
        }
    

    definitionDic = {
        'definition':'',
        'examples':[] #the list item comes from exampleList
        }
  
    
    url = oxford_url + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    js=r.json()
    #print (js)
 
    #Start extracting information from JSON
    for item in js['results']:
      if 'lexicalEntries' in item:
        lexicalEntry = item['lexicalEntries']
        
              
        for item2 in lexicalEntry:
          PoS = item2['lexicalCategory']['text']
          Phonetic = item2['entries'][0]['pronunciations'][0]['phoneticSpelling']
          
          #definition
          definitionDicList = []
          senses = item2['entries'][0]['senses']

          for sense in senses:                
            if 'definitions' in sense:
              definition = sense['definitions'][0]
                    
              #example
              exampleList = []
              if 'examples' in sense:                       
                for example in sense['examples']:                        
                  example = example['text']
                      
                  
                  #start putting values
                          
                          
                  exampleList.append(example)
            
              
              definitionDic = {
                  'definition':definition,
                  'examples':exampleList
                  }
                    
                    
              definitionDicList.append(definitionDic)

          Entry = {
              'PoS':PoS,
              'Pronunciation':Phonetic,
              'definitions':definitionDicList
          }

          Entries.append(Entry)

                                 
    return (Entries)
    

def search_m():
  word_ids = input('')
  
  for word_id in word_ids.split():
    print (search_s(word_id))
  

def display_s(word_id): 
  Entries = search_s(word_id)

  for Entry in Entries:   
    print (Entry['PoS'])  
    print (Entry['Pronunciation'])  
    for item in Entry['definitions']:
      print (item['definition'])
      for example in item['examples']:
        print (example)


def display_m():
  word_ids = input('')
  
  for word_id in word_ids.split():
    display_s(word_id)


def quizlet_s(word_id):
  Entries = search_s(word_id)
  print ('@' + word_id + '|')
  for Entry in Entries:   
    count = 0
    print ('[' + Entry['PoS'] + ']')  
    print ('/' + Entry['Pronunciation'] + '/')  
    for item in Entry['definitions']:
      count += 1
      print (str(count) + '. ' + item['definition'])
      for example in item['examples']:
        print ("'" + example + "'")


def quizlet_m():
  word_ids = input('')
  for word_id in word_ids.split():
    quizlet_s(word_id)

   
