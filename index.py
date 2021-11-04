import json
import json, requests
import asyncio

enviornment = {
  "hostLocal": 'localhost',
  "hostProd": 'localhost',
  "hostStaging": 'localhost',
  "port": 3331,
  "path": '/api/v1/daml/validateAuthentication',
};

class Validator:

    def __init__(self, key, envType):
        self.key
        self.envType = envType

    @staticmethod
    def clientId(self,key):
        self.key = "s"
        print(self.envType)

print(Validator.clientId())