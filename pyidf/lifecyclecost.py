from collections import OrderedDict

class LifeCycleCostParameters(object):
    """ Corresponds to IDD object `LifeCycleCost:Parameters`
        Provides inputs related to the overall life-cycle analysis. It establishes many of
        the assumptions used in computing the present value. It is important that when
        comparing the results of multiple simulations that the fields in the
        LifeCycleCost:Parameters objects are the same for all the simulations. When this
        object is present the tabular report file will contain the Life-Cycle Cost Report.
    """
    internal_name = "LifeCycleCost:Parameters"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LifeCycleCost:Parameters`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Discounting Convention"] = None
        self._data["Inflation Approach"] = None
        self._data["Real Discount Rate"] = None
        self._data["Nominal Discount Rate"] = None
        self._data["Inflation"] = None
        self._data["Base Date Month"] = None
        self._data["Base Date Year"] = None
        self._data["Service Date Month"] = None
        self._data["Service Date Year"] = None
        self._data["Length of Study Period in Years"] = None
        self._data["Tax rate"] = None
        self._data["Depreciation Method"] = None

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
            self.discounting_convention = None
        else:
            self.discounting_convention = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inflation_approach = None
        else:
            self.inflation_approach = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.real_discount_rate = None
        else:
            self.real_discount_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_discount_rate = None
        else:
            self.nominal_discount_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inflation = None
        else:
            self.inflation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.base_date_month = None
        else:
            self.base_date_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.base_date_year = None
        else:
            self.base_date_year = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.service_date_month = None
        else:
            self.service_date_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.service_date_year = None
        else:
            self.service_date_year = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length_of_study_period_in_years = None
        else:
            self.length_of_study_period_in_years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tax_rate = None
        else:
            self.tax_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.depreciation_method = None
        else:
            self.depreciation_method = vals[i]
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
    def discounting_convention(self):
        """Get discounting_convention

        Returns:
            str: the value of `discounting_convention` or None if not set
        """
        return self._data["Discounting Convention"]

    @discounting_convention.setter
    def discounting_convention(self, value="EndOfYear"):
        """  Corresponds to IDD Field `discounting_convention`
        The field specifies if the discounting of future costs should be computed as occurring at the end
        of each year or the middle of each year or the beginning of each year. The most common discounting
        convention uses the end of each year.

        Args:
            value (str): value for IDD Field `discounting_convention`
                Accepted values are:
                      - EndOfYear
                      - MidYear
                      - BeginningOfYear
                Default value: EndOfYear
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
                                 'for field `discounting_convention`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discounting_convention`')
            vals = set()
            vals.add("EndOfYear")
            vals.add("MidYear")
            vals.add("BeginningOfYear")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `discounting_convention`'.format(value))

        self._data["Discounting Convention"] = value

    @property
    def inflation_approach(self):
        """Get inflation_approach

        Returns:
            str: the value of `inflation_approach` or None if not set
        """
        return self._data["Inflation Approach"]

    @inflation_approach.setter
    def inflation_approach(self, value="ConstantDollar"):
        """  Corresponds to IDD Field `inflation_approach`
        This field is used to determine if the analysis should use constant dollars or current dollars
        which is related to how inflation is treated. If ConstantDollar is selected then the Real Discount
        Rate input is used and it excludes the rate of inflation. If CurrentDollar is selected then the
        Nominal Discount Rate input is used and it includes the rate of inflation.

        Args:
            value (str): value for IDD Field `inflation_approach`
                Accepted values are:
                      - ConstantDollar
                      - CurrentDollar
                Default value: ConstantDollar
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
                                 'for field `inflation_approach`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inflation_approach`')
            vals = set()
            vals.add("ConstantDollar")
            vals.add("CurrentDollar")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `inflation_approach`'.format(value))

        self._data["Inflation Approach"] = value

    @property
    def real_discount_rate(self):
        """Get real_discount_rate

        Returns:
            float: the value of `real_discount_rate` or None if not set
        """
        return self._data["Real Discount Rate"]

    @real_discount_rate.setter
    def real_discount_rate(self, value=None):
        """  Corresponds to IDD Field `real_discount_rate`
        Enter the real discount rate as a decimal. For a 3% rate enter the value 0.03. This input is
        used when the Inflation Approach is ConstantDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when
        general inflation is ignored. When Inflation Approach is set to CurrentDollar this input is ignored.

        Args:
            value (float): value for IDD Field `real_discount_rate`
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
                                 'for field `real_discount_rate`'.format(value))

        self._data["Real Discount Rate"] = value

    @property
    def nominal_discount_rate(self):
        """Get nominal_discount_rate

        Returns:
            float: the value of `nominal_discount_rate` or None if not set
        """
        return self._data["Nominal Discount Rate"]

    @nominal_discount_rate.setter
    def nominal_discount_rate(self, value=None):
        """  Corresponds to IDD Field `nominal_discount_rate`
        Enter the nominal discount rate as a decimal. For a 5% rate enter the value 0.05. This input
        is used when the Inflation Approach is CurrentDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when general
        inflation is included. When Inflation Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `nominal_discount_rate`
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
                                 'for field `nominal_discount_rate`'.format(value))

        self._data["Nominal Discount Rate"] = value

    @property
    def inflation(self):
        """Get inflation

        Returns:
            float: the value of `inflation` or None if not set
        """
        return self._data["Inflation"]

    @inflation.setter
    def inflation(self, value=None):
        """  Corresponds to IDD Field `inflation`
        Enter the rate of inflation for general goods and services as a decimal. For a 2% rate enter
        the value 0.02.

        Args:
            value (float): value for IDD Field `inflation`
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
                                 'for field `inflation`'.format(value))

        self._data["Inflation"] = value

    @property
    def base_date_month(self):
        """Get base_date_month

        Returns:
            str: the value of `base_date_month` or None if not set
        """
        return self._data["Base Date Month"]

    @base_date_month.setter
    def base_date_month(self, value="January"):
        """  Corresponds to IDD Field `base_date_month`
        Enter the month that is the beginning of study period also known as the beginning of the base period.

        Args:
            value (str): value for IDD Field `base_date_month`
                Accepted values are:
                      - January
                      - February
                      - March
                      - April
                      - May
                      - June
                      - July
                      - August
                      - September
                      - October
                      - November
                      - December
                Default value: January
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
                                 'for field `base_date_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `base_date_month`')
            vals = set()
            vals.add("January")
            vals.add("February")
            vals.add("March")
            vals.add("April")
            vals.add("May")
            vals.add("June")
            vals.add("July")
            vals.add("August")
            vals.add("September")
            vals.add("October")
            vals.add("November")
            vals.add("December")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `base_date_month`'.format(value))

        self._data["Base Date Month"] = value

    @property
    def base_date_year(self):
        """Get base_date_year

        Returns:
            int: the value of `base_date_year` or None if not set
        """
        return self._data["Base Date Year"]

    @base_date_year.setter
    def base_date_year(self, value=None):
        """  Corresponds to IDD Field `base_date_year`
        Enter the four digit year that is the beginning of study period such as 2010. The study period is
        also known as the base period.

        Args:
            value (int): value for IDD Field `base_date_year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `base_date_year`'.format(value))
            if value < 1900:
                raise ValueError('value need to be greater or equal 1900 '
                                 'for field `base_date_year`')
            if value > 2100:
                raise ValueError('value need to be smaller 2100 '
                                 'for field `base_date_year`')

        self._data["Base Date Year"] = value

    @property
    def service_date_month(self):
        """Get service_date_month

        Returns:
            str: the value of `service_date_month` or None if not set
        """
        return self._data["Service Date Month"]

    @service_date_month.setter
    def service_date_month(self, value="January"):
        """  Corresponds to IDD Field `service_date_month`
        Enter the month that is the beginning of building occupancy. Energy costs computed by EnergyPlus
        are assumed to occur during the year following the service date. The service date must be the
        same or later than the Base Date. This field could also be referred to as part of beneficial
        occupancy date.

        Args:
            value (str): value for IDD Field `service_date_month`
                Accepted values are:
                      - January
                      - February
                      - March
                      - April
                      - May
                      - June
                      - July
                      - August
                      - September
                      - October
                      - November
                      - December
                Default value: January
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
                                 'for field `service_date_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `service_date_month`')
            vals = set()
            vals.add("January")
            vals.add("February")
            vals.add("March")
            vals.add("April")
            vals.add("May")
            vals.add("June")
            vals.add("July")
            vals.add("August")
            vals.add("September")
            vals.add("October")
            vals.add("November")
            vals.add("December")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `service_date_month`'.format(value))

        self._data["Service Date Month"] = value

    @property
    def service_date_year(self):
        """Get service_date_year

        Returns:
            int: the value of `service_date_year` or None if not set
        """
        return self._data["Service Date Year"]

    @service_date_year.setter
    def service_date_year(self, value=None):
        """  Corresponds to IDD Field `service_date_year`
        Enter the four digit year that is the beginning of occupancy such as 2010.

        Args:
            value (int): value for IDD Field `service_date_year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `service_date_year`'.format(value))
            if value < 1900:
                raise ValueError('value need to be greater or equal 1900 '
                                 'for field `service_date_year`')
            if value > 2100:
                raise ValueError('value need to be smaller 2100 '
                                 'for field `service_date_year`')

        self._data["Service Date Year"] = value

    @property
    def length_of_study_period_in_years(self):
        """Get length_of_study_period_in_years

        Returns:
            int: the value of `length_of_study_period_in_years` or None if not set
        """
        return self._data["Length of Study Period in Years"]

    @length_of_study_period_in_years.setter
    def length_of_study_period_in_years(self, value=None):
        """  Corresponds to IDD Field `length_of_study_period_in_years`
        Enter the number of years of the study period. It is the number of years that the study continues
        based on the start at the base date. The default value is 25 years. Only integers may be used
        indicating whole years.

        Args:
            value (int): value for IDD Field `length_of_study_period_in_years`
                value >= 1
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `length_of_study_period_in_years`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `length_of_study_period_in_years`')
            if value > 100:
                raise ValueError('value need to be smaller 100 '
                                 'for field `length_of_study_period_in_years`')

        self._data["Length of Study Period in Years"] = value

    @property
    def tax_rate(self):
        """Get tax_rate

        Returns:
            float: the value of `tax_rate` or None if not set
        """
        return self._data["Tax rate"]

    @tax_rate.setter
    def tax_rate(self, value=None):
        """  Corresponds to IDD Field `tax_rate`
        Enter the overall marginal tax rate for the project costs. This does not include energy or water
        taxes. The tax rate entered should be based on the marginal tax rate for the entity and not the
        average tax rate. Enter the tax rate results in present value calculations after taxes. Most
        analyses do not factor in the impact of taxes and assume that all options under consideration
        have roughly the same tax impact. Due to this many times the tax rate can be left to default
        to zero and the present value results before taxes are used to make decisions. The value
        should be entered as a decimal value. For 15% enter 0.15. For an analysis that does not include
        tax impacts enter 0.0.

        Args:
            value (float): value for IDD Field `tax_rate`
                value >= 0.0
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
                                 'for field `tax_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tax_rate`')

        self._data["Tax rate"] = value

    @property
    def depreciation_method(self):
        """Get depreciation_method

        Returns:
            str: the value of `depreciation_method` or None if not set
        """
        return self._data["Depreciation Method"]

    @depreciation_method.setter
    def depreciation_method(self, value="None"):
        """  Corresponds to IDD Field `depreciation_method`
        For an analysis that includes income tax impacts this entry describes how capital costs are
        depreciated. Only one depreciation method may be used for an analysis and is applied to all
        capital expenditures.

        Args:
            value (str): value for IDD Field `depreciation_method`
                Accepted values are:
                      - ModifiedAcceleratedCostRecoverySystem-3year
                      - ModifiedAcceleratedCostRecoverySystem-5year
                      - ModifiedAcceleratedCostRecoverySystem-7year
                      - ModifiedAcceleratedCostRecoverySystem-10year
                      - ModifiedAcceleratedCostRecoverySystem-15year
                      - ModifiedAcceleratedCostRecoverySystem-20year
                      - StraightLine-27year
                      - StraightLine-31year
                      - StraightLine-39year
                      - StraightLine-40year
                      - None
                Default value: None
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
                                 'for field `depreciation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `depreciation_method`')
            vals = set()
            vals.add("ModifiedAcceleratedCostRecoverySystem-3year")
            vals.add("ModifiedAcceleratedCostRecoverySystem-5year")
            vals.add("ModifiedAcceleratedCostRecoverySystem-7year")
            vals.add("ModifiedAcceleratedCostRecoverySystem-10year")
            vals.add("ModifiedAcceleratedCostRecoverySystem-15year")
            vals.add("ModifiedAcceleratedCostRecoverySystem-20year")
            vals.add("StraightLine-27year")
            vals.add("StraightLine-31year")
            vals.add("StraightLine-39year")
            vals.add("StraightLine-40year")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `depreciation_method`'.format(value))

        self._data["Depreciation Method"] = value

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
        out.append(self._to_str(self.discounting_convention))
        out.append(self._to_str(self.inflation_approach))
        out.append(self._to_str(self.real_discount_rate))
        out.append(self._to_str(self.nominal_discount_rate))
        out.append(self._to_str(self.inflation))
        out.append(self._to_str(self.base_date_month))
        out.append(self._to_str(self.base_date_year))
        out.append(self._to_str(self.service_date_month))
        out.append(self._to_str(self.service_date_year))
        out.append(self._to_str(self.length_of_study_period_in_years))
        out.append(self._to_str(self.tax_rate))
        out.append(self._to_str(self.depreciation_method))
        return ",".join(out)

