import { Component, OnInit } from '@angular/core';
import {EmployeeService} from '../../services/employee.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  name;
  email;
  address;

  constructor(private employeeService: EmployeeService) { }

  ngOnInit() {
  }

  addEmployee() {

    if (!this.name || this.name === '') {
      alert('please enter the name of the employee');
      return;
    }

    if (!this.email || this.name === '') {
      alert('please enter the name of the employee');
      return;
    }

    const payload = {
      name : this.name,
      email : this.email
    };
    this.employeeService.createEmployee(payload).subscribe( res => {
      console.log('Employee List', res);
      if (res.success) {
        alert('Employee has been added successfully!');
        location.reload();
      } else {
        alert('Oops There is an error adding employee!');
      }
    });
  }
}
