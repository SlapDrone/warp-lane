import { Component, Inject, OnInit } from '@angular/core';
import { LoginService } from '../login.service';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';

export interface DialogData {

}


@Component({
    selector: 'wl-login-button',
    templateUrl: './login-button.component.html',
    styleUrls: ['./login-button.component.scss']
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
        private loginService: LoginService) { }

    onNoClick(): void {
        this.dialogRef.close();
    }

    public username: string;

    public password: string;

    public get canLogin(): boolean {
        return this.usernameFormControl.valid
            && this.passwordFormControl.valid;
    }

    login = () => {
        this.loginService.login(this.username, this.password)
    }

    matcher = new MyErrorStateMatcher();

    passwordFormControl = new FormControl('', [
        Validators.required
    ]);
    usernameFormControl = new FormControl('', [
        Validators.required
    ]);

}

export class MyErrorStateMatcher implements ErrorStateMatcher {
    isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
        const isSubmitted = form && form.submitted;
        return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
    }
}