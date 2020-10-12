import { Component, Input, OnInit, Renderer2, ViewChild } from '@angular/core';
import { TrackControllerService } from '../track-controller.service';

@Component({
  selector: 'wl-knob',
  templateUrl: './knob.component.html',
  styleUrls: ['./knob.component.sass']
})
export class KnobComponent implements OnInit {

  constructor(
    private renderer: Renderer2, 
    private trackController: TrackControllerService) { 

  }

  private get tempTargetRadius(): number {
    return this.temporaryTarget.width / 2;
  }

  private get tempTargetCentreY(): number {
    return this.temporaryTarget.offsetTop + this.tempTargetRadius;
  }

  private get tempTargetCentreX(): number {
    return this.temporaryTarget.offsetLeft + this.tempTargetRadius;
  }

  @Input() controlName: string;

  @ViewChild('knob') knobElem: any;

  dialValue = 0;

  private temporaryTarget: HTMLImageElement;

  ngOnInit(): void {
  }

  getDegrees(mouseX: number, mouseY: number): number {
    const radians = Math.atan2(mouseX - this.tempTargetCentreX, mouseY - this.tempTargetCentreY);
    const degrees = Math.round((radians * (180 / Math.PI) * -1) + 100);
    return degrees;
  }

  rotate($event: any): void{
    // TODO SM: Note this is only tested in Firefox, it's likely to break in all other browsers.
    this.temporaryTarget = $event.target;
    // Only work on left most click.
    if ($event.button === 0){
      document.addEventListener('mousemove', this.onMouseMoveHandler, true);
      document.addEventListener('mouseup', this.onMouseUpHandler, true);
    }

  }

  onMouseMoveHandler = ($event: any): void => {
    // Disable if the button is no longer pressed but the 'up' listener hasn't fired.
    if ($event.buttons > 0){
      const mouseX = $event.x;
      const mouseY = $event.y;
      const degrees = this.getDegrees(mouseX, mouseY);
      this.dialValue = degrees > 0 ? degrees : 360 + degrees;
      this.renderer.setStyle(this.knobElem.nativeElement, 'transform', `rotate(${degrees}deg)`);
    }else{
      this.onMouseUpHandler();
    }
  }

  onMouseUpHandler = (): void => {
    document.removeEventListener('mousemove', this.onMouseMoveHandler, true);
    document.removeEventListener('mouseup', this.onMouseUpHandler, true);
    this.trackController.setControl(this.controlName, this.dialValue);
  }

}
