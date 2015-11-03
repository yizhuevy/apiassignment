# Step 3

import urllib2, re, json, csv

def clean_json(json):
    return re.sub(r'new Date\(.*?\)', '""', json)

# Step 1 & 2 Hillary Clinton's emails containing Benghazi
dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446510657718&searchText=Benghazi&beginDate=false&endDate=false&collectionMatch=false&postedBeginDate=false&postedEndDate=false&caseNumber=F-2014-20439&page=1&start=1&limit=20000#').read()

valid_json = clean_json(dirty_json)
data = json.loads(valid_json)

output = open('api.csv', 'w')
writer = csv.writer(output)

for row in data['Results']:
    writer.writerow([row['pdfLink']])


