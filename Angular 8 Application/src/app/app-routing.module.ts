import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CommonErrorsComponent} from './pages/common-errors/common-errors.component';
import {HomeComponent} from './pages/home/home.component';
import {AllEmployeesComponent} from './pages/all-employees/all-employees.component';


const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent },
  {path: 'allEmployees', component: AllEmployeesComponent},
  {path: 'error', component: CommonErrorsComponent},
  {path: '**', redirectTo: 'home', pathMatch: 'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
