#Access Nested dict Items
emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}

for key, value in emp_dict.items():
    print(key, value)
print(emp_dict['company']['employee']['payable']['increment'])