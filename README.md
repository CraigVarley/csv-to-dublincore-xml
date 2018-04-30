# metadata-csv-to-xml
Python script to take cleaned csv format with dublin core headers and convert to XML. Project was converting in house CSV metadata to DPLA-ready Dublin Core. Script is project specific but easily adaptable.

Useful thing: tests for attributes and removes for closing XML tags. Tests for empty cells in CSV and moves on.

Clunky thing: the attribute test looks for specific attribute text in the csv header, which is stored in a variable. So if it finds string "aat" in the header it will simple use the dc:subject for the closing tag and skip the attribute. This requires a separate variable for each attribute text. Not ideal.

All records are required to be in the same csv but one could adapt easily to iterate through several different files. I quickly cleaned the metadata in a spreadsheet first before conversion.

Adapted from: http://code.activestate.com/recipes/577423-convert-csv-to-xml/ so thanks to that person for the useful script.
