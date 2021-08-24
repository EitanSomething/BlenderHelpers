from collections import OrderedDict

def do():
  clean_data = OrderedDict()
  with open("logs.md", "r") as f:
    [clean_data.setdefault(line.strip()) for line in f if line.strip() != ""]
  
  with open("logs.md", "w") as f:
    [print(one, file=f, end="\n\n") for one in clean_data]

if __name__ == '__main__':
  do()
