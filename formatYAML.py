#TODO CREATE REQUIREMENTS FILE
#TODO don't remove unicode

import yaml
import os

def properYMALFormat (inputFile=None,outputFile=None):
    #Use the resulting file if able
    if os.path.isfile(outputFile):
        return yaml.load(open(outputFile,'r'))

    startingFile=open(inputFile)
    ymalFileWrite=open(outputFile,'w')
    ayatanScuptureArea = False
    ayatanSculptureDict = {}
    for line in startingFile:
        #Tickets can take multiple lines messing things up.  
        #TODO Need to make it work or confirm that it's at the end
        if line[0:6] == "LOCALE":
            break

        newline = line

        #Make it lower case for simplicity
        newline=newline.lower()
    
        #The ayatan scupture section is completely messed up, as duplicates get removed.
        if ayatanScuptureArea==True:
            if newline[0]!='\t':
                for key in ayatanSculptureDict:
                    keylist = key.split(" ")
                    print keylist
                    newkey= " ".join([keylist[1],keylist[0],keylist[2]])
                    ymalFileWrite.write("    "+newkey+" : "+ str(ayatanSculptureDict[key])+"\r\n")
                ayatanScuptureArea=False
            else:
                print "LINE",newline
                if "sculpture" in newline:
                    if newline.split(":")[0].strip() in ayatanSculptureDict:
                        ayatanSculptureDict[newline.split(":")[0].strip()] = ayatanSculptureDict[newline.split(":")[0].strip()] + 1
                    else:
                        ayatanSculptureDict[newline.split(":")[0].strip()] = 1
                continue

        if newline.lower().strip() == "ayatan sculptures :":
            ayatanScuptureArea=True

        #Remove Blank Lines
        if len(line.strip())==0:
            continue #remove blank lines

        #Some words have double spaces in them
        newline = newline.replace("  "," ")
        newline = newline.replace("  "," ")


        #TODO please fix me.  I am really sad about this :(
        newline = newline.replace("( ","(")
        newline = newline.replace('khut-khut (s)',"small khut-khut")
        newline = newline.replace('karkina (l)',"large karkina")
        newline = newline.replace('charc eel (l)',"large charc eel")
        newline = newline.replace('norg (m)',"medium norg")
        newline = newline.replace('cuthol (m)',"medium cuthol")
        newline = newline.replace('yogwun (s)',"small yogwun")
        newline = newline.replace('charc eel (m)',"medium charc eel")
        newline = newline.replace('khut-khut (m)',"medium khut-khut")
        newline = newline.replace('sharrac (m)',"medium sharrac")
        newline = newline.replace('goopolla (m)',"medium goopolla")
        newline = newline.replace('tralok (m)',"medium tralok")
        newline = newline.replace('cuthol (s)',"small cuthol")
        newline = newline.replace('mortus lungfish (l)',"large mortus lungfish")
        newline = newline.replace('norg (s)',"small norg")
        newline = newline.replace('mawfish (m)',"medium mawfish")
        newline = newline.replace('charc eel (s)',"small charc eel")
        newline = newline.replace('goopolla (s)',"small goopolla")
        newline = newline.replace('glappid (l)',"large glappid")
        newline = newline.replace('cuthol (l)',"large cuthol")
        newline = newline.replace('tralok (s)',"small tralok")
        newline = newline.replace('mawfish (s)',"small mawfish")
        newline = newline.replace('yogwun (m)',"medium yogwun")
        newline = newline.replace('khut-khut (l)',"large khut-khut")
        newline = newline.replace('murkray (m)',"medium murkray")
        newline = newline.replace('goopolla (l)',"large goopolla")
        newline = newline.replace('sharrac (s)',"small sharrac")
        newline = newline.replace('tralok (l)',"large tralok")
        newline = newline.replace('mortus lungfish (s)',"small mortus lungfish")
        newline = newline.replace('mortus lungfish (m)',"medium mortus lungfish")
        newline = newline.replace('karkina (s)',"small karkina")
        newline = newline.replace('yogwun (l)',"large yogwun")
        newline = newline.replace('murkray (l)',"large murkray")
        newline = newline.replace('mawfish (l)',"large mawfish")
        newline = newline.replace('murkray (s)',"small murkray")
        newline = newline.replace('glappid (s)',"small glappid")
        newline = newline.replace('norg (l)',"large norg")
        newline = newline.replace('glappid (m)',"medium glappid")
        newline = newline.replace('sharrac (l)',"large sharrac")

        #Some things are different between yaml and warframe market
        newline = newline.replace("primed pistol ammo mutation","primed pistol mutation")
        newline = newline.replace("vermillion storm","vermilion storm")
        if len(newline.strip().split(" "))>=4 and newline.strip().split(" ")[3]=="relic":
            values =  newline.split(" ")
            newline=values[0]+" "+values[1]+values[2]+" intact"+ " ".join(values[4:])

        #"-" are followed by spaces for some silly reason
        newline = newline.replace("- ","-")
        #Some keys start with a space (probably should turn into a loop)
        newline = newline.replace("\t ","\t")
        newline = newline.replace("\t ","\t")
        newline = newline.replace("\t ","\t")

        #Some things randomly have a space at the begining
        if newline[0] ==" ":
            newline=newline[1:]

        #YAML can't have tabs, and removes new lines
        newline = newline.replace("\t","    ").replace("\r\n","")
        newline = unicode(newline, errors='ignore')   
   
        #Deals with exta ":" in names
        newline=newline.replace("index:","index")
        newline=newline.replace("drawing:","drawing")
   
        #Deals with keys that are empty (happens in 1 node in the starchart)
        if len(newline.split("  :")[0].strip())==0:
            splitLine = newline.split("  :")
            newline=splitLine[0]+"  UNKNOWN : "+splitLine[1]

        #Make it lower case for simplicity
        newline=newline.lower()

        #Deals with the fact not all lines have ":"
        if ":" in line:
            ymalFileWrite.write(newline+"\r\n")
        else:
            ymalFileWrite.write(newline+": ymal_compliance\r\n")
    startingFile.close()
    ymalFileWrite.close()
    return yaml.load(open(outputFile,'r'))

#ymalFile=open("1296211_throtecutter_GDPR_Warframe.ymal")
#a=yaml.load(ymalFile)
