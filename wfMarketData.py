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
        time.sleep(.4)
    pickle.dump( fullDict, open( wfmFile, "wb" ) )
    return fullDict

def getOneItemValue(itemUrlValue=None):
    volumeRequest =  "https://api.warframe.market/v1/items/"+itemUrlValue+"/statistics"
    volR = requests.get(volumeRequest)
    volJson = volR.json()
    
    totalVolume = sum([ int(volume['volume']) for volume in volJson['payload']['statistics']['90days']])
    if totalVolume < 30:
        return 0
    value = "https://api.warframe.market/v1/items/"+itemUrlValue+"/orders"
    r = requests.get(value)
    json_result = r.json()
    sellValues= [item['platinum'] for item in json_result['payload']['orders'] if item['order_type']=='sell' and item['user']['status']=='ingame' and ('mod_rank' not in item or item['mod_rank']<3)]
    sellValues.sort()
    if len(sellValues)==0:
        return 0
    fewSellVal = sellValues[0:3]
    return sum(fewSellVal)/len(fewSellVal)

#Currently unused
def is_item_a_mod(itemUrlValue=None):
    r=requests.get("https://api.warframe.market/v1/items/"+itemUrlValue)
    result=r.json()
    if 'mod' in result['payload']['item']['items_in_set'][0]['tags']:
        return True
    return False

if __name__ == "__main__":
    print getAllItems()

