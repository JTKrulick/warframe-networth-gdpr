import argparse

import formatYAML
import wfMarketData

def main():

    parser = argparse.ArgumentParser(description='Warframe net worth calculator')
    parser.add_argument('-i','--inputFile', help='Gets the txt file given by DE', required=True)
    parser.add_argument('-y','--yamlSaveLocation', help='File to save proper YAML from data', required=False)
    parser.add_argument('-o','--outputFile', help='Output of results', required=False,default="results/results.tsv")
    parser.add_argument('-w','--wfMarket', help='stores Warframe.Market data', required=False,default="data/warframeMarketData.pickle")
    
    args = vars(parser.parse_args())
    print args
    inputFile=args['inputFile']
    yamlSaveLocation =args['yamlSaveLocation']
    if yamlSaveLocation == None:
        yamlSaveLocation = inputFile.split(".")[0]+".yaml"
    outputFile =args['outputFile'] 


      
    yamlResult = formatYAML.properYMALFormat(inputFile=inputFile,outputFile=outputFile)
     
    wfMarketData.getAllItems()




if __name__ == "__main__":
    main()

#https://docs.google.com/document/d/1121cjBNN4BeZdMBGil6Qbuqse-sWpEXPpitQH5fb_Fo/edit#
