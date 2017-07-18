name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('2008'): continue 
    words = line.split() 
    #time = words[1]
    print words

 #   piece = time.split(':')
  #  print piece[0]


    
