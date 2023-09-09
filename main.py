# Weezer Esoteric Programming Language
import sys
#read and split code. It runs any main.wzr in the current directory.
f = open("main.wzr","r")
code = f.read()
f.close()
code = code.split(";")
code.append("ALBUM END")
code.append("THANK YOU AND GOOD NIGHT")
Y = 2
#remove /n and spaces at the beggining of every line
i = 0
while(i < len(code)):
  while(code[i].startswith("\n") or code[i].startswith("  ") or code[i].startswith(" ")):
    code[i] = code[i][1:]
  
  i = i + 1
i = 0
#pre defined functions
def get_content(content):
  if(len(content.split(">>")) > 2):
    content = content.split("<<")
    one = "<<" + content[1]
    two = "<<" + content[2]
    start_index = one.find('<<')
    end_index = one.find('>>', start_index + 2)
    one = one[start_index + 2:end_index]
    start_index = two.find('<<')
    end_index = two.find('>>', start_index + 2)
    two = two[start_index + 2:end_index]
    ls = [one,two]
    return ls
  else:
    content = content.split("<<")
    one = "<<" + content[1]
    start_index = one.find('<<')
    end_index = one.find('>>', start_index + 2)
    one = one[start_index + 2:end_index]
    ls = [one]
    return ls
#interpret the code
isFinished = 0;
def run(line):
  global isFinished
  global code
  global i
  if(line.startswith("SAY IT AINT SO")):
    print(eval(get_content(line)[0]))
  if(line.startswith("GETCHOO")):
    vname = get_content(line)[0]
    exec("global " + vname,globals())
    exec(vname + " = input();",globals())
  if(line.startswith("MY NAME IS") or line.startswith("AND")):
    vname = get_content(line)[0]
    vcontent = get_content(line)[1]
    exec("global " + vname,globals())
    exec(vname + " = " + vcontent,globals())
  if(line.startswith("NUMBERS ARE OUT TO GET YOU")):
    vname = get_content(line)[0]
    exec("global " + vname,globals())
    exec(vname + " = int(" + vname + ")",globals())
  if(line.startswith("STRINGS ARE OUT TO GET YOU")):
    vname = get_content(line)[0]
    exec("global " + vname,globals())
    exec(vname + " = str(" + vname + ")",globals())
  if(line.startswith("SWITCH TO")):
    target = line.replace("SWITCH TO ","")
    target_i = 0
    j = 0
    while(j < len(code)):
      if(code[j].startswith("ALBUM " + target)):
        target_i = j
      j = j + 1
    i = target_i
  if(line.startswith("IF YOU WANT")):
    condition = get_content(line)[0]
    output = get_content(line)[1]
    if(eval(condition)):
      run("SWITCH TO " + output)
  if(line.startswith("THEY GO ROUND")):
    j = i
    while(not code[j].startswith("IV")):
      j = j - 1
    condition = get_content(code[j])[0]
    if(eval(condition)):
      i = j
    else:
      i = i
  if(line == "THANK YOU AND GOOD NIGHT"):
    isFinished = 1;
while(isFinished == 0):
  line = code[i]
  run(line)
  i = i + 1
