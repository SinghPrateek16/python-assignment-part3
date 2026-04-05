

#Part 3: File I/O, APIs & Exception Handling

# Task 1- File Read & Write

# Part A

# writing data into file
file_name = "python_notes.txt"

file = open(file_name, "w", encoding="utf-8")

# writing given lines
file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
file.write("Topic 2: Lists are ordered and mutable.\n")
file.write("Topic 3: Dictionaries store key-value pairs.\n")
file.write("Topic 4: Loops automate repetitive tasks.\n")
file.write("Topic 5: Exception handling prevents crashes.\n")

file.close()

print("File written successfully")

# now appending extra lines
file = open(file_name, "a", encoding="utf-8")
file.write("Topic 6: Functions help reuse code.\n")
file.write("Topic 7: Python is easy to learn.\n")

file.close()

print("Lines appended successfully")


# Part B

# opening file for reading
file = open(file_name, "r", encoding="utf-8")

all_lines = file.readlines()   # reading all lines into list

file.close()

print("\nReading file with numbering:")

count = 1

for line in all_lines:
    print(str(count) + ". " + line.strip())   # removing \n
    count = count + 1


# total number of lines
print("\nTotal lines:", len(all_lines))


# searching keyword
word = input("\nEnter a keyword to search: ")

found_flag = False

for line in all_lines:
    if word.lower() in line.lower():
        print(line.strip())
        found_flag = True

if found_flag == False:
    print("No matching lines found")
     
File written successfully
Lines appended successfully

Reading file with numbering:
1. Topic 1: Variables store data. Python is dynamically typed.
2. Topic 2: Lists are ordered and mutable.
3. Topic 3: Dictionaries store key-value pairs.
4. Topic 4: Loops automate repetitive tasks.
5. Topic 5: Exception handling prevents crashes.
6. Topic 6: Functions help reuse code.
7. Topic 7: Python is easy to learn.

Total lines: 7

Enter a keyword to search: data
Topic 1: Variables store data. Python is dynamically typed.

# Task 2: API Integration

import requests   # need to call API


#  Step 1-Fetch 20 products

print("Fetch products using API Integration\n")
url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)   # sending GET request
data = response.json()   # convert to python dictionary
product_list = data["products"]   # getting only products list


# print table
print("ID | Title | Category | Price | Rating")
print("-"*60)

for item in product_list:
    print(item["id"], "|", item["title"], "|", item["category"],
          "| $"+str(item["price"]), "|", item["rating"])

# Step 2-Filter & Sort
print("\nFiltered Products (rating >= 4.5):")

filtered_list = []

# filtering
for item in product_list:
    if item["rating"] >= 4.5:
        filtered_list.append(item)

# sorting by price (high to low)
filtered_list.sort(key=lambda x: x["price"], reverse=True)

# printing
for item in filtered_list:
    print(item["title"], "-", item["price"], "-", item["rating"])

# Step 3- Category search (laptops)
print("\nLaptop Products:")
url2 = "https://dummyjson.com/products/category/laptops"

response2 = requests.get(url2)
data2 = response2.json()
laptop_list = data2["products"]

for item in laptop_list:
    print(item["title"], "- $"+str(item["price"]))

#  Step 4- POST request

print("\nSending POST request...")
post_url = "https://dummyjson.com/products/add"
new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

post_response = requests.post(post_url, json=new_product)
result = post_response.json()

print("\nResponse from server:")
print(result)
     
Fetch products using API Integration

ID | Title | Category | Price | Rating
------------------------------------------------------------
1 | Essence Mascara Lash Princess | beauty | $9.99 | 2.56
2 | Eyeshadow Palette with Mirror | beauty | $19.99 | 2.86
3 | Powder Canister | beauty | $14.99 | 4.64
4 | Red Lipstick | beauty | $12.99 | 4.36
5 | Red Nail Polish | beauty | $8.99 | 4.32
6 | Calvin Klein CK One | fragrances | $49.99 | 4.37
7 | Chanel Coco Noir Eau De | fragrances | $129.99 | 4.26
8 | Dior J'adore | fragrances | $89.99 | 3.8
9 | Dolce Shine Eau de | fragrances | $69.99 | 3.96
10 | Gucci Bloom Eau de | fragrances | $79.99 | 2.74
11 | Annibale Colombo Bed | furniture | $1899.99 | 4.77
12 | Annibale Colombo Sofa | furniture | $2499.99 | 3.92
13 | Bedside Table African Cherry | furniture | $299.99 | 2.87
14 | Knoll Saarinen Executive Conference Chair | furniture | $499.99 | 4.88
15 | Wooden Bathroom Sink With Mirror | furniture | $799.99 | 3.59
16 | Apple | groceries | $1.99 | 4.19
17 | Beef Steak | groceries | $12.99 | 4.47
18 | Cat Food | groceries | $8.99 | 3.13
19 | Chicken Meat | groceries | $9.99 | 3.19
20 | Cooking Oil | groceries | $4.99 | 4.8

Filtered Products (rating >= 4.5):
Annibale Colombo Bed - 1899.99 - 4.77
Knoll Saarinen Executive Conference Chair - 499.99 - 4.88
Powder Canister - 14.99 - 4.64
Cooking Oil - 4.99 - 4.8

