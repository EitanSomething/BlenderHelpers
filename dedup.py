from collections import OrderedDict

def do():
  f = open("logs.json", "a")
  f.truncate()
  f.close()
  clean_data = OrderedDict()
  with open("logs.json", "r") as f:
    [clean_data.setdefault(line.strip()) for line in f if line.strip() != ""]
  
  with open("logs.json", "w") as f:
    [print(one, file=f) for one in clean_data]

if __name__ == '__main__':
  do()
