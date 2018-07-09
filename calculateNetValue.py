


def calculateNetValue(itemPriceDict, yamlDict, outputfile, minCost=0):
    totalPlatValue = 0
    listOfItemsWithoutPrices =[]

    print "NAME","\t","COST","\t","COUNT","\t","TOTAL_VALUE"
    
    for mod in yamlDict['unranked mods']:
        if mod in itemPriceDict:
            if yamlDict['unranked mods'][mod]==0 or itemPriceDict[mod]<=minCost:
                continue
            print mod,"\t" ,yamlDict['unranked mods'][mod],"\t",itemPriceDict[mod],"\t" ,yamlDict['unranked mods'][mod]*itemPriceDict[mod]
            totalPlatValue+=yamlDict['unranked mods'][mod]*itemPriceDict[mod]
        else:
            listOfItemsWithoutPrices.append(mod)
   

    for item in yamlDict['items']:
        if item in itemPriceDict:
            if yamlDict['items'][item]==0 or itemPriceDict[item]<=minCost:
                continue
            print item,"\t" ,yamlDict['items'][item],"\t",itemPriceDict[item],"\t" ,yamlDict['items'][item]*itemPriceDict[item]
            totalPlatValue+=yamlDict['items'][item]*itemPriceDict[item]
        else:
            listOfItemsWithoutPrices.append(item)


    for ayatan in yamlDict['ayatan sculptures']:
        if ayatan in itemPriceDict:
            if yamlDict['ayatan sculptures'][ayatan]==0 or itemPriceDict[ayatan]<=minCost:
                continue
            print ayatan,"\t" ,yamlDict['ayatan sculptures'][ayatan],"\t",itemPriceDict[ayatan],"\t" ,yamlDict['ayatan sculptures'][ayatan]*itemPriceDict[ayatan]
            totalPlatValue+=yamlDict['ayatan sculptures'][ayatan]*itemPriceDict[ayatan]
        else:
            listOfItemsWithoutPrices.append(ayatan)


    for blueprint in yamlDict['blueprints']:
        if blueprint in itemPriceDict:
            if yamlDict['blueprints'][blueprint]==0 or itemPriceDict[blueprint]<=minCost:
                continue
            print blueprint,"\t" ,yamlDict['blueprints'][blueprint],"\t",itemPriceDict[blueprint],"\t" ,yamlDict['blueprints'][blueprint]*itemPriceDict[blueprint]
            totalPlatValue+=yamlDict['blueprints'][blueprint]*itemPriceDict[blueprint]
        #Frame blueprints lack the word blueprint, so make sure to check for them
        elif blueprint+" blueprint" in itemPriceDict:
            blueprintBlueprintPrice = blueprint+" blueprint"
            if yamlDict['blueprints'][blueprint]==0 or itemPriceDict[blueprintBlueprintPrice]<=minCost:
                continue
            print blueprintBlueprintPrice,"\t" ,yamlDict['blueprints'][blueprint],"\t",itemPriceDict[blueprintBlueprintPrice],"\t" ,yamlDict['blueprints'][blueprint]*itemPriceDict[blueprintBlueprintPrice]
            totalPlatValue+=yamlDict['blueprints'][blueprint]*itemPriceDict[blueprintBlueprintPrice]
        else:
            listOfItemsWithoutPrices.append(blueprint)


    print "\n\nTOTAL VALUE OF EVERYTHING", totalPlatValue,"\n\n"

    print "\n\n\n","ITEMS WITHOUT VALUE"
    for uselessVal in listOfItemsWithoutPrices:
        print uselessVal

     
    #loop though blueprints, if it has a price include it
