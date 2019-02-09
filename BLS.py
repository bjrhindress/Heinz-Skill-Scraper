import requests
import json
# import prettytable


# headers = {'Content-type': 'application/json'}
# data = json.dumps({"seriesid": ['JTS00000000HIR','SUUR0000SA0'],"startyear":"2011", "endyear":"2014"})
# p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
# json_data = json.loads(p.text)
# output = open("test" + '.txt','w')

# for series in json_data['Results']['series']:
#     # x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
#     seriesId = series['seriesID']
#     for item in series['data']:
#         year = item['year']
#         period = item['period']
#         value = item['value']
#         # footnotes=""
#         # for footnote in item['footnotes']:
#         #     if footnote:
#         #         footnotes = footnotes + footnote['text'] + ',' 
#         #     if 'M01' <= period <= 'M12':
#         #         pass
#                 # x.add_row([seriesId,year,period,value,footnotes[0:-1]])
#     output.write (str([seriesId,year,period,value]))
# output.close()