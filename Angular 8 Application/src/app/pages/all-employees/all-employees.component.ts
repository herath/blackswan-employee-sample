import { Component, OnInit } from '@angular/core';
import {EmployeeService} from '../../services/employee.service';

@Component({
  selector: 'app-all-employees',
  templateUrl: './all-employees.component.html',
  styleUrls: ['./all-employees.component.css']
})
export class AllEmployeesComponent implements OnInit {

  EMPLOYEES;

  constructor(private employeeService: EmployeeService) { }

  ngOnInit() {
    console.log('staring');
    this.employeeService.getAllUsers().subscribe( res => {
      console.log('Employee List', res);
      if (res.success) {
        this.EMPLOYEES = res.data;
      } else {
        console.log('Error getting employee list');
        alert('Oops! There is an error getting Employees !');
        this.EMPLOYEES = [];
      }
    });
  }

  deleteEmployee(id) {
    console.log('going to delete the user with id', id);
    const confirmationStatus = confirm('Are you sure you want to delete?');
    console.log('delete confirmation', confirmationStatus);
    if (confirmationStatus) {
      // delete
      this.employeeService.deleteEmployee(id).subscribe( res => {
        console.log('res', res);
        if (res.success) {
          alert('employee deleted successfully');
          location.reload();
        } else {
          console.log('error deleting employee');
        }
      });
      console.log('deleting employee');
    } else {
      return;
    }
  }

  editEmployee(id) {
    console.log('id', id);
    console.log('value', this.EMPLOYEES.filter( data => data.id === id)[0].name);

    const employeeNameForEdit = prompt('Please enter employee name', this.EMPLOYEES.filter( data => data.id === id)[0].name);
    console.log('employeeNameForEdit', employeeNameForEdit);

    if (!employeeNameForEdit || employeeNameForEdit === '') {
      alert('Employee name can not be empty');
      return;
    }

    const employeeEmailForEdit = prompt('Please enter employee email', this.EMPLOYEES.filter( data => data.id === id)[0].email);
    console.log('employeeNameForEdit', employeeEmailForEdit);
    if (!employeeEmailForEdit || employeeEmailForEdit === '') {
      alert('Employee email can not be empty');
      return;
    }

    const payload = {
      id : id,
      name : employeeNameForEdit,
      email : employeeEmailForEdit
    };

    this.employeeService.updateEmployee(payload).subscribe( res => {
      console.log('res', res);
      if (res.success) {
        alert('employee updated successfully');
        location.reload();
      } else {
        console.log('error updating employee');
      }
    });
  }

}