class LifeCycleCostRecurringCosts(object):
    """ Corresponds to IDD object `LifeCycleCost:RecurringCosts`
        Recurring costs are costs that repeat over time on a regular schedule during the
        study period. If costs associated with equipment do repeat but not on a regular
        schedule, use LifeCycleCost:NonrecurringCost objects instead.
    """
    internal_name = "LifeCycleCost:RecurringCosts"
    field_count = 9

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LifeCycleCost:RecurringCosts`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Category"] = None
        self._data["Cost"] = None
        self._data["Start of Costs"] = None
        self._data["Years from Start"] = None
        self._data["Months from Start"] = None
        self._data["Repeat Period Years"] = None
        self._data["Repeat Period Months"] = None
        self._data["Annual escalation rate"] = None

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
            self.category = None
        else:
            self.category = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost = None
        else:
            self.cost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_of_costs = None
        else:
            self.start_of_costs = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.years_from_start = None
        else:
            self.years_from_start = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.months_from_start = None
        else:
            self.months_from_start = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.repeat_period_years = None
        else:
            self.repeat_period_years = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.repeat_period_months = None
        else:
            self.repeat_period_months = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.annual_escalation_rate = None
        else:
            self.annual_escalation_rate = vals[i]
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
    def category(self):
        """Get category

        Returns:
            str: the value of `category` or None if not set
        """
        return self._data["Category"]

    @category.setter
    def category(self, value="Maintenance"):
        """  Corresponds to IDD Field `category`

        Args:
            value (str): value for IDD Field `category`
                Accepted values are:
                      - Maintenance
                      - Repair
                      - Operation
                      - Replacement
                      - MinorOverhaul
                      - MajorOverhaul
                      - OtherOperational
                Default value: Maintenance
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
                                 'for field `category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category`')
            vals = set()
            vals.add("Maintenance")
            vals.add("Repair")
            vals.add("Operation")
            vals.add("Replacement")
            vals.add("MinorOverhaul")
            vals.add("MajorOverhaul")
            vals.add("OtherOperational")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `category`'.format(value))

        self._data["Category"] = value

    @property
    def cost(self):
        """Get cost

        Returns:
            float: the value of `cost` or None if not set
        """
        return self._data["Cost"]

    @cost.setter
    def cost(self, value=None):
        """  Corresponds to IDD Field `cost`
        Enter the cost in dollars (or the appropriate monetary unit) for the recurring costs. Enter
        the cost for each time it occurs. For example if the annual maintenance cost is 500 dolllars
        enter 500 here.

        Args:
            value (float): value for IDD Field `cost`
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
                                 'for field `cost`'.format(value))

        self._data["Cost"] = value

    @property
    def start_of_costs(self):
        """Get start_of_costs

        Returns:
            str: the value of `start_of_costs` or None if not set
        """
        return self._data["Start of Costs"]

    @start_of_costs.setter
    def start_of_costs(self, value="ServicePeriod"):
        """  Corresponds to IDD Field `start_of_costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most maintenance costs the Start of Costs should be Service Period.

        Args:
            value (str): value for IDD Field `start_of_costs`
                Accepted values are:
                      - ServicePeriod
                      - BasePeriod
                Default value: ServicePeriod
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
                                 'for field `start_of_costs`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_of_costs`')
            vals = set()
            vals.add("ServicePeriod")
            vals.add("BasePeriod")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `start_of_costs`'.format(value))

        self._data["Start of Costs"] = value

    @property
    def years_from_start(self):
        """Get years_from_start

        Returns:
            int: the value of `years_from_start` or None if not set
        """
        return self._data["Years from Start"]

    @years_from_start.setter
    def years_from_start(self, value=None):
        """  Corresponds to IDD Field `years_from_start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `years_from_start`
                value >= 0
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `years_from_start`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `years_from_start`')
            if value > 100:
                raise ValueError('value need to be smaller 100 '
                                 'for field `years_from_start`')

        self._data["Years from Start"] = value

    @property
    def months_from_start(self):
        """Get months_from_start

        Returns:
            int: the value of `months_from_start` or None if not set
        """
        return self._data["Months from Start"]

    @months_from_start.setter
    def months_from_start(self, value=None):
        """  Corresponds to IDD Field `months_from_start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `months_from_start`
                value >= 0
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `months_from_start`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `months_from_start`')
            if value > 1200:
                raise ValueError('value need to be smaller 1200 '
                                 'for field `months_from_start`')

        self._data["Months from Start"] = value

    @property
    def repeat_period_years(self):
        """Get repeat_period_years

        Returns:
            int: the value of `repeat_period_years` or None if not set
        """
        return self._data["Repeat Period Years"]

    @repeat_period_years.setter
    def repeat_period_years(self, value=1 ):
        """  Corresponds to IDD Field `repeat_period_years`
        This field and the Repeat Period Months field indicate how much time elapses between
        reoccurrences of the cost. For costs that occur every year such the Repeat Period Years
        should be 1 and Repeat Period Months should be 0. Only integers should be entered
        representing whole years.

        Args:
            value (int): value for IDD Field `repeat_period_years`
                Default value: 1
                value >= 0
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `repeat_period_years`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `repeat_period_years`')
            if value > 100:
                raise ValueError('value need to be smaller 100 '
                                 'for field `repeat_period_years`')

        self._data["Repeat Period Years"] = value

    @property
    def repeat_period_months(self):
        """Get repeat_period_months

        Returns:
            int: the value of `repeat_period_months` or None if not set
        """
        return self._data["Repeat Period Months"]

    @repeat_period_months.setter
    def repeat_period_months(self, value=0 ):
        """  Corresponds to IDD Field `repeat_period_months`
        This field and the Repeat Period Years field indicate how much time elapses between
        reoccurrences of the cost. Only integers should be entered representing whole years.
        The Repeat Period Years (times 12) and Repeat Period Months are added together.

        Args:
            value (int): value for IDD Field `repeat_period_months`
                Default value: 0
                value >= 0
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `repeat_period_months`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `repeat_period_months`')
            if value > 1200:
                raise ValueError('value need to be smaller 1200 '
                                 'for field `repeat_period_months`')

        self._data["Repeat Period Months"] = value

    @property
    def annual_escalation_rate(self):
        """Get annual_escalation_rate

        Returns:
            float: the value of `annual_escalation_rate` or None if not set
        """
        return self._data["Annual escalation rate"]

    @annual_escalation_rate.setter
    def annual_escalation_rate(self, value=None):
        """  Corresponds to IDD Field `annual_escalation_rate`
        Enter the annual escalation rate as a decimal. For a 1% rate enter the value 0.01.
        This input is used when the Inflation Approach is CurrentDollar. When Inflation
        Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `annual_escalation_rate`
                value >= -0.3
                value <= 0.3
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
                                 'for field `annual_escalation_rate`'.format(value))
            if value < -0.3:
                raise ValueError('value need to be greater or equal -0.3 '
                                 'for field `annual_escalation_rate`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `annual_escalation_rate`')

        self._data["Annual escalation rate"] = value

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
        out.append(self._to_str(self.category))
        out.append(self._to_str(self.cost))
        out.append(self._to_str(self.start_of_costs))
        out.append(self._to_str(self.years_from_start))
        out.append(self._to_str(self.months_from_start))
        out.append(self._to_str(self.repeat_period_years))
        out.append(self._to_str(self.repeat_period_months))
        out.append(self._to_str(self.annual_escalation_rate))
        return ",".join(out)

class LifeCycleCostNonrecurringCost(object):
    """ Corresponds to IDD object `LifeCycleCost:NonrecurringCost`
        A non-recurring cost happens only once during the study period. For costs that occur
        more than once during the study period on a regular schedule, use the
        LifeCycleCost:RecurringCost object.
    """
    internal_name = "LifeCycleCost:NonrecurringCost"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LifeCycleCost:NonrecurringCost`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Category"] = None
        self._data["Cost"] = None
        self._data["Start of Costs"] = None
        self._data["Years from Start"] = None
        self._data["Months from Start"] = None

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
            self.category = None
        else:
            self.category = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cost = None
        else:
            self.cost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.start_of_costs = None
        else:
            self.start_of_costs = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.years_from_start = None
        else:
            self.years_from_start = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.months_from_start = None
        else:
            self.months_from_start = vals[i]
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
    def category(self):
        """Get category

        Returns:
            str: the value of `category` or None if not set
        """
        return self._data["Category"]

    @category.setter
    def category(self, value="Construction"):
        """  Corresponds to IDD Field `category`

        Args:
            value (str): value for IDD Field `category`
                Accepted values are:
                      - Construction
                      - Salvage
                      - OtherCapital
                Default value: Construction
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
                                 'for field `category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category`')
            vals = set()
            vals.add("Construction")
            vals.add("Salvage")
            vals.add("OtherCapital")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `category`'.format(value))

        self._data["Category"] = value

    @property
    def cost(self):
        """Get cost

        Returns:
            float: the value of `cost` or None if not set
        """
        return self._data["Cost"]

    @cost.setter
    def cost(self, value=None):
        """  Corresponds to IDD Field `cost`
        Enter the non-recurring cost value. For construction and other capital costs the value
        entered is typically a positive value. For salvage costs the value entered is typically a
        negative value which represents the money paid to the investor for the equipment at the
        end of the study period.

        Args:
            value (float): value for IDD Field `cost`
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
                                 'for field `cost`'.format(value))

        self._data["Cost"] = value

    @property
    def start_of_costs(self):
        """Get start_of_costs

        Returns:
            str: the value of `start_of_costs` or None if not set
        """
        return self._data["Start of Costs"]

    @start_of_costs.setter
    def start_of_costs(self, value="ServicePeriod"):
        """  Corresponds to IDD Field `start_of_costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most non-recurring costs the Start of Costs should be Base Period which
        begins at the base month and year.

        Args:
            value (str): value for IDD Field `start_of_costs`
                Accepted values are:
                      - ServicePeriod
                      - BasePeriod
                Default value: ServicePeriod
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
                                 'for field `start_of_costs`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_of_costs`')
            vals = set()
            vals.add("ServicePeriod")
            vals.add("BasePeriod")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `start_of_costs`'.format(value))

        self._data["Start of Costs"] = value

    @property
    def years_from_start(self):
        """Get years_from_start

        Returns:
            int: the value of `years_from_start` or None if not set
        """
        return self._data["Years from Start"]

    @years_from_start.setter
    def years_from_start(self, value=None):
        """  Corresponds to IDD Field `years_from_start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `years_from_start`
                value >= 0
                value <= 100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `years_from_start`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `years_from_start`')
            if value > 100:
                raise ValueError('value need to be smaller 100 '
                                 'for field `years_from_start`')

        self._data["Years from Start"] = value

    @property
    def months_from_start(self):
        """Get months_from_start

        Returns:
            int: the value of `months_from_start` or None if not set
        """
        return self._data["Months from Start"]

    @months_from_start.setter
    def months_from_start(self, value=None):
        """  Corresponds to IDD Field `months_from_start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `months_from_start`
                value >= 0
                value <= 1200
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `months_from_start`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `months_from_start`')
            if value > 1200:
                raise ValueError('value need to be smaller 1200 '
                                 'for field `months_from_start`')

        self._data["Months from Start"] = value

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
        out.append(self._to_str(self.category))
        out.append(self._to_str(self.cost))
        out.append(self._to_str(self.start_of_costs))
        out.append(self._to_str(self.years_from_start))
        out.append(self._to_str(self.months_from_start))
        return ",".join(out)

