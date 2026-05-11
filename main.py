from paddleocr import PaddleOCR
from pathlib import Path
import re  #regular expression
import os
import json
import requests
import numpy as np
from PIL import Image
import io

class Pathfile:
    def readfile(self):
        path_folder = r"input"
        self.path_allfile = []
        for file_name in os.listdir(path_folder):
            self.full_path = os.path.join(path_folder,file_name)
            self.path_allfile.append(self.full_path)

class OCR:  
    @staticmethod
    def input_api(self,img_file):
        paddle_ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        lang = 'th',
        )
        self.result = paddle_ocr.predict(
        input = "https://cdn.pixabay.com/photo/2013/07/12/19/03/id-154285_1280.png"
        #input = r"input\card1.JPG"
        )
    def input_api_img(self,img_file):
        paddle_ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        lang = 'th',
        )
        img_array = np.array(Image.open(io.BytesIO(img_file.read())))
        self.result = paddle_ocr.predict(
        input = img_array
        )

    def input_service(self): #8
        paddle_ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        lang = 'th',
        )
        pathfile = Pathfile()
        pathfile.readfile()
        self.result = paddle_ocr.predict(
        input = pathfile.path_allfile
        )

    def run_service(self,image_case,img_file): #เปลี่ยนเป็น switch case
        if image_case == "case1":
            #print(f"image_case: {image_case,img_file}")
            self.input_case = image_case,img_file
        elif image_case == "case3":
            #print(f"image_case: {image_case,img_file}")
            self.input_case = image_case,img_file
        else:
            image_case = "case2"
            #print(f"image_case_defult : {image_case}")
            self.input_case = image_case
        if self.input_case == "case2":
            return self.input_service()
        if self.input_case == "case1":
            return self.input_api(self,img_file)
        if self.input_case == "case3":
            return self.input_api_img(self,img_file)

class Jsonfile:
    @staticmethod
    def savefile(image_case,img_file=None):
        paddle_ocr = OCR()
        pathfile = Pathfile()
        pathfile.readfile()
        paddle_ocr.run_service(image_case,img_file)
        if image_case == "case3":
            paddle_ocr.input_api_img(img_file)
            paddle_ocr.input_case = "case3"
        result = paddle_ocr.result
        c1 = "case1"
        c2 = "case2"
        c3 = "case3"
        for i, file_path in enumerate(pathfile.path_allfile):
            if paddle_ocr.input_case == c2:
                call_result = result[i]['rec_texts']
                for find_name in call_result: #หาชื่อ
                   name_data = re.findall(r'[Mm][Rr]\.[a-zA-Z ]*|[Mm][Ii][Ss][Ss]\.[a-zA-Z ]*',find_name)
                   if name_data:
                       username = name_data[0].strip()
                       break
                for i in range(len(call_result)):
                    if "MR." in call_result[i]:
                        if i > 0:
                            lastname_data = call_result[i-1]
                if lastname_data:
                       lastname = lastname_data   
                for find_id in call_result:
                    id_data = re.findall(r'\d{13}|\d\s\d{4}\s\d{5}\s\d{2}\s\d*',find_id)
                    if id_data:
                        user_id = id_data[0].strip()
                        break
                for find_driver_id in call_result:
                    driver_id = re.findall(r'\d{8}',find_driver_id)
                    if driver_id:
                       driver_license_id = driver_id[0].strip()
                       break
                for find_vehicle_type in call_result:
                    vehicle_type = re.findall(r'.*Driving',find_vehicle_type)
                    if vehicle_type:
                       vehicle_type = vehicle_type[0].strip()
                       break
                formatdata_json = {
                "PaddleOCR_Output": [
                    {
                    "name" : username,
                    "lastname" : lastname,
                    "id" :user_id,
                    "driver_license_id" :driver_license_id,
                    "vehicle_type" : vehicle_type
                    }
                ]
                }
                output_folder = "output"
                file_name = Path(file_path).with_suffix('.json').name
                output_path = os.path.join(output_folder, file_name)
                with open(output_path,"w",encoding="utf-8") as f:
                    json.dump(formatdata_json,f,ensure_ascii=False, indent=4)
                for res in result:  
                    res.save_to_json("original_output")
            if paddle_ocr.input_case == c1 or paddle_ocr.input_case == c3:
                call_result = result[0]['rec_texts']
                for res_data in call_result:
                   name_data = re.findall(r'[Mm][Rr]\.[a-zA-Z ]*|[Mm][Ii][Ss][Ss]\.[a-zA-Z ]*',res_data)
                   id_data = re.findall(r'\d{13}|\d\s\d{4}\s\d{5}\s\d{2}\s\d*',res_data)
                   driver_id = re.findall(r'\d{8}',res_data)
                   car_type = re.findall(r'.*Driving',res_data)
                   for i in range(len(call_result)):
                       if "MR." in call_result[i]:
                           if i > 0:
                            lastname_data = call_result[i-1]
                   if name_data:
                       username = name_data[0].strip()
                   if lastname_data:
                       lastname = lastname_data   
                   if id_data:
                       user_id = id_data[0].strip()
                   if driver_id:
                       driver_license_id = driver_id[0].strip()
                   if car_type:
                       vehicle_type = car_type[0].strip()
                formatdata_json = {
                "PaddleOCR_Output": [
                    {
                    "name" : username,
                    "lastname" : lastname,
                    "id" :user_id,
                    "driver_license_id" :driver_license_id,
                    "vehicle_type" : vehicle_type
                    }
                ]
                }
                output_folder = "output"
                file_name = Path("ocr-output").with_suffix('.json').name
                output_path = os.path.join(output_folder, file_name)
                with open(output_path,"w",encoding="utf-8") as f:
                    json.dump(formatdata_json,f,ensure_ascii=False, indent=4)
                for res in result:  
                    res.save_to_json("original_output")

def check_status(paddleocr_url):
    try:
        response = requests.get(paddleocr_url, timeout=5)
        if response.status_code == 200:
            print("server : connected")
            return True
    except requests.exceptions.ConnectionError:
        print("server : offline")
        image_case = "case2"
        Jsonfile.savefile(image_case)
    except Exception as e:
        print(f"⚠️ Error occurred: {e}")
    return False

if __name__ == '__main__':
    check_status("http://127.0.0.1:5000/ServerStatus")

