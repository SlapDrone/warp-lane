import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DropAreaDirective } from './directives/drop-area/drop-area.directive';


@NgModule({
  declarations: [DropAreaDirective],
  exports: [DropAreaDirective],
  imports: [
    CommonModule
  ]
})
export class WlCoreModule { }
