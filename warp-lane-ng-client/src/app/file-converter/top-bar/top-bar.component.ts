import { Component, OnInit } from '@angular/core';
import { EntityService } from 'src/app/core/entity.service';

@Component({
  selector: 'wl-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.sass']
})
export class TopBarComponent implements OnInit {

  constructor(private entityService: EntityService) { }

  entityName: string;

  ngOnInit(): void {
    this.entityService.currentEntity.subscribe(
      entity => {
        if (entity && entity.name){
          this.entityName = entity.name;
        } else {
          this.entityName = undefined;
        }
      }
    );
  }

}
