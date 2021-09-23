import requests as req
import os

url = 'http://192.168.117.20:8000/api/snapshot/'
file_name = 'background.jpg'
file_path = os.path.join('.', 'background.jpg')
print(1)
data = {
    'size': os.path.getsize(file_path),
    'filename': file_name,
    'content_type': 'image/jpeg'
}
print(2)

res = req.post(url, data=data, files={
    'image_file': open(file_path, 'br') # File 객체 또는 BytesIO 객체
})
print(3)

if res.status_code == 200:
    # print(res.json())
    pass
else:
    print(res.text)
    print(res.status_code)
