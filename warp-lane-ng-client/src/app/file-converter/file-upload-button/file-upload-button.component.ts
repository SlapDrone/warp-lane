import { HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/core/http/api.service';
import { saveAs } from 'file-saver'

@Component({
  selector: 'wl-file-upload-button',
  templateUrl: './file-upload-button.component.html',
  styleUrls: ['./file-upload-button.component.sass']
})
export class FileUploadButtonComponent implements OnInit {

  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {
  }

  private uploadedFile: {
    lastModified: number, 
    name: string, 
    size: number, 
    type: string, 
    webkitRelativePath: string
  };

  uploadFile($event: { target: { files: any[]; }; }): void {
    this.uploadedFile = $event.target.files[0];
    console.log(this.uploadedFile)
    if (this.uploadedFile.type !== 'audio/x-wav'){
      // TODO SM: alerting code to be added.
      window.alert('Invalid file type.')
      this.uploadedFile = undefined;
    }
    else{
      let headers = new HttpHeaders()
      headers = headers.append('file-name', this.uploadedFile.name)
      this.ApiService.uploadToServer(this.uploadedFile, headers)
        .subscribe(
          success => this.handleUploadSuccess(this.uploadedFile.name, success),
          error => this.handleUploadError(this.uploadedFile.name, error)
        )
    }
  }

  private handleUploadSuccess(fileName: string, data: any): void {

    console.log(`Response received for fileName ${fileName}.`)
    console.log(data)
    let headers = new HttpHeaders()
    headers = headers.append('file-path', data["file-path"])
    this.ApiService.downloadFromServer(headers).subscribe(
      success => this.handleDownloadSuccess(this.uploadedFile.name, success),
      error => this.handleDownloadError(this.uploadedFile.name, error)
    )
  }

  private handleUploadError(fileName: string, data: any): void {
    console.error(`An error occurred processing the file ${fileName}.`)
  }

  private handleDownloadSuccess(fileName: string, data: any): void {
    console.log(`Successfully downloaded ${fileName}, response: ${data}`)

    var blob = new Blob([data], {type: 'audio/x-wav'});
    saveAs(blob, "inverted.wav");
  }

  private handleDownloadError(fileName: string, data: any): void {
    console.error(`An error occurred downloading file ${fileName}`)
    console.log(data)
  }
}
