import requests
import time 
import pickle
import os
def getAllItems(wfmFile='data/item_data.pickle'):
    if os.path.isfile(wfmFile):
        results = pickle.load( open( wfmFile, "rb" ))
        return results
    r = requests.get("https://api.warframe.market/v1/items")
    payload = r.json()['payload']['items']['en']

    #id, item_name, url_name
    fullDict={}
    count =0
    for item in payload:
        count+=1
        print count, len(payload)
        value =getOneItemValue(item['url_name'])
        fullDict[item["item_name"].lower()]=value
        time.sleep(.2)
    pickle.dump( fullDict, open( wfmFile, "wb" ) )
    return fullDict

def getOneItemValue(itemUrlValue=None):
    value = "https://api.warframe.market/v1/items/"+itemUrlValue+"/statistics"
    r = requests.get(value)
    json_result = r.json()
    value = json_result['payload']['statistics']['90days']
    count = 0
    median = 0
    minimum=0
    for result in value:
        count+=result['volume']
        median+=result['median']*result['volume']
        minimum=minimum+result['min_price']*result['volume']
    if count==0:
        return 0
    return median/count

#Currently unused
def is_item_a_mod(itemUrlValue=None):
    r=requests.get("https://api.warframe.market/v1/items/"+itemUrlValue)
    result=r.json()
    if 'mod' in result['payload']['item']['items_in_set'][0]['tags']:
        return True
    return False

if __name__ == "__main__":
    getAllItems()

