import { Component, OnInit, ViewChild } from '@angular/core';
import { EntityService } from 'src/app/core/entity.service';
import { UserDetailsService } from 'src/app/user/user-details.service';
import { ITrackDetails } from '../ITrackDetails';
import { IUploadedFile } from '../IUploadedFile';
import { TrackControllerService } from '../track-controller.service';

@Component({
  selector: 'wl-my-track-search',
  templateUrl: './my-track-search.component.html',
  styleUrls: ['./my-track-search.component.scss']
})
export class MyTrackSearchComponent implements OnInit {

  constructor(
    private trackController: TrackControllerService,
    private entityService: EntityService,
    private userService: UserDetailsService) { }

  @ViewChild('uploader') uploaderButton;

  public get trackList(): ITrackDetails[]{
    return this.userService.trackCollection;
  }

  ngOnInit(): void {
    this.entityService.clear();
    this.entityService.setCurrentEntity({name: 'Select a track to begin modification.'});
  }

  trackSelect(track: any): void{
    this.trackController.selectedTrack = track;
  }

  addFile(file): void{
    if (file.type !== 'audio/x-wav' && file.type !== 'audio/wav'){
      // TODO SM: alerting code to be added.
      window.alert('Invalid file type.');
    }
    else{
      this.trackController.originalFile = file;
      this.trackList.push({name: this.trackController.originalFile.name})
    }
  }

  uploadFile = (event: { dataTransfer: { files: any[]; }; }): void => {

    if (event.dataTransfer){
      for(const file of <IUploadedFile[]>event.dataTransfer.files){
        // const file = <IUploadedFile>event.dataTransfer.files[0];
        //this.showSpinner = true;
        this.addFile(file)
      }
    }else{
      let file = (this.uploaderButton.nativeElement.files[0] as IUploadedFile);
      this.addFile(file)
    }
  }
}
