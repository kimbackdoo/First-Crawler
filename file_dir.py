import os
import urllib.request as req

class FileDir:
    def __init__(self):
        self.product_name_list = os.listdir("C:/Users/metasoft/Desktop/test") # 이미지가 없는 상품의 폴더 이름들을 리스트로 추출

    def mkdir(self, supplier_name, product_name):
        print("===================================")
        path = "D:/info_no_img/"
        self.path = (path + supplier_name + "_" + product_name + "/")
        if not(os.path.isdir(self.path)):
            os.mkdir(self.path)
            print("폴더 생성")
            return True
        else:
            print("폴더 존재")
            return False
        print("===================================")

    def mktxt(self, product_name, text):
        file_path = self.path + product_name + ".txt"
        file = open(file_path, "w")
        file.write(text)
        file.close()

    def img_download(self, img, img_name):
        img_path = self.path + str(img_name) + ".jpg"
        req.urlretrieve(img, img_path) # 저장할 이미지와 경로 설정