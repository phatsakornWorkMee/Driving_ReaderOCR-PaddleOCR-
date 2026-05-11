ENG:

Driving_ReaderOCR is an automated data extraction tool designed to read information from driver's license images using high-performance PaddleOCR technology. 
The system processes images to extract essential fields and converts them into JSON format, ensuring seamless integration with databases or other third-party applications.

Key Features
The program supports two primary input workflows:
1.Local File Processing: Read images directly from your local directory.
2.API Integration: Send images via API endpoints for real-time processing.

Workflow Process
1.Input Submission: The user sends an image to the OCR engine (via local file or API).
2.OCR Processing: PaddleOCR analyzes the driver's license and extracts text data.
3.Data Filtering: The system filters and maps the raw text into a predefined JSON structure.
4.Data Storage: The processed data is saved locally as a .json file for future use.

Integration & Use Cases
Currently, the project supports a Local API, allowing for immediate integration with various platforms such as:
Frontend Web Applications: For automated form filling , Mobile Apps: For on-the-go license scanning,Internal Management Systems: For employee registration and identity verification.

Note: This tool is ideal for developers seeking a lightweight, easy-to-install, and fast solution for document data extraction.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Driving_ReaderOCR เป็นโปรเจกต์ การนำภาพไปประมวณผลเพื่อดึงข้อมูลจากบัตรใบอนุญาตขับขี่ โดยใช้ PaddleOCR ในการอ่าน หลังจากประมวณผลเสร็จจะทำการดึงข้อมูลบางส่วนที่จำเป็นไปบันทึกเป็นข้อมูลเป็น Json
เพื่อนำข้อมูลไปใช้ต่อในส่วนต่างๆได้

Driving_ReaderOCR(PaddleOCR)
คือโปรแกรมสำรับอ่านข้อมูลอัตโนมัติจากภาพถ่ายบัตรใบอนุญาตขับขี่ โดยใช้เทคโนโลยี PaddleOCR ประสิทธิภาพสูง ระบบจะทำการประมวลผลภาพ (Image Processing) เพื่อดึงเฉพาะข้อมูลสำคัญที่จำเป็น และแปลงให้อยู่ในรูปแบบ JSON เพื่อความสะดวกในการนำไปเชื่อมต่อกับฐานข้อมูลหรือระบบอื่น ๆ

โดย process ในการทำงานของโปรแกรมจะทำงานได้ 2 แบบ คือ 

1. รับ input จากไฟล์ในเครื่อง 
2. รับ input จากการส่งรูปผ่านการยิง API


ขั้นตอนการทำงานของโปรแกรม

1.ส่งรูปเข้าไปใน  OCR (รูปแบบการส่งขึ้นอยู่กับ User เลือกใช้จาก 2 Process ด้านบน)
2.OCR ทำการ อ่านใบขับขี่
3.ระบบทำการ กรองข้อมูลบางส่วนที่ OCR อ่านได้  ออกมาตาม format json ที่กำหนดไว้
4.ระบบทำการบันทึกข้อมูลลงในเครื่อง โดยบันทึกข้อมูลออกมาในรูปแบบ Json

ปัจจุบันโปรเจกต์นี้รองรับการทำงานแบบ Local API ซึ่งคุณสามารถนำไปเชื่อมต่อ (Integrate) กับโปรแกรมอื่นๆ ได้ทันที กรณีเป็นแบบ local เช่น:

Frontend Web Application,Mobile App สำหรับสแกนบัตร, ระบบลงทะเบียนพนักงาน (Internal Management System)

Note: เหมาะสำหรับนักพัฒนาที่ต้องการ โปรแกรม สำหรับอ่านบัตรที่ติดตั้งง่ายและทำงานได้รวดเร็ว


