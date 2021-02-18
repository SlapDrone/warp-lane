import { Component, Inject, OnInit } from '@angular/core';
import { LoginService } from '../login.service';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

export interface DialogData {
  
}


@Component({
  selector: 'wl-login-button',
  templateUrl: './login-button.component.html',
  styleUrls: ['./login-button.component.sass']
})
export class LoginButtonComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }


  openDialog(): void {
    const dialogRef = this.dialog.open(LoginDialog, {
      width: '250px',
      data: {}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('Login dialog closed.');
    });
  }

}

@Component({
  selector: 'login-dialog',
  templateUrl: './login-dialog.html',
})
export class LoginDialog {

  constructor(
    public dialogRef: MatDialogRef<LoginButtonComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,
    private loginService: LoginService) {}

  onNoClick(): void {
    this.dialogRef.close();
  }

  public username: string;

  public password: string;

  public get canLogin(): boolean{
    if(this.username && this.password){
      return true;
    }
  }

  login = () => {
    this.loginService.login(this.username, this.password)
  }

}
