import requests
from config import headers
import os
from write_results import write_json
# import dropbox

# def dropbox_upload(filepath, company, dbx):
#     """
#     Args:
#         filepath (string): pdf path to save
#         company (string)
#         dbx (Dropbox)
#     """
#     with open(filepath, "rb") as f:
#         dbx.files_upload(f.read(), "/2023-05-19 (msci)/"+company+"/"+filepath, mode=dropbox.files.WriteMode("overwrite"))

def download_pdf(link, yearString, companyName, sort):
    """_summary_

    Args:
        link (string): link of pdf
        yearString (string)
        companyName (string)
        sort ("string"): indicates if the pdf is doubtful or not

    Returns:
        _type_: _description_
    """

    path = f"D:/SFDH/Sustainability Reports Web Scraping/"

    try:
        response = requests.get(link, headers=headers, timeout=30)
        status_code = response.status_code
        print(status_code)
    except:
        status_code = None

    if status_code == 200:
        if sort == "doubt":

            if not os.path.exists(path + "doubtPDFs/"+companyName):
                os.makedirs(path + "doubtPDFs/"+companyName)

            pdf = open(os.path.join(path + "doubtPDFs/"+companyName, yearString+"_report.pdf"), 'wb')
            pdf.write(response.content)
            pdf.close()
        
            filepath = path + "doubtPDFs/" + companyName + "/" + yearString + "_report.pdf"
            return filepath
        
        elif sort == "found":

            if not os.path.exists(path + "foundPDFs/"+companyName):
                os.makedirs(path + "foundPDFs/"+companyName)

            pdf = open(os.path.join(path + "foundPDFs/"+companyName, yearString+"_report.pdf"), 'wb')
            pdf.write(response.content)
            pdf.close()
        
            filepath = path + "foundPDFs/" + companyName + "/" + yearString + "_report.pdf"
            return filepath

        # pdf = open(yearString + "_report.pdf", 'wb')
        # pdf.write(response.content)
        # pdf.close()
    
        # filepath = yearString + "_report.pdf"

        # dropbox_upload(filepath, companyName, dbx)
        # return filepath
    else:
        print("GET REQUEST FAILED")
        write_json({'company': companyName, 'link': link}, 'exception_at_download.json', yearString)
        return None