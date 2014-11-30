#pyidf

Python library to read, modify and create EnergyPlus idf files


*This is a work in progress, do NOT expect it to actually work! As this is an early work, changes in the API are very likely to happen.*

##Todos:


* field attributes
* read / write support
* handle \note fields as indicated in idd (ignore corresponding objects for the moment?)
* unit tests
* field comments not implemented:
  * required-field
  * begin-extensible
  * ip-units
  * unitsBasedOnField
  * deprecated
  * autosizeable
  * autocalculatabel
  * type: object-list, external-list, node
  * retaincase
  * object-list
  * external-list
  * reference
* object level comments not yet implemented
  * unique-object
  * required-object
  * min-fields
  * obsolete
  * extensible
  * begin-extensible
  * format
  * reference-class-name