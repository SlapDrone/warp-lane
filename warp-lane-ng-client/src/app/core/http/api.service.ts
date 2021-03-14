import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ApiService {


    PORT = 8000;

    constructor(private http: HttpClient) { }

    private get serverUrl(): string {
        return `http://127.0.0.1:${this.PORT}`;
    }

    public login(body: any, customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {
        console.log('Signing in.');
        const endpoint = '/token';

        return this._basePost(body, endpoint, customHeaders);
    }

    public createUser(body: any, customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {
        console.log('Signing up.');
        const endpoint = '/create_user';

        return this._basePost(body, endpoint, customHeaders);
    }

    public uploadToServer(body: any, customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {
        console.log('Posting to server.');
        const endpoint = '/upload';

        return this._basePost(body, endpoint, customHeaders);
    }

    private _basePost(body: any, endpoint: string, customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {

        let headers = new HttpHeaders();
        for (const key of customHeaders.keys()) {
            headers = headers.append(key, customHeaders.getAll(key));
        }
        const options = { headers };
        return this.http.post(this.serverUrl + endpoint, body, options);
    }

    public downloadFromServer(customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {
        console.log('Getting from server.');
        const endpoint = '/download';

        let headers = new HttpHeaders();
        for (const key of customHeaders.keys()) {
            headers = headers.append(key, customHeaders.getAll(key));
        }
        const options = { headers, observe: 'response' as 'response', responseType: 'arraybuffer' as 'arraybuffer' };
        return this.http.get(this.serverUrl + endpoint, options);
    }

}
