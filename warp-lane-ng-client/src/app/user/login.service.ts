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
        const body = {
            'username': username,
            'password': password
        };
        this.apiService.login(body).subscribe(
            success => this.handleSuccess(success),
            error => this.handleError(error)
        );
    }


    public sessionId: string;

    private isLoggedInSubject = new BehaviorSubject<boolean>(false);

    isLoggedIn$: Observable<boolean> = this.isLoggedInSubject.asObservable();

    setLoggedIn(val: boolean) {
        this.isLoggedInSubject.next(val);
    }

    private handleSuccess(data: any): void {
        console.log()
        console.log('Login Successful');
        this.sessionId = data['session_id'];
        this.setLoggedIn(true);
    }

    private handleError(data: any): void {
        console.error('Login Failed.');
    }
}
