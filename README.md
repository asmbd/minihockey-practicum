# Mini-Hockey
01204223 Practicum for Computer Engineering
Department of Computer Engineering Faculty of Engineering Kasetsart University

## Project Name 
Mini-Hockey (ฮอกกี้น้อยคอยรัก)

## Developers
- Ms.Chanya Pookkarat       6010502527 <br/>
  นางสาวชัญญา พุกกะรัตน์
- Ms.Asamabhorn Deewarat    6010502748 <br/>
  นางสาวอสมาภรณ์ ดีวรัตน์
- Ms.Sarita Puttitanun      6010504848 <br/>
  นางสาวสริตา พุฒิทานันท์
  
## Source Codes
- hockey_firmware (directory) 
  - python (directory)
    - practicum.py <br/>
        ใช้ติดต่อกับบอร์ดไมโครคอนโทรลเลอร์
    - test-peri-flask.py <br/>
        ใช้ติดต่อกับ Web Application เพื่อนำค่าไปแสดงผลบน html
    - test-peri.py <br/>
        ใช้ทดสอบการทำงานของบอร์ดและค่าที่ได้จากการติดต่อกับบอร์ด
  - usbdrv
  - hockey_firmware.ino <br/>
      เฟิร์มแวร์ฝั่งอุปกรณ์ ประกอบด้วยคำสั่ง Sensors และการส่งและรับข้อมูลผ่าน USB
  - usbconfig.h <br/>
      เก็บข้อมูลการตั้งค่าเกี่ยวกับอุปกรณ์ USB
- hockey.html <br/>
  ไฟล์ code HTML ในส่วนของการแสดงผลคะแนนและเวลาในการเล่น
- Minihockey-schematic.png <br/>
  Schematic ของ Mini-Hockey
- license.txt 

## Libraries
- PyUSB
- Flask
- CrossPack-AVR


## Hardwares
- Practicum Board ATMega328P
- Servo Motor S3003 (2)
- Infrared Barrier Tracking Avoidance Obstacle Sensor Module (3)
