
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
   key= issue['key']
   issue_url= 'https://sample-project-anirudh.atlassian.net/rest/api/3/issue'+key
   res= requests.get(issue_url, headers=headers, auth=('anirudhpunaruru1999@gmail.com', 'X79BUmVfIjaynmP0Vu7672CB'))
   data= res.json()
   print(data['fields']['status']['name'])



