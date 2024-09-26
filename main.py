import os
import shutil

class Sorter:
    def __init__(self):
        #Here We Have List For The File types, Folder Names (You Can Add More..!)
        self.folders_name = ["music","photos","document"]
        self.photo_file_types = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'heic', 'raw', 'svg']
        self.music_file_types = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'alac', 'aiff', 'pcm']
        self.doc_file_types = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'odt', 'ods', 'rtf', 'html', 'md']
        self.path = "./"
        self.files_number = 0

    def create_folders(self):
        #Here we loop in folders name and create each folder
        try:
            for name in self.folders_name:
                os.makedirs(name)
        except FileExistsError as error:
            print(f"Create Folder {name} Error : {error}")

    def move_file(self,type,file_path,file_name):
        #Here we use shutil to move the file
        try:
            if type in self.photo_file_types:
                shutil.move(file_path,"./photos")
            if type in self.music_file_types:
                shutil.move(file_path,"./music")
            if type in self.doc_file_types:
                shutil.move(file_path,"./document")
        except Exception as e:
            print(f"Error In Moving {file_name} : {e}")

    def start(self):
        self.create_folders()
        for file_name in os.listdir(self.path):
            file_path = os.path.join(self.path,file_name)
            if os.path.isfile(file_path):
                type = file_name.split(".")[1]
                self.move_file(type,file_path,file_name)
                self.files_number +1
        print(f"Sorted {self.files_number} Files !")

input("Press Enter To Sort The Files !")
Sorter().start()