import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EntityService {

  constructor() { }

  private currentEntitySubject: BehaviorSubject<{name: string}> = new BehaviorSubject(undefined);
  public currentEntity: Observable<{name: string}> = this.currentEntitySubject.asObservable();

  setCurrentEntity(val: {name: string}): void{
    this.currentEntitySubject.next(val);
  }

  clear(): void{
    this.currentEntitySubject.next(undefined);
  }
}
