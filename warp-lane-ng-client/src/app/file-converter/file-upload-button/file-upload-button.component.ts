import { HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/core/http/api.service';
import { saveAs } from 'file-saver';

@Component({
  selector: 'wl-file-upload-button',
  templateUrl: './file-upload-button.component.html',
  styleUrls: ['./file-upload-button.component.sass']
})
export class FileUploadButtonComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  private uploadedFile: {
    lastModified: number,
    name: string,
    size: number,
    type: string,
    webkitRelativePath: string
  };

  public showSpinner = false;

  ngOnInit(): void {
  }

  uploadFile($event: { target: { files: any[]; }; }): void {
    this.uploadedFile = $event.target.files[0];
    this.showSpinner = true;
    console.log(this.uploadedFile);
    if (this.uploadedFile.type !== 'audio/x-wav'){
      // TODO SM: alerting code to be added.
      window.alert('Invalid file type.');
      this.uploadedFile = undefined;
    }
    else{
      let headers = new HttpHeaders();
      headers = headers.append('file-name', this.uploadedFile.name);
      this.apiService.uploadToServer(this.uploadedFile, headers)
        .subscribe(
          success => this.handleUploadSuccess(this.uploadedFile.name, success),
          error => this.handleUploadError(this.uploadedFile.name, error)
        );
    }
  }

  private handleUploadSuccess(fileName: string, data: any): void {

    console.log(`Response received for fileName ${fileName}.`);
    let headers = new HttpHeaders();
    headers = headers.append('file-path', data['file-path']);
    this.apiService.downloadFromServer(headers).subscribe(
      success => this.handleDownloadSuccess(this.uploadedFile.name, success),
      error => this.handleDownloadError(this.uploadedFile.name, error)
    );
  }

  private handleUploadError(fileName: string, data: any): void {
    console.error(`An error occurred processing the file ${fileName}.`);
    this.showSpinner = false;
  }

  private handleDownloadSuccess(fileName: string, data: any): void {
    console.log(`Successfully downloaded ${fileName}, response: ${data}`);
    fileName = data.headers.get('file-name');
    // headerFileName = data.
    const blob = new Blob([data.body], {type: 'audio/x-wav'});
    saveAs(blob, fileName);
    this.showSpinner = false;
  }

  private handleDownloadError(fileName: string, data: any): void {
    console.error(`An error occurred downloading file ${fileName}`);
    console.log(data);
    this.showSpinner = false;
  }
}
