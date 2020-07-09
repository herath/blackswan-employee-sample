import unittest
import requests
import json

class MyTestCase(unittest.TestCase):

    baseUrl = "https://mip1bm64gl.execute-api.us-east-1.amazonaws.com/dev/"
    apiModule = "employee"
    headers = {"Content-Type": "application/json"}

    def test_employee_create_employee(self):
        url = self.baseUrl + self.apiModule + "/create-employee"
        test_user = '{"name":"Test User 1","email":"TestUser1@gmail.com"}'
        data = test_user
        response = requests.put(url, data=data, headers=self.headers)
        assert response.status_code == 200

    def test_employee_get_employee_list(self):
        url = self.baseUrl + self.apiModule + "/get-employee-list"
        response = requests.get(url, headers=self.headers)
        assert response.status_code == 200

    def test_employee_update_employee(self):
        url = self.baseUrl + self.apiModule + "/update-employee"
        test_user_update = '{"id": 1 ,"name":"Updated User 1","email":"UpdatedUser1@gmail.com"}'
        response = requests.post(url, data=test_user_update, headers=self.headers)
        assert response.status_code == 200

    def test_employee_delete_employee(self):
        url = self.baseUrl + self.apiModule + "/delete-employee"
        test_user_to_delete = '{"id" : 1}'
        response = requests.delete(url, data=test_user_to_delete, headers=self.headers)
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
