import requests
import json


def get_data(msg_text, num):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        "X-RapidAPI-Key": "b0e8adfb2fmshb9c958d198bb1d4p13a9f0jsn28997e5d2f03",
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.text
    data = json.loads(data)
    for i in range(len(data["response"])):
        x = data["response"][i]["country"]
        if (x.lower() == msg_text.lower()):
            total = data["response"][i]["cases"]["total"]
            active_cases = data["response"][i]["cases"]["active"]
            recovered = data["response"][i]["cases"]["recovered"]
            critical_cases = data["response"][i]["cases"]["critical"]
            new_cases = data["response"][i]["cases"]["new"]
            total_deaths = data["response"][i]["deaths"]["total"]
            new_deaths = data["response"][i]["deaths"]["new"]
            data_complete = "Data of " + x + "\n" + """total_infected: """ + str(total) + """
active_case: """ + str(active_cases) + """
recovered: """ + str(recovered) + """
critical_cases: """ + str(critical_cases) + """    
new_cases: """ + str(new_cases) + """
total_death: """ + str(total_deaths) + """
new_deaths: """ + str(new_deaths)

            return (data_complete)


