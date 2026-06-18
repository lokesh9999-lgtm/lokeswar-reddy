try:
    file=open("myfile.txt","r")
except IDError:
    print("Error:unable to read the file!")
finally:
    file.close()
