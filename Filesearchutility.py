import os

def list_text_files(directory_path):
	for dirs,subdirs,files in os.walk(directory_path):
		for file in files:
			if file.endswith('.txt'):
				print(os.path.join(dirs,file))

def list_pdf_files(directory_path):
	for dirs,subdirs,files in os.walk(directory_path):
		for file in files:
			if file.endswith('.pdf'):
				print(os.path.join(dirs,file))

def list_docx_files(directory_path):
	for dirs,subdirs,files in os.walk(directory_path):
		for file in files:
			if file.endswith('.docx'):
				print(os.path.join(dirs,file))

def list_three_types_of_files(directory_path):
	valid_extensions=('.pdf','.txt','.docx')
	for dirs,subdirs,files in os.walk(directory_path):
		for file in files:
			if file.endswith(valid_extensions):
				print(os.path.join(dirs,file))

#Main function
directory_to_search=str(input("Enter the path to the directory you want to get the files of(Hint:Use pwd to get the absolute file path)")) #A placeholder directory path used for now.
print("Enter either 1,2 or 3")
print("Enter 1 if you want to list all the text files in a given directory")
print("Enter 2 if you want to list all the pdf files in a given directory")
print("Enter 3 if you want to list all the document files in a given directory")
choice=int(input("Enter either 1,2 or 3"))
if(choice==1):
	#The list_text_files function will run
	list_text_files(directory_to_search)
elif(choice==2):
	#The list_pdf_files function will run
	list_pdf_files(directory_to_search)
elif(choice==3):
	#The list_docx_files function will run
	list_docx_files(directory_to_search)
else:
	print("Error. No command will run. Pleas type 1,2 or 3")#Program is finished
