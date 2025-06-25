import requests

BASE = "http://192.168.100.253:5000"  # 🔁 заміни на IP твоєї VM, якщо інший
results = []

def log(response):
    try:
        data = response.json()
    except Exception:
        data = response.text
    text = f"URL: {response.url}\nSTATUS: {response.status_code}\nRESPONSE: {data}\n\n"
    print(text)
    results.append(text)

# 1. GET all existing students
log(requests.get(f"{BASE}/students"))

# 2. POST three students
students_data = [
    {"first_name": "John", "last_name": "Doe", "age": 20},
    {"first_name": "Jane", "last_name": "Doe", "age": 22},
    {"first_name": "Mark", "last_name": "Twain", "age": 25}
]
for student in students_data:
    log(requests.post(f"{BASE}/students", json=student))

# 3. GET all students
log(requests.get(f"{BASE}/students"))

# 4. PATCH: update age of second student (id=2)
log(requests.patch(f"{BASE}/students/2", json={"age": 23}))

# 5. GET student with id=2
log(requests.get(f"{BASE}/students/id/2"))

# 6. PUT: update full info of student with id=3
log(requests.put(f"{BASE}/students/3", json={
    "first_name": "Marcus",
    "last_name": "Twain",
    "age": 26
}))

# 7. GET student with id=3
log(requests.get(f"{BASE}/students/id/3"))

# 8. GET all students
log(requests.get(f"{BASE}/students"))

# 9. DELETE student with id=1
log(requests.delete(f"{BASE}/students/1"))

# 10. GET all students
log(requests.get(f"{BASE}/students"))

# 11. Save results to file
with open("results.txt", "w") as f:
    f.writelines(results)
