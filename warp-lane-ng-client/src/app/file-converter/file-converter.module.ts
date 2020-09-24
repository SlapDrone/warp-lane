import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FileUploadButtonComponent } from './file-upload-button/file-upload-button.component';
import { FileConverterDashboardComponent } from './file-converter-dashboard/file-converter-dashboard.component';



@NgModule({
  declarations: [FileUploadButtonComponent, FileConverterDashboardComponent],
  imports: [
    CommonModule
  ]
})
export class FileConverterModule { }
