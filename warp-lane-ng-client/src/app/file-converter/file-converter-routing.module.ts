import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MyTrackSearchComponent } from './my-track-search/my-track-search.component';
import { TrackModifierComponent } from './track-modifier/track-modifier.component';

const routes: Routes = [
    {
      path: '',
      component: MyTrackSearchComponent
    },
    {
      path: 'file-converter/track-modifier',
      component: TrackModifierComponent
    }
];
@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class FileConverterRoutingModule { }