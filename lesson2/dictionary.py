contact_info ={"Liron": "043-822-778",
               "Melina": "123-456-789"
}

Liron_phone = contact_info["Liron"]
print(Liron_phone)

contact_info["Melina"] = "123-456-788"
print(contact_info)

contact_info["egzon"] = "123-456-788"
print(contact_info)

# del contact_info["egzon"] = "123-456-788"
# print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {
    "Liron":{
        "phone_number" : "043 822 778",
        "email" : "Lironaliu01@icloud.com",
        "home_address" : "Fushe Kosove",
        "birthday" : "01/04/08"
    },


    "Sara" :{
        "phone_number": "123-123",
        "email": "sara@icloud.com",
        "home_address": "Fushe Kosove",
        "birthday": "24/12/07"
    },

    "Liron":{
        "phone_number" : "043 822 778",
        "email" : "Lironaliu01@icloud.com",
        "home_address" : "Fushe Kosove",
        "birthday" : "01/04/08"
    }
}

print(contact_information)

sara_information = contact_information["sara"]
print(sara_information)

contacts = {
    "Festa":("123-456", "festa@gmail.com"),
    "sara":("123-123", "sara@gmail.com"),
    "Liron": ("111-123", "liron@gmail.com")
}

festa_info = contacts["festa"]
phone_number = festa_info[0]
print(phone_number)


phone_number, email = contacts["festa"]