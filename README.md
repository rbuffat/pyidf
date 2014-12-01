#pyidf

Python library to read, modify and create EnergyPlus idf files


*This is a work in progress, do NOT expect it to actually work! As this is an early work, changes in the API are very likely to happen.*

##Todos:


* write support
* unit tests
* field comments not implemented:
  * begin-extensible
  * unitsBasedOnField
  * type: object-list, external-list, node
  * retaincase
  * object-list
  * external-list
  * reference
* object level comments not yet implemented
  * min-fields
  * obsolete
  * extensible
  * begin-extensible
  * format
  * reference-class-name

Currently ignored objects (begin-extensible and lists not yet supported):
* Schedule:Day:List
* Schedule:Year
* Schedule:Compact
* MaterialProperty:GlazingSpectralData
* ZoneList
* GroundHeatTransfer:Slab:XFACE
* GroundHeatTransfer:Slab:YFACE
* GroundHeatTransfer:Slab:ZFACE
* GroundHeatTransfer:Basement:XFACE
* GroundHeatTransfer:Basement:YFACE
* GroundHeatTransfer:Basement:ZFACE
* EvaporativeCooler:Direct:CelDekPad
* EvaporativeCooler:Indirect:CelDekPad
* EvaporativeCooler:Indirect:WetCoil
* EvaporativeCooler:Indirect:ResearchSpecial
* EvaporativeCooler:Direct:ResearchSpecial
* AirLoopHVAC:ZoneSplitter
* AirLoopHVAC:SupplyPlenum
* AirLoopHVAC:ZoneMixer
* AirLoopHVAC:ReturnPlenum
* BranchList
* Connector:Splitter
* Connector:Mixer
* NodeList
* OutdoorAir:NodeList
* HeaderedPumps:VariableSpeed
* SolarCollector:FlatPlate:PhotovoltaicThermal
* EnergyManagementSystem:Program
* EnergyManagementSystem:Subroutine
* EnergyManagementSystem:GlobalVariable
* ZoneHVAC:RefrigerationChillerSet
* Matrix:TwoDimension
* Table:OneIndependentVariable
* Table:TwoIndependentVariables
* Table:MultiVariableLookup