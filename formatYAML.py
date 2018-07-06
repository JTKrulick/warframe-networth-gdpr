#TODO CREATE REQUIREMENTS FILE
#TODO don't remove unicode

import yaml
import os

def properYMALFormat (inputFile="1296211_throtecutter_GDPR_Warframe.txt",outputFile="1296211_throtecutter_GDPR_Warframe.ymal"):
    #Use the resulting file if able
    if os.path.isfile(outputFile):
        return yaml.load(open(outputFile,'r'))

    startingFile=open(inputFile)
    ymalFileWrite=open(outputFile,'w')
    for line in startingFile:
    
        #Tickets can take multiple lines messing things up.  
        #TODO Need to make it work or confirm that it's at the end
        if line[0:7] == "TICKETS":
            break
    
        #Remove Blank Lines
        if len(line.strip())==0:
            continue #remove blank lines
    
        #Some keys start with a space (probably should turn into a loop)
        newline = line.replace("\t ","\t")
        newline = newline.replace("\t ","\t")
        newline = newline.replace("\t ","\t")
        if newline[0] ==" ":
            newline=newline[1:]
    
        #YAML can't have tabs, and removes new lines
        newline = newline.replace("\t","    ").replace("\r\n","")
        newline = unicode(newline, errors='ignore')   
    
        #Deals with exta ":" in names
        newline=newline.replace("INDEX:","INDEX")
        newline=newline.replace("DRAWING:","DRAWING")
    
        #Deals with keys that are empty (happens in 1 node in the starchart)
        if len(newline.split("  :")[0].strip())==0:
            splitLine = newline.split("  :")
            newline=splitLine[0]+"  UNKNOWN : "+splitLine[1]
    
        #Deals with the fact not all lines have ":"
        if ":" in line:
            ymalFileWrite.write(newline+"\r\n")
        else:
            ymalFileWrite.write(newline+": YMAL_Compliance\r\n")
    startingFile.close()
    ymalFileWrite.close()
    return yaml.load(open(outputFile,'r'))

#ymalFile=open("1296211_throtecutter_GDPR_Warframe.ymal")
#a=yaml.load(ymalFile)
properYMALFormat()
