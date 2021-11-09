from enviornments import enviornment
import json

print(enviornment["hostLocal"])
print(enviornment["port"])

class Validator:

  key = None
  envType = 'production'

  def __init__(self):

    @staticmethod
    def clientId(key):
      key = key

    @staticmethod
    def environment(env):
      self.envType = env if env else self.envType
    
    @staticmethod
    async def rbac(user,action,target):
      result = await execOPA(user,action,target,'rbac')
      return result

    @staticmethod
    async def abac(user,action,target):
      result = await execOPA(user,action,target,'abac')
      return result


    @staticmethod
    async def execOPA(user,action,target,type,host):

      self.bodyToExec = { 
        type:type,
        user: user,
        action: action,
        target: {             
            id: target,
        },
      }

      if(host):
        self.envType == 'staging' and  self.envType["envType"] == 'local'
      else:
        environment["hostStaging"] and environment["hostProd"] 
      print('envType:',host)

      https = 'http'
      
      postheaders = {
          'Content-Type': 'application/json',
          'Content-Length': self.Buffer.byteLength(self.jsonObject, 'utf8'),
          'Authentication': 'Bearer ' + self.key
      }
      self.optionsPost = {   
          "host": host,
          "port": environment["port"],
          "path": environment["path"],
          "method": 'POST',
          "headers": postheaders
          }
      try:

        StringDecoder = self.StringDecoder.decode('utf-8')
        async def res(self,chunk,optionPost):
          req = https.requests.get(optionPost)
          decoder = StringDecoder
          if self.buffer == '':
            self.buffer += decoder.write(chunk)
            # self.reqPost = await https.requests.get(optionsPost)
            return self.buffer
          else:
            print("buffer is not string")

          if self.buffer != 'Unauthenticated' and self.buffer != 'No Policy Found!':
            json.load(self.buffer)
          else:
            # self.buffer
            return self.buffer


          req.write(self.jsonObject)
          req.end()
          # req.on('error')
      except:
        print('error')

# val = Validator()
# print(val.clientId(123))

if __name__ == '__main__':
    Validator()
