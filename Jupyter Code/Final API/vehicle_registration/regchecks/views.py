from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
import json

def check_vehicle(request):
    vehicle_info = None
    error_message = None

    if request.method == 'POST':
        registration_number = request.POST.get('registration_number')
        state = request.POST.get('states')
        district = request.POST.get('district')

        # SOAP endpoint URL
        url = "http://www.regcheck.org.uk/api/reg.asmx"
        
        # SOAP headers
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://regcheck.org.uk/CheckPakistan",
        }
        
        # SOAP request body with user inputs
        soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <CheckPakistan xmlns="http://regcheck.org.uk">
              <RegistrationNumber>{registration_number}</RegistrationNumber>
              <state>{state}</state>
              <district>{district}</district>
              <username>kiet2</username>
            </CheckPakistan>
          </soap:Body>
        </soap:Envelope>"""

        # Sending the request
        response = requests.post(url, data=soap_body, headers=headers)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            check_pakistan_result = root.find('.//{http://regcheck.org.uk}CheckPakistanResult')

            if check_pakistan_result is not None:
                vehicle_json_str = check_pakistan_result.find('{http://regcheck.org.uk}vehicleJson').text
                vehicle_info = json.loads(vehicle_json_str)  # Convert to JSON
            else:
                error_message = "Vehicle information not found in the response."
        else:
            error_message = f"Please enter correct car information"

    return render(request, 'regchecks/check-vehicle.html', {'vehicle_info': vehicle_info, 'error_message': error_message})
