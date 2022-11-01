import csv
import sys
import os

# Converts a google contacts csv file to a collection of markdown files


if (len(sys.argv)!=3):
    print("\ncontacts2obsidian.py - by Jonathan Beckett\n\npython contacts2obsidian.py <source_file> <output_directory>\n\nExample : python google_contacts_to_obsidian.py contacts.csv c:\\my\\vault\\contacts\n\n")
    sys.exit(0)

source_file = sys.argv[1]
output_path = sys.argv[2]

with open(source_file,newline="") as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=",",quotechar="\"")
    for row in csvreader:

        name = row["Name"]

        print("Processing " + name)

        emails = []
        if (row["E-mail 1 - Value"]):
            emails.append(row["E-mail 1 - Value"].replace(" ::: ",","))
        if (row["E-mail 2 - Value"]):
            emails.append(row["E-mail 2 - Value"].replace(" ::: ",","))
        if (row["E-mail 3 - Value"]):
            emails.append(row["E-mail 3 - Value"].replace(" ::: ",","))

        phones = []
        if (row["Phone 1 - Value"]):
            phones.append(row["Phone 1 - Value"].replace(" ::: ",","))
        if (row["Phone 2 - Value"]):
            phones.append(row["Phone 2 - Value"].replace(" ::: ",","))
        if (row["Phone 3 - Value"]):
            phones.append(row["Phone 3 - Value"].replace(" ::: ",","))
        if (row["Phone 4 - Value"]):
            phones.append(row["Phone 4 - Value"].replace(" ::: ",","))
        
        output_text = "---\nname: " + name + "\nemail: [" + ",".join(emails) + "]\nphone: [" + ",".join(phones) + "]\n---\n"
        
        if (row["Photo"]):
            output_text += "\n![" + row["Name"] + "](" + row["Photo"] + ")\n"

        output_text += "\n### Name\n" + name + "\n"
        
        if (len(emails) > 0):
            output_text += "\n### Email\n" + "\n".join(emails) + "\n"

        if (len(phones) > 0):
            output_text += "\n### Phone\n" + "\n".join(phones) + "\n"

        if (row["Address 1 - Formatted"]):
            output_text += "\n### Address\n" + row["Address 1 - Formatted"] + "\n"

        
        
        output_file_path = os.path.join(output_path,name + ".md")
        output_file = open(output_file_path, 'wb')
        output_file.write(bytes(output_text,'utf-8'))
        output_file.close()
