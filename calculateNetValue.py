


def calculateNetValue(itemPriceDict, yamlDict, outputfile, minCost=3):
    resultFile =open(outputfile,'w+')
    listOfItemsWithoutPrices =[]

    resultFile.write("NAME\tCOUNT\tCOST\tTOTAL_VALUE\r\n")

    resultFile.write("platinum"+"\t" +str(yamlDict['platinum'])+"\t"+str(1)+"\t" +str(yamlDict['platinum'])+"\r\n")
    totalPlatValue = yamlDict['platinum']
 
    for mod in yamlDict['unranked mods']:
        if mod in itemPriceDict:
            if yamlDict['unranked mods'][mod]==0 or itemPriceDict[mod]<=minCost:
                continue
            resultFile.write(mod+"\t" +str(yamlDict['unranked mods'][mod])+"\t"+str(itemPriceDict[mod])+"\t" +str(yamlDict['unranked mods'][mod]*itemPriceDict[mod])+"\r\n")
            totalPlatValue+=yamlDict['unranked mods'][mod]*itemPriceDict[mod]
        else:
            listOfItemsWithoutPrices.append(mod)
   

    for item in yamlDict['items']:
        if item in itemPriceDict:
            if yamlDict['items'][item]==0 or itemPriceDict[item]<=minCost:
                continue
            resultFile.write(item+"\t" +str(yamlDict['items'][item])+"\t"+str(itemPriceDict[item])+"\t" +str(yamlDict['items'][item]*itemPriceDict[item])+"\r\n")
            totalPlatValue+=yamlDict['items'][item]*itemPriceDict[item]
        else:
            listOfItemsWithoutPrices.append(item)


    for ayatan in yamlDict['ayatan sculptures']:
        if ayatan in itemPriceDict:
            if yamlDict['ayatan sculptures'][ayatan]==0 or itemPriceDict[ayatan]<=minCost:
                continue
            resultFile.write(ayatan+"\t" +str(yamlDict['ayatan sculptures'][ayatan])+"\t"+str(itemPriceDict[ayatan])+"\t" +str(yamlDict['ayatan sculptures'][ayatan]*itemPriceDict[ayatan])+"\r\n")
            totalPlatValue+=yamlDict['ayatan sculptures'][ayatan]*itemPriceDict[ayatan]
        else:
            listOfItemsWithoutPrices.append(ayatan)


    for blueprint in yamlDict['blueprints']:
        if blueprint in itemPriceDict:
            if yamlDict['blueprints'][blueprint]==0 or itemPriceDict[blueprint]<=minCost:
                continue
            resultFile.write(blueprint+"\t" +str(yamlDict['blueprints'][blueprint])+"\t"+str(itemPriceDict[blueprint])+"\t" +str(yamlDict['blueprints'][blueprint]*itemPriceDict[blueprint])+"\r\n")
            totalPlatValue+=yamlDict['blueprints'][blueprint]*itemPriceDict[blueprint]
        #Frame blueprints lack the word blueprint, so make sure to check for them
        elif blueprint+" blueprint" in itemPriceDict:
            blueprintBlueprintPrice = blueprint+" blueprint"
            if yamlDict['blueprints'][blueprint]==0 or itemPriceDict[blueprintBlueprintPrice]<=minCost:
                continue
            resultFile.write(blueprintBlueprintPrice+"\t" +str(yamlDict['blueprints'][blueprint])+"\t"+str(itemPriceDict[blueprintBlueprintPrice])+"\t" +str(yamlDict['blueprints'][blueprint]*itemPriceDict[blueprintBlueprintPrice])+"\r\n")
            totalPlatValue+=yamlDict['blueprints'][blueprint]*itemPriceDict[blueprintBlueprintPrice]
        else:
            listOfItemsWithoutPrices.append(blueprint)


    resultFile.write("\r\n\r\nTOTAL VALUE OF EVERYTHING:  "+ str(totalPlatValue)+"\n\n")

    resultFile.write("\r\n\r\n\r\nITEMS WITHOUT VALUE\r\n")
    for uselessVal in listOfItemsWithoutPrices:
        resultFile.write(uselessVal+"\r\n")

     
    #loop though blueprints, if it has a price include it
