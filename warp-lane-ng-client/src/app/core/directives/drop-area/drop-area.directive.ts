import { Directive, ElementRef, HostBinding, HostListener, Input, OnDestroy, OnInit } from '@angular/core';

@Directive({
  selector: '[wlDropArea]'
})
export class DropAreaDirective {

  constructor() { }

  @Input() dropFunction: (event: any) => any;
  @Input() dragOverClass: string;

  @HostBinding('class.drop-hover')
  isDragOver = false;

  @HostListener('drop', ['$event'])
  onDrop(event: any): void {
    this.dropFunction(event);
    this.cancelEvent(event);
    this.endDragTransaction();
  }

  @HostListener('dragenter', ['$event'])
  onDragEnter = (event: any) => {
    this.cancelEvent(event);
  }

  @HostListener('dragleave', ['$event'])
  onDragLeave = (event: any) => {
    this.cancelEvent(event);
    this.endDragTransaction();
  }

  @HostListener('dragover', ['$event'])
  onDragOver = (event: any) => {
    this.cancelEvent(event);
    this.isDragOver = true;
  }

  cancelEvent = (event: any) => {
    event.preventDefault();
    event.stopPropagation();
  }

  endDragTransaction = () => {
    this.isDragOver = false;
  }


}
