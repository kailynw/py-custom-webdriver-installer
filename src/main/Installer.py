import os
import zipfile
import urllib.request as request

class Installer:
    def __init__(self):
        self.BIN_FOLDER= "bin/"
        self.temp_zip_file_name=self.BIN_FOLDER+"temp_zip_file.zip"

    def get_driver(self, url):
        self.clear_bin()
        zip_file_path= self.retrieve_zip_file(url)
        self.extract_and_delete_zip(zip_file_path)
        driver_path= self.get_driver_path()
        return driver_path
        
    def retrieve_zip_file(self, url):
        try:
            zip_file_path, _= request.urlretrieve(url, self.temp_zip_file_name)
        except Exception as ex:
            print("Failed to retrieve driver zip file")
            raise ex
        return zip_file_path
    
    def extract_and_delete_zip(self, zip_file_path):
        zip_file_reader= zipfile.ZipFile(zip_file_path, 'r')
        zip_file_reader.extractall(self.BIN_FOLDER)
        zip_file_reader.close()
        os.remove(self.temp_zip_file_name)

    def get_driver_path(self):
         for file in os.listdir(self.BIN_FOLDER):
            return self.BIN_FOLDER+file
    
    def clear_bin(self):
        for file in os.listdir(self.BIN_FOLDER):
            os.remove(self.BIN_FOLDER+file)

# if __name__=="__main__":
#     url= 'https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-29/stable-headless-chromium-amazonlinux-2017-03.zip'
#     driver_path=Installer().get_driver(url)
#     print(driver_path)