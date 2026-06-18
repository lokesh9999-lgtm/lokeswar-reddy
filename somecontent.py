file_path="output.text"
with open(file_path,"w")as file:
    file.write("hello world!\n")
    file.write("this is a sample text")
    print("content written to",file_path)
