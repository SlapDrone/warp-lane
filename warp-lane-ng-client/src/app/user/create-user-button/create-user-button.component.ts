import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'wl-create-user-button',
  templateUrl: './create-user-button.component.html',
  styleUrls: ['./create-user-button.component.scss']
})
export class CreateUserButtonComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  public createUser(){}
}
