import requests 

def compute_seed(student_key):
    return sum(ord(ch) for ch in student_key.strip())

def get_valid_sku(prompt):
    while True:
        sku = input(prompt).strip()
        if sku == "":
            print("SKU cannot be empty. Please try again.")
        else:
            return sku

def get_valid_onhand(prompt):
    while True:
        try:
            onhand = int(input(prompt).strip())
            if onhand < 0:
                print("On-hand must be greater than or equal to zero. Please try again.")
            else:
                return onhand
        except ValueError:
            print("Invalid input. Please enter a valid integer for the on-hand quantity.")

student_key = input("Enter your student key: ")
seed = compute_seed(student_key)

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

total_skus = 0
reorder_skus = 0

while True:
    sku = get_valid_sku("Enter SKU (or 'DONE' to finish): ")

    if sku.upper() == 'DONE':
        break

    onhand = get_valid_onhand("Enter on-hand quantity: ")

    total_skus += 1
    if onhand < threshold:
        reorder_skus += 1

term = "weezer" if seed % 2 == 0 else "drake"

api_status = "OK"
song_count = "N/A"

try:
    response = requests.get ("https://itunes.apple.com/search",
        params={"entity": "song", "limit": 5, "term": term},
        timeout = 5
    )

    if response.status_code != 200:
        api_status = "FAILED"
    else:
        try:
            data = response.json()
            results = data.get("results", [])
            song_count = sum(1 for item in results if item.get("kind") == "song")
        except Exception:
            api_status = "INVALID_RESPONSE"
            song_count = "N/A"

except Exception:
    api_status = "FAILED"
    song_count = "N/A"
    
 
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_skus}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {song_count}")
print(f"API status: {api_status}")
 
