import { Component, Input, OnInit } from '@angular/core';
import { Theme } from 'src/app/theme.enum';
import { ThemeService } from 'src/app/theme.service';
import { TrackControllerService } from '../track-controller.service';

@Component({
  selector: 'wl-track-list-item',
  templateUrl: './track-list-item.component.html',
  styleUrls: ['./track-list-item.component.scss']
})
export class TrackListItemComponent implements OnInit {

  constructor(
    private trackController: TrackControllerService,
    private themeService: ThemeService) { }

  ngOnInit(): void {
  }

  @Input() track: any;

  public bgColor = '';

  onTrackMouseEnter(event){
    if(this.themeService.theme == Theme.Dark){
      this.bgColor = '#0c2d47'
    } else{
      this.bgColor = '#cee4f6'
    }
  }
  onTrackMouseLeave(event){
    this.bgColor = ''
  }
  trackSelect(track: any): void{
    this.trackController.selectedTrack = track;
  }
}
