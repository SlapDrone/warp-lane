import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FileConverterDashboardComponent } from './file-converter/file-converter-dashboard/file-converter-dashboard.component';
import { MyTrackSearchComponent } from './file-converter/my-track-search/my-track-search.component';
import { TrackModifierComponent } from './file-converter/track-modifier/track-modifier.component';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { LoggedOut } from './logged-out-router-guard';
import { SignUpPageComponent } from './user/sign-up-page/sign-up-page.component';


const routes: Routes = [
  {
    path: 'file-converter',
    component: FileConverterDashboardComponent,
    canActivate: [LoggedOut],
    children: [
      {
        path: '',
        component: MyTrackSearchComponent
      },
      {
        path: 'track-modifier',
        component: TrackModifierComponent
      }
    ]
  },
  {
    path: 'sign-up',
    component: SignUpPageComponent
  },
  {
    path: 'home',
    component: HomeScreenComponent
  },
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  }
];
@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
