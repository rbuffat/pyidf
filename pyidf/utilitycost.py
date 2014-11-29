from collections import OrderedDict

class UtilityCostTariff(object):
    """ Corresponds to IDD object `UtilityCost:Tariff`
        Defines the name of a utility cost tariff, the type of tariff, and other details
        about the overall tariff. Each other object that is part of the tariff model
        references the tariff name.  See UtilityCost:Charge:Simple, UtilityCost:Charge:Block,
        UtilityCost:Ratchet, UtilityCost:Qualify, UtilityCost:Variable and
        UtilityCost:Computation objects.
    """
    internal_name = "UtilityCost:Tariff"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Tariff`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Output Meter Name"] = None
        self._data["Conversion Factor Choice"] = None
        self._data["Energy Conversion Factor"] = None
        self._data["Demand Conversion Factor"] = None
        self._data["Time of Use Period Schedule Name"] = None
        self._data["Season Schedule Name"] = None
        self._data["Month Schedule Name"] = None
        self._data["Demand Window Length"] = None
        self._data["Monthly Charge or Variable Name"] = None
        self._data["Minimum Monthly Charge or Variable Name"] = None
        self._data["Real Time Pricing Charge Schedule Name"] = None
        self._data["Customer Baseline Load Schedule Name"] = None
        self._data["Group Name"] = None
        self._data["Buy Or Sell"] = None

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
            self.output_meter_name = None
        else:
            self.output_meter_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conversion_factor_choice = None
        else:
            self.conversion_factor_choice = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.energy_conversion_factor = None
        else:
            self.energy_conversion_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_conversion_factor = None
        else:
            self.demand_conversion_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.time_of_use_period_schedule_name = None
        else:
            self.time_of_use_period_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season_schedule_name = None
        else:
            self.season_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.month_schedule_name = None
        else:
            self.month_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_window_length = None
        else:
            self.demand_window_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.monthly_charge_or_variable_name = None
        else:
            self.monthly_charge_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_monthly_charge_or_variable_name = None
        else:
            self.minimum_monthly_charge_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.real_time_pricing_charge_schedule_name = None
        else:
            self.real_time_pricing_charge_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.customer_baseline_load_schedule_name = None
        else:
            self.customer_baseline_load_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.group_name = None
        else:
            self.group_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.buy_or_sell = None
        else:
            self.buy_or_sell = vals[i]
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
        The name of the tariff. Tariffs are sometimes called rates. The name is used in identifying
        the output results and in associating all of the charges and other objects that make up a tariff.

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
    def output_meter_name(self):
        """Get output_meter_name

        Returns:
            str: the value of `output_meter_name` or None if not set
        """
        return self._data["Output Meter Name"]

    @output_meter_name.setter
    def output_meter_name(self, value=None):
        """  Corresponds to IDD Field `output_meter_name`
        The name of any standard meter or custom meter or but usually set to either Electricity:Facility or Gas:Facility

        Args:
            value (str): value for IDD Field `output_meter_name`
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
                                 'for field `output_meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_meter_name`')

        self._data["Output Meter Name"] = value

    @property
    def conversion_factor_choice(self):
        """Get conversion_factor_choice

        Returns:
            str: the value of `conversion_factor_choice` or None if not set
        """
        return self._data["Conversion Factor Choice"]

    @conversion_factor_choice.setter
    def conversion_factor_choice(self, value=None):
        """  Corresponds to IDD Field `conversion_factor_choice`
        A choice that allows several different predefined conversion factors to be used; otherwise user
        defined conversion factors are used as defined in the next two fields.

        Args:
            value (str): value for IDD Field `conversion_factor_choice`
                Accepted values are:
                      - UserDefined
                      - kWh
                      - Therm
                      - MMBtu
                      - MJ
                      - kBtu
                      - MCF
                      - CCF
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
                                 'for field `conversion_factor_choice`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `conversion_factor_choice`')
            vals = set()
            vals.add("UserDefined")
            vals.add("kWh")
            vals.add("Therm")
            vals.add("MMBtu")
            vals.add("MJ")
            vals.add("kBtu")
            vals.add("MCF")
            vals.add("CCF")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `conversion_factor_choice`'.format(value))

        self._data["Conversion Factor Choice"] = value

    @property
    def energy_conversion_factor(self):
        """Get energy_conversion_factor

        Returns:
            float: the value of `energy_conversion_factor` or None if not set
        """
        return self._data["Energy Conversion Factor"]

    @energy_conversion_factor.setter
    def energy_conversion_factor(self, value=None):
        """  Corresponds to IDD Field `energy_conversion_factor`
        Is a multiplier used to convert energy into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion). This field should will be used only if Conversion Factor
        Choice is set to UserDefined.  Within EnergyPlus energy always has units of J (joules).  For
        conversion from J to kWh use the value of 0.0000002778. This is also used for all objects that
        reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `energy_conversion_factor`
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
                                 'for field `energy_conversion_factor`'.format(value))

        self._data["Energy Conversion Factor"] = value

    @property
    def demand_conversion_factor(self):
        """Get demand_conversion_factor

        Returns:
            float: the value of `demand_conversion_factor` or None if not set
        """
        return self._data["Demand Conversion Factor"]

    @demand_conversion_factor.setter
    def demand_conversion_factor(self, value=None):
        """  Corresponds to IDD Field `demand_conversion_factor`
        Is a multiplier used to convert demand into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion).  This field should will be used only if Conversion
        Factor Choice is set to UserDefined.  Within EnergyPlus demand always has units of J/s (joules/sec)
        which equivalent to W (watts).  For conversion from W to kW use the value of 0.001. This is also used
        for all objects that reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `demand_conversion_factor`
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
                                 'for field `demand_conversion_factor`'.format(value))

        self._data["Demand Conversion Factor"] = value

    @property
    def time_of_use_period_schedule_name(self):
        """Get time_of_use_period_schedule_name

        Returns:
            str: the value of `time_of_use_period_schedule_name` or None if not set
        """
        return self._data["Time of Use Period Schedule Name"]

    @time_of_use_period_schedule_name.setter
    def time_of_use_period_schedule_name(self, value=None):
        """  Corresponds to IDD Field `time_of_use_period_schedule_name`
        The name of the schedule that defines the time-of-use periods that occur each day. The values for the
        different variables are: 1 for Peak. 2 for Shoulder. 3 for OffPeak. 4 for MidPeak.

        Args:
            value (str): value for IDD Field `time_of_use_period_schedule_name`
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
                                 'for field `time_of_use_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_of_use_period_schedule_name`')

        self._data["Time of Use Period Schedule Name"] = value

    @property
    def season_schedule_name(self):
        """Get season_schedule_name

        Returns:
            str: the value of `season_schedule_name` or None if not set
        """
        return self._data["Season Schedule Name"]

    @season_schedule_name.setter
    def season_schedule_name(self, value=None):
        """  Corresponds to IDD Field `season_schedule_name`
        The name of a schedule that defines the seasons.  The schedule values are: 1 for Winter. 2 for Spring.
        3 for Summer. 4 for Autumn.

        Args:
            value (str): value for IDD Field `season_schedule_name`
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
                                 'for field `season_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_schedule_name`')

        self._data["Season Schedule Name"] = value

    @property
    def month_schedule_name(self):
        """Get month_schedule_name

        Returns:
            str: the value of `month_schedule_name` or None if not set
        """
        return self._data["Month Schedule Name"]

    @month_schedule_name.setter
    def month_schedule_name(self, value=None):
        """  Corresponds to IDD Field `month_schedule_name`
        The name of the schedule that defines the billing periods of the year. Normally this entry is allowed
        to default and a schedule will be internally used that has the breaks between billing periods occurring
        at the same time as the breaks between months i.e. at midnight prior to the first day of the month.
        If other billing periods are used such as two month cycles or a single bill for an entire season such
        as some natural gas companies do in the summer then the month schedule may be used to redefine it.
        Make sure that the month schedule and season schedule are consistent otherwise an error will be issued.

        Args:
            value (str): value for IDD Field `month_schedule_name`
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
                                 'for field `month_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `month_schedule_name`')

        self._data["Month Schedule Name"] = value

    @property
    def demand_window_length(self):
        """Get demand_window_length

        Returns:
            str: the value of `demand_window_length` or None if not set
        """
        return self._data["Demand Window Length"]

    @demand_window_length.setter
    def demand_window_length(self, value=None):
        """  Corresponds to IDD Field `demand_window_length`
        The determination of demand can vary by utility. Some utilities use the peak instantaneous demand
        measured but most use a fifteen minute average demand or a one hour average demand. Some gas utilities
        measure demand as the use during the peak day or peak week.

        Args:
            value (str): value for IDD Field `demand_window_length`
                Accepted values are:
                      - QuarterHour
                      - HalfHour
                      - FullHour
                      - Day
                      - Week
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
                                 'for field `demand_window_length`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_window_length`')
            vals = set()
            vals.add("QuarterHour")
            vals.add("HalfHour")
            vals.add("FullHour")
            vals.add("Day")
            vals.add("Week")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `demand_window_length`'.format(value))

        self._data["Demand Window Length"] = value

    @property
    def monthly_charge_or_variable_name(self):
        """Get monthly_charge_or_variable_name

        Returns:
            str: the value of `monthly_charge_or_variable_name` or None if not set
        """
        return self._data["Monthly Charge or Variable Name"]

    @monthly_charge_or_variable_name.setter
    def monthly_charge_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `monthly_charge_or_variable_name`
        The fixed monthly service charge that many utilities have.  The entry may be numeric and gets added to
        the ServiceCharges variable or if a variable name is entered here its values for each month are used.

        Args:
            value (str): value for IDD Field `monthly_charge_or_variable_name`
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
                                 'for field `monthly_charge_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `monthly_charge_or_variable_name`')

        self._data["Monthly Charge or Variable Name"] = value

    @property
    def minimum_monthly_charge_or_variable_name(self):
        """Get minimum_monthly_charge_or_variable_name

        Returns:
            str: the value of `minimum_monthly_charge_or_variable_name` or None if not set
        """
        return self._data["Minimum Monthly Charge or Variable Name"]

    @minimum_monthly_charge_or_variable_name.setter
    def minimum_monthly_charge_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `minimum_monthly_charge_or_variable_name`
        The minimum total charge for the tariff or if a variable name is entered here its
        values for each month are used.

        Args:
            value (str): value for IDD Field `minimum_monthly_charge_or_variable_name`
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
                                 'for field `minimum_monthly_charge_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_monthly_charge_or_variable_name`')

        self._data["Minimum Monthly Charge or Variable Name"] = value

    @property
    def real_time_pricing_charge_schedule_name(self):
        """Get real_time_pricing_charge_schedule_name

        Returns:
            str: the value of `real_time_pricing_charge_schedule_name` or None if not set
        """
        return self._data["Real Time Pricing Charge Schedule Name"]

    @real_time_pricing_charge_schedule_name.setter
    def real_time_pricing_charge_schedule_name(self, value=None):
        """  Corresponds to IDD Field `real_time_pricing_charge_schedule_name`
        Used with real time pricing rates. The name of a schedule that contains the cost of
        energy for that particular time period of the year. Real time rates can be modeled using a charge
        schedule with the actual real time prices entered in the schedule.

        Args:
            value (str): value for IDD Field `real_time_pricing_charge_schedule_name`
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
                                 'for field `real_time_pricing_charge_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `real_time_pricing_charge_schedule_name`')

        self._data["Real Time Pricing Charge Schedule Name"] = value

    @property
    def customer_baseline_load_schedule_name(self):
        """Get customer_baseline_load_schedule_name

        Returns:
            str: the value of `customer_baseline_load_schedule_name` or None if not set
        """
        return self._data["Customer Baseline Load Schedule Name"]

    @customer_baseline_load_schedule_name.setter
    def customer_baseline_load_schedule_name(self, value=None):
        """  Corresponds to IDD Field `customer_baseline_load_schedule_name`
        Used with real time pricing rates. The name of a schedule that contains the baseline
        energy use for the customer. Many real time rates apply the charges as a credit or debit only to the
        difference between the baseline use and the actual use.

        Args:
            value (str): value for IDD Field `customer_baseline_load_schedule_name`
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
                                 'for field `customer_baseline_load_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `customer_baseline_load_schedule_name`')

        self._data["Customer Baseline Load Schedule Name"] = value

    @property
    def group_name(self):
        """Get group_name

        Returns:
            str: the value of `group_name` or None if not set
        """
        return self._data["Group Name"]

    @group_name.setter
    def group_name(self, value=None):
        """  Corresponds to IDD Field `group_name`
        The group name of the tariff such as distribution transmission supplier etc. If more than one tariff
        with the same group name is present and qualifies only the lowest cost tariff is used. Usually the group
        name field is left blank which results in all tariffs using the same meter variable being compared and
        the lowest cost one being selected.

        Args:
            value (str): value for IDD Field `group_name`
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
                                 'for field `group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `group_name`')

        self._data["Group Name"] = value

    @property
    def buy_or_sell(self):
        """Get buy_or_sell

        Returns:
            str: the value of `buy_or_sell` or None if not set
        """
        return self._data["Buy Or Sell"]

    @buy_or_sell.setter
    def buy_or_sell(self, value="BuyFromUtility"):
        """  Corresponds to IDD Field `buy_or_sell`
        Sets whether the tariff is used for buying selling or both to the utility.  This
        should be allowed to default to buyFromUtility unless a power generation system is included in the
        building that may generate more power than the building needs during the year

        Args:
            value (str): value for IDD Field `buy_or_sell`
                Accepted values are:
                      - BuyFromUtility
                      - SellToUtility
                      - NetMetering
                Default value: BuyFromUtility
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
                                 'for field `buy_or_sell`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `buy_or_sell`')
            vals = set()
            vals.add("BuyFromUtility")
            vals.add("SellToUtility")
            vals.add("NetMetering")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `buy_or_sell`'.format(value))

        self._data["Buy Or Sell"] = value

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
        out.append(self._to_str(self.output_meter_name))
        out.append(self._to_str(self.conversion_factor_choice))
        out.append(self._to_str(self.energy_conversion_factor))
        out.append(self._to_str(self.demand_conversion_factor))
        out.append(self._to_str(self.time_of_use_period_schedule_name))
        out.append(self._to_str(self.season_schedule_name))
        out.append(self._to_str(self.month_schedule_name))
        out.append(self._to_str(self.demand_window_length))
        out.append(self._to_str(self.monthly_charge_or_variable_name))
        out.append(self._to_str(self.minimum_monthly_charge_or_variable_name))
        out.append(self._to_str(self.real_time_pricing_charge_schedule_name))
        out.append(self._to_str(self.customer_baseline_load_schedule_name))
        out.append(self._to_str(self.group_name))
        out.append(self._to_str(self.buy_or_sell))
        return ",".join(out)

class UtilityCostQualify(object):
    """ Corresponds to IDD object `UtilityCost:Qualify`
        The qualify object allows only tariffs to be selected based on limits which may apply
        such as maximum or minimum demand requirements. If the results of the simulation fall
        outside of the range of qualifications, that tariff is still calculated but the
        "Qualified" entry will say "No" and the UtilityCost:Qualify that caused its exclusion
        is shown. Multiple UtilityCost:Qualify objects can appear for the same tarriff and
        they can be based on any variable.
    """
    internal_name = "UtilityCost:Qualify"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Qualify`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Variable Name"] = None
        self._data["Qualify Type"] = None
        self._data["Threshold Value or Variable Name"] = None
        self._data["Season"] = None
        self._data["Threshold Test"] = None
        self._data["Number of Months"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.variable_name = None
        else:
            self.variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.qualify_type = None
        else:
            self.qualify_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.threshold_value_or_variable_name = None
        else:
            self.threshold_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.threshold_test = None
        else:
            self.threshold_test = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_months = None
        else:
            self.number_of_months = vals[i]
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
        Displayed in the report if the tariff does not qualify

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Qualify.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def variable_name(self):
        """Get variable_name

        Returns:
            str: the value of `variable_name` or None if not set
        """
        return self._data["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """  Corresponds to IDD Field `variable_name`
        The name of the variable used. For energy and demand the automatically created variables totalEnergy
        and totalDemand should be used respectively.

        Args:
            value (str): value for IDD Field `variable_name`
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
                                 'for field `variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `variable_name`')

        self._data["Variable Name"] = value

    @property
    def qualify_type(self):
        """Get qualify_type

        Returns:
            str: the value of `qualify_type` or None if not set
        """
        return self._data["Qualify Type"]

    @qualify_type.setter
    def qualify_type(self, value="Maximum"):
        """  Corresponds to IDD Field `qualify_type`

        Args:
            value (str): value for IDD Field `qualify_type`
                Accepted values are:
                      - Minimum
                      - Maximum
                Default value: Maximum
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
                                 'for field `qualify_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `qualify_type`')
            vals = set()
            vals.add("Minimum")
            vals.add("Maximum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `qualify_type`'.format(value))

        self._data["Qualify Type"] = value

    @property
    def threshold_value_or_variable_name(self):
        """Get threshold_value_or_variable_name

        Returns:
            str: the value of `threshold_value_or_variable_name` or None if not set
        """
        return self._data["Threshold Value or Variable Name"]

    @threshold_value_or_variable_name.setter
    def threshold_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `threshold_value_or_variable_name`
        The minimum or maximum value for the qualify. If the variable has values that are less than this value
        when the qualify type is minimum then the tariff may be disqualified.  If the variable has values that
        are greater than this value when the qualify type is maximum then the tariff may be disqualified.

        Args:
            value (str): value for IDD Field `threshold_value_or_variable_name`
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
                                 'for field `threshold_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `threshold_value_or_variable_name`')

        self._data["Threshold Value or Variable Name"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value=None):
        """  Corresponds to IDD Field `season`
        If the UtilityCost:Qualify only applies to a season enter the season name. If this field is left blank
        it defaults to Annual.

        Args:
            value (str): value for IDD Field `season`
                Accepted values are:
                      - Annual
                      - Summer
                      - Winter
                      - Spring
                      - Fall
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
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            vals = set()
            vals.add("Annual")
            vals.add("Summer")
            vals.add("Winter")
            vals.add("Spring")
            vals.add("Fall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `season`'.format(value))

        self._data["Season"] = value

    @property
    def threshold_test(self):
        """Get threshold_test

        Returns:
            str: the value of `threshold_test` or None if not set
        """
        return self._data["Threshold Test"]

    @threshold_test.setter
    def threshold_test(self, value="Consecutive"):
        """  Corresponds to IDD Field `threshold_test`
        Uses the number in Number of Months in one of two different ways depending on the Threshold  Test. If
        the Threshold Test is set to Count then the qualification is based on the count of the total number
        of months per year.  If the Threshold Test is set to consecutive then the qualification is based on
        a consecutive number of months.

        Args:
            value (str): value for IDD Field `threshold_test`
                Accepted values are:
                      - Count
                      - Consecutive
                Default value: Consecutive
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
                                 'for field `threshold_test`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `threshold_test`')
            vals = set()
            vals.add("Count")
            vals.add("Consecutive")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `threshold_test`'.format(value))

        self._data["Threshold Test"] = value

    @property
    def number_of_months(self):
        """Get number_of_months

        Returns:
            float: the value of `number_of_months` or None if not set
        """
        return self._data["Number of Months"]

    @number_of_months.setter
    def number_of_months(self, value=None):
        """  Corresponds to IDD Field `number_of_months`
        A number from 1 to 12.  If no value entered 12 is assumed when the qualify type is minimum and 1 when
        the qualify type is maximum.  This is the number of months that the threshold test applies to determine
        if the rate qualifies or not.  If the season is less than 12 months (if it is not annual) then the
        value is automatically reduced to the number of months of the seaon.

        Args:
            value (float): value for IDD Field `number_of_months`
                value >= 1.0
                value <= 12.0
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
                                 'for field `number_of_months`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `number_of_months`')
            if value > 12.0:
                raise ValueError('value need to be smaller 12.0 '
                                 'for field `number_of_months`')

        self._data["Number of Months"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.variable_name))
        out.append(self._to_str(self.qualify_type))
        out.append(self._to_str(self.threshold_value_or_variable_name))
        out.append(self._to_str(self.season))
        out.append(self._to_str(self.threshold_test))
        out.append(self._to_str(self.number_of_months))
        return ",".join(out)

