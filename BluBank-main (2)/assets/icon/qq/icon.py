import os
import shutil

def organize_icons():
    """سازماندهی خودکار ایکون‌ها بر اساس لیست واقعی"""
    
    # مسیر فعلی
    current_dir = os.getcwd()
    
    # دسته‌بندی ایکون‌ها (بر اساس لیست شما)
    icon_categories = {
        'header': [
            'search.png',      # جستجو
            'wallet.png',      # کیف پول
            'notification.png',# اعلان
            'help.png'         # راهنما
        ],
        'actions': [
            'chart.png',       # گزارش مالی
            'settings.png',    # تنظیمات
            'add.png',         # شارژ حساب
            'moneyback.png',   # بازگشت وجه
            'utopay.png'       # اتوپی
        ],
        'transactions': [
            'arrow_transaction.png',  # انتقال وجه
            'ghabz.png',             # قبض
            'dong.png',              # دونگ
            'qrphoto.png'            # QR کد
        ],
        'services': [
            'car.png',         # خودرو
            'simcart.png',     # سیم‌کارت
            'internet.png',    # اینترنت
            'vam.png',         # وام
            'sayadi.png',      # صیادی
            'invite.png'       # دعوت
        ],
        'card_management': [
            'changecart.png',  # تعویض کارت
            'disable.png',     # غیرفعال‌سازی
            'suspend.png',     # تعلیق
            'security.png'     # امنیت
        ],
        'pages': [
            'Header.jpg',
            'headerQRpage.jpg',
            'Home(12).png'
        ]
    }
    
    print("🚀 شروع سازماندهی ایکون‌ها...\n")
    
    # شمارش موفقیت‌ها و خطاها
    success_count = 0
    error_count = 0
    
    # ساخت پوشه‌ها و جابجایی فایل‌ها
    for category, files in icon_categories.items():
        category_path = os.path.join(current_dir, category)
        os.makedirs(category_path, exist_ok=True)
        print(f"📁 پوشه '{category}' ساخته شد")
        
        for file in files:
            source = os.path.join(current_dir, file)
            destination = os.path.join(category_path, file)
            
            if os.path.exists(source):
                shutil.move(source, destination)
                print(f"   ✅ {file} → {category}/")
                success_count += 1
            else:
                print(f"   ⚠️  {file} پیدا نشد!")
                error_count += 1
        print()
    
    # خلاصه نتایج
    print("="*60)
    print(f"🎉 سازماندهی تمام شد!")
    print(f"   ✅ موفق: {success_count} فایل")
    print(f"   ⚠️  خطا: {error_count} فایل")
    print("="*60)
    
    # نمایش ساختار نهایی
    print("\n📂 ساختار نهایی پوشه‌ها:\n")
    for category in icon_categories.keys():
        category_path = os.path.join(current_dir, category)
        if os.path.exists(category_path):
            files_in_category = os.listdir(category_path)
            print(f"📁 {category}/ ({len(files_in_category)} فایل)")
            for file in sorted(files_in_category):
                print(f"   ├── {file}")
            print()

if __name__ == "__main__":
    organize_icons()
