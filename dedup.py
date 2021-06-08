from collections import OrderedDict

def do():
  clean_data = OrderedDict()
  with open("logs.json", "r") as f:
    [clean_data.setdefault(line.strip()) for line in f if line.strip() != ""]
  
  with open("logs.json", "w") as f:
    for one in clean_data:
       if one not in f.read():
          print(one, file=f)one

if __name__ == '__main__':
  do()
