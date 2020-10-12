import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyTrackSearchComponent } from './my-track-search.component';

describe('MyTrackSearchComponent', () => {
  let component: MyTrackSearchComponent;
  let fixture: ComponentFixture<MyTrackSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MyTrackSearchComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MyTrackSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
