from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import xlwt

def excel_output(filename, sheet, entries):
    
    # Standard xlwt initialization 
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)

    # Write column headings 
    sh.write(0, 0, entries[0][0])
    sh.write(0, 1, entries[0][1])

    # Write all data to sheet 
    for i in range(1, len(entries), 1):
    	sh.write(i, 0, entries[i][0])
    	sh.write(i, 1, entries[i][1])

    # Save excel file 
    book.save(filename)

def main():
	html = urlopen('https://www.payscale.com/index/US/Skill')
	bsyc = BeautifulSoup(html.read(), "lxml")

	table = bsyc.findAll('table')

	# Initialize list of lists 
	entries = []

	# For all rows in the table, collect the data 
	for rows in table[0].children:

		try:
			# Initialize the [job skill, # entries] pair
			pair = []

			# For each td in row, collect the job title and entry
			for data in rows.children:				
				try:
					# If length is 3, it is an <a href= ...> data </a> tag with \n on each side.  We want the data, not the tag 
					if( len(data) == 3 ):
						pair.append(data.contents[1].contents[0]) 

					# Else, it is the # of entries, but needs to be cleaned of spaces and \n 
					elif( len(data) == 1 ):
						data = data.contents[0]
						data_clean = data.replace(' ', '')
						data_clean = data_clean.replace('\n', '')
						pair.append(data_clean)
				except:
					pass

			# Add the pair to the final list 
			entries.append(pair)
		except:
			pass

	# for i in entries:
	# 	print(i)

	# Write the data to excel  
	excel_output("payscale.xls","clean_data",entries)

if __name__ == "__main__":
	main()