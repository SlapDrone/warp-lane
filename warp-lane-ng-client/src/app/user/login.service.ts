import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { Observable } from 'rxjs/internal/Observable';
import { ApiService } from '../core/http/api.service';

@Injectable({
    providedIn: 'root'
})
export class LoginService {

    constructor(private apiService: ApiService) { }

    public login(username: string, password: string): void {
        const body = `username=${username}&password=${password}`
        const headers = new HttpHeaders({
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json'
        });
        this.apiService.login(body, headers).subscribe(
            success => this.handleSuccess(success),
            error => this.handleError(error)
        );
    }

    public logout(): void{
        this.accessToken = undefined;
        this.setLoggedIn(false);
    }

    public accessToken: string;

    private isLoggedInSubject = new BehaviorSubject<boolean>(false);

    isLoggedIn$: Observable<boolean> = this.isLoggedInSubject.asObservable();

    setLoggedIn(val: boolean) {
        this.isLoggedInSubject.next(val);
    }

    private handleSuccess(data: any): void {
        console.log()
        console.log('Login Successful');
        this.accessToken = data['access_token'];
        this.setLoggedIn(true);
    }

    private handleError(data: any): void {
        console.error('Login Failed.');
    }
}
