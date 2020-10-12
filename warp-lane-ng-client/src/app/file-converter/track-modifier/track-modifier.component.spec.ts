import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrackModifierComponent } from './track-modifier.component';

describe('TrackModifierComponent', () => {
  let component: TrackModifierComponent;
  let fixture: ComponentFixture<TrackModifierComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrackModifierComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrackModifierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
