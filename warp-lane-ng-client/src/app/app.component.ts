import { OverlayContainer } from '@angular/cdk/overlay';
import { Component, HostBinding, OnDestroy, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Subscription } from 'rxjs';
import { Theme } from './theme.enum';
import { ThemeService } from './theme.service';
import { LoginService } from './user/login.service';

@Component({
    selector: 'wl-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
    static readonly title = 'warp-lane-ng-client';
    static readonly darkClassName = 'darkMode';

    @HostBinding('class') className = '';

    constructor(
        private dialog: MatDialog,
        private overlay: OverlayContainer,
        private loginService: LoginService,
        private themeService: ThemeService) { }

    private subscriptions: Subscription[] = [];

    ngOnInit(): void {
    }

    ngOnDestroy(): void {
        this.subscriptions.forEach(sub => sub.unsubscribe());
    }

    public get isSignedOut(){
        return !this.loginService.accessToken;
    }

    public modeText: string = 'Dark Mode';

    public toggleDarkMode() {
        this.className = AppComponent.darkClassName;
        this.overlay.getContainerElement().classList.add(AppComponent.darkClassName);
        this.themeService.theme = Theme.Dark;
        this.modeText = 'Light Mode';
    }

    public toggleLightMode() {
        this.className = '';
        this.overlay.getContainerElement().classList.remove(AppComponent.darkClassName);
        this.themeService.theme = Theme.Light;
        this.modeText = 'Dark Mode';
    }

    public toggleTheme() {
        if (this.themeService.theme == Theme.Light) {
            this.toggleDarkMode();
        } else {
            this.toggleLightMode();
        }
    }
}
