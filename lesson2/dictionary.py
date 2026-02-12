contact_info ={"Liron": "043-822-778",
               "Melina": "123-456-789"
}

Liron_phone = contact_info["Liron"]
print(Liron_phone)

contact_info["Melina"] = "123-456-788"
print(contact_info)

contact_info["egzon"] = "123-456-788"
print(contact_info)

del contact_info["egzon"]"123-456-788"
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)