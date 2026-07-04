response = {
    "status": "success",
    "user": {
        "name": "Kate",
        "age": 25,
        "country": "Czech Republic"
},
    "permissions": {
        "admin": True,
        "can_edit": False
    }
}

print(response["user"]["name"])
print(response["user"]["country"])
print(response["permissions"]["admin"])
assert response["status"] == "success"
assert response["permissions"]["can_edit"] == False



response = {
    "name": "Emma",
    "age": 28,
    "country": "Canada"
}

print(response["name"])
print(response["age"])
print(response["country"])


response = {
    "user": {
        "name": "Oliver",
        "age": 31
    }
}

print(response["user"]["name"])
print(response["user"]["age"])

response = {
    "status": "success",
    "message": "User created",
    "admin": False
}

assert response["status"] == "success"
assert response["message"] == "User created"
assert response["admin"] is False


response = {
    "order": {
        "id": 154,
        "customer": {
            "name": "Alice",
            "city": "London"
        },
        "paid": True
    },
    "status": "completed"
}

print(response["order"]["id"])
print(response["order"]["customer"]["name"])
print(response["order"]["customer"]["city"])
assert response["order"]["paid"] is True
assert response["status"] == "completed"


response = {
    "name": "Emma"
}
#add data
response["age"] = 30
print(response)

#change data
response = {
    "status": "error"
}

response["status"] = "success"
print(response)