import os
from PIL import Image

def convert_images_to_webp(folder_path):
    # لیست تمام فایل‌های موجود در پوشه
    for filename in os.listdir(folder_path):
        # فقط فایل‌هایی که پسوند تصویر دارند باید پردازش شوند
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            file_path = os.path.join(folder_path, filename)
            # باز کردن و تبدیل تصویر به فرمت webp
            with Image.open(file_path) as img:
                # نام جدید تصویر با پسوند webp
                new_filename = os.path.splitext(filename)[0] + '.webp'
                new_file_path = os.path.join(folder_path + '/../output', new_filename)
                # ذخیره تصویر به فرمت webp
                img.save(new_file_path, 'webp')
                print(f"تبدیل شد: {filename} به {new_filename}")

# استفاده از تابع با مسیر دلخواه
folder_path = "./" #ادرس پوشه 
convert_images_to_webp(folder_path) 