class LifeCycleCostUsePriceEscalation(object):
    """ Corresponds to IDD object `LifeCycleCost:UsePriceEscalation`
        Life cycle cost escalation factors. The values for this object may be found in the
        annual supplement to NIST Handbook 135 in Tables Ca-1 to Ca-5 and are included in an
        EnergyPlus dataset file.
    """
    internal_name = "LifeCycleCost:UsePriceEscalation"
    field_count = 34

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LifeCycleCost:UsePriceEscalation`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Resource"] = None
        self._data["Escalation Start Year"] = None
        self._data["Escalation Start Month"] = None
        self._data["Year 1 Escalation"] = None
        self._data["Year 2 Escalation"] = None
        self._data["Year 3 Escalation"] = None
        self._data["Year 4 Escalation"] = None
        self._data["Year 5 Escalation"] = None
        self._data["Year 6 Escalation"] = None
        self._data["Year 7 Escalation"] = None
        self._data["Year 8 Escalation"] = None
        self._data["Year 9 Escalation"] = None
        self._data["Year 10 Escalation"] = None
        self._data["Year 11 Escalation"] = None
        self._data["Year 12 Escalation"] = None
        self._data["Year 13 Escalation"] = None
        self._data["Year 14 Escalation"] = None
        self._data["Year 15 Escalation"] = None
        self._data["Year 16 Escalation"] = None
        self._data["Year 17 Escalation"] = None
        self._data["Year 18 Escalation"] = None
        self._data["Year 19 Escalation"] = None
        self._data["Year 20 Escalation"] = None
        self._data["Year 21 Escalation"] = None
        self._data["Year 22 Escalation"] = None
        self._data["Year 23 Escalation"] = None
        self._data["Year 24 Escalation"] = None
        self._data["Year 25 Escalation"] = None
        self._data["Year 26 Escalation"] = None
        self._data["Year 27 Escalation"] = None
        self._data["Year 28 Escalation"] = None
        self._data["Year 29 Escalation"] = None
        self._data["Year 30 Escalation"] = None

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
            self.resource = None
        else:
            self.resource = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.escalation_start_year = None
        else:
            self.escalation_start_year = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.escalation_start_month = None
        else:
            self.escalation_start_month = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_1_escalation = None
        else:
            self.year_1_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_2_escalation = None
        else:
            self.year_2_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_3_escalation = None
        else:
            self.year_3_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_4_escalation = None
        else:
            self.year_4_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_5_escalation = None
        else:
            self.year_5_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_6_escalation = None
        else:
            self.year_6_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_7_escalation = None
        else:
            self.year_7_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_8_escalation = None
        else:
            self.year_8_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_9_escalation = None
        else:
            self.year_9_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_10_escalation = None
        else:
            self.year_10_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_11_escalation = None
        else:
            self.year_11_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_12_escalation = None
        else:
            self.year_12_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_13_escalation = None
        else:
            self.year_13_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_14_escalation = None
        else:
            self.year_14_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_15_escalation = None
        else:
            self.year_15_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_16_escalation = None
        else:
            self.year_16_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_17_escalation = None
        else:
            self.year_17_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_18_escalation = None
        else:
            self.year_18_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_19_escalation = None
        else:
            self.year_19_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_20_escalation = None
        else:
            self.year_20_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_21_escalation = None
        else:
            self.year_21_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_22_escalation = None
        else:
            self.year_22_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_23_escalation = None
        else:
            self.year_23_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_24_escalation = None
        else:
            self.year_24_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_25_escalation = None
        else:
            self.year_25_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_26_escalation = None
        else:
            self.year_26_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_27_escalation = None
        else:
            self.year_27_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_28_escalation = None
        else:
            self.year_28_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_29_escalation = None
        else:
            self.year_29_escalation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_30_escalation = None
        else:
            self.year_30_escalation = vals[i]
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
        The identifier used for the object. The name usually identifies the location (such as the
        state or region or country or census area) that the escalations apply to. In addition the
        name should identify the building class such as residential or commercial or industrial
        and the use type such as electricity or natural gas or water.

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
    def resource(self):
        """Get resource

        Returns:
            str: the value of `resource` or None if not set
        """
        return self._data["Resource"]

    @resource.setter
    def resource(self, value=None):
        """  Corresponds to IDD Field `resource`

        Args:
            value (str): value for IDD Field `resource`
                Accepted values are:
                      - Electricity
                      - ElectricityPurchased
                      - ElectricityProduced
                      - ElectricitySurplusSold
                      - ElectricityNet
                      - NaturalGas
                      - Steam
                      - Gasoline
                      - Diesel
                      - Coal
                      - FuelOil#1
                      - FuelOil#2
                      - Propane
                      - OtherFuel1
                      - OtherFuel2
                      - Water
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
                                 'for field `resource`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource`')
            vals = set()
            vals.add("Electricity")
            vals.add("ElectricityPurchased")
            vals.add("ElectricityProduced")
            vals.add("ElectricitySurplusSold")
            vals.add("ElectricityNet")
            vals.add("NaturalGas")
            vals.add("Steam")
            vals.add("Gasoline")
            vals.add("Diesel")
            vals.add("Coal")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Propane")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            vals.add("Water")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `resource`'.format(value))

        self._data["Resource"] = value

    @property
    def escalation_start_year(self):
        """Get escalation_start_year

        Returns:
            int: the value of `escalation_start_year` or None if not set
        """
        return self._data["Escalation Start Year"]

    @escalation_start_year.setter
    def escalation_start_year(self, value=None):
        """  Corresponds to IDD Field `escalation_start_year`
        This field and the Escalation Start Month define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Month
        define the time that escalation begins.

        Args:
            value (int): value for IDD Field `escalation_start_year`
                value >= 1900
                value <= 2100
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `escalation_start_year`'.format(value))
            if value < 1900:
                raise ValueError('value need to be greater or equal 1900 '
                                 'for field `escalation_start_year`')
            if value > 2100:
                raise ValueError('value need to be smaller 2100 '
                                 'for field `escalation_start_year`')

        self._data["Escalation Start Year"] = value

    @property
    def escalation_start_month(self):
        """Get escalation_start_month

        Returns:
            str: the value of `escalation_start_month` or None if not set
        """
        return self._data["Escalation Start Month"]

    @escalation_start_month.setter
    def escalation_start_month(self, value="January"):
        """  Corresponds to IDD Field `escalation_start_month`
        This field and the Escalation Start Year define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Year
        define the time that escalation begins.

        Args:
            value (str): value for IDD Field `escalation_start_month`
                Accepted values are:
                      - January
                      - February
                      - March
                      - April
                      - May
                      - June
                      - July
                      - August
                      - September
                      - October
                      - November
                      - December
                Default value: January
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
                                 'for field `escalation_start_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `escalation_start_month`')
            vals = set()
            vals.add("January")
            vals.add("February")
            vals.add("March")
            vals.add("April")
            vals.add("May")
            vals.add("June")
            vals.add("July")
            vals.add("August")
            vals.add("September")
            vals.add("October")
            vals.add("November")
            vals.add("December")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `escalation_start_month`'.format(value))

        self._data["Escalation Start Month"] = value

    @property
    def year_1_escalation(self):
        """Get year_1_escalation

        Returns:
            float: the value of `year_1_escalation` or None if not set
        """
        return self._data["Year 1 Escalation"]

    @year_1_escalation.setter
    def year_1_escalation(self, value=None):
        """  Corresponds to IDD Field `year_1_escalation`
        The escalation in price of the energy or water use for the first year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_1_escalation`
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
                                 'for field `year_1_escalation`'.format(value))

        self._data["Year 1 Escalation"] = value

    @property
    def year_2_escalation(self):
        """Get year_2_escalation

        Returns:
            float: the value of `year_2_escalation` or None if not set
        """
        return self._data["Year 2 Escalation"]

    @year_2_escalation.setter
    def year_2_escalation(self, value=None):
        """  Corresponds to IDD Field `year_2_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_2_escalation`
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
                                 'for field `year_2_escalation`'.format(value))

        self._data["Year 2 Escalation"] = value

    @property
    def year_3_escalation(self):
        """Get year_3_escalation

        Returns:
            float: the value of `year_3_escalation` or None if not set
        """
        return self._data["Year 3 Escalation"]

    @year_3_escalation.setter
    def year_3_escalation(self, value=None):
        """  Corresponds to IDD Field `year_3_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_3_escalation`
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
                                 'for field `year_3_escalation`'.format(value))

        self._data["Year 3 Escalation"] = value

    @property
    def year_4_escalation(self):
        """Get year_4_escalation

        Returns:
            float: the value of `year_4_escalation` or None if not set
        """
        return self._data["Year 4 Escalation"]

    @year_4_escalation.setter
    def year_4_escalation(self, value=None):
        """  Corresponds to IDD Field `year_4_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_4_escalation`
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
                                 'for field `year_4_escalation`'.format(value))

        self._data["Year 4 Escalation"] = value

    @property
    def year_5_escalation(self):
        """Get year_5_escalation

        Returns:
            float: the value of `year_5_escalation` or None if not set
        """
        return self._data["Year 5 Escalation"]

    @year_5_escalation.setter
    def year_5_escalation(self, value=None):
        """  Corresponds to IDD Field `year_5_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_5_escalation`
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
                                 'for field `year_5_escalation`'.format(value))

        self._data["Year 5 Escalation"] = value

    @property
    def year_6_escalation(self):
        """Get year_6_escalation

        Returns:
            float: the value of `year_6_escalation` or None if not set
        """
        return self._data["Year 6 Escalation"]

    @year_6_escalation.setter
    def year_6_escalation(self, value=None):
        """  Corresponds to IDD Field `year_6_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_6_escalation`
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
                                 'for field `year_6_escalation`'.format(value))

        self._data["Year 6 Escalation"] = value

    @property
    def year_7_escalation(self):
        """Get year_7_escalation

        Returns:
            float: the value of `year_7_escalation` or None if not set
        """
        return self._data["Year 7 Escalation"]

    @year_7_escalation.setter
    def year_7_escalation(self, value=None):
        """  Corresponds to IDD Field `year_7_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_7_escalation`
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
                                 'for field `year_7_escalation`'.format(value))

        self._data["Year 7 Escalation"] = value

    @property
    def year_8_escalation(self):
        """Get year_8_escalation

        Returns:
            float: the value of `year_8_escalation` or None if not set
        """
        return self._data["Year 8 Escalation"]

    @year_8_escalation.setter
    def year_8_escalation(self, value=None):
        """  Corresponds to IDD Field `year_8_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_8_escalation`
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
                                 'for field `year_8_escalation`'.format(value))

        self._data["Year 8 Escalation"] = value

    @property
    def year_9_escalation(self):
        """Get year_9_escalation

        Returns:
            float: the value of `year_9_escalation` or None if not set
        """
        return self._data["Year 9 Escalation"]

    @year_9_escalation.setter
    def year_9_escalation(self, value=None):
        """  Corresponds to IDD Field `year_9_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_9_escalation`
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
                                 'for field `year_9_escalation`'.format(value))

        self._data["Year 9 Escalation"] = value

    @property
    def year_10_escalation(self):
        """Get year_10_escalation

        Returns:
            float: the value of `year_10_escalation` or None if not set
        """
        return self._data["Year 10 Escalation"]

    @year_10_escalation.setter
    def year_10_escalation(self, value=None):
        """  Corresponds to IDD Field `year_10_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_10_escalation`
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
                                 'for field `year_10_escalation`'.format(value))

        self._data["Year 10 Escalation"] = value

    @property
    def year_11_escalation(self):
        """Get year_11_escalation

        Returns:
            float: the value of `year_11_escalation` or None if not set
        """
        return self._data["Year 11 Escalation"]

    @year_11_escalation.setter
    def year_11_escalation(self, value=None):
        """  Corresponds to IDD Field `year_11_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_11_escalation`
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
                                 'for field `year_11_escalation`'.format(value))

        self._data["Year 11 Escalation"] = value

    @property
    def year_12_escalation(self):
        """Get year_12_escalation

        Returns:
            float: the value of `year_12_escalation` or None if not set
        """
        return self._data["Year 12 Escalation"]

    @year_12_escalation.setter
    def year_12_escalation(self, value=None):
        """  Corresponds to IDD Field `year_12_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_12_escalation`
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
                                 'for field `year_12_escalation`'.format(value))

        self._data["Year 12 Escalation"] = value

    @property
    def year_13_escalation(self):
        """Get year_13_escalation

        Returns:
            float: the value of `year_13_escalation` or None if not set
        """
        return self._data["Year 13 Escalation"]

    @year_13_escalation.setter
    def year_13_escalation(self, value=None):
        """  Corresponds to IDD Field `year_13_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_13_escalation`
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
                                 'for field `year_13_escalation`'.format(value))

        self._data["Year 13 Escalation"] = value

    @property
    def year_14_escalation(self):
        """Get year_14_escalation

        Returns:
            float: the value of `year_14_escalation` or None if not set
        """
        return self._data["Year 14 Escalation"]

    @year_14_escalation.setter
    def year_14_escalation(self, value=None):
        """  Corresponds to IDD Field `year_14_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_14_escalation`
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
                                 'for field `year_14_escalation`'.format(value))

        self._data["Year 14 Escalation"] = value

    @property
    def year_15_escalation(self):
        """Get year_15_escalation

        Returns:
            float: the value of `year_15_escalation` or None if not set
        """
        return self._data["Year 15 Escalation"]

    @year_15_escalation.setter
    def year_15_escalation(self, value=None):
        """  Corresponds to IDD Field `year_15_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_15_escalation`
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
                                 'for field `year_15_escalation`'.format(value))

        self._data["Year 15 Escalation"] = value

    @property
    def year_16_escalation(self):
        """Get year_16_escalation

        Returns:
            float: the value of `year_16_escalation` or None if not set
        """
        return self._data["Year 16 Escalation"]

    @year_16_escalation.setter
    def year_16_escalation(self, value=None):
        """  Corresponds to IDD Field `year_16_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_16_escalation`
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
                                 'for field `year_16_escalation`'.format(value))

        self._data["Year 16 Escalation"] = value

    @property
    def year_17_escalation(self):
        """Get year_17_escalation

        Returns:
            float: the value of `year_17_escalation` or None if not set
        """
        return self._data["Year 17 Escalation"]

    @year_17_escalation.setter
    def year_17_escalation(self, value=None):
        """  Corresponds to IDD Field `year_17_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_17_escalation`
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
                                 'for field `year_17_escalation`'.format(value))

        self._data["Year 17 Escalation"] = value

    @property
    def year_18_escalation(self):
        """Get year_18_escalation

        Returns:
            float: the value of `year_18_escalation` or None if not set
        """
        return self._data["Year 18 Escalation"]

    @year_18_escalation.setter
    def year_18_escalation(self, value=None):
        """  Corresponds to IDD Field `year_18_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_18_escalation`
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
                                 'for field `year_18_escalation`'.format(value))

        self._data["Year 18 Escalation"] = value

    @property
    def year_19_escalation(self):
        """Get year_19_escalation

        Returns:
            float: the value of `year_19_escalation` or None if not set
        """
        return self._data["Year 19 Escalation"]

    @year_19_escalation.setter
    def year_19_escalation(self, value=None):
        """  Corresponds to IDD Field `year_19_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_19_escalation`
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
                                 'for field `year_19_escalation`'.format(value))

        self._data["Year 19 Escalation"] = value

    @property
    def year_20_escalation(self):
        """Get year_20_escalation

        Returns:
            float: the value of `year_20_escalation` or None if not set
        """
        return self._data["Year 20 Escalation"]

    @year_20_escalation.setter
    def year_20_escalation(self, value=None):
        """  Corresponds to IDD Field `year_20_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_20_escalation`
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
                                 'for field `year_20_escalation`'.format(value))

        self._data["Year 20 Escalation"] = value

    @property
    def year_21_escalation(self):
        """Get year_21_escalation

        Returns:
            float: the value of `year_21_escalation` or None if not set
        """
        return self._data["Year 21 Escalation"]

    @year_21_escalation.setter
    def year_21_escalation(self, value=None):
        """  Corresponds to IDD Field `year_21_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_21_escalation`
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
                                 'for field `year_21_escalation`'.format(value))

        self._data["Year 21 Escalation"] = value

    @property
    def year_22_escalation(self):
        """Get year_22_escalation

        Returns:
            float: the value of `year_22_escalation` or None if not set
        """
        return self._data["Year 22 Escalation"]

    @year_22_escalation.setter
    def year_22_escalation(self, value=None):
        """  Corresponds to IDD Field `year_22_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_22_escalation`
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
                                 'for field `year_22_escalation`'.format(value))

        self._data["Year 22 Escalation"] = value

    @property
    def year_23_escalation(self):
        """Get year_23_escalation

        Returns:
            float: the value of `year_23_escalation` or None if not set
        """
        return self._data["Year 23 Escalation"]

    @year_23_escalation.setter
    def year_23_escalation(self, value=None):
        """  Corresponds to IDD Field `year_23_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_23_escalation`
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
                                 'for field `year_23_escalation`'.format(value))

        self._data["Year 23 Escalation"] = value

    @property
    def year_24_escalation(self):
        """Get year_24_escalation

        Returns:
            float: the value of `year_24_escalation` or None if not set
        """
        return self._data["Year 24 Escalation"]

    @year_24_escalation.setter
    def year_24_escalation(self, value=None):
        """  Corresponds to IDD Field `year_24_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_24_escalation`
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
                                 'for field `year_24_escalation`'.format(value))

        self._data["Year 24 Escalation"] = value

    @property
    def year_25_escalation(self):
        """Get year_25_escalation

        Returns:
            float: the value of `year_25_escalation` or None if not set
        """
        return self._data["Year 25 Escalation"]

    @year_25_escalation.setter
    def year_25_escalation(self, value=None):
        """  Corresponds to IDD Field `year_25_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_25_escalation`
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
                                 'for field `year_25_escalation`'.format(value))

        self._data["Year 25 Escalation"] = value

    @property
    def year_26_escalation(self):
        """Get year_26_escalation

        Returns:
            float: the value of `year_26_escalation` or None if not set
        """
        return self._data["Year 26 Escalation"]

    @year_26_escalation.setter
    def year_26_escalation(self, value=None):
        """  Corresponds to IDD Field `year_26_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_26_escalation`
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
                                 'for field `year_26_escalation`'.format(value))

        self._data["Year 26 Escalation"] = value

    @property
    def year_27_escalation(self):
        """Get year_27_escalation

        Returns:
            float: the value of `year_27_escalation` or None if not set
        """
        return self._data["Year 27 Escalation"]

    @year_27_escalation.setter
    def year_27_escalation(self, value=None):
        """  Corresponds to IDD Field `year_27_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_27_escalation`
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
                                 'for field `year_27_escalation`'.format(value))

        self._data["Year 27 Escalation"] = value

    @property
    def year_28_escalation(self):
        """Get year_28_escalation

        Returns:
            float: the value of `year_28_escalation` or None if not set
        """
        return self._data["Year 28 Escalation"]

    @year_28_escalation.setter
    def year_28_escalation(self, value=None):
        """  Corresponds to IDD Field `year_28_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_28_escalation`
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
                                 'for field `year_28_escalation`'.format(value))

        self._data["Year 28 Escalation"] = value

    @property
    def year_29_escalation(self):
        """Get year_29_escalation

        Returns:
            float: the value of `year_29_escalation` or None if not set
        """
        return self._data["Year 29 Escalation"]

    @year_29_escalation.setter
    def year_29_escalation(self, value=None):
        """  Corresponds to IDD Field `year_29_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_29_escalation`
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
                                 'for field `year_29_escalation`'.format(value))

        self._data["Year 29 Escalation"] = value

    @property
    def year_30_escalation(self):
        """Get year_30_escalation

        Returns:
            float: the value of `year_30_escalation` or None if not set
        """
        return self._data["Year 30 Escalation"]

    @year_30_escalation.setter
    def year_30_escalation(self, value=None):
        """  Corresponds to IDD Field `year_30_escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `year_30_escalation`
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
                                 'for field `year_30_escalation`'.format(value))

        self._data["Year 30 Escalation"] = value

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
        out.append(self._to_str(self.resource))
        out.append(self._to_str(self.escalation_start_year))
        out.append(self._to_str(self.escalation_start_month))
        out.append(self._to_str(self.year_1_escalation))
        out.append(self._to_str(self.year_2_escalation))
        out.append(self._to_str(self.year_3_escalation))
        out.append(self._to_str(self.year_4_escalation))
        out.append(self._to_str(self.year_5_escalation))
        out.append(self._to_str(self.year_6_escalation))
        out.append(self._to_str(self.year_7_escalation))
        out.append(self._to_str(self.year_8_escalation))
        out.append(self._to_str(self.year_9_escalation))
        out.append(self._to_str(self.year_10_escalation))
        out.append(self._to_str(self.year_11_escalation))
        out.append(self._to_str(self.year_12_escalation))
        out.append(self._to_str(self.year_13_escalation))
        out.append(self._to_str(self.year_14_escalation))
        out.append(self._to_str(self.year_15_escalation))
        out.append(self._to_str(self.year_16_escalation))
        out.append(self._to_str(self.year_17_escalation))
        out.append(self._to_str(self.year_18_escalation))
        out.append(self._to_str(self.year_19_escalation))
        out.append(self._to_str(self.year_20_escalation))
        out.append(self._to_str(self.year_21_escalation))
        out.append(self._to_str(self.year_22_escalation))
        out.append(self._to_str(self.year_23_escalation))
        out.append(self._to_str(self.year_24_escalation))
        out.append(self._to_str(self.year_25_escalation))
        out.append(self._to_str(self.year_26_escalation))
        out.append(self._to_str(self.year_27_escalation))
        out.append(self._to_str(self.year_28_escalation))
        out.append(self._to_str(self.year_29_escalation))
        out.append(self._to_str(self.year_30_escalation))
        return ",".join(out)

class LifeCycleCostUseAdjustment(object):
    """ Corresponds to IDD object `LifeCycleCost:UseAdjustment`
        Used by advanced users to adjust the energy or water use costs for future years. This
        should not be used for compensating for inflation but should only be used to increase
        the costs of energy or water based on assumed changes to the actual usage, such as
        anticipated changes in the future function of the building. The adjustments begin at
        the start of the service period.
    """
    internal_name = "LifeCycleCost:UseAdjustment"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LifeCycleCost:UseAdjustment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Resource"] = None
        self._data["Year 1 Multiplier"] = None
        self._data["Year 2 Multiplier"] = None
        self._data["Year 3 Multiplier"] = None
        self._data["Year 4 Multiplier"] = None
        self._data["Year 5 Multiplier"] = None
        self._data["Year 6 Multiplier"] = None
        self._data["Year 7 Multiplier"] = None
        self._data["Year 8 Multiplier"] = None
        self._data["Year 9 Multiplier"] = None
        self._data["Year 10 Multiplier"] = None
        self._data["Year 11 Multiplier"] = None
        self._data["Year 12 Multiplier"] = None
        self._data["Year 13 Multiplier"] = None
        self._data["Year 14 Multiplier"] = None
        self._data["Year 15 Multiplier"] = None
        self._data["Year 16 Multiplier"] = None
        self._data["Year 17 Multiplier"] = None
        self._data["Year 18 Multiplier"] = None
        self._data["Year 19 Multiplier"] = None
        self._data["Year 20 Multiplier"] = None
        self._data["Year 21 Multiplier"] = None
        self._data["Year 22 Multiplier"] = None
        self._data["Year 23 Multiplier"] = None
        self._data["Year 24 Multiplier"] = None
        self._data["Year 25 Multiplier"] = None
        self._data["Year 26 Multiplier"] = None
        self._data["Year 27 Multiplier"] = None
        self._data["Year 28 Multiplier"] = None
        self._data["Year 29 Multiplier"] = None
        self._data["Year 30 Multiplier"] = None

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
            self.resource = None
        else:
            self.resource = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_1_multiplier = None
        else:
            self.year_1_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_2_multiplier = None
        else:
            self.year_2_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_3_multiplier = None
        else:
            self.year_3_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_4_multiplier = None
        else:
            self.year_4_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_5_multiplier = None
        else:
            self.year_5_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_6_multiplier = None
        else:
            self.year_6_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_7_multiplier = None
        else:
            self.year_7_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_8_multiplier = None
        else:
            self.year_8_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_9_multiplier = None
        else:
            self.year_9_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_10_multiplier = None
        else:
            self.year_10_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_11_multiplier = None
        else:
            self.year_11_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_12_multiplier = None
        else:
            self.year_12_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_13_multiplier = None
        else:
            self.year_13_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_14_multiplier = None
        else:
            self.year_14_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_15_multiplier = None
        else:
            self.year_15_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_16_multiplier = None
        else:
            self.year_16_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_17_multiplier = None
        else:
            self.year_17_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_18_multiplier = None
        else:
            self.year_18_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_19_multiplier = None
        else:
            self.year_19_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_20_multiplier = None
        else:
            self.year_20_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_21_multiplier = None
        else:
            self.year_21_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_22_multiplier = None
        else:
            self.year_22_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_23_multiplier = None
        else:
            self.year_23_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_24_multiplier = None
        else:
            self.year_24_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_25_multiplier = None
        else:
            self.year_25_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_26_multiplier = None
        else:
            self.year_26_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_27_multiplier = None
        else:
            self.year_27_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_28_multiplier = None
        else:
            self.year_28_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_29_multiplier = None
        else:
            self.year_29_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.year_30_multiplier = None
        else:
            self.year_30_multiplier = vals[i]
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
    def resource(self):
        """Get resource

        Returns:
            str: the value of `resource` or None if not set
        """
        return self._data["Resource"]

    @resource.setter
    def resource(self, value=None):
        """  Corresponds to IDD Field `resource`

        Args:
            value (str): value for IDD Field `resource`
                Accepted values are:
                      - Electricity
                      - ElectricityPurchased
                      - ElectricityProduced
                      - ElectricitySurplusSold
                      - ElectricityNet
                      - NaturalGas
                      - Steam
                      - Gasoline
                      - Diesel
                      - Coal
                      - FuelOil#1
                      - FuelOil#2
                      - Propane
                      - OtherFuel1
                      - OtherFuel2
                      - Water
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
                                 'for field `resource`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource`')
            vals = set()
            vals.add("Electricity")
            vals.add("ElectricityPurchased")
            vals.add("ElectricityProduced")
            vals.add("ElectricitySurplusSold")
            vals.add("ElectricityNet")
            vals.add("NaturalGas")
            vals.add("Steam")
            vals.add("Gasoline")
            vals.add("Diesel")
            vals.add("Coal")
            vals.add("FuelOil#1")
            vals.add("FuelOil#2")
            vals.add("Propane")
            vals.add("OtherFuel1")
            vals.add("OtherFuel2")
            vals.add("Water")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `resource`'.format(value))

        self._data["Resource"] = value

    @property
    def year_1_multiplier(self):
        """Get year_1_multiplier

        Returns:
            float: the value of `year_1_multiplier` or None if not set
        """
        return self._data["Year 1 Multiplier"]

    @year_1_multiplier.setter
    def year_1_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_1_multiplier`
        The multiplier to be applied to the end-use cost for the first year in the service period.
        The total utility costs for the selected end-use is multiplied by this value. For no change
        enter 1.0.

        Args:
            value (float): value for IDD Field `year_1_multiplier`
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
                                 'for field `year_1_multiplier`'.format(value))

        self._data["Year 1 Multiplier"] = value

    @property
    def year_2_multiplier(self):
        """Get year_2_multiplier

        Returns:
            float: the value of `year_2_multiplier` or None if not set
        """
        return self._data["Year 2 Multiplier"]

    @year_2_multiplier.setter
    def year_2_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_2_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_2_multiplier`
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
                                 'for field `year_2_multiplier`'.format(value))

        self._data["Year 2 Multiplier"] = value

    @property
    def year_3_multiplier(self):
        """Get year_3_multiplier

        Returns:
            float: the value of `year_3_multiplier` or None if not set
        """
        return self._data["Year 3 Multiplier"]

    @year_3_multiplier.setter
    def year_3_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_3_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_3_multiplier`
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
                                 'for field `year_3_multiplier`'.format(value))

        self._data["Year 3 Multiplier"] = value

    @property
    def year_4_multiplier(self):
        """Get year_4_multiplier

        Returns:
            float: the value of `year_4_multiplier` or None if not set
        """
        return self._data["Year 4 Multiplier"]

    @year_4_multiplier.setter
    def year_4_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_4_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_4_multiplier`
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
                                 'for field `year_4_multiplier`'.format(value))

        self._data["Year 4 Multiplier"] = value

    @property
    def year_5_multiplier(self):
        """Get year_5_multiplier

        Returns:
            float: the value of `year_5_multiplier` or None if not set
        """
        return self._data["Year 5 Multiplier"]

    @year_5_multiplier.setter
    def year_5_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_5_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_5_multiplier`
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
                                 'for field `year_5_multiplier`'.format(value))

        self._data["Year 5 Multiplier"] = value

    @property
    def year_6_multiplier(self):
        """Get year_6_multiplier

        Returns:
            float: the value of `year_6_multiplier` or None if not set
        """
        return self._data["Year 6 Multiplier"]

    @year_6_multiplier.setter
    def year_6_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_6_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_6_multiplier`
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
                                 'for field `year_6_multiplier`'.format(value))

        self._data["Year 6 Multiplier"] = value

    @property
    def year_7_multiplier(self):
        """Get year_7_multiplier

        Returns:
            float: the value of `year_7_multiplier` or None if not set
        """
        return self._data["Year 7 Multiplier"]

    @year_7_multiplier.setter
    def year_7_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_7_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_7_multiplier`
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
                                 'for field `year_7_multiplier`'.format(value))

        self._data["Year 7 Multiplier"] = value

    @property
    def year_8_multiplier(self):
        """Get year_8_multiplier

        Returns:
            float: the value of `year_8_multiplier` or None if not set
        """
        return self._data["Year 8 Multiplier"]

    @year_8_multiplier.setter
    def year_8_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_8_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_8_multiplier`
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
                                 'for field `year_8_multiplier`'.format(value))

        self._data["Year 8 Multiplier"] = value

    @property
    def year_9_multiplier(self):
        """Get year_9_multiplier

        Returns:
            float: the value of `year_9_multiplier` or None if not set
        """
        return self._data["Year 9 Multiplier"]

    @year_9_multiplier.setter
    def year_9_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_9_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_9_multiplier`
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
                                 'for field `year_9_multiplier`'.format(value))

        self._data["Year 9 Multiplier"] = value

    @property
    def year_10_multiplier(self):
        """Get year_10_multiplier

        Returns:
            float: the value of `year_10_multiplier` or None if not set
        """
        return self._data["Year 10 Multiplier"]

    @year_10_multiplier.setter
    def year_10_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_10_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_10_multiplier`
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
                                 'for field `year_10_multiplier`'.format(value))

        self._data["Year 10 Multiplier"] = value

    @property
    def year_11_multiplier(self):
        """Get year_11_multiplier

        Returns:
            float: the value of `year_11_multiplier` or None if not set
        """
        return self._data["Year 11 Multiplier"]

    @year_11_multiplier.setter
    def year_11_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_11_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_11_multiplier`
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
                                 'for field `year_11_multiplier`'.format(value))

        self._data["Year 11 Multiplier"] = value

    @property
    def year_12_multiplier(self):
        """Get year_12_multiplier

        Returns:
            float: the value of `year_12_multiplier` or None if not set
        """
        return self._data["Year 12 Multiplier"]

    @year_12_multiplier.setter
    def year_12_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_12_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_12_multiplier`
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
                                 'for field `year_12_multiplier`'.format(value))

        self._data["Year 12 Multiplier"] = value

    @property
    def year_13_multiplier(self):
        """Get year_13_multiplier

        Returns:
            float: the value of `year_13_multiplier` or None if not set
        """
        return self._data["Year 13 Multiplier"]

    @year_13_multiplier.setter
    def year_13_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_13_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_13_multiplier`
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
                                 'for field `year_13_multiplier`'.format(value))

        self._data["Year 13 Multiplier"] = value

    @property
    def year_14_multiplier(self):
        """Get year_14_multiplier

        Returns:
            float: the value of `year_14_multiplier` or None if not set
        """
        return self._data["Year 14 Multiplier"]

    @year_14_multiplier.setter
    def year_14_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_14_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_14_multiplier`
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
                                 'for field `year_14_multiplier`'.format(value))

        self._data["Year 14 Multiplier"] = value

    @property
    def year_15_multiplier(self):
        """Get year_15_multiplier

        Returns:
            float: the value of `year_15_multiplier` or None if not set
        """
        return self._data["Year 15 Multiplier"]

    @year_15_multiplier.setter
    def year_15_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_15_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_15_multiplier`
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
                                 'for field `year_15_multiplier`'.format(value))

        self._data["Year 15 Multiplier"] = value

    @property
    def year_16_multiplier(self):
        """Get year_16_multiplier

        Returns:
            float: the value of `year_16_multiplier` or None if not set
        """
        return self._data["Year 16 Multiplier"]

    @year_16_multiplier.setter
    def year_16_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_16_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_16_multiplier`
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
                                 'for field `year_16_multiplier`'.format(value))

        self._data["Year 16 Multiplier"] = value

    @property
    def year_17_multiplier(self):
        """Get year_17_multiplier

        Returns:
            float: the value of `year_17_multiplier` or None if not set
        """
        return self._data["Year 17 Multiplier"]

    @year_17_multiplier.setter
    def year_17_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_17_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_17_multiplier`
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
                                 'for field `year_17_multiplier`'.format(value))

        self._data["Year 17 Multiplier"] = value

    @property
    def year_18_multiplier(self):
        """Get year_18_multiplier

        Returns:
            float: the value of `year_18_multiplier` or None if not set
        """
        return self._data["Year 18 Multiplier"]

    @year_18_multiplier.setter
    def year_18_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_18_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_18_multiplier`
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
                                 'for field `year_18_multiplier`'.format(value))

        self._data["Year 18 Multiplier"] = value

    @property
    def year_19_multiplier(self):
        """Get year_19_multiplier

        Returns:
            float: the value of `year_19_multiplier` or None if not set
        """
        return self._data["Year 19 Multiplier"]

    @year_19_multiplier.setter
    def year_19_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_19_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_19_multiplier`
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
                                 'for field `year_19_multiplier`'.format(value))

        self._data["Year 19 Multiplier"] = value

    @property
    def year_20_multiplier(self):
        """Get year_20_multiplier

        Returns:
            float: the value of `year_20_multiplier` or None if not set
        """
        return self._data["Year 20 Multiplier"]

    @year_20_multiplier.setter
    def year_20_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_20_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_20_multiplier`
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
                                 'for field `year_20_multiplier`'.format(value))

        self._data["Year 20 Multiplier"] = value

    @property
    def year_21_multiplier(self):
        """Get year_21_multiplier

        Returns:
            float: the value of `year_21_multiplier` or None if not set
        """
        return self._data["Year 21 Multiplier"]

    @year_21_multiplier.setter
    def year_21_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_21_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_21_multiplier`
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
                                 'for field `year_21_multiplier`'.format(value))

        self._data["Year 21 Multiplier"] = value

    @property
    def year_22_multiplier(self):
        """Get year_22_multiplier

        Returns:
            float: the value of `year_22_multiplier` or None if not set
        """
        return self._data["Year 22 Multiplier"]

    @year_22_multiplier.setter
    def year_22_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_22_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_22_multiplier`
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
                                 'for field `year_22_multiplier`'.format(value))

        self._data["Year 22 Multiplier"] = value

    @property
    def year_23_multiplier(self):
        """Get year_23_multiplier

        Returns:
            float: the value of `year_23_multiplier` or None if not set
        """
        return self._data["Year 23 Multiplier"]

    @year_23_multiplier.setter
    def year_23_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_23_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_23_multiplier`
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
                                 'for field `year_23_multiplier`'.format(value))

        self._data["Year 23 Multiplier"] = value

    @property
    def year_24_multiplier(self):
        """Get year_24_multiplier

        Returns:
            float: the value of `year_24_multiplier` or None if not set
        """
        return self._data["Year 24 Multiplier"]

    @year_24_multiplier.setter
    def year_24_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_24_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_24_multiplier`
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
                                 'for field `year_24_multiplier`'.format(value))

        self._data["Year 24 Multiplier"] = value

    @property
    def year_25_multiplier(self):
        """Get year_25_multiplier

        Returns:
            float: the value of `year_25_multiplier` or None if not set
        """
        return self._data["Year 25 Multiplier"]

    @year_25_multiplier.setter
    def year_25_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_25_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_25_multiplier`
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
                                 'for field `year_25_multiplier`'.format(value))

        self._data["Year 25 Multiplier"] = value

    @property
    def year_26_multiplier(self):
        """Get year_26_multiplier

        Returns:
            float: the value of `year_26_multiplier` or None if not set
        """
        return self._data["Year 26 Multiplier"]

    @year_26_multiplier.setter
    def year_26_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_26_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_26_multiplier`
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
                                 'for field `year_26_multiplier`'.format(value))

        self._data["Year 26 Multiplier"] = value

    @property
    def year_27_multiplier(self):
        """Get year_27_multiplier

        Returns:
            float: the value of `year_27_multiplier` or None if not set
        """
        return self._data["Year 27 Multiplier"]

    @year_27_multiplier.setter
    def year_27_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_27_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_27_multiplier`
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
                                 'for field `year_27_multiplier`'.format(value))

        self._data["Year 27 Multiplier"] = value

    @property
    def year_28_multiplier(self):
        """Get year_28_multiplier

        Returns:
            float: the value of `year_28_multiplier` or None if not set
        """
        return self._data["Year 28 Multiplier"]

    @year_28_multiplier.setter
    def year_28_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_28_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_28_multiplier`
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
                                 'for field `year_28_multiplier`'.format(value))

        self._data["Year 28 Multiplier"] = value

    @property
    def year_29_multiplier(self):
        """Get year_29_multiplier

        Returns:
            float: the value of `year_29_multiplier` or None if not set
        """
        return self._data["Year 29 Multiplier"]

    @year_29_multiplier.setter
    def year_29_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_29_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_29_multiplier`
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
                                 'for field `year_29_multiplier`'.format(value))

        self._data["Year 29 Multiplier"] = value

    @property
    def year_30_multiplier(self):
        """Get year_30_multiplier

        Returns:
            float: the value of `year_30_multiplier` or None if not set
        """
        return self._data["Year 30 Multiplier"]

    @year_30_multiplier.setter
    def year_30_multiplier(self, value=None):
        """  Corresponds to IDD Field `year_30_multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `year_30_multiplier`
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
                                 'for field `year_30_multiplier`'.format(value))

        self._data["Year 30 Multiplier"] = value

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
        out.append(self._to_str(self.resource))
        out.append(self._to_str(self.year_1_multiplier))
        out.append(self._to_str(self.year_2_multiplier))
        out.append(self._to_str(self.year_3_multiplier))
        out.append(self._to_str(self.year_4_multiplier))
        out.append(self._to_str(self.year_5_multiplier))
        out.append(self._to_str(self.year_6_multiplier))
        out.append(self._to_str(self.year_7_multiplier))
        out.append(self._to_str(self.year_8_multiplier))
        out.append(self._to_str(self.year_9_multiplier))
        out.append(self._to_str(self.year_10_multiplier))
        out.append(self._to_str(self.year_11_multiplier))
        out.append(self._to_str(self.year_12_multiplier))
        out.append(self._to_str(self.year_13_multiplier))
        out.append(self._to_str(self.year_14_multiplier))
        out.append(self._to_str(self.year_15_multiplier))
        out.append(self._to_str(self.year_16_multiplier))
        out.append(self._to_str(self.year_17_multiplier))
        out.append(self._to_str(self.year_18_multiplier))
        out.append(self._to_str(self.year_19_multiplier))
        out.append(self._to_str(self.year_20_multiplier))
        out.append(self._to_str(self.year_21_multiplier))
        out.append(self._to_str(self.year_22_multiplier))
        out.append(self._to_str(self.year_23_multiplier))
        out.append(self._to_str(self.year_24_multiplier))
        out.append(self._to_str(self.year_25_multiplier))
        out.append(self._to_str(self.year_26_multiplier))
        out.append(self._to_str(self.year_27_multiplier))
        out.append(self._to_str(self.year_28_multiplier))
        out.append(self._to_str(self.year_29_multiplier))
        out.append(self._to_str(self.year_30_multiplier))
        return ",".join(out)