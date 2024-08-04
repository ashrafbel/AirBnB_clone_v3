#!/usr/bin/python3
""" Script to create a new State object """
from models import storage
from models.state import State

# إنشاء كائن State جديد
new_state = State(name="California")

# إضافة الكائن إلى التخزين وحفظه
storage.new(new_state)
storage.save()

print("State created successfully!")

