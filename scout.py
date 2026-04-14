import os

def run_scout():
    # Customize your search terms here
    query = "Indie Comics + Kickstarter -Marvel -DC"
    limit = 50
    region = "US"
    
    print(f"🚀 Searching YouTube for: {query}...")
    
    # This command uses the ytsearch CLI tool
    command = f'ytsearch channel "{query}" --limit {limit} --regionCode {region} --json > raw_data.json'
    
    os.system(command)
    print("✅ Success: raw_data.json created.")

if __name__ == "__main__":
    run_scout()
