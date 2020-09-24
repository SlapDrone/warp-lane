import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FileConverterDashboardComponent } from './file-converter-dashboard.component';

describe('FileConverterDashboardComponent', () => {
  let component: FileConverterDashboardComponent;
  let fixture: ComponentFixture<FileConverterDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FileConverterDashboardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FileConverterDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
