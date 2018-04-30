# csv2xml.py
# adapted from http://code.activestate.com/recipes/577423-convert-csv-to-xml/
# First row of the csv file must be header!

import csv

csvFile = 'architectural_metadata_dcformat.csv'
xmlFile = 'csv_to_dublincore_4.xml'
subj = 'dc:subject' #looks for specific attribute to remove from closing tag; can add multiple variable here and add below
crea = 'dc:creator' #as above, different attribute

#open the csv and xml files
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# top-level & declare namespaces here!
xmlData.write('<architectural-metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:lcsh="http://id.loc.gov/authorities/subjects" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dctype="http://purl.org/dc/dcmitype/">' + "\n")

rowNum = 0
#start with header for tag names
for row in csvData:
    if rowNum == 0:
        tags = row
    else:
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)): #loops through cells per row
            if row[i]: # if the cell contains text go ahead
                if "aat" in tags[i]: # if tag contains the GAAT attribute to prevent it populating the closing XML tag with attributes. very clunky.
                    xmlData.write('    ' + '<' + tags[i] + '>' \
                    + row[i] + '</' + subj + '>' + "\n") # just close it without attribute
                elif "LCSH" in tags[i]: # if tag contains the LCSH attribute to prevent it populating the closing XML tag with attributes. very clunky.
                    xmlData.write('    ' + '<' + tags[i] + '>' \
                    + row[i] + '</' + crea + '>' + "\n") # just close it without attribute
                else:
                    xmlData.write('    ' + '<' + tags[i] + '>' \
                    + row[i] + '</' + tags[i] + '>' + "\n") # or just repeat it in the closing tag if no attributes
            else:
                #go to next tag on empty cell
                i +=1
        # adds new 
        xmlData.write('    ' + '<dc:language>en-US</dc:language>'+ "\n")
        xmlData.write('    ' + '<dc:rights>http://rightsstatements.org/vocab/NoC-NC/1.0/</dc:rights>'+ "\n")
        xmlData.write('    ' + '<dcterms:rightsholder>University of Thing, Dobbs Library</dcterms:rightsholder>'+ "\n")
        xmlData.write('    ' + '<dc:publishers>University of Thing, Dobbs Library</dc:publishers>'+ "\n")
        xmlData.write('</row>' + "\n")
    # onto next row
    rowNum +=1

xmlData.write('</architectural-metadata>' + "\n") #close the top-level tag
xmlData.close()
