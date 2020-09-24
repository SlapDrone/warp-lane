import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  PORT = 8000;

  constructor(private http: HttpClient) { }

  public uploadToServer(body: any, customHeaders: HttpHeaders = new HttpHeaders()): Observable<any> {
    console.log('Posting to server.');
    const endpoint = '/upload';

    let headers = new HttpHeaders();
    for (const key of customHeaders.keys()){
      headers = headers.append(key, customHeaders.getAll(key));
    }
    const options = {headers};
    return this.http.post(this.serverUrl + endpoint, body, options);
  }

  public downloadFromServer(customHeaders: HttpHeaders = new HttpHeaders()): Observable<any>{
    console.log('Getting from server.');
    const endpoint = '/download';

    let headers = new HttpHeaders();
    for (const key of customHeaders.keys()){
      headers = headers.append(key, customHeaders.getAll(key));
    }
    const options = {headers, responseType: 'arraybuffer' as 'arraybuffer'};
    return this.http.get(this.serverUrl + endpoint, options);
  }

  private get serverUrl(): string {
    return `http://localhost:${this.PORT}`;
  }

}
