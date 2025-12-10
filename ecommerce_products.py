import json
import csv

# ১০০+ প্রোডাক্টের JSON ডেটা
products = [
    {"name": "মোবাইল কভার", "category": "মোবাইল ও গ্যাজেট এক্সেসরিজ", "subcategory": "মোবাইল এক্সেসরিজ", "price_range": "200-500 BDT", "market_potential": "উচ্চ"},
    {"name": "স্ক্রিন প্রটেক্টর", "category": "মোবাইল ও গ্যাজেট এক্সেসরিজ", "subcategory": "মোবাইল এক্সেসরিজ", "price_range": "100-300 BDT", "market_potential": "উচ্চ"},
    {"name": "পাওয়ার ব্যাংক", "category": "মোবাইল ও গ্যাজেট এক্সেসরিজ", "subcategory": "গ্যাজেট", "price_range": "500-1500 BDT", "market_potential": "উচ্চ"},
    {"name": "হেডফোন", "category": "মোবাইল ও গ্যাজেট এক্সেসরিজ", "subcategory": "গ্যাজেট", "price_range": "400-2000 BDT", "market_potential": "উচ্চ"},
    {"name": "ব্লুটুথ স্পিকার", "category": "মোবাইল ও গ্যাজেট এক্সেসরিজ", "subcategory": "গ্যাজেট", "price_range": "800-3000 BDT", "market_potential": "উচ্চ"},
    {"name": "ল্যাপটপ ব্যাগ", "category": "কম্পিউটার ও গ্যাজেটস", "subcategory": "অ্যাক্সেসরিজ", "price_range": "800-2000 BDT", "market_potential": "মধ্যম"},
    {"name": "ওয়েবক্যাম", "category": "কম্পিউটার ও গ্যাজেটস", "subcategory": "গ্যাজেট", "price_range": "1500-5000 BDT", "market_potential": "মধ্যম"},
    {"name": "মাউস", "category": "কম্পিউটার ও গ্যাজেটস", "subcategory": "অ্যাক্সেসরিজ", "price_range": "300-1200 BDT", "market_potential": "উচ্চ"},
    {"name": "কীবোর্ড", "category": "কম্পিউটার ও গ্যাজেটস", "subcategory": "অ্যাক্সেসরিজ", "price_range": "500-2000 BDT", "market_potential": "উচ্চ"},
    {"name": "ল্যাপটপ স্ট্যান্ড", "category": "কম্পিউটার ও গ্যাজেটস", "subcategory": "অ্যাক্সেসরিজ", "price_range": "700-1800 BDT", "market_potential": "মধ্যম"},
    {"name": "টিশার্ট", "category": "ফ্যাশন ও পোশাক", "subcategory": "পুরুষ / মহিলা ফ্যাশন", "price_range": "400-1000 BDT", "market_potential": "উচ্চ"},
    {"name": "জিন্স", "category": "ফ্যাশন ও পোশাক", "subcategory": "পুরুষ / মহিলা ফ্যাশন", "price_range": "800-2500 BDT", "market_potential": "উচ্চ"},
    {"name": "কুর্তা", "category": "ফ্যাশন ও পোশাক", "subcategory": "পুরুষ / মহিলা ফ্যাশন", "price_range": "600-2000 BDT", "market_potential": "উচ্চ"},
    {"name": "সালোয়ার কামিজ", "category": "ফ্যাশন ও পোশাক", "subcategory": "মহিলা ফ্যাশন", "price_range": "800-2500 BDT", "market_potential": "উচ্চ"},
    {"name": "ফ্লোরাল স্কার্ট", "category": "ফ্যাশন ও পোশাক", "subcategory": "মহিলা ফ্যাশন", "price_range": "500-1500 BDT", "market_potential": "মধ্যম"},
    {"name": "হ্যান্ডব্যাগ", "category": "বেগ ও এক্সেসরিজ", "subcategory": "ফ্যাশন অ্যাক্সেসরিজ", "price_range": "800-2500 BDT", "market_potential": "উচ্চ"},
    {"name": "ব্যাকপ্যাক", "category": "বেগ ও এক্সেসরিজ", "subcategory": "ফ্যাশন অ্যাক্সেসরিজ", "price_range": "1000-3000 BDT", "market_potential": "উচ্চ"},
    {"name": "ওয়ালেট", "category": "বেগ ও এক্সেসরিজ", "subcategory": "ফ্যাশন অ্যাক্সেসরিজ", "price_range": "400-1200 BDT", "market_potential": "মধ্যম"},
    {"name": "স্যান্ডেল", "category": "ফ্যাশন ও পোশাক", "subcategory": "জুতা", "price_range": "400-1500 BDT", "market_potential": "উচ্চ"},
    {"name": "স্নিকারস", "category": "ফ্যাশন ও পোশাক", "subcategory": "জুতা", "price_range": "800-3500 BDT", "market_potential": "উচ্চ"}
    # এখান থেকে আরও ১০০+ প্রোডাক্ট একইভাবে যুক্ত করতে হবে
]

# CSV বানানোর ফাংশন
def generate_csv(filename="products.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Category", "Subcategory", "Price Range", "Market Potential"])
        for product in products:
            writer.writerow([product["name"], product["category"], product["subcategory"], product["price_range"], product["market_potential"]])
    print(f"CSV ফাইল তৈরি হয়েছে: {filename}")

# রান করলে CSV বানাবে
if __name__ == "__main__":
    generate_csv()
