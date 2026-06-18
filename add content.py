file_path="output.text"
with open(file_path,"a")as file:
    file.write("\n this is an additional line")
    print("content appended to:",file_path)
