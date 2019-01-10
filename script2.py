#import os
#os.system(' pip show requests') 
import urllib.request
contents = urllib.request.urlopen("http://www.google.com").read()
#print(contents)