import requests, json, csv, time

def check_active_matches(matchId):
  input = requests.get('https://api.cuescore.com/tournament/?id=' + matchId)

  if input.text.find("error") != -1:
    print('Could not find tournament with given ID')
    return -1
  
  matches = json.loads(input.text)['matches']
  matchData = []

  for match in matches:
    if match['matchstatus'] == 'playing':
      playerA = match['playerA']['name']
      playerB = match['playerB']['name']
      scoreA = match['scoreA']
      scoreB = match['scoreB']
      if len(match['table']) != 0:
        table = match['table']['name']
      else:
        table = 'null'

      matchData.append([playerA, playerB, scoreA, scoreB, table])


  with open('matches.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(matchData)

  print('Data saved to file matches.csv')
  time.sleep(60)

matchId = input('Give match ID: ')

while True:
  if check_active_matches(matchId) == -1:
    break
