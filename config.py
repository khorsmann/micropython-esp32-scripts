import json
class App:
  __conf = { json.loads('config.json') }
  __setters = ['essid', 'password']

  @staticmethod
  def config(name):
    return App.__conf[name]

  @staticmethod
  def set(name, value):
    if name in App.__setters:
      App.__conf[name] = value
    else:
      raise NameError("Name not accepted in set() method")
