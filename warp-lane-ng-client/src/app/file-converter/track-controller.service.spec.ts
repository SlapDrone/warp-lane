import { TestBed } from '@angular/core/testing';
import { TrackControllerService } from './track-controller.service';


describe('TrackControllerService', () => {
  let service: TrackControllerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TrackControllerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
