# UCDGenCatScraper
A little python script to scrape data from the UC Davis General Catalog

HOW TO USE:

First download the UCD general catalog: https://ucdavis.pubs.curricunet.com/Catalog
When it's done, open it. Scroll down to "Courses by Subject Code." Start selecting and don't stop selecting until you get to the very last course, which would likely be the last WMS course.
Ctrl-C then Ctrl-V in a blank .txt file. Save, then rename this file to gencat.txt. 
	*NOTE I used Foxit PDF viewer to do this. I'm not too sure, but your results may differ depending on what PDF viewer you use. Regardless, you can just use the provided gencat.txt

With that taken care of, all you need to do is run gencatreader.py. You can do this by just double clicking on it, provided you have python installed.

This will generate two files. You can ignore temp.txt. Output.txt is the actual output and will contain a csv with all UC Davis courses. 
To open this, you can just right click and open with your favorite spreadsheet editor. 
Alternatively, you can also rename the file to output.csv (make sure file extensions are enabled so you can actually change this and not just rename the file to output.csv.txt) then upload to Google Drive to edit with Google Sheets.