import requests
import json

def repoToString(name, commits):
    return 'Repo: ' + name + ' Number of commits: ' + str(commits)

def queryGithub(id):
    response = requests.get('https://api.github.com/users/'+id+'/repos')

    output = []

    if response.status_code != 200:
        print('There is no github account with the id: ' + id)
        return []
    
    jsonRes = response.json()

    if len(jsonRes) == 0: 
        print('No repositories found for the user with id: ' + id)
        return []

    for repo in jsonRes:
        name = repo['name']
        commits = len(requests.get('https://api.github.com/repos/'+id+'/'+name+'/commits').json())
        temp = repoToString(name, commits)
        print(temp)
        output.append(temp)

    return output

if __name__ == '__main__':
    userId = input('Enter Github user ID: ')
    queryGithub(userId)