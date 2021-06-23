class open_file():
    def __init__(self,filename, mode):#will take the parameters to open file
        self.filename=filename
        self.mode = mode
        self.file = open(self.filename,self.mode)
        print("your file has been opened!")
        #file opened
        
          
    def __enter__(self):#will give access to user to work)
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        print("File is closed?")
        print(self.file.closed)
        #file closed
  
  
with open_file("class.txt", "w") as f:
    print("starting to write in file")
    f.write("Good to go to create ur custom context manager!")


