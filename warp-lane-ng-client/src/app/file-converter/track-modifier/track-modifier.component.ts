import { HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/core/http/api.service';
import { TrackControllerService } from '../track-controller.service';

@Component({
  selector: 'wl-track-modifier',
  templateUrl: './track-modifier.component.html',
  styleUrls: ['./track-modifier.component.scss']
})
export class TrackModifierComponent implements OnInit {

  constructor(
    private apiService: ApiService,
    private trackController: TrackControllerService) { }

  public uploadResponse: any;

  ngOnInit(): void {
  }

  submitTrack(): void{

    let headers = new HttpHeaders({
      'accept': 'application/json'
    });
    const formData = new FormData()
    console.log(this.trackController.originalFile instanceof Blob)
    formData.append('user_id', '2')
    formData.append('file', <Blob><any>this.trackController.originalFile);
    this.apiService.uploadToServer(formData, headers)
      .subscribe(
        success => this.handleUploadSuccess(this.trackController.originalFile.name, success),
        error => this.handleUploadError(this.trackController.originalFile.name, error)
      );
  }

  private handleUploadSuccess(fileName: string, data: any): void {

    console.log(`Response received for fileName ${fileName}.`);
    this.uploadResponse = data;

  }

  private handleUploadError(fileName: string, data: any): void {
    console.error(`An error occurred processing the file ${fileName}.`);
  }

  saveTrack(): void{
    let headers = new HttpHeaders();
    headers = headers.append('file-path', this.uploadResponse['file-path']);
    this.apiService.downloadFromServer(headers).subscribe(
      success => this.handleDownloadSuccess(this.trackController.originalFile.name, success),
      error => this.handleDownloadError(this.trackController.originalFile.name, error)
    );
  }

  private handleDownloadSuccess(fileName: string, data: any): void {
    console.log(`Successfully downloaded ${fileName}, response: ${data}`);
    fileName = data.headers.get('file-name');
    const blob = new Blob([data.body], {type: 'audio/x-wav'});
    saveAs(blob, fileName);
  }

  private handleDownloadError(fileName: string, data: any): void {
    console.error(`An error occurred downloading file ${fileName}`);
  }

}
