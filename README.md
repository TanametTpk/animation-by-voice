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
- โหลด python 3 https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
- ลง python ตามนี้ https://phoenixnap.com/kb/how-to-install-python-3-windows
- ลง ffmpeg ตามนี้ http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/
- คลิก install.bat
- เอาไฟล์ เสียงแปลงเป็น .mp4 ก่อน
- เอาไฟล์ .mp4 ที่ต้องการทำ animation มาไว้ใน folder นี้(ที่เดียวกับ jumpcutter.py)
- ลาก ไฟล์เสียง(.mp4) มาใส่ ไฟล์ create-animation-60fps.bat หรือ create-animation-30fps.bat ตาม fps ของไฟล์ .mp4 (ลากเสียงมาทับได้เลย)
- จะได้ output ชื่อว่า char_talk.mp4