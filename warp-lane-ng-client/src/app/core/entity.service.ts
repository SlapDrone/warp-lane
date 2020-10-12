import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EntityService {

  constructor() { }

  private _currentEntity: BehaviorSubject<{name: string}> = new BehaviorSubject(undefined);
  public currentEntity: Observable<{name: string}> = this._currentEntity.asObservable()

  setCurrentEntity(val: {name: string}){
    this._currentEntity.next(val);
  }

  clear(){
    this._currentEntity.next(undefined)
  }
}
