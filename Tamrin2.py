def save_to_file(name):
    """ذخیره نام در فایل"""
    with open("names.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")
    
def read_from_file():
    """خواندن نام‌ها از فایل"""
    try:
        with open("names.txt", "r", encoding="utf-8") as file:
            names = file.readlines()
        return [name.strip() for name in names]
    except FileNotFoundError:
        return []

def main():
    # دریافت نام از کاربر
    name = input("لطفاً نام خود را وارد کنید: ")
    
    # ذخیره نام در فایل
    save_to_file(name)
    print(f"نام '{name}' با موفقیت ذخیره شد.")
    
    # خواندن همه نام‌ها از فایل
    all_names = read_from_file()
    
    # نمایش نام‌ها
    if all_names:
        print("\nتمام نام‌های ذخیره شده:")
        for i, saved_name in enumerate(all_names, 1):
            print(f"{i}. {saved_name}")
    else:
        print("هنوز نامی ذخیره نشده است.")

if __name__ == "__main__":
    main()