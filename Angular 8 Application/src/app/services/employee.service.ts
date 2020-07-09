import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {API_ENDPOINTS} from '../api-endpoints';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  constructor(private http: HttpClient) {}

  getAllUsers() {
    return this.http.get<any>(environment.apiHost + API_ENDPOINTS.getAllEmployees);
  }

  createEmployee(payload) {
    return this.http.put<any>(environment.apiHost + API_ENDPOINTS.createEmployee, payload);
  }

  updateEmployee(payload) {
    return this.http.post<any>(environment.apiHost + API_ENDPOINTS.updateEmployee, payload);
  }

  deleteEmployee(employeeId) {
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      body: {
        id: employeeId
      }
    };
    return this.http.delete<any>(environment.apiHost + API_ENDPOINTS.deleteEmployee, options);
  }

}
