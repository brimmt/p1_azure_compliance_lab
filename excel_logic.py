from openpyxl import Workbook;
from baseline_logic import update_results_list
from pathlib import Path




def export_compliance_results(results):

    wb = Workbook();


    ws = wb.active;

    ws.title = "Compliance Results"

    #Create the headers
    headers = ["Rule", "Resource", "Status", "Remediation"]
    ws.append(headers);

    

    for result in results:
        ws.append(
            [result["rule"], 
            result["resource"], 
            result["status"], 
            result["Remediation"]
            ])

    # this is to add versioning
    count = 1;

    while Path(f"compliance_results_{count}.xlsx").exists():
        count += 1

    filename = f"compliance_results_{count}.xlsx"

    wb.save(filename)
    return filename;


# this is the main entry point for the script <- similiar to Java main
if __name__ == "__main__":
    results = update_results_list()
    filename = export_compliance_results(results)
    print(f"Report saved: {filename}")