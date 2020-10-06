import { TestBed } from '@angular/core/testing';

import { TrackControlPaneService } from './track-control-pane.service';

describe('TrackControlPaneService', () => {
  let service: TrackControlPaneService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TrackControlPaneService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
