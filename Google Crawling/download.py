import requests
from vars_for_requests import headers
import os
from write_results import write_json

def download_pdf(link, yearString, companyName):

    try:
        response = requests.get(link, headers=headers, timeout=30)
        status_code = response.status_code
        print(status_code)
    except:
        status_code = None

    if status_code == 200:

        if not os.path.exists("resultPDFs/"+companyName):
            os.makedirs("resultPDFs/"+companyName)

        pdf = open(os.path.join("resultPDFs/"+companyName, yearString+"_report.pdf"), 'wb')
        pdf.write(response.content)
        pdf.close()
    
        filepath = "resultPDFs/" + companyName + "/" + yearString + "_report.pdf"
        return filepath
    else:
        print("GET REQUEST FAILED")
        write_json({'company': companyName, 'link': link}, 'exception_at_download.json', yearString)
        return None