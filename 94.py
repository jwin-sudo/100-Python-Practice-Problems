'''
Exercise 94 - URL Cleaner

Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com
Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

Expected output: 

http://www.google.com
http://www.yahoo.com
http://www.stackoverflow.com
http://www.pythonhow.com
'''

with open("urls.txt", "r") as file:
    urls = file.readlines()
    
cleaned_urls = [url.replace("https:/", "http://") for url in urls]

with open("cleaned_urls.txt", "w") as file:
    for url in cleaned_urls:
        file.write(url)