import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'wl-file-converter-dashboard',
  templateUrl: './file-converter-dashboard.component.html',
  styleUrls: ['./file-converter-dashboard.component.sass']
})
export class FileConverterDashboardComponent implements OnInit {
  /*
  This is the dashboard for file converter tasks. The landing screen will show a widget containing the list of files
  being worked on. Server side we store the configuration file in json format that the user has set up but don't store
  the wav file they are working on.

  The dashboard provides users the option to perform the ml enhancing in browser or on the server.
  The dashboard provides links to 3 pages: home screen with a blurb and list of files, "Studio" screen that provides
  controls to work on the file and "Help" screen providing useful tips on what the controls and different modes do.

  The site should be set up as a PWA so that in browser mode can run offline.
  */
  constructor() { }

  ngOnInit(): void {
  }

}
