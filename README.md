#pyidf

Python library to read, modify and create EnergyPlus idf files

[![Code Health](https://landscape.io/github/rbuffat/pyidf/master/landscape.svg)](https://landscape.io/github/rbuffat/pyidf/master)

*This is a work in progress, do NOT expect it to actually work! As this is an early work, changes in the API are very likely to happen.*

##Todos:

* unit tests
* doc
* field comments not implemented:
  * type: object-list, external-list, node
  * retaincase
  * object-list
  * external-list
  * reference
* object level comments not yet implemented
  * obsolete
  * reference-class-name
  
## Usage

### Validation levels

Pyidf supports four different levels of validation. `ValidationLevel.no` does not perform any validation. `ValidationLevel.warn` issues warnings for all values not following the specification. `ValidationLevel.transition` tries to transition values to follow the specification. This includes casting float values to integers, matching values of choice types to values from the specification and setting default values for required fields when no value is set. For values not possible to match or cast, a warning is issued. `ValidationLevel.error` issues exceptions when a value is not valid according the specification. The default validation level is `ValidationLevel.transition`. The level can be changed with:

```python
from pyidf import ValidationLevel
import pyidf

pyidf.validation_level = ValidationLevel.no
```

### Reading an existing idf file

```python
from pyidf.idf import IDF

idf = IDF(r"/usr/local/EnergyPlus-8-2-0/ExampleFiles/BasicsFiles/Exercise1A.idf")
```

### Writing an existing idf file

```python
idf.save(r"~/Exercise1A_out.idf")
```

### Accessing data objects

Accessing data objects is possible either by the name of the object:

```python
for building in idf['Building']:
    print building
```

or by the corresponding property:

```python
for building in idf.buildings:
    print building
```

Both variants return a list of the corresponding data objects present in the idf object. The name of data objects were pythonified, for example  the idd data object `BuildingSurface:Detailed` is represented by the Python class `BuildingSurfaceDetailed`.

It is possible to iterate over all data objects of an idf object:
```python
for obj in idf:
    print obj
```

There are two types of fields. Normal fields and extensible fields. Normal fields exists only once while extensible fields can exist multiple times. Normal fields of a data object can similarly be accessed as data objects by their name, corresponding property or additionally by their index:

```python
print idf['Building'][0]['Name']
```

```python
print idf.buildings[0].name
```

```python
print idf.buildings[0][0]
```

The schema of normal fields can be accessed with:
```python
print idf['Building'][0].schema['fields']
```

and of extensible fields with:
```python
print idf['Building'][0].schema['extensible-fields']
```

Extensible fields can be accessed with:
```python
print idf.buildingsurfacedetaileds[0].extensibles
```

For example for `BuildingSurface:Detailed` the extensible fields are vertexes consisting of x,y,z values. The following code adds one to all coordinates:

```python
print idf["BuildingSurface:Detailed"][0].schema['extensible-fields'].keys()
a = idf.buildingsurfacedetaileds[0].extensibles
b = [map(lambda x: x + 1, ext) for ext in a]
idf.buildingsurfacedetaileds[0].extensibles = b
```

### Creating data objects

The following code creates a new `BuildingSurfaceDetailed` object and fills the values from an existing object: 

```python
bsd = BuildingSurfaceDetailed()
for key in bsd.schema['fields']:
    bsd[key] = idf.buildingsurfacedetaileds[0][key]
bsd.extensibles = idf.buildingsurfacedetaileds[0].extensibles
bsd.name = "test"

idf.add(bsd)
```