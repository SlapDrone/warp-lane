import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FileConverterDashboardComponent } from './file-converter/file-converter-dashboard/file-converter-dashboard.component';
import { MyTrackSearchComponent } from './file-converter/my-track-search/my-track-search.component';
import { TrackModifierComponent } from './file-converter/track-modifier/track-modifier.component';
import { SignUpPageComponent } from './user/sign-up-page/sign-up-page.component';


const routes: Routes = [
  {
    path: 'file-converter',
    component: FileConverterDashboardComponent,
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
    path: '',
    redirectTo: '/file-converter',
    pathMatch: 'full'
  }
];
@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
