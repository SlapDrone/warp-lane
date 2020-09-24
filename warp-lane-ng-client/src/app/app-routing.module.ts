import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FileConverterDashboardComponent } from './file-converter/file-converter-dashboard/file-converter-dashboard.component';


const routes: Routes = [
  {
    path: 'file-converter',
    component: FileConverterDashboardComponent
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
