import requests
import json

def queryGithub(id):
    print(id)

if __name__ == '__main__':
    userId = input('Enter Github user ID: ')
    queryGithub(userId)