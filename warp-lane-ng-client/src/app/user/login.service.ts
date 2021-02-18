import { Injectable } from '@angular/core';
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

    private handleSuccess(data: any): void {
        console.log()
        console.log('Login Successful');
        this.sessionId = data['session_id'];
    }

    private handleError(data: any): void {
        console.error('Login Failed.');
    }
}
