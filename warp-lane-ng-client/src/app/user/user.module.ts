import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { LoginButtonComponent, LoginDialog } from './login-button/login-button.component';
import { MatDialogModule } from '@angular/material/dialog';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';


@NgModule({
  declarations: [
    LoginButtonComponent,
    LoginDialog
  ],
  imports: [
    BrowserModule,
    CommonModule,
    MatDialogModule,
    MatButtonModule,
    MatInputModule
  ],
  exports: [
    LoginButtonComponent
  ]
})
export class UserModule { }
