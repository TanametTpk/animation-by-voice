# How to use

อันแรก jumpcutter script ไว้ทำ jumpcutter ด้วย และ ก็สร้าง animation ด้วย
```
python jumpcutter.py --input_file <input_path> --sounded_speed <new speed for sounded frame> --silent_speed <new speed for silent frame> --frame_margin <gap of silent frame and loud frame> --frame_rate <your_vdo_frame_rate> --animate_loop <boolean>
```

อันที่สอง extract เวลาจะสร้าง frame เพื่อทำ action สำหรับ animation
```
python extract.py --input_file <input_path> --frame_rate <your_vdo_frame_rate>
```

## Details

- script การทำงานส่วนของ jumpcutter มาจาก https://github.com/carykh/jumpcutter แต่เขียนเพิ่มเพื่อสร้าง animation
- params sounded_speed, silent_speed ใส่เป็นเลขเท่าตัวเช่น ความเร็วเท่าเดิมใส่ 1 ความเร็ว 2 เท่าใส่ 2 แต่ถ้าใส่ 999999 คือ skip
- params animate_loop ที่เพิ่มมาคือ เวลา animation หมด frame แล้วจะให้ loop ไหมถ้าไม่ก็จะอยู่ frame สุดท้าย
- เวลา extract ควรจะเรียง action ตามตัวเลข หรือ อะไรก็ตามที่ทำให้ file เรียง frame ได้ถูก ไม่งั้น animation อาจผิดได้

## For non programmer / คนที่ไม่ใช้โปรแกรมเมอร์ หรือ อ่านโค้ดไม่ออก
- นี้คือภาษา python ปกติแล้วในคอมของคุณไม่มีต้องลงก่อน
- เวลาลง python ให้ดีที่สุดคือลง anaconda
- นอกจากนี้คุณต้องมี ffmpeg ไปโหลดมาด้วยมันฟรี
- จากนั้นใน เครื่องคุณจะต้องมี anaconda prompt แล้วกดใช้
- ย้ายไปที่ folder ที่เก็บไฟล์นี้
- ถ้าไม่รู้ให้ copy path folder มาใส่แล้วเขียนว่า "cd <path folder ของคุณ>"
- แต่ถ้าอยู่คนละ drive ให้ใส่ drive ก่อน เช่น อยู่drive f ให้ใส่ว่า "f:" แล้วทำตามข้อที่แล้ว
- เมื่ออยู่ใน folder ที่ถูกแล้วลง modules โดยพิมพ์ "pip install -f ./requirements.txt"
- จากนั้นก็ใช้คำสั่งตามด้านบน
