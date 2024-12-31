# from fastapi import FastAPI, HTTPException, UploadFile, File
# from fastapi.responses import FileResponse
# from PIL import Image
# import os
# import json

# # JSON fayl nomi
# DATA_FILE = "data.json"

# # FastAPI ilovasi
# app = FastAPI()

# # JSON faylini o'qish
# def read_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as file:
#             return json.load(file)
#     return {}

# # JSON fayliga yozish
# def write_data(data):
#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # Rasmni PDF formatga aylantirish funksiyasi
# def convert_image_to_pdf(image_path, pdf_path):
#     try:
#         img = Image.open(image_path)
#         img.convert('RGB').save(pdf_path, "PDF")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Rasmni PDFga aylantirishda xatolik: {str(e)}")

# # Foydalanuvchi qo'shish API
# @app.post("/add_user/")
# async def add_user(ism: str, familiya: str, user_id: str, file: UploadFile = File(...)):

#     # Papkalarni yaratish (rasim va rasim_pdf)
#     os.makedirs("rasim", exist_ok=True)
#     os.makedirs("rasim_pdf", exist_ok=True)

#     # Rasmni yuklash
#     file_extension = file.filename.split(".")[-1]
#     file_path = f"./rasim/{user_id}.{file_extension}"
    
#     try:
#         with open(file_path, "wb") as image_file:
#             image_file.write(await file.read())
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Rasm yuklashda xatolik: {str(e)}")

#     # PDF fayl nomini yaratish va rasmni PDF ga aylantirish
#     pdf_path = f"./rasim_pdf/{user_id}.pdf"
#     try:
#         convert_image_to_pdf(file_path, pdf_path)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Rasmni PDFga aylantirishda xatolik: {str(e)}")

#     # Yangi foydalanuvchi ma'lumotlarini JSON faylga yozish
#     data = read_data()
#     data[user_id] = {
#         "ism": ism,
#         "familiya": familiya,
#         "rasm": file_path,
#         "rasm_pdf": pdf_path
#     }
#     write_data(data)

#     return {"message": "Foydalanuvchi muvaffaqiyatli qo'shildi", "user_id": user_id}

# # Foydalanuvchini olish API (ID bo'yicha, ismi, familiyasi va rasmni qaytaradi)
# @app.get("/get_user/{user_id}")
# async def get_user(user_id: str):
#     data = read_data()
#     if user_id not in data:
#         raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")

#     # Ism, familiya va rasm yo'lini qaytarish
#     rasm_yoli = f"http://localhost:8083/download/rasm/{user_id}"
#     return {
#         "ism": data[user_id]['ism'],
#         "familiya": data[user_id]['familiya'],
#         "rasm_yo'li": rasm_yoli
#     }

# # Rasm faylini ko'rsatish uchun
# @app.get("/download/rasm/{user_id}")
# async def download_rasm(user_id: str):
#     data = read_data()
#     if user_id not in data:
#         raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")

#     rasm_path = data[user_id]['rasm']
#     if not os.path.exists(rasm_path):
#         raise HTTPException(status_code=404, detail="Rasm topilmadi")
    
#     return FileResponse(rasm_path, media_type='image/jpeg', filename=f"{user_id}.jpg")

# # PDF faylini yuklash (alohida GET so'rovi)
# @app.get("/download/pdf/{user_id}")
# async def download_pdf(user_id: str):
#     data = read_data()
#     if user_id not in data:
#         raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")

#     pdf_path = data[user_id]['rasm_pdf']
#     if not os.path.exists(pdf_path):
#         raise HTTPException(status_code=404, detail="PDF topilmadi")
    
#     return FileResponse(pdf_path, media_type='application/pdf', filename=f"{user_id}.pdf")
