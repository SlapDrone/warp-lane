import { Injectable } from '@angular/core';
import { IUploadedFile } from '../IUploadedFile';

@Injectable({
  providedIn: 'root'
})
export class TrackControllerService {

  constructor() { }

  private controlSettings: Map<string, any> = new Map();
  public trackIdentifier: string;

  public originalFile: IUploadedFile;
  
  public setControl(name: string, value: any): void {
    this.controlSettings.set(name, value);
  }

  public getTrackControlSetting(): Map<string, any> {
    return this.controlSettings;
  }
}
