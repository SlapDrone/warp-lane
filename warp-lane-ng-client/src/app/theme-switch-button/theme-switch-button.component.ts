import { OverlayContainer } from '@angular/cdk/overlay';
import { Component, HostBinding, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'wl-theme-switch-button',
  templateUrl: './theme-switch-button.component.html',
  styleUrls: ['./theme-switch-button.component.scss']
})
export class ThemeSwitchButtonComponent implements OnInit {

  @HostBinding('class') className = '';

  themeButton = new FormControl(false);

  constructor(private dialog: MatDialog, private overlay: OverlayContainer) { }

  ngOnInit(): void {
  }

  private get darkMode(): boolean {
    return this.className == 'darkMode';
  }

  public toggleTheme() {
      console.log(this.className)
      const darkClassName = 'darkMode';
      this.className = this.className == '' ? darkClassName : '';

      console.log(this.className)
      if (this.darkMode) {
        this.overlay.getContainerElement().classList.add(darkClassName);
      } else {
        this.overlay.getContainerElement().classList.remove(darkClassName);
      }
  }
}
