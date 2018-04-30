# csv-to-dublincore_xml
Python script to take cleaned csv format with dublin core headers and convert to XML. Project was converting in house CSV metadata to DPLA-ready Dublin Core. DC is a mix of simple and qualified elements. Script is project specific but easily adaptable.

Useful thing: tests for attributes and removes for closing XML tags. Tests for empty cells in CSV and moves on.

Adapted from: http://code.activestate.com/recipes/577423-convert-csv-to-xml/
