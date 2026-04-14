import json
import csv

def filter_data():
    try:
        with open('raw_data.json', 'r') as f:
            data = json.load(f)
        
        with open('targets.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Description', 'Link'])
            
            for item in data:
                title = item.get('title', 'Unknown')
                desc = item.get('description', '').replace('\n', ' ')
                
                # Logic: Only keep if 'indie', 'kickstarter', or 'review' is in the bio
                if any(word in desc.lower() for word in ['indie', 'kickstarter', 'review']):
                    writer.writerow([title, desc[:150], f"https://youtube.com/channel/{item.get('id')}"])
        
        print("🎯 Targets filtered and saved to targets.csv")
    except FileNotFoundError:
        print("❌ Error: Run scout.py first to generate raw_data.json")

if __name__ == "__main__":
    filter_data()
