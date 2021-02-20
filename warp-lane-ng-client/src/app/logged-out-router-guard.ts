import { Injectable } from "@angular/core";
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from "@angular/router";
import { LoginService } from "./user/login.service";


@Injectable({
    providedIn: 'root'
})
export class LoggedOut implements CanActivate {

    constructor(private loginService: LoginService, private router: Router) { }

    canActivate(
        next: ActivatedRouteSnapshot,
        state: RouterStateSnapshot): boolean {
        // your  logic goes here
        if (this.loginService.sessionId) {
            return true;
        } else {
            this.router.navigate(['/home']);
        }
    }
}