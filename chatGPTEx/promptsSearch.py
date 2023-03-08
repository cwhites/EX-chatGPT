import os
import re
from fuzzywuzzy import process
from xpinyin import Pinyin
import csv
import json
name_list=[]
program_path = os.path.realpath(__file__)
program_dir = os.path.dirname(program_path)
json_file_path = program_dir+'/prompts/prompts.json'
name_list = []
with open(json_file_path, 'r', encoding='utf-8') as f:
        prompts = json.load(f)
        for prompt in prompts:
                name_list.append(prompt['act'])
pinlist=[]
pin =Pinyin()
for i in name_list:
        pinlist.append([re.sub('-','',pin.get_pinyin(i)),i])
def SearchPrompt(name,resultLimit=7):
        searchResults=process.extract(name, name_list, limit=resultLimit)
        if name == pin.get_pinyin(name):
                searchResultsPin=[]
        else:
                searchResultsPin=process.extract(name, pinlist, limit=resultLimit)
        finalResult=[]
        for searchResult in searchResults:
                finalResult.append([searchResult[1],searchResult[0]])
        flag=0
        for searchResult in searchResultsPin:
                flag=0
                for i in finalResult:
                        if searchResult[0][1]==i[1]:
                                flag=1
                                break
                if flag==0:
                        finalResult.append([searchResult[1],searchResult[0][1]])
        finalResult.sort(reverse=True)
        finalResultList=[]
        cnt=0
        for res in finalResult:
                finalResultList.append(res[1])
                cnt+=1
                if cnt>=resultLimit:break
        return finalResultList
if __name__ == '__main__':
        print(SearchName('comedy'))
                


 