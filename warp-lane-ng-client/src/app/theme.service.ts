import { Injectable } from '@angular/core';
import { Theme } from './theme.enum';

@Injectable({
    providedIn: 'root'
})
export class ThemeService {

    constructor() { }

    public theme: Theme = Theme.Light;
}
