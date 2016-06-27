import csv

csvfile = open('processed_data.csv','r')

csvreader = csv.reader(csvfile)

for row in csvreader:
      print("activities_list.push({{\nactivity_type: '{0}',\ndesc:'{1}',\ndate_str: '{2}',\nstart_time: '{3}',\nend_time: '{4}'\n}});\n".format(row[0],row[1],row[2],row[3],row[4]))
