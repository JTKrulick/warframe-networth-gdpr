import argparse

import formatYAML
import wfMarketData
import calculateNetValue
def main():

    parser = argparse.ArgumentParser(description='Warframe net worth calculator')
    parser.add_argument('-i','--inputFile', help='Gets the txt file given by DE', required=True)
    parser.add_argument('-y','--yamlSaveLocation', help='File to save proper YAML from data', required=False)
    parser.add_argument('-o','--outputFile', help='Output of results', required=False,default="results/results.tsv")
    parser.add_argument('-w','--wfMarket', help='stores Warframe.Market data', required=False,default="data/item_data.pickle")
    parser.add_argument('-m','--minval', help='sets a minimum value, to remove all the common 1 plat items', required=False,default=0)
    
    args = vars(parser.parse_args())
    inputFile=args['inputFile']
    yamlSaveLocation =args['yamlSaveLocation']
    if yamlSaveLocation == None:
        yamlSaveLocation = inputFile.split(".")[0]+".yaml"
    outputFile =args['outputFile'] 
    wfMarket = args['wfMarket']
    mincost = int(args['minval'])

    yamlResult = formatYAML.properYMALFormat(inputFile=inputFile,outputFile=yamlSaveLocation)
     
    dictOfItems = wfMarketData.getAllItems(wfmFile = wfMarket)
    
    calculateNetValue.calculateNetValue(dictOfItems, yamlResult, outputfile=outputFile,minCost=int(mincost))    
    #get unranked mods
    #add ranked mods to that list
    #loop through pricing them All? should be there?

    #loop through items, if they have a price include it

    #loop though blueprints, if it has a price include it

    #AYATAN SCULPTURES

    #Rivens?
    
if __name__ == "__main__":
    main()

#https://docs.google.com/document/d/1121cjBNN4BeZdMBGil6Qbuqse-sWpEXPpitQH5fb_Fo/edit#
