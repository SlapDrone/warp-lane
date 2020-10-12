import { Injectable } from '@angular/core';
import { EntityService } from '../core/entity.service';
import { IUploadedFile } from './IUploadedFile';

@Injectable({
  providedIn: 'root'
})
export class TrackControllerService {

  constructor(private entityService: EntityService) { }

  private controlSettings: Map<string, any> = new Map();
  public trackIdentifier: string;

  private _selectedTrack: any;
  public get selectedTrack(): any{
    return this._selectedTrack;
  }

  public set selectedTrack(val: any){
    this._selectedTrack = val;
    this.entityService.setCurrentEntity(val);
  }

  public originalFile: IUploadedFile;
  
  public setControl(name: string, value: any): void {
    this.controlSettings.set(name, value);
  }

  public getTrackControlSetting(): Map<string, any> {
    return this.controlSettings;
  }
}
