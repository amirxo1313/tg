import os

# --- تنظیمات ---
# مسیرهای هدف
TARGET_DIRS = {
    'lib',
    os.path.join('android', 'app', 'src', 'main'),
    'UI'
}

# پسوندهای مجاز
EXTENSIONS = {'.dart', '.yaml', '.xml', '.kt', '.java'}

# فایل خروجی
OUTPUT_FILE = "blubank_ui_source_v2.txt"

# محدودیت حجم (افزایش دادم به ۲ مگابایت محض احتیاط)
MAX_FILE_SIZE = 2 * 1024 * 1024 

def scan_and_debug():
    root_path = os.getcwd()
    print(f"🚀 Starting Deep Scan in: {root_path}\n")
    
    found_files_count = 0
    content_buffer = []
    
    # هدر فایل خروجی
    content_buffer.append("BLUBANK FULL SOURCE CODE (DEBUG VERSION)\n")
    content_buffer.append("="*80 + "\n\n")

    for target in TARGET_DIRS:
        full_path = os.path.join(root_path, target)
        
        if not os.path.exists(full_path):
            print(f"⚠️ Directory NOT FOUND: {target}")
            continue

        print(f"📂 Scanning directory: {target} ...")

        for root, dirs, files in os.walk(full_path):
            # حذف پوشه‌های مزاحم از جستجو
            if 'build' in dirs: dirs.remove('build')
            if '.dart_tool' in dirs: dirs.remove('.dart_tool')

            for file in files:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1]
                
                # 1. بررسی پسوند
                if ext not in EXTENSIONS:
                    continue # فایل‌های متفرقه رو بی سر و صدا رد کن

                relative_path = os.path.relpath(file_path, root_path)

                # 2. بررسی حجم
                try:
                    size = os.path.getsize(file_path)
                    if size > MAX_FILE_SIZE:
                        print(f"❌ SKIPPED (Too Large): {relative_path} ({size} bytes)")
                        continue
                except OSError:
                    print(f"❌ SKIPPED (OS Error): {relative_path}")
                    continue

                # 3. تلاش برای خواندن فایل
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                        
                        # اضافه کردن به بافر
                        content_buffer.append(f"{'='*80}\n")
                        content_buffer.append(f"📄 FILE: {file}\n")
                        content_buffer.append(f"📂 PATH: {relative_path}\n")
                        content_buffer.append(f"{'='*80}\n")
                        content_buffer.append(content + "\n\n")
                        
                        found_files_count += 1
                        # چاپ فایل‌های مهم برای اطمینان شما
                        if "Screen" in file or "main" in file:
                             print(f"   ✅ Captured: {relative_path}")
                        
                except Exception as e:
                    print(f"❌ FAILED TO READ: {relative_path} -> Error: {e}")

    # نوشتن فایل نهایی
    print(f"\n💾 Writing {len(content_buffer)} chunks to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(content_buffer)
        
    print(f"\n✅ DONE! Captured {found_files_count} files.")
    print("Please check the console logs above to see if 'mainScreen.dart' was captured.")

if __name__ == "__main__":
    scan_and_debug()
