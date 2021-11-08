
import json
import json, requests
import asyncio

environment = {
  "hostLocal": 'localhost',
  "hostProd": 'localhost',
  "hostStaging": 'localhost',
  "port": 3331,
  "path": '/api/v1/daml/validateAuthentication',
};

print(environment["hostLocal"])
print(environment["port"])




class Validator:

    def __init__(self, key, envType):

        self.key
        self.envType = envType
    
    @staticmethod
    def clientId(self,key):
        self.key = key
        
    @staticmethod
    def environment(self,env):
#         self.envType = self.env == env ? env : this.envType;
        self.envType = env if env else self.envType
    @staticmethod
    def execOPA(self,user,action,target):
        atob = 'atob'
        bodyToExec = {
            "user":user,
            "action":action,
            "target":{
                "id":target
            },
        }
    key = JSON.loads(atob.self.key)
    host = self.envType
    if(self.envType == 'staging'):
        environment["hostStaging"],
        environment["hostLocal"]
    else:
        self.envType == 'local',
        environment['hostProd']
        print("self.envType:",host)
        
        
    https = 'http'
#     return async def run
    async def run():
        stringDecoder.decode(obj, encoding='utf-8', errors='strict')
        jsonObject = JSON.stringify(bodyToExec)
        postheaders = {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(jsonObject, 'utf8'),
            Authentication: 'Bearer ' + key,
          };

    optionspost = {
        "host": host,
        "port": environment.port,
        "path": environment.path,
        "method": 'POST',
        "headers": postheaders,
      }
    def reqPost():
        
        reqPost = https.requests(optionspost)
    def res():
        decoder = StringDecoder('utf-8')
        buffer = ''
        res.on('data')

    def d():
        
        
        buffer += decoder.write(d)
        return buffer
    reqPost.write(jsonObject);
    reqPost.end();
    reqPost.on('error');


if __name__ == '__main__':
    Validator()
#     -------------------------------------------------
import json
import json, requests
import asyncio

environment = {
  "hostLocal": 'localhost',
  "hostProd": 'localhost',
  "hostStaging": 'localhost',
  "port": 3331,
  "path": '/api/v1/daml/validateAuthentication',
};

print(environment["hostLocal"])
print(environment["port"])




class Validator:
  key = None
  envType = 'production'

  def __init__(self):

    @staticmethod
    def clientId(key):
      key = key

    @staticmethod
    def environment(env):
      envType = env if env else envType
    
    @staticmethod
    async def rbac(user,action,target):
      result = await execOPA(user,action,target)
      return result

    @staticmethod
    def execOPA(user,action,target):
      atob = 'atob'
      bodyToExec = {        
          user: user,
          action: action,
          target: {             
              id: target,
              },
              };
      key = json.loads(atob(key))
      if(host):
        envType == 'staging' and  envType["envType"] == 'local'
      else:
        environment["hostStaging"] and environment["hostProd"] 
      print('envType:',host)

      https = 'http'
    # def res(d):
    #   Str = Str.encode('base64','strict');
    #   buffer = ''
    #   d = resolve(buffer =+ Str.write(d))
    #   return buffer
      

      try:

        
        postheaders = {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(jsonObject, 'utf8'),
            Authentication: 'Bearer ' + key
        }
        optionsPost = {   
            "host": host,
            "port": environment["port"],
            "path": environment["path"],
            "method": 'POST',
            "headers": postheaders
            }


        jsonObject = json.dumps(bodyToExec)
        # decoder = StringDecoder('utf-8')
        async def res(d,optionPost):

            decoder = StringDecoder('utf-8')
            buffer += decoder.write(d)
            reqPost = await https.requests(optionsPost)
        reqPost.write(jsonObject)
        reqPost.end()
        reqPost.on('error')
      except:
        print("aman")


      # async def StringDecoderToEncode():

      #   optionsPost = {       
      #         "host": host,
      #         "port": environment["port"],
      #         "path": environment["path"],
      #         "method": 'POST',
      #         "headers": postheaders 
      #         }
      #   try:

      #     jsonObject = json.dumps(bodyToExec)

      #   except:
      #     print("aman")

if __name__ == '__main__':
    Validator()
