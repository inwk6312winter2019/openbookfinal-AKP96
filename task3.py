def post_ticket(json):
  headers = {'x-API-Key': 'mykey'}
  response = requests.post("http://mydomani.com/api/tickets.json", data=create_json_ticket(json), headers=headers)
  for r in response:
    print(r)
