import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { LoginButtonComponent, LoginDialog } from './login-button/login-button.component';
import { MatDialogModule } from '@angular/material/dialog';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CreateUserButtonComponent } from './create-user-button/create-user-button.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';


@NgModule({
  declarations: [
    LoginButtonComponent,
    LoginDialog,
    CreateUserButtonComponent,
    SignUpPageComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    MatDialogModule,
    MatButtonModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule
  ],
  exports: [
    LoginButtonComponent
  ]
})
export class UserModule { }
