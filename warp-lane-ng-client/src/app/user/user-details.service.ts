import { Injectable } from '@angular/core';
import { EntityService } from '../core/entity.service';
import { ITrackDetails } from '../file-converter/ITrackDetails';

@Injectable({
  providedIn: 'root'
})
export class UserDetailsService {

  constructor(private entityService: EntityService) { }

  trackCollection: ITrackDetails[] = [];

  username: string;
}
