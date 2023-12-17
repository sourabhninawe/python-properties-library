import sys
sys.path.append('/Users/sninawe/Desktop/github/python-properties-library/pyprops')

from pyprops import PyProps as p
replacementStrings={ "ADDR_SEQUENCE":"250931","WO_TMPL_ID_SEQ":"2"}
p.replaceStringsInPlace(replacementStrings,"RMS20230426.csv")