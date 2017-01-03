def text_create(name, msg):
     desktop_path = '/Users/Ace/Desktop/'
     full_path = desktop_path + name + '.txt'
     file = open(full_path,'w')
     file.write(msg + '\n')
     for i in range(1,10):
          i = str(i)
          file.write("First line " + i + '\n')
     file.close()
     f = open(full_path,"r") # Opens file for reading
     for line in f:
          print (line)
     f.close()     
     print('Done')
text_create('hello','hello world')
