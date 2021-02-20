import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThemeSwitchButtonComponent } from './theme-switch-button.component';

describe('ThemeSwitchButtonComponent', () => {
  let component: ThemeSwitchButtonComponent;
  let fixture: ComponentFixture<ThemeSwitchButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ThemeSwitchButtonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ThemeSwitchButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
