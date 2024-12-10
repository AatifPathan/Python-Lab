info={'name':'Paul','age':40,'city':'Venice'}
print("Name:", info['name'])
info['email'] = 'paul@google.com'
print("\nAfter adding email:",info)
info['age'] = 35
print("\nAfter updating age:",info)
r_v= info.pop('city')
print("\nAfter removing 'city':",info)
print("Removed value:", r_v)
email =info.get('email')
print("\nEmail:", email)
print("\nKeys:", list(info.keys()))
print("Values:", list(info.values()))
print("Items:", list(info.items()))
print("\nIs 'name' a key in info?", 'name' in info)
info.clear()
print("\nAfter clearing dictionary:", info)
