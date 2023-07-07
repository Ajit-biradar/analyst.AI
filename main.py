#part1
from bs4 import BeautifulSoup
import requests
import pandas as pd
URL="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
#headers for request
HEADERS=({"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',"Accept-Language":'en-IND, en;q=0.5',})

webpage=requests.get(URL,headers=HEADERS)


#soup object containing all data
soup=BeautifulSoup(webpage.content,'html.parser')





links=soup.find_all("a",aatrs={ 'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})


                               #here we not getting proper output of 'soup'
'''
    <html>
<head>
<title>503 - Service Unavailable Error</title>
</head>
<body bgcolor="#FFFFFF" text="#000000">
<!--
        To discuss automated access to Amazon data please contact api-services-support@amazon.com.
        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.in/ref=rm_5_sv, or our Product Advertising API at https://affiliate-program.amazon.in/gp/advertising/api/detail/main.html/ref=rm_5_ac for advertising use cases.
-->
<center>
<a href="https://www.amazon.in/ref=cs_503_logo/">
<img alt="Amazon.in" border="0" height="45" src="https://images-eu.ssl-images-amazon.com/images/G/31/x-locale/communities/people/logo.gif" width="200"/></a>
<p align="center">
<font face="Verdana,Arial,Helvetica">
<font color="#CC6600" size="+2"><b>Oops!</b></font><br/>
<b>It's rush hour and traffic is piling up on that page. Please try again in a short while.<br/>If you were trying to place an order, it will not have been processed at this time.</b><p>
<img alt="*" border="0" height="9" src="https://images-eu.ssl-images-amazon.com/images/G/02/x-locale/common/orange-arrow.gif" width="10"/>
<b><a href="https://www.amazon.in/ref=cs_503_link/">Go to the Amazon.in home page to continue shopping</a></b>
</p></font>
</p></center>
</body>
</html>

'''
print(links)#it gives us the -------- "Service Unavailable Error"