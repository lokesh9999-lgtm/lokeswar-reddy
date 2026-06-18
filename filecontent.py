file_path="example.text"
with open(file_path,"w")as file:
    file.write("helllo world!")
with open(file_path,"r")as file:
    content=file.read()
    print("file content:",content)