class UtilityCostChargeSimple(object):
    """ Corresponds to IDD object `UtilityCost:Charge:Simple`
        UtilityCost:Charge:Simple is one of the most often used objects for tariff
        calculation. It is used to compute energy and demand charges that are very simple.
        It may also be used for taxes, surcharges and any other charges that occur on a
        utility bill. Multiple UtilityCost:Charge:Simple objects may be defined for a single
        tariff and they will be added together.
    """
    internal_name = "UtilityCost:Charge:Simple"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Charge:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Source Variable"] = None
        self._data["Season"] = None
        self._data["Category Variable Name"] = None
        self._data["Cost per Unit Value or Variable Name"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_variable = None
        else:
            self.source_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.category_variable_name = None
        else:
            self.category_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost_per_unit_value_or_variable_name = None
        else:
            self.cost_per_unit_value_or_variable_name = vals[i]
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
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Simple object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Simple calculation are stored in a variable with the
        same name.  That way the results may be used for further calculation.  Spaces are not significant in
        Charge variable names. They are removed during the utility bill calculation process.

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Simple.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def source_variable(self):
        """Get source_variable

        Returns:
            str: the value of `source_variable` or None if not set
        """
        return self._data["Source Variable"]

    @source_variable.setter
    def source_variable(self, value=None):
        """  Corresponds to IDD Field `source_variable`
        The name of the source used by the UtilityCost:Charge:Simple.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis
        if other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `source_variable`
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
                                 'for field `source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_variable`')

        self._data["Source Variable"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value=None):
        """  Corresponds to IDD Field `season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Simple for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `season`
                Accepted values are:
                      - Annual
                      - Summer
                      - Winter
                      - Spring
                      - Fall
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
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            vals = set()
            vals.add("Annual")
            vals.add("Summer")
            vals.add("Winter")
            vals.add("Spring")
            vals.add("Fall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `season`'.format(value))

        self._data["Season"] = value

    @property
    def category_variable_name(self):
        """Get category_variable_name

        Returns:
            str: the value of `category_variable_name` or None if not set
        """
        return self._data["Category Variable Name"]

    @category_variable_name.setter
    def category_variable_name(self, value=None):
        """  Corresponds to IDD Field `category_variable_name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `category_variable_name`
                Accepted values are:
                      - EnergyCharges
                      - DemandCharges
                      - ServiceCharges
                      - Basis
                      - Adjustment
                      - Surcharge
                      - Subtotal
                      - Taxes
                      - Total
                      - NotIncluded
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
                                 'for field `category_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category_variable_name`')
            vals = set()
            vals.add("EnergyCharges")
            vals.add("DemandCharges")
            vals.add("ServiceCharges")
            vals.add("Basis")
            vals.add("Adjustment")
            vals.add("Surcharge")
            vals.add("Subtotal")
            vals.add("Taxes")
            vals.add("Total")
            vals.add("NotIncluded")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `category_variable_name`'.format(value))

        self._data["Category Variable Name"] = value

    @property
    def cost_per_unit_value_or_variable_name(self):
        """Get cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Cost per Unit Value or Variable Name"]

    @cost_per_unit_value_or_variable_name.setter
    def cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `cost_per_unit_value_or_variable_name`
        This field contains either a single number or the name of a variable.  The number is multiplied with
        all of the energy or demand or other source that is specified in the source field.  If a variable is
        used then the monthly values of the variable are multiplied against the variable specified in the
        source field.  This field makes it easy to include a simple charge without specifying block sizes.
        This is a good way to include a tax or cost adjustment.

        Args:
            value (str): value for IDD Field `cost_per_unit_value_or_variable_name`
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
                                 'for field `cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cost_per_unit_value_or_variable_name`')

        self._data["Cost per Unit Value or Variable Name"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.source_variable))
        out.append(self._to_str(self.season))
        out.append(self._to_str(self.category_variable_name))
        out.append(self._to_str(self.cost_per_unit_value_or_variable_name))
        return ",".join(out)

class UtilityCostChargeBlock(object):
    """ Corresponds to IDD object `UtilityCost:Charge:Block`
        Used to compute energy and demand charges (or any other charges) that are structured
        in blocks of charges. Multiple UtilityCost:Charge:Block objects may be defined for a
        single tariff and they will be added together.
    """
    internal_name = "UtilityCost:Charge:Block"
    field_count = 37

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Charge:Block`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Source Variable"] = None
        self._data["Season"] = None
        self._data["Category Variable Name"] = None
        self._data["Remaining Into Variable"] = None
        self._data["Block Size Multiplier Value or Variable Name"] = None
        self._data["Block Size 1 Value or Variable Name"] = None
        self._data["Block 1 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 2 Value or Variable Name"] = None
        self._data["Block 2 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 3 Value or Variable Name"] = None
        self._data["Block 3 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 4 Value or Variable Name"] = None
        self._data["Block 4 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 5 Value or Variable Name"] = None
        self._data["Block 5 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 6 Value or Variable Name"] = None
        self._data["Block 6 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 7 Value or Variable Name"] = None
        self._data["Block 7 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 8 Value or Variable Name"] = None
        self._data["Block 8 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 9 Value or Variable Name"] = None
        self._data["Block 9 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 10 Value or Variable Name"] = None
        self._data["Block 10 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 11 Value or Variable Name"] = None
        self._data["Block 11 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 12 Value or Variable Name"] = None
        self._data["Block 12 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 13 Value or Variable Name"] = None
        self._data["Block 13 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 14 Value or Variable Name"] = None
        self._data["Block 14 Cost per Unit Value or Variable Name"] = None
        self._data["Block Size 15 Value or Variable Name"] = None
        self._data["Block 15 Cost per Unit Value or Variable Name"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_variable = None
        else:
            self.source_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.category_variable_name = None
        else:
            self.category_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.remaining_into_variable = None
        else:
            self.remaining_into_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_multiplier_value_or_variable_name = None
        else:
            self.block_size_multiplier_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_1_value_or_variable_name = None
        else:
            self.block_size_1_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_1_cost_per_unit_value_or_variable_name = None
        else:
            self.block_1_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_2_value_or_variable_name = None
        else:
            self.block_size_2_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_2_cost_per_unit_value_or_variable_name = None
        else:
            self.block_2_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_3_value_or_variable_name = None
        else:
            self.block_size_3_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_3_cost_per_unit_value_or_variable_name = None
        else:
            self.block_3_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_4_value_or_variable_name = None
        else:
            self.block_size_4_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_4_cost_per_unit_value_or_variable_name = None
        else:
            self.block_4_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_5_value_or_variable_name = None
        else:
            self.block_size_5_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_5_cost_per_unit_value_or_variable_name = None
        else:
            self.block_5_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_6_value_or_variable_name = None
        else:
            self.block_size_6_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_6_cost_per_unit_value_or_variable_name = None
        else:
            self.block_6_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_7_value_or_variable_name = None
        else:
            self.block_size_7_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_7_cost_per_unit_value_or_variable_name = None
        else:
            self.block_7_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_8_value_or_variable_name = None
        else:
            self.block_size_8_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_8_cost_per_unit_value_or_variable_name = None
        else:
            self.block_8_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_9_value_or_variable_name = None
        else:
            self.block_size_9_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_9_cost_per_unit_value_or_variable_name = None
        else:
            self.block_9_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_10_value_or_variable_name = None
        else:
            self.block_size_10_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_10_cost_per_unit_value_or_variable_name = None
        else:
            self.block_10_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_11_value_or_variable_name = None
        else:
            self.block_size_11_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_11_cost_per_unit_value_or_variable_name = None
        else:
            self.block_11_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_12_value_or_variable_name = None
        else:
            self.block_size_12_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_12_cost_per_unit_value_or_variable_name = None
        else:
            self.block_12_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_13_value_or_variable_name = None
        else:
            self.block_size_13_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_13_cost_per_unit_value_or_variable_name = None
        else:
            self.block_13_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_14_value_or_variable_name = None
        else:
            self.block_size_14_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_14_cost_per_unit_value_or_variable_name = None
        else:
            self.block_14_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_size_15_value_or_variable_name = None
        else:
            self.block_size_15_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.block_15_cost_per_unit_value_or_variable_name = None
        else:
            self.block_15_cost_per_unit_value_or_variable_name = vals[i]
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
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Block object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Block are stored in a variable with the same name.
        That way the results may be used for further calculation.

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Block.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def source_variable(self):
        """Get source_variable

        Returns:
            str: the value of `source_variable` or None if not set
        """
        return self._data["Source Variable"]

    @source_variable.setter
    def source_variable(self, value=None):
        """  Corresponds to IDD Field `source_variable`
        The name of the source used by the UtilityCost:Charge:Block.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis if
        other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `source_variable`
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
                                 'for field `source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_variable`')

        self._data["Source Variable"] = value

    @property
    def season(self):
        """Get season

        Returns:
            str: the value of `season` or None if not set
        """
        return self._data["Season"]

    @season.setter
    def season(self, value="Season"):
        """  Corresponds to IDD Field `season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Block for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `season`
                Accepted values are:
                      - Annual
                      - Summer
                      - Winter
                      - Spring
                      - Fall
                Default value: Season
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
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            vals = set()
            vals.add("Annual")
            vals.add("Summer")
            vals.add("Winter")
            vals.add("Spring")
            vals.add("Fall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `season`'.format(value))

        self._data["Season"] = value

    @property
    def category_variable_name(self):
        """Get category_variable_name

        Returns:
            str: the value of `category_variable_name` or None if not set
        """
        return self._data["Category Variable Name"]

    @category_variable_name.setter
    def category_variable_name(self, value=None):
        """  Corresponds to IDD Field `category_variable_name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `category_variable_name`
                Accepted values are:
                      - EnergyCharges
                      - DemandCharges
                      - ServiceCharges
                      - Basis
                      - Adjustment
                      - Surcharge
                      - Subtotal
                      - Taxes
                      - Total
                      - NotIncluded
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
                                 'for field `category_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category_variable_name`')
            vals = set()
            vals.add("EnergyCharges")
            vals.add("DemandCharges")
            vals.add("ServiceCharges")
            vals.add("Basis")
            vals.add("Adjustment")
            vals.add("Surcharge")
            vals.add("Subtotal")
            vals.add("Taxes")
            vals.add("Total")
            vals.add("NotIncluded")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `category_variable_name`'.format(value))

        self._data["Category Variable Name"] = value

    @property
    def remaining_into_variable(self):
        """Get remaining_into_variable

        Returns:
            str: the value of `remaining_into_variable` or None if not set
        """
        return self._data["Remaining Into Variable"]

    @remaining_into_variable.setter
    def remaining_into_variable(self, value=None):
        """  Corresponds to IDD Field `remaining_into_variable`
        If the blocks do not use all of the energy or demand from the source some energy and demand remains
        then the remaining amount should be assigned to a variable. If no variable is assigned and some amount
        of energy or demand is not used in the block structure a warning will be issued.

        Args:
            value (str): value for IDD Field `remaining_into_variable`
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
                                 'for field `remaining_into_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `remaining_into_variable`')

        self._data["Remaining Into Variable"] = value

    @property
    def block_size_multiplier_value_or_variable_name(self):
        """Get block_size_multiplier_value_or_variable_name

        Returns:
            str: the value of `block_size_multiplier_value_or_variable_name` or None if not set
        """
        return self._data["Block Size Multiplier Value or Variable Name"]

    @block_size_multiplier_value_or_variable_name.setter
    def block_size_multiplier_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_multiplier_value_or_variable_name`
        The sizes of the blocks are usually used directly but if a value or a variable is entered here the block
        sizes entered in the rest of the charge are first multiplied by the entered value prior to being used.
        This is common for rates that are kWh/kW rates and in that case the variable that holds the monthly
        total electric demand would be entered.  If no value is entered a default value of one is assumed so
        that the block sizes remain exactly as entered.  This field is unusual for the EnergyPlus syntax because
        it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_multiplier_value_or_variable_name`
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
                                 'for field `block_size_multiplier_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_multiplier_value_or_variable_name`')

        self._data["Block Size Multiplier Value or Variable Name"] = value

    @property
    def block_size_1_value_or_variable_name(self):
        """Get block_size_1_value_or_variable_name

        Returns:
            str: the value of `block_size_1_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 1 Value or Variable Name"]

    @block_size_1_value_or_variable_name.setter
    def block_size_1_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_1_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_1_value_or_variable_name`
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
                                 'for field `block_size_1_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_1_value_or_variable_name`')

        self._data["Block Size 1 Value or Variable Name"] = value

    @property
    def block_1_cost_per_unit_value_or_variable_name(self):
        """Get block_1_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_1_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 1 Cost per Unit Value or Variable Name"]

    @block_1_cost_per_unit_value_or_variable_name.setter
    def block_1_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_1_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_1_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_1_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_1_cost_per_unit_value_or_variable_name`')

        self._data["Block 1 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_2_value_or_variable_name(self):
        """Get block_size_2_value_or_variable_name

        Returns:
            str: the value of `block_size_2_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 2 Value or Variable Name"]

    @block_size_2_value_or_variable_name.setter
    def block_size_2_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_2_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_2_value_or_variable_name`
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
                                 'for field `block_size_2_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_2_value_or_variable_name`')

        self._data["Block Size 2 Value or Variable Name"] = value

    @property
    def block_2_cost_per_unit_value_or_variable_name(self):
        """Get block_2_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_2_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 2 Cost per Unit Value or Variable Name"]

    @block_2_cost_per_unit_value_or_variable_name.setter
    def block_2_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_2_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_2_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_2_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_2_cost_per_unit_value_or_variable_name`')

        self._data["Block 2 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_3_value_or_variable_name(self):
        """Get block_size_3_value_or_variable_name

        Returns:
            str: the value of `block_size_3_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 3 Value or Variable Name"]

    @block_size_3_value_or_variable_name.setter
    def block_size_3_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_3_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_3_value_or_variable_name`
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
                                 'for field `block_size_3_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_3_value_or_variable_name`')

        self._data["Block Size 3 Value or Variable Name"] = value

    @property
    def block_3_cost_per_unit_value_or_variable_name(self):
        """Get block_3_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_3_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 3 Cost per Unit Value or Variable Name"]

    @block_3_cost_per_unit_value_or_variable_name.setter
    def block_3_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_3_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_3_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_3_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_3_cost_per_unit_value_or_variable_name`')

        self._data["Block 3 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_4_value_or_variable_name(self):
        """Get block_size_4_value_or_variable_name

        Returns:
            str: the value of `block_size_4_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 4 Value or Variable Name"]

    @block_size_4_value_or_variable_name.setter
    def block_size_4_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_4_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_4_value_or_variable_name`
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
                                 'for field `block_size_4_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_4_value_or_variable_name`')

        self._data["Block Size 4 Value or Variable Name"] = value

    @property
    def block_4_cost_per_unit_value_or_variable_name(self):
        """Get block_4_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_4_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 4 Cost per Unit Value or Variable Name"]

    @block_4_cost_per_unit_value_or_variable_name.setter
    def block_4_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_4_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_4_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_4_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_4_cost_per_unit_value_or_variable_name`')

        self._data["Block 4 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_5_value_or_variable_name(self):
        """Get block_size_5_value_or_variable_name

        Returns:
            str: the value of `block_size_5_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 5 Value or Variable Name"]

    @block_size_5_value_or_variable_name.setter
    def block_size_5_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_5_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_5_value_or_variable_name`
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
                                 'for field `block_size_5_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_5_value_or_variable_name`')

        self._data["Block Size 5 Value or Variable Name"] = value

    @property
    def block_5_cost_per_unit_value_or_variable_name(self):
        """Get block_5_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_5_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 5 Cost per Unit Value or Variable Name"]

    @block_5_cost_per_unit_value_or_variable_name.setter
    def block_5_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_5_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_5_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_5_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_5_cost_per_unit_value_or_variable_name`')

        self._data["Block 5 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_6_value_or_variable_name(self):
        """Get block_size_6_value_or_variable_name

        Returns:
            str: the value of `block_size_6_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 6 Value or Variable Name"]

    @block_size_6_value_or_variable_name.setter
    def block_size_6_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_6_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_6_value_or_variable_name`
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
                                 'for field `block_size_6_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_6_value_or_variable_name`')

        self._data["Block Size 6 Value or Variable Name"] = value

    @property
    def block_6_cost_per_unit_value_or_variable_name(self):
        """Get block_6_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_6_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 6 Cost per Unit Value or Variable Name"]

    @block_6_cost_per_unit_value_or_variable_name.setter
    def block_6_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_6_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_6_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_6_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_6_cost_per_unit_value_or_variable_name`')

        self._data["Block 6 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_7_value_or_variable_name(self):
        """Get block_size_7_value_or_variable_name

        Returns:
            str: the value of `block_size_7_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 7 Value or Variable Name"]

    @block_size_7_value_or_variable_name.setter
    def block_size_7_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_7_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_7_value_or_variable_name`
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
                                 'for field `block_size_7_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_7_value_or_variable_name`')

        self._data["Block Size 7 Value or Variable Name"] = value

    @property
    def block_7_cost_per_unit_value_or_variable_name(self):
        """Get block_7_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_7_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 7 Cost per Unit Value or Variable Name"]

    @block_7_cost_per_unit_value_or_variable_name.setter
    def block_7_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_7_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_7_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_7_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_7_cost_per_unit_value_or_variable_name`')

        self._data["Block 7 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_8_value_or_variable_name(self):
        """Get block_size_8_value_or_variable_name

        Returns:
            str: the value of `block_size_8_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 8 Value or Variable Name"]

    @block_size_8_value_or_variable_name.setter
    def block_size_8_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_8_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_8_value_or_variable_name`
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
                                 'for field `block_size_8_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_8_value_or_variable_name`')

        self._data["Block Size 8 Value or Variable Name"] = value

    @property
    def block_8_cost_per_unit_value_or_variable_name(self):
        """Get block_8_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_8_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 8 Cost per Unit Value or Variable Name"]

    @block_8_cost_per_unit_value_or_variable_name.setter
    def block_8_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_8_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_8_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_8_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_8_cost_per_unit_value_or_variable_name`')

        self._data["Block 8 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_9_value_or_variable_name(self):
        """Get block_size_9_value_or_variable_name

        Returns:
            str: the value of `block_size_9_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 9 Value or Variable Name"]

    @block_size_9_value_or_variable_name.setter
    def block_size_9_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_9_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_9_value_or_variable_name`
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
                                 'for field `block_size_9_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_9_value_or_variable_name`')

        self._data["Block Size 9 Value or Variable Name"] = value

    @property
    def block_9_cost_per_unit_value_or_variable_name(self):
        """Get block_9_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_9_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 9 Cost per Unit Value or Variable Name"]

    @block_9_cost_per_unit_value_or_variable_name.setter
    def block_9_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_9_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_9_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_9_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_9_cost_per_unit_value_or_variable_name`')

        self._data["Block 9 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_10_value_or_variable_name(self):
        """Get block_size_10_value_or_variable_name

        Returns:
            str: the value of `block_size_10_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 10 Value or Variable Name"]

    @block_size_10_value_or_variable_name.setter
    def block_size_10_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_10_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_10_value_or_variable_name`
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
                                 'for field `block_size_10_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_10_value_or_variable_name`')

        self._data["Block Size 10 Value or Variable Name"] = value

    @property
    def block_10_cost_per_unit_value_or_variable_name(self):
        """Get block_10_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_10_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 10 Cost per Unit Value or Variable Name"]

    @block_10_cost_per_unit_value_or_variable_name.setter
    def block_10_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_10_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_10_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_10_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_10_cost_per_unit_value_or_variable_name`')

        self._data["Block 10 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_11_value_or_variable_name(self):
        """Get block_size_11_value_or_variable_name

        Returns:
            str: the value of `block_size_11_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 11 Value or Variable Name"]

    @block_size_11_value_or_variable_name.setter
    def block_size_11_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_11_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_11_value_or_variable_name`
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
                                 'for field `block_size_11_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_11_value_or_variable_name`')

        self._data["Block Size 11 Value or Variable Name"] = value

    @property
    def block_11_cost_per_unit_value_or_variable_name(self):
        """Get block_11_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_11_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 11 Cost per Unit Value or Variable Name"]

    @block_11_cost_per_unit_value_or_variable_name.setter
    def block_11_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_11_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_11_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_11_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_11_cost_per_unit_value_or_variable_name`')

        self._data["Block 11 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_12_value_or_variable_name(self):
        """Get block_size_12_value_or_variable_name

        Returns:
            str: the value of `block_size_12_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 12 Value or Variable Name"]

    @block_size_12_value_or_variable_name.setter
    def block_size_12_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_12_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_12_value_or_variable_name`
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
                                 'for field `block_size_12_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_12_value_or_variable_name`')

        self._data["Block Size 12 Value or Variable Name"] = value

    @property
    def block_12_cost_per_unit_value_or_variable_name(self):
        """Get block_12_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_12_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 12 Cost per Unit Value or Variable Name"]

    @block_12_cost_per_unit_value_or_variable_name.setter
    def block_12_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_12_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_12_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_12_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_12_cost_per_unit_value_or_variable_name`')

        self._data["Block 12 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_13_value_or_variable_name(self):
        """Get block_size_13_value_or_variable_name

        Returns:
            str: the value of `block_size_13_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 13 Value or Variable Name"]

    @block_size_13_value_or_variable_name.setter
    def block_size_13_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_13_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_13_value_or_variable_name`
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
                                 'for field `block_size_13_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_13_value_or_variable_name`')

        self._data["Block Size 13 Value or Variable Name"] = value

    @property
    def block_13_cost_per_unit_value_or_variable_name(self):
        """Get block_13_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_13_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 13 Cost per Unit Value or Variable Name"]

    @block_13_cost_per_unit_value_or_variable_name.setter
    def block_13_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_13_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_13_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_13_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_13_cost_per_unit_value_or_variable_name`')

        self._data["Block 13 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_14_value_or_variable_name(self):
        """Get block_size_14_value_or_variable_name

        Returns:
            str: the value of `block_size_14_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 14 Value or Variable Name"]

    @block_size_14_value_or_variable_name.setter
    def block_size_14_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_14_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_14_value_or_variable_name`
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
                                 'for field `block_size_14_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_14_value_or_variable_name`')

        self._data["Block Size 14 Value or Variable Name"] = value

    @property
    def block_14_cost_per_unit_value_or_variable_name(self):
        """Get block_14_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_14_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 14 Cost per Unit Value or Variable Name"]

    @block_14_cost_per_unit_value_or_variable_name.setter
    def block_14_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_14_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_14_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_14_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_14_cost_per_unit_value_or_variable_name`')

        self._data["Block 14 Cost per Unit Value or Variable Name"] = value

    @property
    def block_size_15_value_or_variable_name(self):
        """Get block_size_15_value_or_variable_name

        Returns:
            str: the value of `block_size_15_value_or_variable_name` or None if not set
        """
        return self._data["Block Size 15 Value or Variable Name"]

    @block_size_15_value_or_variable_name.setter
    def block_size_15_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_size_15_value_or_variable_name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `block_size_15_value_or_variable_name`
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
                                 'for field `block_size_15_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_15_value_or_variable_name`')

        self._data["Block Size 15 Value or Variable Name"] = value

    @property
    def block_15_cost_per_unit_value_or_variable_name(self):
        """Get block_15_cost_per_unit_value_or_variable_name

        Returns:
            str: the value of `block_15_cost_per_unit_value_or_variable_name` or None if not set
        """
        return self._data["Block 15 Cost per Unit Value or Variable Name"]

    @block_15_cost_per_unit_value_or_variable_name.setter
    def block_15_cost_per_unit_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `block_15_cost_per_unit_value_or_variable_name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `block_15_cost_per_unit_value_or_variable_name`
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
                                 'for field `block_15_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_15_cost_per_unit_value_or_variable_name`')

        self._data["Block 15 Cost per Unit Value or Variable Name"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.source_variable))
        out.append(self._to_str(self.season))
        out.append(self._to_str(self.category_variable_name))
        out.append(self._to_str(self.remaining_into_variable))
        out.append(self._to_str(self.block_size_multiplier_value_or_variable_name))
        out.append(self._to_str(self.block_size_1_value_or_variable_name))
        out.append(self._to_str(self.block_1_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_2_value_or_variable_name))
        out.append(self._to_str(self.block_2_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_3_value_or_variable_name))
        out.append(self._to_str(self.block_3_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_4_value_or_variable_name))
        out.append(self._to_str(self.block_4_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_5_value_or_variable_name))
        out.append(self._to_str(self.block_5_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_6_value_or_variable_name))
        out.append(self._to_str(self.block_6_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_7_value_or_variable_name))
        out.append(self._to_str(self.block_7_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_8_value_or_variable_name))
        out.append(self._to_str(self.block_8_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_9_value_or_variable_name))
        out.append(self._to_str(self.block_9_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_10_value_or_variable_name))
        out.append(self._to_str(self.block_10_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_11_value_or_variable_name))
        out.append(self._to_str(self.block_11_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_12_value_or_variable_name))
        out.append(self._to_str(self.block_12_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_13_value_or_variable_name))
        out.append(self._to_str(self.block_13_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_14_value_or_variable_name))
        out.append(self._to_str(self.block_14_cost_per_unit_value_or_variable_name))
        out.append(self._to_str(self.block_size_15_value_or_variable_name))
        out.append(self._to_str(self.block_15_cost_per_unit_value_or_variable_name))
        return ",".join(out)

class UtilityCostRatchet(object):
    """ Corresponds to IDD object `UtilityCost:Ratchet`
        Allows the modeling of tariffs that include some type of seasonal ratcheting.
        Ratchets are most common when used with electric demand charges. A ratchet is when a
        utility requires that the demand charge for a month with a low demand may be
        increased to be more consistent with a month that set a higher demand charge.
    """
    internal_name = "UtilityCost:Ratchet"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Ratchet`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Baseline Source Variable"] = None
        self._data["Adjustment Source Variable"] = None
        self._data["Season From"] = None
        self._data["Season To"] = None
        self._data["Multiplier Value or Variable Name"] = None
        self._data["Offset Value or Variable Name"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.baseline_source_variable = None
        else:
            self.baseline_source_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.adjustment_source_variable = None
        else:
            self.adjustment_source_variable = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season_from = None
        else:
            self.season_from = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.season_to = None
        else:
            self.season_to = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.multiplier_value_or_variable_name = None
        else:
            self.multiplier_value_or_variable_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.offset_value_or_variable_name = None
        else:
            self.offset_value_or_variable_name = vals[i]
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
        Ratchet Variable Name
        The name of the ratchet and the name of the result of this single ratchet.

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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Ratchet.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def baseline_source_variable(self):
        """Get baseline_source_variable

        Returns:
            str: the value of `baseline_source_variable` or None if not set
        """
        return self._data["Baseline Source Variable"]

    @baseline_source_variable.setter
    def baseline_source_variable(self, value=None):
        """  Corresponds to IDD Field `baseline_source_variable`
        When the ratcheted value exceeds the baseline value for a month the ratcheted value is used but when the
        baseline value is greater then the ratcheted value the baseline value is used. Usually the electric
        demand charge is used.  The baseline source variable can be the results of another ratchet object. This
        allows utility tariffs that have multiple ratchets to be modeled.

        Args:
            value (str): value for IDD Field `baseline_source_variable`
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
                                 'for field `baseline_source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `baseline_source_variable`')

        self._data["Baseline Source Variable"] = value

    @property
    def adjustment_source_variable(self):
        """Get adjustment_source_variable

        Returns:
            str: the value of `adjustment_source_variable` or None if not set
        """
        return self._data["Adjustment Source Variable"]

    @adjustment_source_variable.setter
    def adjustment_source_variable(self, value=None):
        """  Corresponds to IDD Field `adjustment_source_variable`
        The variable that the ratchet is calculated from. It is often but not always the same as the baseline
        source variable.  The ratcheting calculations using offset and multiplier are using the values from the
        adjustment source variable. If left blank the adjustment source variable is the same as the baseline
        source variable.

        Args:
            value (str): value for IDD Field `adjustment_source_variable`
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
                                 'for field `adjustment_source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `adjustment_source_variable`')

        self._data["Adjustment Source Variable"] = value

    @property
    def season_from(self):
        """Get season_from

        Returns:
            str: the value of `season_from` or None if not set
        """
        return self._data["Season From"]

    @season_from.setter
    def season_from(self, value=None):
        """  Corresponds to IDD Field `season_from`
        The name of the season that is being examined.  The maximum value for all of the months in the named
        season is what is used with the multiplier and offset.  This is most commonly Summer or Annual.  When
        Monthly is used the adjustment source variable is used directly for all months.

        Args:
            value (str): value for IDD Field `season_from`
                Accepted values are:
                      - Annual
                      - Summer
                      - Winter
                      - Spring
                      - Fall
                      - Monthly
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
                                 'for field `season_from`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_from`')
            vals = set()
            vals.add("Annual")
            vals.add("Summer")
            vals.add("Winter")
            vals.add("Spring")
            vals.add("Fall")
            vals.add("Monthly")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `season_from`'.format(value))

        self._data["Season From"] = value

    @property
    def season_to(self):
        """Get season_to

        Returns:
            str: the value of `season_to` or None if not set
        """
        return self._data["Season To"]

    @season_to.setter
    def season_to(self, value=None):
        """  Corresponds to IDD Field `season_to`
        The name of the season when the ratchet would be calculated.  This is most commonly Winter.  The ratchet
        only is applied to the months in the named season. The resulting variable for months not in the Season To
        selection will contain the values as appear in the baseline source variable.

        Args:
            value (str): value for IDD Field `season_to`
                Accepted values are:
                      - Annual
                      - Summer
                      - Winter
                      - Spring
                      - Fall
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
                                 'for field `season_to`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_to`')
            vals = set()
            vals.add("Annual")
            vals.add("Summer")
            vals.add("Winter")
            vals.add("Spring")
            vals.add("Fall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `season_to`'.format(value))

        self._data["Season To"] = value

    @property
    def multiplier_value_or_variable_name(self):
        """Get multiplier_value_or_variable_name

        Returns:
            str: the value of `multiplier_value_or_variable_name` or None if not set
        """
        return self._data["Multiplier Value or Variable Name"]

    @multiplier_value_or_variable_name.setter
    def multiplier_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `multiplier_value_or_variable_name`
        Often the ratchet has a clause such as "the current month demand or 90% of the summer month demand".  For
        this case a value of 0.9 would be entered here as the multiplier.  This value may be left blank if no
        multiplier is needed and a value of one will be used as a default.

        Args:
            value (str): value for IDD Field `multiplier_value_or_variable_name`
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
                                 'for field `multiplier_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `multiplier_value_or_variable_name`')

        self._data["Multiplier Value or Variable Name"] = value

    @property
    def offset_value_or_variable_name(self):
        """Get offset_value_or_variable_name

        Returns:
            str: the value of `offset_value_or_variable_name` or None if not set
        """
        return self._data["Offset Value or Variable Name"]

    @offset_value_or_variable_name.setter
    def offset_value_or_variable_name(self, value=None):
        """  Corresponds to IDD Field `offset_value_or_variable_name`
        A less common strategy is to say that the ratchet must be all demand greater than a value in this case
        an offset that is added to the demand may be entered here. If entered it is common for the offset value
        to be negative representing that the demand be reduced.   If no value is entered it is assumed to be
        zero and not affect the ratchet.

        Args:
            value (str): value for IDD Field `offset_value_or_variable_name`
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
                                 'for field `offset_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `offset_value_or_variable_name`')

        self._data["Offset Value or Variable Name"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.baseline_source_variable))
        out.append(self._to_str(self.adjustment_source_variable))
        out.append(self._to_str(self.season_from))
        out.append(self._to_str(self.season_to))
        out.append(self._to_str(self.multiplier_value_or_variable_name))
        out.append(self._to_str(self.offset_value_or_variable_name))
        return ",".join(out)

class UtilityCostVariable(object):
    """ Corresponds to IDD object `UtilityCost:Variable`
        Allows for the direct entry of monthly values into a utility tariff variable.
    """
    internal_name = "UtilityCost:Variable"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Variable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Variable Type"] = None
        self._data["January Value"] = None
        self._data["February Value"] = None
        self._data["March Value"] = None
        self._data["April Value"] = None
        self._data["May Value"] = None
        self._data["June Value"] = None
        self._data["July Value"] = None
        self._data["August Value"] = None
        self._data["September Value"] = None
        self._data["October Value"] = None
        self._data["November Value"] = None
        self._data["December Value"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.variable_type = None
        else:
            self.variable_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.january_value = None
        else:
            self.january_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.february_value = None
        else:
            self.february_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.march_value = None
        else:
            self.march_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.april_value = None
        else:
            self.april_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.may_value = None
        else:
            self.may_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.june_value = None
        else:
            self.june_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.july_value = None
        else:
            self.july_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.august_value = None
        else:
            self.august_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.september_value = None
        else:
            self.september_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.october_value = None
        else:
            self.october_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.november_value = None
        else:
            self.november_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.december_value = None
        else:
            self.december_value = vals[i]
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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def variable_type(self):
        """Get variable_type

        Returns:
            str: the value of `variable_type` or None if not set
        """
        return self._data["Variable Type"]

    @variable_type.setter
    def variable_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `variable_type`

        Args:
            value (str): value for IDD Field `variable_type`
                Accepted values are:
                      - Energy
                      - Power
                      - Dimensionless
                      - Currency
                Default value: Dimensionless
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
                                 'for field `variable_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `variable_type`')
            vals = set()
            vals.add("Energy")
            vals.add("Power")
            vals.add("Dimensionless")
            vals.add("Currency")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `variable_type`'.format(value))

        self._data["Variable Type"] = value

    @property
    def january_value(self):
        """Get january_value

        Returns:
            float: the value of `january_value` or None if not set
        """
        return self._data["January Value"]

    @january_value.setter
    def january_value(self, value=None):
        """  Corresponds to IDD Field `january_value`

        Args:
            value (float): value for IDD Field `january_value`
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
                                 'for field `january_value`'.format(value))

        self._data["January Value"] = value

    @property
    def february_value(self):
        """Get february_value

        Returns:
            float: the value of `february_value` or None if not set
        """
        return self._data["February Value"]

    @february_value.setter
    def february_value(self, value=None):
        """  Corresponds to IDD Field `february_value`

        Args:
            value (float): value for IDD Field `february_value`
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
                                 'for field `february_value`'.format(value))

        self._data["February Value"] = value

    @property
    def march_value(self):
        """Get march_value

        Returns:
            float: the value of `march_value` or None if not set
        """
        return self._data["March Value"]

    @march_value.setter
    def march_value(self, value=None):
        """  Corresponds to IDD Field `march_value`

        Args:
            value (float): value for IDD Field `march_value`
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
                                 'for field `march_value`'.format(value))

        self._data["March Value"] = value

    @property
    def april_value(self):
        """Get april_value

        Returns:
            float: the value of `april_value` or None if not set
        """
        return self._data["April Value"]

    @april_value.setter
    def april_value(self, value=None):
        """  Corresponds to IDD Field `april_value`

        Args:
            value (float): value for IDD Field `april_value`
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
                                 'for field `april_value`'.format(value))

        self._data["April Value"] = value

    @property
    def may_value(self):
        """Get may_value

        Returns:
            float: the value of `may_value` or None if not set
        """
        return self._data["May Value"]

    @may_value.setter
    def may_value(self, value=None):
        """  Corresponds to IDD Field `may_value`

        Args:
            value (float): value for IDD Field `may_value`
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
                                 'for field `may_value`'.format(value))

        self._data["May Value"] = value

    @property
    def june_value(self):
        """Get june_value

        Returns:
            float: the value of `june_value` or None if not set
        """
        return self._data["June Value"]

    @june_value.setter
    def june_value(self, value=None):
        """  Corresponds to IDD Field `june_value`

        Args:
            value (float): value for IDD Field `june_value`
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
                                 'for field `june_value`'.format(value))

        self._data["June Value"] = value

    @property
    def july_value(self):
        """Get july_value

        Returns:
            float: the value of `july_value` or None if not set
        """
        return self._data["July Value"]

    @july_value.setter
    def july_value(self, value=None):
        """  Corresponds to IDD Field `july_value`

        Args:
            value (float): value for IDD Field `july_value`
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
                                 'for field `july_value`'.format(value))

        self._data["July Value"] = value

    @property
    def august_value(self):
        """Get august_value

        Returns:
            float: the value of `august_value` or None if not set
        """
        return self._data["August Value"]

    @august_value.setter
    def august_value(self, value=None):
        """  Corresponds to IDD Field `august_value`

        Args:
            value (float): value for IDD Field `august_value`
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
                                 'for field `august_value`'.format(value))

        self._data["August Value"] = value

    @property
    def september_value(self):
        """Get september_value

        Returns:
            float: the value of `september_value` or None if not set
        """
        return self._data["September Value"]

    @september_value.setter
    def september_value(self, value=None):
        """  Corresponds to IDD Field `september_value`

        Args:
            value (float): value for IDD Field `september_value`
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
                                 'for field `september_value`'.format(value))

        self._data["September Value"] = value

    @property
    def october_value(self):
        """Get october_value

        Returns:
            float: the value of `october_value` or None if not set
        """
        return self._data["October Value"]

    @october_value.setter
    def october_value(self, value=None):
        """  Corresponds to IDD Field `october_value`

        Args:
            value (float): value for IDD Field `october_value`
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
                                 'for field `october_value`'.format(value))

        self._data["October Value"] = value

    @property
    def november_value(self):
        """Get november_value

        Returns:
            float: the value of `november_value` or None if not set
        """
        return self._data["November Value"]

    @november_value.setter
    def november_value(self, value=None):
        """  Corresponds to IDD Field `november_value`

        Args:
            value (float): value for IDD Field `november_value`
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
                                 'for field `november_value`'.format(value))

        self._data["November Value"] = value

    @property
    def december_value(self):
        """Get december_value

        Returns:
            float: the value of `december_value` or None if not set
        """
        return self._data["December Value"]

    @december_value.setter
    def december_value(self, value=None):
        """  Corresponds to IDD Field `december_value`

        Args:
            value (float): value for IDD Field `december_value`
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
                                 'for field `december_value`'.format(value))

        self._data["December Value"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.variable_type))
        out.append(self._to_str(self.january_value))
        out.append(self._to_str(self.february_value))
        out.append(self._to_str(self.march_value))
        out.append(self._to_str(self.april_value))
        out.append(self._to_str(self.may_value))
        out.append(self._to_str(self.june_value))
        out.append(self._to_str(self.july_value))
        out.append(self._to_str(self.august_value))
        out.append(self._to_str(self.september_value))
        out.append(self._to_str(self.october_value))
        out.append(self._to_str(self.november_value))
        out.append(self._to_str(self.december_value))
        return ",".join(out)

class UtilityCostComputation(object):
    """ Corresponds to IDD object `UtilityCost:Computation`
        The object lists a series of computations that are used to perform the utility bill
        calculation. The object is only used for complex tariffs that cannot be modeled any
        other way. For most utility tariffs, UtilityCost:Computation is unnecessary and
        should be avoided. If UtilityCost:Computation is used, it must contain references
        to all objects involved in the rate in the order that they should be computed.
    """
    internal_name = "UtilityCost:Computation"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `UtilityCost:Computation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Compute Step 1"] = None
        self._data["Compute Step 2"] = None
        self._data["Compute Step 3"] = None
        self._data["Compute Step 4"] = None
        self._data["Compute Step 5"] = None
        self._data["Compute Step 6"] = None
        self._data["Compute Step 7"] = None
        self._data["Compute Step 8"] = None
        self._data["Compute Step 9"] = None
        self._data["Compute Step 10"] = None
        self._data["Compute Step 11"] = None
        self._data["Compute Step 12"] = None
        self._data["Compute Step 13"] = None
        self._data["Compute Step 14"] = None
        self._data["Compute Step 15"] = None
        self._data["Compute Step 16"] = None
        self._data["Compute Step 17"] = None
        self._data["Compute Step 18"] = None
        self._data["Compute Step 19"] = None
        self._data["Compute Step 20"] = None
        self._data["Compute Step 21"] = None
        self._data["Compute Step 22"] = None
        self._data["Compute Step 23"] = None
        self._data["Compute Step 24"] = None
        self._data["Compute Step 25"] = None
        self._data["Compute Step 26"] = None
        self._data["Compute Step 27"] = None
        self._data["Compute Step 28"] = None
        self._data["Compute Step 29"] = None
        self._data["Compute Step 30"] = None

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
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_1 = None
        else:
            self.compute_step_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_2 = None
        else:
            self.compute_step_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_3 = None
        else:
            self.compute_step_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_4 = None
        else:
            self.compute_step_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_5 = None
        else:
            self.compute_step_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_6 = None
        else:
            self.compute_step_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_7 = None
        else:
            self.compute_step_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_8 = None
        else:
            self.compute_step_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_9 = None
        else:
            self.compute_step_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_10 = None
        else:
            self.compute_step_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_11 = None
        else:
            self.compute_step_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_12 = None
        else:
            self.compute_step_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_13 = None
        else:
            self.compute_step_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_14 = None
        else:
            self.compute_step_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_15 = None
        else:
            self.compute_step_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_16 = None
        else:
            self.compute_step_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_17 = None
        else:
            self.compute_step_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_18 = None
        else:
            self.compute_step_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_19 = None
        else:
            self.compute_step_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_20 = None
        else:
            self.compute_step_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_21 = None
        else:
            self.compute_step_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_22 = None
        else:
            self.compute_step_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_23 = None
        else:
            self.compute_step_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_24 = None
        else:
            self.compute_step_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_25 = None
        else:
            self.compute_step_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_26 = None
        else:
            self.compute_step_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_27 = None
        else:
            self.compute_step_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_28 = None
        else:
            self.compute_step_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_29 = None
        else:
            self.compute_step_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.compute_step_30 = None
        else:
            self.compute_step_30 = vals[i]
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
    def tariff_name(self):
        """Get tariff_name

        Returns:
            str: the value of `tariff_name` or None if not set
        """
        return self._data["Tariff Name"]

    @tariff_name.setter
    def tariff_name(self, value=None):
        """  Corresponds to IDD Field `tariff_name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `tariff_name`
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
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')

        self._data["Tariff Name"] = value

    @property
    def compute_step_1(self):
        """Get compute_step_1

        Returns:
            str: the value of `compute_step_1` or None if not set
        """
        return self._data["Compute Step 1"]

    @compute_step_1.setter
    def compute_step_1(self, value=None):
        """  Corresponds to IDD Field `compute_step_1`
        Contain a simple language that describes the steps used in the computation process similar to a
        programming language.

        Args:
            value (str): value for IDD Field `compute_step_1`
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
                                 'for field `compute_step_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_1`')

        self._data["Compute Step 1"] = value

    @property
    def compute_step_2(self):
        """Get compute_step_2

        Returns:
            str: the value of `compute_step_2` or None if not set
        """
        return self._data["Compute Step 2"]

    @compute_step_2.setter
    def compute_step_2(self, value=None):
        """  Corresponds to IDD Field `compute_step_2`

        Args:
            value (str): value for IDD Field `compute_step_2`
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
                                 'for field `compute_step_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_2`')

        self._data["Compute Step 2"] = value

    @property
    def compute_step_3(self):
        """Get compute_step_3

        Returns:
            str: the value of `compute_step_3` or None if not set
        """
        return self._data["Compute Step 3"]

    @compute_step_3.setter
    def compute_step_3(self, value=None):
        """  Corresponds to IDD Field `compute_step_3`

        Args:
            value (str): value for IDD Field `compute_step_3`
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
                                 'for field `compute_step_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_3`')

        self._data["Compute Step 3"] = value

    @property
    def compute_step_4(self):
        """Get compute_step_4

        Returns:
            str: the value of `compute_step_4` or None if not set
        """
        return self._data["Compute Step 4"]

    @compute_step_4.setter
    def compute_step_4(self, value=None):
        """  Corresponds to IDD Field `compute_step_4`

        Args:
            value (str): value for IDD Field `compute_step_4`
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
                                 'for field `compute_step_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_4`')

        self._data["Compute Step 4"] = value

    @property
    def compute_step_5(self):
        """Get compute_step_5

        Returns:
            str: the value of `compute_step_5` or None if not set
        """
        return self._data["Compute Step 5"]

    @compute_step_5.setter
    def compute_step_5(self, value=None):
        """  Corresponds to IDD Field `compute_step_5`

        Args:
            value (str): value for IDD Field `compute_step_5`
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
                                 'for field `compute_step_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_5`')

        self._data["Compute Step 5"] = value

    @property
    def compute_step_6(self):
        """Get compute_step_6

        Returns:
            str: the value of `compute_step_6` or None if not set
        """
        return self._data["Compute Step 6"]

    @compute_step_6.setter
    def compute_step_6(self, value=None):
        """  Corresponds to IDD Field `compute_step_6`

        Args:
            value (str): value for IDD Field `compute_step_6`
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
                                 'for field `compute_step_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_6`')

        self._data["Compute Step 6"] = value

    @property
    def compute_step_7(self):
        """Get compute_step_7

        Returns:
            str: the value of `compute_step_7` or None if not set
        """
        return self._data["Compute Step 7"]

    @compute_step_7.setter
    def compute_step_7(self, value=None):
        """  Corresponds to IDD Field `compute_step_7`

        Args:
            value (str): value for IDD Field `compute_step_7`
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
                                 'for field `compute_step_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_7`')

        self._data["Compute Step 7"] = value

    @property
    def compute_step_8(self):
        """Get compute_step_8

        Returns:
            str: the value of `compute_step_8` or None if not set
        """
        return self._data["Compute Step 8"]

    @compute_step_8.setter
    def compute_step_8(self, value=None):
        """  Corresponds to IDD Field `compute_step_8`

        Args:
            value (str): value for IDD Field `compute_step_8`
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
                                 'for field `compute_step_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_8`')

        self._data["Compute Step 8"] = value

    @property
    def compute_step_9(self):
        """Get compute_step_9

        Returns:
            str: the value of `compute_step_9` or None if not set
        """
        return self._data["Compute Step 9"]

    @compute_step_9.setter
    def compute_step_9(self, value=None):
        """  Corresponds to IDD Field `compute_step_9`

        Args:
            value (str): value for IDD Field `compute_step_9`
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
                                 'for field `compute_step_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_9`')

        self._data["Compute Step 9"] = value

    @property
    def compute_step_10(self):
        """Get compute_step_10

        Returns:
            str: the value of `compute_step_10` or None if not set
        """
        return self._data["Compute Step 10"]

    @compute_step_10.setter
    def compute_step_10(self, value=None):
        """  Corresponds to IDD Field `compute_step_10`

        Args:
            value (str): value for IDD Field `compute_step_10`
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
                                 'for field `compute_step_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_10`')

        self._data["Compute Step 10"] = value

    @property
    def compute_step_11(self):
        """Get compute_step_11

        Returns:
            str: the value of `compute_step_11` or None if not set
        """
        return self._data["Compute Step 11"]

    @compute_step_11.setter
    def compute_step_11(self, value=None):
        """  Corresponds to IDD Field `compute_step_11`

        Args:
            value (str): value for IDD Field `compute_step_11`
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
                                 'for field `compute_step_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_11`')

        self._data["Compute Step 11"] = value

    @property
    def compute_step_12(self):
        """Get compute_step_12

        Returns:
            str: the value of `compute_step_12` or None if not set
        """
        return self._data["Compute Step 12"]

    @compute_step_12.setter
    def compute_step_12(self, value=None):
        """  Corresponds to IDD Field `compute_step_12`

        Args:
            value (str): value for IDD Field `compute_step_12`
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
                                 'for field `compute_step_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_12`')

        self._data["Compute Step 12"] = value

    @property
    def compute_step_13(self):
        """Get compute_step_13

        Returns:
            str: the value of `compute_step_13` or None if not set
        """
        return self._data["Compute Step 13"]

    @compute_step_13.setter
    def compute_step_13(self, value=None):
        """  Corresponds to IDD Field `compute_step_13`

        Args:
            value (str): value for IDD Field `compute_step_13`
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
                                 'for field `compute_step_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_13`')

        self._data["Compute Step 13"] = value

    @property
    def compute_step_14(self):
        """Get compute_step_14

        Returns:
            str: the value of `compute_step_14` or None if not set
        """
        return self._data["Compute Step 14"]

    @compute_step_14.setter
    def compute_step_14(self, value=None):
        """  Corresponds to IDD Field `compute_step_14`

        Args:
            value (str): value for IDD Field `compute_step_14`
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
                                 'for field `compute_step_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_14`')

        self._data["Compute Step 14"] = value

    @property
    def compute_step_15(self):
        """Get compute_step_15

        Returns:
            str: the value of `compute_step_15` or None if not set
        """
        return self._data["Compute Step 15"]

    @compute_step_15.setter
    def compute_step_15(self, value=None):
        """  Corresponds to IDD Field `compute_step_15`

        Args:
            value (str): value for IDD Field `compute_step_15`
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
                                 'for field `compute_step_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_15`')

        self._data["Compute Step 15"] = value

    @property
    def compute_step_16(self):
        """Get compute_step_16

        Returns:
            str: the value of `compute_step_16` or None if not set
        """
        return self._data["Compute Step 16"]

    @compute_step_16.setter
    def compute_step_16(self, value=None):
        """  Corresponds to IDD Field `compute_step_16`

        Args:
            value (str): value for IDD Field `compute_step_16`
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
                                 'for field `compute_step_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_16`')

        self._data["Compute Step 16"] = value

    @property
    def compute_step_17(self):
        """Get compute_step_17

        Returns:
            str: the value of `compute_step_17` or None if not set
        """
        return self._data["Compute Step 17"]

    @compute_step_17.setter
    def compute_step_17(self, value=None):
        """  Corresponds to IDD Field `compute_step_17`

        Args:
            value (str): value for IDD Field `compute_step_17`
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
                                 'for field `compute_step_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_17`')

        self._data["Compute Step 17"] = value

    @property
    def compute_step_18(self):
        """Get compute_step_18

        Returns:
            str: the value of `compute_step_18` or None if not set
        """
        return self._data["Compute Step 18"]

    @compute_step_18.setter
    def compute_step_18(self, value=None):
        """  Corresponds to IDD Field `compute_step_18`

        Args:
            value (str): value for IDD Field `compute_step_18`
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
                                 'for field `compute_step_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_18`')

        self._data["Compute Step 18"] = value

    @property
    def compute_step_19(self):
        """Get compute_step_19

        Returns:
            str: the value of `compute_step_19` or None if not set
        """
        return self._data["Compute Step 19"]

    @compute_step_19.setter
    def compute_step_19(self, value=None):
        """  Corresponds to IDD Field `compute_step_19`

        Args:
            value (str): value for IDD Field `compute_step_19`
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
                                 'for field `compute_step_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_19`')

        self._data["Compute Step 19"] = value

    @property
    def compute_step_20(self):
        """Get compute_step_20

        Returns:
            str: the value of `compute_step_20` or None if not set
        """
        return self._data["Compute Step 20"]

    @compute_step_20.setter
    def compute_step_20(self, value=None):
        """  Corresponds to IDD Field `compute_step_20`

        Args:
            value (str): value for IDD Field `compute_step_20`
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
                                 'for field `compute_step_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_20`')

        self._data["Compute Step 20"] = value

    @property
    def compute_step_21(self):
        """Get compute_step_21

        Returns:
            str: the value of `compute_step_21` or None if not set
        """
        return self._data["Compute Step 21"]

    @compute_step_21.setter
    def compute_step_21(self, value=None):
        """  Corresponds to IDD Field `compute_step_21`

        Args:
            value (str): value for IDD Field `compute_step_21`
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
                                 'for field `compute_step_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_21`')

        self._data["Compute Step 21"] = value

    @property
    def compute_step_22(self):
        """Get compute_step_22

        Returns:
            str: the value of `compute_step_22` or None if not set
        """
        return self._data["Compute Step 22"]

    @compute_step_22.setter
    def compute_step_22(self, value=None):
        """  Corresponds to IDD Field `compute_step_22`

        Args:
            value (str): value for IDD Field `compute_step_22`
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
                                 'for field `compute_step_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_22`')

        self._data["Compute Step 22"] = value

    @property
    def compute_step_23(self):
        """Get compute_step_23

        Returns:
            str: the value of `compute_step_23` or None if not set
        """
        return self._data["Compute Step 23"]

    @compute_step_23.setter
    def compute_step_23(self, value=None):
        """  Corresponds to IDD Field `compute_step_23`

        Args:
            value (str): value for IDD Field `compute_step_23`
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
                                 'for field `compute_step_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_23`')

        self._data["Compute Step 23"] = value

    @property
    def compute_step_24(self):
        """Get compute_step_24

        Returns:
            str: the value of `compute_step_24` or None if not set
        """
        return self._data["Compute Step 24"]

    @compute_step_24.setter
    def compute_step_24(self, value=None):
        """  Corresponds to IDD Field `compute_step_24`

        Args:
            value (str): value for IDD Field `compute_step_24`
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
                                 'for field `compute_step_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_24`')

        self._data["Compute Step 24"] = value

    @property
    def compute_step_25(self):
        """Get compute_step_25

        Returns:
            str: the value of `compute_step_25` or None if not set
        """
        return self._data["Compute Step 25"]

    @compute_step_25.setter
    def compute_step_25(self, value=None):
        """  Corresponds to IDD Field `compute_step_25`

        Args:
            value (str): value for IDD Field `compute_step_25`
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
                                 'for field `compute_step_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_25`')

        self._data["Compute Step 25"] = value

    @property
    def compute_step_26(self):
        """Get compute_step_26

        Returns:
            str: the value of `compute_step_26` or None if not set
        """
        return self._data["Compute Step 26"]

    @compute_step_26.setter
    def compute_step_26(self, value=None):
        """  Corresponds to IDD Field `compute_step_26`

        Args:
            value (str): value for IDD Field `compute_step_26`
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
                                 'for field `compute_step_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_26`')

        self._data["Compute Step 26"] = value

    @property
    def compute_step_27(self):
        """Get compute_step_27

        Returns:
            str: the value of `compute_step_27` or None if not set
        """
        return self._data["Compute Step 27"]

    @compute_step_27.setter
    def compute_step_27(self, value=None):
        """  Corresponds to IDD Field `compute_step_27`

        Args:
            value (str): value for IDD Field `compute_step_27`
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
                                 'for field `compute_step_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_27`')

        self._data["Compute Step 27"] = value

    @property
    def compute_step_28(self):
        """Get compute_step_28

        Returns:
            str: the value of `compute_step_28` or None if not set
        """
        return self._data["Compute Step 28"]

    @compute_step_28.setter
    def compute_step_28(self, value=None):
        """  Corresponds to IDD Field `compute_step_28`

        Args:
            value (str): value for IDD Field `compute_step_28`
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
                                 'for field `compute_step_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_28`')

        self._data["Compute Step 28"] = value

    @property
    def compute_step_29(self):
        """Get compute_step_29

        Returns:
            str: the value of `compute_step_29` or None if not set
        """
        return self._data["Compute Step 29"]

    @compute_step_29.setter
    def compute_step_29(self, value=None):
        """  Corresponds to IDD Field `compute_step_29`

        Args:
            value (str): value for IDD Field `compute_step_29`
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
                                 'for field `compute_step_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_29`')

        self._data["Compute Step 29"] = value

    @property
    def compute_step_30(self):
        """Get compute_step_30

        Returns:
            str: the value of `compute_step_30` or None if not set
        """
        return self._data["Compute Step 30"]

    @compute_step_30.setter
    def compute_step_30(self, value=None):
        """  Corresponds to IDD Field `compute_step_30`

        Args:
            value (str): value for IDD Field `compute_step_30`
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
                                 'for field `compute_step_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_30`')

        self._data["Compute Step 30"] = value

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
        out.append(self._to_str(self.tariff_name))
        out.append(self._to_str(self.compute_step_1))
        out.append(self._to_str(self.compute_step_2))
        out.append(self._to_str(self.compute_step_3))
        out.append(self._to_str(self.compute_step_4))
        out.append(self._to_str(self.compute_step_5))
        out.append(self._to_str(self.compute_step_6))
        out.append(self._to_str(self.compute_step_7))
        out.append(self._to_str(self.compute_step_8))
        out.append(self._to_str(self.compute_step_9))
        out.append(self._to_str(self.compute_step_10))
        out.append(self._to_str(self.compute_step_11))
        out.append(self._to_str(self.compute_step_12))
        out.append(self._to_str(self.compute_step_13))
        out.append(self._to_str(self.compute_step_14))
        out.append(self._to_str(self.compute_step_15))
        out.append(self._to_str(self.compute_step_16))
        out.append(self._to_str(self.compute_step_17))
        out.append(self._to_str(self.compute_step_18))
        out.append(self._to_str(self.compute_step_19))
        out.append(self._to_str(self.compute_step_20))
        out.append(self._to_str(self.compute_step_21))
        out.append(self._to_str(self.compute_step_22))
        out.append(self._to_str(self.compute_step_23))
        out.append(self._to_str(self.compute_step_24))
        out.append(self._to_str(self.compute_step_25))
        out.append(self._to_str(self.compute_step_26))
        out.append(self._to_str(self.compute_step_27))
        out.append(self._to_str(self.compute_step_28))
        out.append(self._to_str(self.compute_step_29))
        out.append(self._to_str(self.compute_step_30))
        return ",".join(out)