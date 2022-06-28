
import requests


url = "https://sample-project-anirudh.atlassian.net/rest/api/3/search"

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

query = {
   'jql': 'project = PS'
}

response_=requests.get(url, headers=headers, params=query, auth=('anirudhpunaruru1999@gmail.com', 'X79BUmVfIjaynmP0Vu7672CB'))
data= response_.json()
issues= data['issues']
for issue in issues:
    print(issue['key'])

