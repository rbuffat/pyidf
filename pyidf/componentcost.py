from collections import OrderedDict

class ComponentCostAdjustments(object):
    """ Corresponds to IDD object `ComponentCost:Adjustments`
        Used to perform various modifications to the construction costs to arrive at an
        estimate for total project costs. This object allows extending the line item model
        so that the overall costs of the project will reflect various profit and fees.
    """
    internal_name = "ComponentCost:Adjustments"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ComponentCost:Adjustments`
        """
        self._data = OrderedDict()
        self._data["Miscellaneous Cost per Conditioned Area"] = None
        self._data["Design and Engineering Fees"] = None
        self._data["Contractor Fee"] = None
        self._data["Contingency"] = None
        self._data["Permits, Bonding and Insurance"] = None
        self._data["Commissioning Fee"] = None
        self._data["Regional Adjustment Factor"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.miscellaneous_cost_per_conditioned_area = None
        else:
            self.miscellaneous_cost_per_conditioned_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_and_engineering_fees = None
        else:
            self.design_and_engineering_fees = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.contractor_fee = None
        else:
            self.contractor_fee = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.contingency = None
        else:
            self.contingency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.permits_bonding_and_insurance = None
        else:
            self.permits_bonding_and_insurance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.commissioning_fee = None
        else:
            self.commissioning_fee = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.regional_adjustment_factor = None
        else:
            self.regional_adjustment_factor = vals[i]
        i += 1

    @property
    def miscellaneous_cost_per_conditioned_area(self):
        """Get miscellaneous_cost_per_conditioned_area

        Returns:
            float: the value of `miscellaneous_cost_per_conditioned_area` or None if not set
        """
        return self._data["Miscellaneous Cost per Conditioned Area"]

    @miscellaneous_cost_per_conditioned_area.setter
    def miscellaneous_cost_per_conditioned_area(self, value=None):
        """  Corresponds to IDD Field `miscellaneous_cost_per_conditioned_area`
        based on conditioned floor area
        for cost not accounted for in current line item cost model

        Args:
            value (float): value for IDD Field `miscellaneous_cost_per_conditioned_area`
                Unit: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `miscellaneous_cost_per_conditioned_area`'.format(value))

        self._data["Miscellaneous Cost per Conditioned Area"] = value

    @property
    def design_and_engineering_fees(self):
        """Get design_and_engineering_fees

        Returns:
            float: the value of `design_and_engineering_fees` or None if not set
        """
        return self._data["Design and Engineering Fees"]

    @design_and_engineering_fees.setter
    def design_and_engineering_fees(self, value=None):
        """  Corresponds to IDD Field `design_and_engineering_fees`

        Args:
            value (float): value for IDD Field `design_and_engineering_fees`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_and_engineering_fees`'.format(value))

        self._data["Design and Engineering Fees"] = value

    @property
    def contractor_fee(self):
        """Get contractor_fee

        Returns:
            float: the value of `contractor_fee` or None if not set
        """
        return self._data["Contractor Fee"]

    @contractor_fee.setter
    def contractor_fee(self, value=None):
        """  Corresponds to IDD Field `contractor_fee`

        Args:
            value (float): value for IDD Field `contractor_fee`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `contractor_fee`'.format(value))

        self._data["Contractor Fee"] = value

    @property
    def contingency(self):
        """Get contingency

        Returns:
            float: the value of `contingency` or None if not set
        """
        return self._data["Contingency"]

    @contingency.setter
    def contingency(self, value=None):
        """  Corresponds to IDD Field `contingency`

        Args:
            value (float): value for IDD Field `contingency`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `contingency`'.format(value))

        self._data["Contingency"] = value

    @property
    def permits_bonding_and_insurance(self):
        """Get permits_bonding_and_insurance

        Returns:
            float: the value of `permits_bonding_and_insurance` or None if not set
        """
        return self._data["Permits, Bonding and Insurance"]

    @permits_bonding_and_insurance.setter
    def permits_bonding_and_insurance(self, value=None):
        """  Corresponds to IDD Field `permits_bonding_and_insurance`

        Args:
            value (float): value for IDD Field `permits_bonding_and_insurance`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `permits_bonding_and_insurance`'.format(value))

        self._data["Permits, Bonding and Insurance"] = value

    @property
    def commissioning_fee(self):
        """Get commissioning_fee

        Returns:
            float: the value of `commissioning_fee` or None if not set
        """
        return self._data["Commissioning Fee"]

    @commissioning_fee.setter
    def commissioning_fee(self, value=None):
        """  Corresponds to IDD Field `commissioning_fee`

        Args:
            value (float): value for IDD Field `commissioning_fee`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `commissioning_fee`'.format(value))

        self._data["Commissioning Fee"] = value

    @property
    def regional_adjustment_factor(self):
        """Get regional_adjustment_factor

        Returns:
            float: the value of `regional_adjustment_factor` or None if not set
        """
        return self._data["Regional Adjustment Factor"]

    @regional_adjustment_factor.setter
    def regional_adjustment_factor(self, value=None):
        """  Corresponds to IDD Field `regional_adjustment_factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `regional_adjustment_factor`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `regional_adjustment_factor`'.format(value))

        self._data["Regional Adjustment Factor"] = value

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
        out.append(self._to_str(self.miscellaneous_cost_per_conditioned_area))
        out.append(self._to_str(self.design_and_engineering_fees))
        out.append(self._to_str(self.contractor_fee))
        out.append(self._to_str(self.contingency))
        out.append(self._to_str(self.permits_bonding_and_insurance))
        out.append(self._to_str(self.commissioning_fee))
        out.append(self._to_str(self.regional_adjustment_factor))
        return ",".join(out)

class ComponentCostReference(object):
    """ Corresponds to IDD object `ComponentCost:Reference`
        Used to allow comparing the current cost estimate to the results of a previous
        estimate for a reference building. This object parallels the ComponentCost:Adjustments
        object but adds a field for entering the cost line item model result for the reference
        building. The factors entered in this object are applied to the reference building
        while the factors listed in the ComponentCost:Adjustments object are applied to the
        current building model cost estimate.
    """
    internal_name = "ComponentCost:Reference"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ComponentCost:Reference`
        """
        self._data = OrderedDict()
        self._data["Reference Building Line Item Costs"] = None
        self._data["Reference Building Miscellaneous Cost per Conditioned Area"] = None
        self._data["Reference Building Design and Engineering Fees"] = None
        self._data["Reference Building Contractor Fee"] = None
        self._data["Reference Building Contingency"] = None
        self._data["Reference Building Permits, Bonding and Insurance"] = None
        self._data["Reference Building Commissioning Fee"] = None
        self._data["Reference Building Regional Adjustment Factor"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.reference_building_line_item_costs = None
        else:
            self.reference_building_line_item_costs = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_miscellaneous_cost_per_conditioned_area = None
        else:
            self.reference_building_miscellaneous_cost_per_conditioned_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_design_and_engineering_fees = None
        else:
            self.reference_building_design_and_engineering_fees = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_contractor_fee = None
        else:
            self.reference_building_contractor_fee = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_contingency = None
        else:
            self.reference_building_contingency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_permits_bonding_and_insurance = None
        else:
            self.reference_building_permits_bonding_and_insurance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_commissioning_fee = None
        else:
            self.reference_building_commissioning_fee = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_building_regional_adjustment_factor = None
        else:
            self.reference_building_regional_adjustment_factor = vals[i]
        i += 1

    @property
    def reference_building_line_item_costs(self):
        """Get reference_building_line_item_costs

        Returns:
            float: the value of `reference_building_line_item_costs` or None if not set
        """
        return self._data["Reference Building Line Item Costs"]

    @reference_building_line_item_costs.setter
    def reference_building_line_item_costs(self, value=None):
        """  Corresponds to IDD Field `reference_building_line_item_costs`
        should be comparable to the components in current line item cost model

        Args:
            value (float): value for IDD Field `reference_building_line_item_costs`
                Unit: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_line_item_costs`'.format(value))

        self._data["Reference Building Line Item Costs"] = value

    @property
    def reference_building_miscellaneous_cost_per_conditioned_area(self):
        """Get reference_building_miscellaneous_cost_per_conditioned_area

        Returns:
            float: the value of `reference_building_miscellaneous_cost_per_conditioned_area` or None if not set
        """
        return self._data["Reference Building Miscellaneous Cost per Conditioned Area"]

    @reference_building_miscellaneous_cost_per_conditioned_area.setter
    def reference_building_miscellaneous_cost_per_conditioned_area(self, value=None):
        """  Corresponds to IDD Field `reference_building_miscellaneous_cost_per_conditioned_area`
        based on conditioned floor area
        for cost not accounted for in reference line item costs

        Args:
            value (float): value for IDD Field `reference_building_miscellaneous_cost_per_conditioned_area`
                Unit: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_miscellaneous_cost_per_conditioned_area`'.format(value))

        self._data["Reference Building Miscellaneous Cost per Conditioned Area"] = value

    @property
    def reference_building_design_and_engineering_fees(self):
        """Get reference_building_design_and_engineering_fees

        Returns:
            float: the value of `reference_building_design_and_engineering_fees` or None if not set
        """
        return self._data["Reference Building Design and Engineering Fees"]

    @reference_building_design_and_engineering_fees.setter
    def reference_building_design_and_engineering_fees(self, value=None):
        """  Corresponds to IDD Field `reference_building_design_and_engineering_fees`

        Args:
            value (float): value for IDD Field `reference_building_design_and_engineering_fees`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_design_and_engineering_fees`'.format(value))

        self._data["Reference Building Design and Engineering Fees"] = value

    @property
    def reference_building_contractor_fee(self):
        """Get reference_building_contractor_fee

        Returns:
            float: the value of `reference_building_contractor_fee` or None if not set
        """
        return self._data["Reference Building Contractor Fee"]

    @reference_building_contractor_fee.setter
    def reference_building_contractor_fee(self, value=None):
        """  Corresponds to IDD Field `reference_building_contractor_fee`

        Args:
            value (float): value for IDD Field `reference_building_contractor_fee`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_contractor_fee`'.format(value))

        self._data["Reference Building Contractor Fee"] = value

    @property
    def reference_building_contingency(self):
        """Get reference_building_contingency

        Returns:
            float: the value of `reference_building_contingency` or None if not set
        """
        return self._data["Reference Building Contingency"]

    @reference_building_contingency.setter
    def reference_building_contingency(self, value=None):
        """  Corresponds to IDD Field `reference_building_contingency`

        Args:
            value (float): value for IDD Field `reference_building_contingency`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_contingency`'.format(value))

        self._data["Reference Building Contingency"] = value

    @property
    def reference_building_permits_bonding_and_insurance(self):
        """Get reference_building_permits_bonding_and_insurance

        Returns:
            float: the value of `reference_building_permits_bonding_and_insurance` or None if not set
        """
        return self._data["Reference Building Permits, Bonding and Insurance"]

    @reference_building_permits_bonding_and_insurance.setter
    def reference_building_permits_bonding_and_insurance(self, value=None):
        """  Corresponds to IDD Field `reference_building_permits_bonding_and_insurance`

        Args:
            value (float): value for IDD Field `reference_building_permits_bonding_and_insurance`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_permits_bonding_and_insurance`'.format(value))

        self._data["Reference Building Permits, Bonding and Insurance"] = value

    @property
    def reference_building_commissioning_fee(self):
        """Get reference_building_commissioning_fee

        Returns:
            float: the value of `reference_building_commissioning_fee` or None if not set
        """
        return self._data["Reference Building Commissioning Fee"]

    @reference_building_commissioning_fee.setter
    def reference_building_commissioning_fee(self, value=None):
        """  Corresponds to IDD Field `reference_building_commissioning_fee`

        Args:
            value (float): value for IDD Field `reference_building_commissioning_fee`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_commissioning_fee`'.format(value))

        self._data["Reference Building Commissioning Fee"] = value

    @property
    def reference_building_regional_adjustment_factor(self):
        """Get reference_building_regional_adjustment_factor

        Returns:
            float: the value of `reference_building_regional_adjustment_factor` or None if not set
        """
        return self._data["Reference Building Regional Adjustment Factor"]

    @reference_building_regional_adjustment_factor.setter
    def reference_building_regional_adjustment_factor(self, value=None):
        """  Corresponds to IDD Field `reference_building_regional_adjustment_factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `reference_building_regional_adjustment_factor`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_regional_adjustment_factor`'.format(value))

        self._data["Reference Building Regional Adjustment Factor"] = value

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
        out.append(self._to_str(self.reference_building_line_item_costs))
        out.append(self._to_str(self.reference_building_miscellaneous_cost_per_conditioned_area))
        out.append(self._to_str(self.reference_building_design_and_engineering_fees))
        out.append(self._to_str(self.reference_building_contractor_fee))
        out.append(self._to_str(self.reference_building_contingency))
        out.append(self._to_str(self.reference_building_permits_bonding_and_insurance))
        out.append(self._to_str(self.reference_building_commissioning_fee))
        out.append(self._to_str(self.reference_building_regional_adjustment_factor))
        return ",".join(out)

class ComponentCostLineItem(object):
    """ Corresponds to IDD object `ComponentCost:LineItem`
        Each instance of this object creates a cost line item and will contribute to the total
        for a cost estimate.
    """
    internal_name = "ComponentCost:LineItem"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ComponentCost:LineItem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Type"] = None
        self._data["Line Item Type"] = None
        self._data["Item Name"] = None
        self._data["Object End-Use Key"] = None
        self._data["Cost per Each"] = None
        self._data["Cost per Area"] = None
        self._data["Cost per Unit of Output Capacity"] = None
        self._data["Cost per Unit of Output Capacity per COP"] = None
        self._data["Cost per Volume"] = None
        self._data["Cost per Volume Rate"] = None
        self._data["Cost per Energy per Temperature Difference"] = None
        self._data["Quantity"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type = None
        else:
            self.type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.line_item_type = None
        else:
            self.line_item_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.item_name = None
        else:
            self.item_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.object_enduse_key = None
        else:
            self.object_enduse_key = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_each = None
        else:
            self.cost_per_each = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_area = None
        else:
            self.cost_per_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_unit_of_output_capacity = None
        else:
            self.cost_per_unit_of_output_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_unit_of_output_capacity_per_cop = None
        else:
            self.cost_per_unit_of_output_capacity_per_cop = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_volume = None
        else:
            self.cost_per_volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_volume_rate = None
        else:
            self.cost_per_volume_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_energy_per_temperature_difference = None
        else:
            self.cost_per_energy_per_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.quantity = None
        else:
            self.quantity = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def type(self):
        """Get type

        Returns:
            str: the value of `type` or None if not set
        """
        return self._data["Type"]

    @type.setter
    def type(self, value=None):
        """  Corresponds to IDD Field `type`

        Args:
            value (str): value for IDD Field `type`
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
                                 'for field `type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type`')

        self._data["Type"] = value

    @property
    def line_item_type(self):
        """Get line_item_type

        Returns:
            str: the value of `line_item_type` or None if not set
        """
        return self._data["Line Item Type"]

    @line_item_type.setter
    def line_item_type(self, value=None):
        """  Corresponds to IDD Field `line_item_type`
        extend choice-keys as Cases are added to code

        Args:
            value (str): value for IDD Field `line_item_type`
                Accepted values are:
                      - General
                      - Construction
                      - Coil:DX
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Heating:Gas
                      - Chiller:Electric
                      - Daylighting:Controls
                      - Shading:Zone:Detailed
                      - Lights
                      - Generator:Photovoltaic
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
                                 'for field `line_item_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `line_item_type`')
            vals = set()
            vals.add("General")
            vals.add("Construction")
            vals.add("Coil:DX")
            vals.add("Coil:Cooling:DX:SingleSpeed")
            vals.add("Coil:Heating:Gas")
            vals.add("Chiller:Electric")
            vals.add("Daylighting:Controls")
            vals.add("Shading:Zone:Detailed")
            vals.add("Lights")
            vals.add("Generator:Photovoltaic")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `line_item_type`'.format(value))

        self._data["Line Item Type"] = value

    @property
    def item_name(self):
        """Get item_name

        Returns:
            str: the value of `item_name` or None if not set
        """
        return self._data["Item Name"]

    @item_name.setter
    def item_name(self, value=None):
        """  Corresponds to IDD Field `item_name`
        wildcard "*" is acceptable for some components

        Args:
            value (str): value for IDD Field `item_name`
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
                                 'for field `item_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `item_name`')

        self._data["Item Name"] = value

    @property
    def object_enduse_key(self):
        """Get object_enduse_key

        Returns:
            str: the value of `object_enduse_key` or None if not set
        """
        return self._data["Object End-Use Key"]

    @object_enduse_key.setter
    def object_enduse_key(self, value=None):
        """  Corresponds to IDD Field `object_enduse_key`
        not yet used

        Args:
            value (str): value for IDD Field `object_enduse_key`
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
                                 'for field `object_enduse_key`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `object_enduse_key`')

        self._data["Object End-Use Key"] = value

    @property
    def cost_per_each(self):
        """Get cost_per_each

        Returns:
            float: the value of `cost_per_each` or None if not set
        """
        return self._data["Cost per Each"]

    @cost_per_each.setter
    def cost_per_each(self, value=None):
        """  Corresponds to IDD Field `cost_per_each`

        Args:
            value (float): value for IDD Field `cost_per_each`
                Unit: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_each`'.format(value))

        self._data["Cost per Each"] = value

    @property
    def cost_per_area(self):
        """Get cost_per_area

        Returns:
            float: the value of `cost_per_area` or None if not set
        """
        return self._data["Cost per Area"]

    @cost_per_area.setter
    def cost_per_area(self, value=None):
        """  Corresponds to IDD Field `cost_per_area`

        Args:
            value (float): value for IDD Field `cost_per_area`
                Unit: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_area`'.format(value))

        self._data["Cost per Area"] = value

    @property
    def cost_per_unit_of_output_capacity(self):
        """Get cost_per_unit_of_output_capacity

        Returns:
            float: the value of `cost_per_unit_of_output_capacity` or None if not set
        """
        return self._data["Cost per Unit of Output Capacity"]

    @cost_per_unit_of_output_capacity.setter
    def cost_per_unit_of_output_capacity(self, value=None):
        """  Corresponds to IDD Field `cost_per_unit_of_output_capacity`

        Args:
            value (float): value for IDD Field `cost_per_unit_of_output_capacity`
                Unit: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_unit_of_output_capacity`'.format(value))

        self._data["Cost per Unit of Output Capacity"] = value

    @property
    def cost_per_unit_of_output_capacity_per_cop(self):
        """Get cost_per_unit_of_output_capacity_per_cop

        Returns:
            float: the value of `cost_per_unit_of_output_capacity_per_cop` or None if not set
        """
        return self._data["Cost per Unit of Output Capacity per COP"]

    @cost_per_unit_of_output_capacity_per_cop.setter
    def cost_per_unit_of_output_capacity_per_cop(self, value=None):
        """  Corresponds to IDD Field `cost_per_unit_of_output_capacity_per_cop`
        The value is per change in COP.

        Args:
            value (float): value for IDD Field `cost_per_unit_of_output_capacity_per_cop`
                Unit: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_unit_of_output_capacity_per_cop`'.format(value))

        self._data["Cost per Unit of Output Capacity per COP"] = value

    @property
    def cost_per_volume(self):
        """Get cost_per_volume

        Returns:
            float: the value of `cost_per_volume` or None if not set
        """
        return self._data["Cost per Volume"]

    @cost_per_volume.setter
    def cost_per_volume(self, value=None):
        """  Corresponds to IDD Field `cost_per_volume`

        Args:
            value (float): value for IDD Field `cost_per_volume`
                Unit: $/m3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_volume`'.format(value))

        self._data["Cost per Volume"] = value

    @property
    def cost_per_volume_rate(self):
        """Get cost_per_volume_rate

        Returns:
            float: the value of `cost_per_volume_rate` or None if not set
        """
        return self._data["Cost per Volume Rate"]

    @cost_per_volume_rate.setter
    def cost_per_volume_rate(self, value=None):
        """  Corresponds to IDD Field `cost_per_volume_rate`

        Args:
            value (float): value for IDD Field `cost_per_volume_rate`
                Unit: $/(m3/s)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_volume_rate`'.format(value))

        self._data["Cost per Volume Rate"] = value

    @property
    def cost_per_energy_per_temperature_difference(self):
        """Get cost_per_energy_per_temperature_difference

        Returns:
            float: the value of `cost_per_energy_per_temperature_difference` or None if not set
        """
        return self._data["Cost per Energy per Temperature Difference"]

    @cost_per_energy_per_temperature_difference.setter
    def cost_per_energy_per_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `cost_per_energy_per_temperature_difference`
        as in for use with UA sizing of Coils

        Args:
            value (float): value for IDD Field `cost_per_energy_per_temperature_difference`
                Unit: $/(W/K)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cost_per_energy_per_temperature_difference`'.format(value))

        self._data["Cost per Energy per Temperature Difference"] = value

    @property
    def quantity(self):
        """Get quantity

        Returns:
            float: the value of `quantity` or None if not set
        """
        return self._data["Quantity"]

    @quantity.setter
    def quantity(self, value=None):
        """  Corresponds to IDD Field `quantity`
        optional for use with Cost per Each and "General" object Type

        Args:
            value (float): value for IDD Field `quantity`
                Unit: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `quantity`'.format(value))

        self._data["Quantity"] = value

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
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.type))
        out.append(self._to_str(self.line_item_type))
        out.append(self._to_str(self.item_name))
        out.append(self._to_str(self.object_enduse_key))
        out.append(self._to_str(self.cost_per_each))
        out.append(self._to_str(self.cost_per_area))
        out.append(self._to_str(self.cost_per_unit_of_output_capacity))
        out.append(self._to_str(self.cost_per_unit_of_output_capacity_per_cop))
        out.append(self._to_str(self.cost_per_volume))
        out.append(self._to_str(self.cost_per_volume_rate))
        out.append(self._to_str(self.cost_per_energy_per_temperature_difference))
        out.append(self._to_str(self.quantity))
        return ",".join(out)