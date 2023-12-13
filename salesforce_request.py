import requests
import xml.etree.ElementTree as ET

#SOAP request URL
DOMAIN = "https://solera-amer.my.salesforce.com/services/Soap/u/45.0"
 
#Structured XML
payload = """<?xml version="1.0" encoding="utf-8" ?>
<env:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
  <env:Body>
    <n1:login xmlns:n1="urn:partner.soap.sforce.com">
      <n1:username>automate@solera.com.amer</n1:username>
      <n1:password>AutodsIntegr@tion2023!jrvKbZSekuYjY9zrI5CwErjI</n1:password>
    </n1:login>
  </env:Body>
</env:Envelope>"""

#header
headers = {
    'Content-Type': 'text/xml',
    'SOAPAction': 'login'
    }

#POST request
response = requests.post(DOMAIN, headers=headers, data=payload)

root = ET.fromstring(response.text)

namespace = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/', 'sf': 'urn:partner.soap.sforce.com'}
userId_element = root.find(".//sf:userId", namespace)

userId_value = userId_element.text if userId_element is not None else None

print(userId_value)

print(userId_element)