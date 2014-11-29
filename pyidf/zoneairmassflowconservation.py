from collections import OrderedDict

class ZoneAirMassFlowConservation(object):
    """ Corresponds to IDD object `ZoneAirMassFlowConservation`
        Enforces the zone air mass flow balance by adjusting zone mixing object flow rates.
        The infiltration object mass flow rate may also be adjusted or may add infiltration
        air flow to the base infiltration air flow for source zones only.
    """
    internal_name = "ZoneAirMassFlowConservation"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneAirMassFlowConservation`
        """
        self._data = OrderedDict()
        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = None
        self._data["Source Zone Infiltration Treatment"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = None
        else:
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_zone_infiltration_treatment = None
        else:
            self.source_zone_infiltration_treatment = vals[i]
        i += 1

    @property
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self):
        """Get adjust_zone_mixing_for_zone_air_mass_flow_balance

        Returns:
            str: the value of `adjust_zone_mixing_for_zone_air_mass_flow_balance` or None if not set
        """
        return self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"]

    @adjust_zone_mixing_for_zone_air_mass_flow_balance.setter
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self, value="No"):
        """  Corresponds to IDD Field `adjust_zone_mixing_for_zone_air_mass_flow_balance`
        If Yes, Zone mixing object flow rates are adjusted to balance the zone air mass flow
        and additional infiltration air flow may be added if required in order to balance the
        zone air mass flow.
        This optional choice input field allows users triggering the zone air mass flow
        balance calculation when desired. This global object has two choice KEYs: Yes and
        No. If this input field is specified as Yes, then EnergyPlus attempts to enforce
        the zone air mass flow conservation, or else if it is specified as No, then EnergyPlus
        calculation defaults to zone air mass flow balance that does not include zone mixing
        objects and that assumes self-balanced simple flow objects per the default procedure,
        which may not necessarily enforce zone mass conservation unless the user specified
        a balanced flow to begin with. Mass conservation is enforced both for the receiving
        and source zones if there is at least one mixing object defined. The default input
        is No. (Note that No input may also results in balanced flow depending on the
        system specified).

        Args:
            value (str): value for IDD Field `adjust_zone_mixing_for_zone_air_mass_flow_balance`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `adjust_zone_mixing_for_zone_air_mass_flow_balance`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))

        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = value

    @property
    def source_zone_infiltration_treatment(self):
        """Get source_zone_infiltration_treatment

        Returns:
            str: the value of `source_zone_infiltration_treatment` or None if not set
        """
        return self._data["Source Zone Infiltration Treatment"]

    @source_zone_infiltration_treatment.setter
    def source_zone_infiltration_treatment(self, value="AddInfiltrationFlow"):
        """  Corresponds to IDD Field `source_zone_infiltration_treatment`
        This input field allows user to choose how zone infiltration flow is treated during
        the zone air mass flow balance calculation.
        It has two choice KEYs: AddInfiltrationFlow and AdjustInfiltrationFlow.  If this
        input is specified as AddInfiltrationFlow, then energy plus adds infiltration air
        mass flow on top of the base flow, which is calculated using the infiltration object
        user inputs, in order to balance the zone air mass flow.  The additional infiltration
        air mass flow is not self-balanced.  If this input is specified as
        AdjustInfiltrationFlow, then energy plus may adjust the base flow calculated using
        the infiltration object user inputs in order to balance the zone air mass flow. If it
        is not required to adjust the base infiltration air flow calculated from the user
        specified infiltration object inputs, then the base infiltration air mass flow
        is assumed self-balanced. If the above input field specified as "No", then this input
        field has no impact on the simulation.

        Args:
            value (str): value for IDD Field `source_zone_infiltration_treatment`
                Accepted values are:
                      - AddInfiltrationFlow
                      - AdjustInfiltrationFlow
                Default value: AddInfiltrationFlow
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_zone_infiltration_treatment`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_zone_infiltration_treatment`')
            vals = set()
            vals.add("AddInfiltrationFlow")
            vals.add("AdjustInfiltrationFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `source_zone_infiltration_treatment`'.format(value))

        self._data["Source Zone Infiltration Treatment"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.adjust_zone_mixing_for_zone_air_mass_flow_balance))
        out.append(self._to_str(self.source_zone_infiltration_treatment))
        return ",".join(out)