Laptop Products:
Apple MacBook Pro 14 Inch Space Grey - $1999.99
Asus Zenbook Pro Dual Screen Laptop - $1799.99
Huawei Matebook X Pro - $1399.99
Lenovo Yoga 920 - $1099.99
New DELL XPS 13 9300 Laptop - $1499.99

Sending POST request...

Response from server:
{'id': 195, 'title': 'My Custom Product', 'price': 999, 'description': 'A product I created via API', 'category': 'electronics'}

#Task 3 — Exception Handling

# Part A — Guarded Calculator

print("\n PART A \n")

def safe_divide(num1, num2):
    try:
        result = num1 / num2
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except TypeError:
        return "Error: Invalid input types"
# testing
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Part B — Guarded File Reader


print("\n PART B \n")
def read_file_safe(file_name):

    try:
        file = open(file_name, "r", encoding="utf-8")
        content = file.read()
        file.close()
        return content

    except FileNotFoundError:
        print("Error: File", file_name, "not found")

    finally:
        print("File operation attempt complete.")


# testing
print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


# Part C — Robust API Calls

print("\n PART C \n")

import requests

url = "https://dummyjson.com/products?limit=5"

try:
    response = requests.get(url, timeout=5)
    data = response.json()

    for item in data["products"]:
        print(item["title"], "-", item["price"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print("Some error occurred:", e)


#Part D — Input Validation Loop:

print("\n PART D \n")
import requests

while True:

    user_input = input("Enter product ID (1-100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    # checking if number
    if not user_input.isdigit():
        print("Please enter a valid number")
        continue

    product_id = int(user_input)

    # checking range
    if product_id < 1 or product_id > 100:
        print("Enter number between 1 and 100")
        continue

    # API call
    url = "https://dummyjson.com/products/" + str(product_id)

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Product not found")

        elif response.status_code == 200:
            data = response.json()
            print(data["title"], "-", data["price"])

    except requests.exceptions.ConnectionError:
        print("Connection failed")

    except requests.exceptions.Timeout:
        print("Timeout error")

    except Exception as e:
        print("Error:", e)
     
 PART A 

5.0
Error: Cannot divide by zero
Error: Invalid input types

 PART B 

File operation attempt complete.
Topic 1: Variables store data. Python is dynamically typed.
Topic 2: Lists are ordered and mutable.
Topic 3: Dictionaries store key-value pairs.
Topic 4: Loops automate repetitive tasks.
Topic 5: Exception handling prevents crashes.
Topic 6: Functions help reuse code.
Topic 7: Python is easy to learn.

Error: File ghost_file.txt not found
File operation attempt complete.
None

 PART C 

Essence Mascara Lash Princess - 9.99
Eyeshadow Palette with Mirror - 19.99
Powder Canister - 14.99
Red Lipstick - 12.99
Red Nail Polish - 8.99

 PART D 

Enter product ID (1-100) or 'quit': quit

# Task 4- Logging to File

# Task 4: Logging to File

import requests
from datetime import datetime


# function to save error in file
def save_error(place_name, err_type, err_msg):

    print("Writing error to file...")   # debug

    # current time
    now_val = datetime.now()

    # converting to string
    time_val = now_val.strftime("%Y-%m-%d %H:%M:%S")

    # making full line
    final_text = "[" + time_val + "] ERROR in " + place_name + ": " + err_type + " - " + err_msg + "\n"

    # writing to file
    f = open("error_log.txt", "a", encoding="utf-8")
    f.write(final_text)
    f.close()


# ERROR 1 (Connection Error)

print("Testing connection error...")

bad_link = "https://abcxyz12345-not-real.com"   # fake URL

try:
    r1 = requests.get(bad_link, timeout=5)

except requests.exceptions.ConnectionError:
    print("Connection failed")
    save_error("fetch_products", "ConnectionError", "No connection could be made")

except Exception as e:
    print("Some error:", e)
    save_error("fetch_products", "OtherError", str(e))


#  ERROR 2 (404 error)

print("\nTesting 404 error...")

good_link = "https://dummyjson.com/products/999"

try:
    r2 = requests.get(good_link, timeout=5)

    if r2.status_code != 200:
        print("Product not found")

        save_error("lookup_product", "HTTPError",
                   "404 Not Found for product ID 999")

except Exception as e:
    print("Error:", e)
    save_error("lookup_product", "OtherError", str(e))


#  SHOW FILE CONTENT

print("\nReading file now...\n")

file_obj = open("error_log.txt", "r", encoding="utf-8")
data_all = file_obj.read()
print(data_all)
file_obj.close()


     
Testing connection error...
Connection failed
Writing error to file...

Testing 404 error...
Product not found
Writing error to file...

Reading file now...

[2026-03-31 06:23:32] ERROR in fetch_products: ConnectionError - No connection could be made
[2026-03-31 06:23:32] ERROR in lookup_product: HTTPError - 404 Not Found for product ID 999


!ls
     
error_log.txt  python_notes.txt  sample_data

!cat error_log.txt
     
[2026-03-31 06:23:32] ERROR in fetch_products: ConnectionError - No connection could be made
[2026-03-31 06:23:32] ERROR in lookup_product: HTTPError - 404 Not Found for product ID 999

from google.colab import files
files.download("python_notes.txt")
files.download("error_log.txt")
     

