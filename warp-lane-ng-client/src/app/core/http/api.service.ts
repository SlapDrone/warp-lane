import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  PORT = 8000

  constructor(private http: HttpClient) { }

  public uploadToServer(body: any, custom_headers: HttpHeaders = new HttpHeaders()){
    console.log('Posting to server.')
    let endpoint = "/upload"
    
    let headers = new HttpHeaders()
    for(let key of custom_headers.keys()){
      headers = headers.append(key, custom_headers.getAll(key))
    }
    let options = {headers: headers}
    return this.http.post(this.serverUrl + endpoint, body, options);
  }

  public downloadFromServer(custom_headers: HttpHeaders = new HttpHeaders()){
    console.log('Getting from server.')
    let endpoint = "/download"

    let headers = new HttpHeaders()
    for(let key of custom_headers.keys()){
      headers = headers.append(key, custom_headers.getAll(key))
    }
    let options = {headers: headers, responseType: 'arraybuffer' as 'arraybuffer'}
    return this.http.get(this.serverUrl + endpoint, options);
  }

  private get serverUrl(): string {
    return `http://localhost:${this.PORT}`;
  }

}
