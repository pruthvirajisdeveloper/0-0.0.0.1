## Classes and attribuites with methods

### student: 
* attribuits:

  * id
  * name
  * age
  * gender
  * work
  * address

* methods:
  
  * get_imfo - return imfo of a student
  * create_id - make a roll number


### seat:

* attribuits:

  * seat id
  * student id
  * fees id
  * imfo

* methods:

  * assign(student, date, duration, fees)
  * renew(student, date, duration, fees)
  * get_imfo



### manager:
  
* attribuits:

  * members list - ids
  * seats list - ids
  * settings - ini + user

* methods:

  * get_list - return full list with index
  * update student, seat - update with db
  * renew seat - update date and fees of a current student
  * new addmission - add to student
  * new member - assign a student to seat


### plans:
* attribuits:
  
  * id
  * duration
  * shift
  * fees
  * discount - from selection