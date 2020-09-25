import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { KnobComponent } from './widgets/knob/knob.component';



@NgModule({
  declarations: [KnobComponent],
  exports: [KnobComponent],
  imports: [
    CommonModule
  ]
})
export class WlCoreModule { }
