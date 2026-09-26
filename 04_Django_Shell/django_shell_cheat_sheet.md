# 🚀 Django Shell & Basic CRUD Operations

This document contains essential Django shell commands and CRUD (Create, Read, Update, Delete) logic for quick reference.

## 💻 1. Shell Basics
**Open Django Shell:**
```bash
python manage.py shell
```

**Exit Django Shell:**
```python
exit() 
# OR press Ctrl + Z and Enter
```

**Import Model (Required before doing anything):**
```python
# 'mainapp' is the app name, 'student' is the model name
from mainapp.models import student
```

---

## 🛠️ 2. CRUD Operations Cheat Sheet

### 🟢 CREATE (डेटाबेस में नया डेटा डालना)
**Method 1: Create and Save separately (Standard way)**
```python
new_stu = student(name='Rohit', email='rohit@gmail.com', age=20, address='Jaipur', rollno=45)
new_stu.save() # .save() is mandatory here!
```

**Method 2: Create directly (Fastest way - no need to call .save())**
```python
student.objects.create(name='Sanjay Singh', email='sanjay@gmail.com', age=15, address='Dubai', rollno=33)
```

### 🔵 READ (डेटाबेस से डेटा निकालना)
**Get ALL data (Returns a QuerySet/List of all students):**
```python
student.objects.all()
```

**Get SINGLE specific record (Using .get() - Use this for unique values like ID or Roll No):**
```python
# Will give an error if multiple students have the same rollno, or if none exist
stu = student.objects.get(rollno=12)
print(stu.name)
```

**FILTER data (Returns a list of matching records):**
```python
# Find all students who are 19 years old
nineteen_yr_olds = student.objects.filter(age=19)

# Find all students from Chittorgarh
local_students = student.objects.filter(address__icontains='chittorgarh')
```

### 🟡 UPDATE (डेटाबेस में मौजूद डेटा को बदलना)
**Step 1:** First, fetch the exact student you want to update.
**Step 2:** Change the value.
**Step 3:** Save the changes.
```python
# Fetching Deepesh's data using his rollno
stu_to_update = student.objects.get(rollno=12)

# Changing his age and address
stu_to_update.age = 22
stu_to_update.address = 'New Address, Chittorgarh'

# Saving to database (MANDATORY)
stu_to_update.save()
```

### 🔴 DELETE (डेटाबेस से रिकॉर्ड उड़ाना)
**Step 1:** Fetch the student.
**Step 2:** Call `.delete()` function.
```python
stu_to_delete = student.objects.get(rollno=33) # Fetching Sanjay's data
stu_to_delete.delete() # Gone forever! No .save() required after delete.
```

---
**💡 Pro-Tip for UI/Views:**
Later, we will use these exact same `objects.create()`, `objects.all()`, and `objects.filter()` commands inside our `views.py` file to send database data to our HTML/Bootstrap frontend!