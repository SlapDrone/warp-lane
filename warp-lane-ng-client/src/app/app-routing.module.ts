import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FileConverterDashboardComponent } from './file-converter/file-converter-dashboard/file-converter-dashboard.component';
import { MyTrackSearchComponent } from './file-converter/my-track-search/my-track-search.component';
import { TrackModifierComponent } from './file-converter/track-modifier/track-modifier.component';


const routes: Routes = [
  {
    path: 'file-converter',
    component: FileConverterDashboardComponent,
    children:[
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
    path: '',
    redirectTo: '/file-converter',
    pathMatch: 'full'
  }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
