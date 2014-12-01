from collections import OrderedDict

class CurrencyType(object):
    """ Corresponds to IDD object `CurrencyType`
        If CurrencyType is not specified, it will default to USD and produce $ in the reports.
    
    """
    internal_name = "CurrencyType"
    field_count = 1
    required_fields = ["Monetary Unit"]

    def __init__(self):
        """ Init data dictionary object for IDD  `CurrencyType`
        """
        self._data = OrderedDict()
        self._data["Monetary Unit"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.monetary_unit = None
        else:
            self.monetary_unit = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def monetary_unit(self):
        """Get monetary_unit

        Returns:
            str: the value of `monetary_unit` or None if not set
        """
        return self._data["Monetary Unit"]

    @monetary_unit.setter
    def monetary_unit(self, value=None):
        """  Corresponds to IDD Field `Monetary Unit`
        The commonly used three letter currency code for the units of money for the country or region.
        Based on ISO 4217 currency codes.  Common currency codes are USD for $ and EUR for Euros.

        Args:
            value (str): value for IDD Field `Monetary Unit`
                Accepted values are:
                      - USD
                      - AFN
                      - ALL
                      - ANG
                      - ARS
                      - AUD
                      - AWG
                      - AZN
                      - BAM
                      - BBD
                      - BGN
                      - BMD
                      - BND
                      - BOB
                      - BRL
                      - BSD
                      - BWP
                      - BYR
                      - BZD
                      - CAD
                      - CHF
                      - CLP
                      - CNY
                      - COP
                      - CRC
                      - CUP
                      - CZK
                      - DKK
                      - DOP
                      - EEK
                      - EGP
                      - EUR
                      - FJD
                      - GBP
                      - GHC
                      - GIP
                      - GTQ
                      - GYD
                      - HKD
                      - HNL
                      - HRK
                      - HUF
                      - IDR
                      - ILS
                      - IMP
                      - INR
                      - IRR
                      - ISK
                      - JEP
                      - JMD
                      - JPY
                      - KGS
                      - KHR
                      - KPW
                      - KRW
                      - KYD
                      - KZT
                      - LAK
                      - LBP
                      - LKR
                      - LRD
                      - LTL
                      - LVL
                      - MKD
                      - MNT
                      - MUR
                      - MXN
                      - MYR
                      - MZN
                      - NAD
                      - NGN
                      - NIO
                      - NOK
                      - NPR
                      - NZD
                      - OMR
                      - PAB
                      - PEN
                      - PHP
                      - PKR
                      - PLN
                      - PYG
                      - QAR
                      - RON
                      - RSD
                      - RUB
                      - SAR
                      - SBD
                      - SCR
                      - SEK
                      - SGD
                      - SHP
                      - SOS
                      - SRD
                      - SVC
                      - SYP
                      - THB
                      - TRL
                      - TRY
                      - TTD
                      - TVD
                      - TWD
                      - UAH
                      - UYU
                      - UZS
                      - VEF
                      - VND
                      - XCD
                      - YER
                      - ZAR
                      - ZWD
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `monetary_unit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `monetary_unit`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `monetary_unit`')
            vals = {}
            vals["usd"] = "USD"
            vals["afn"] = "AFN"
            vals["all"] = "ALL"
            vals["ang"] = "ANG"
            vals["ars"] = "ARS"
            vals["aud"] = "AUD"
            vals["awg"] = "AWG"
            vals["azn"] = "AZN"
            vals["bam"] = "BAM"
            vals["bbd"] = "BBD"
            vals["bgn"] = "BGN"
            vals["bmd"] = "BMD"
            vals["bnd"] = "BND"
            vals["bob"] = "BOB"
            vals["brl"] = "BRL"
            vals["bsd"] = "BSD"
            vals["bwp"] = "BWP"
            vals["byr"] = "BYR"
            vals["bzd"] = "BZD"
            vals["cad"] = "CAD"
            vals["chf"] = "CHF"
            vals["clp"] = "CLP"
            vals["cny"] = "CNY"
            vals["cop"] = "COP"
            vals["crc"] = "CRC"
            vals["cup"] = "CUP"
            vals["czk"] = "CZK"
            vals["dkk"] = "DKK"
            vals["dop"] = "DOP"
            vals["eek"] = "EEK"
            vals["egp"] = "EGP"
            vals["eur"] = "EUR"
            vals["fjd"] = "FJD"
            vals["gbp"] = "GBP"
            vals["ghc"] = "GHC"
            vals["gip"] = "GIP"
            vals["gtq"] = "GTQ"
            vals["gyd"] = "GYD"
            vals["hkd"] = "HKD"
            vals["hnl"] = "HNL"
            vals["hrk"] = "HRK"
            vals["huf"] = "HUF"
            vals["idr"] = "IDR"
            vals["ils"] = "ILS"
            vals["imp"] = "IMP"
            vals["inr"] = "INR"
            vals["irr"] = "IRR"
            vals["isk"] = "ISK"
            vals["jep"] = "JEP"
            vals["jmd"] = "JMD"
            vals["jpy"] = "JPY"
            vals["kgs"] = "KGS"
            vals["khr"] = "KHR"
            vals["kpw"] = "KPW"
            vals["krw"] = "KRW"
            vals["kyd"] = "KYD"
            vals["kzt"] = "KZT"
            vals["lak"] = "LAK"
            vals["lbp"] = "LBP"
            vals["lkr"] = "LKR"
            vals["lrd"] = "LRD"
            vals["ltl"] = "LTL"
            vals["lvl"] = "LVL"
            vals["mkd"] = "MKD"
            vals["mnt"] = "MNT"
            vals["mur"] = "MUR"
            vals["mxn"] = "MXN"
            vals["myr"] = "MYR"
            vals["mzn"] = "MZN"
            vals["nad"] = "NAD"
            vals["ngn"] = "NGN"
            vals["nio"] = "NIO"
            vals["nok"] = "NOK"
            vals["npr"] = "NPR"
            vals["nzd"] = "NZD"
            vals["omr"] = "OMR"
            vals["pab"] = "PAB"
            vals["pen"] = "PEN"
            vals["php"] = "PHP"
            vals["pkr"] = "PKR"
            vals["pln"] = "PLN"
            vals["pyg"] = "PYG"
            vals["qar"] = "QAR"
            vals["ron"] = "RON"
            vals["rsd"] = "RSD"
            vals["rub"] = "RUB"
            vals["sar"] = "SAR"
            vals["sbd"] = "SBD"
            vals["scr"] = "SCR"
            vals["sek"] = "SEK"
            vals["sgd"] = "SGD"
            vals["shp"] = "SHP"
            vals["sos"] = "SOS"
            vals["srd"] = "SRD"
            vals["svc"] = "SVC"
            vals["syp"] = "SYP"
            vals["thb"] = "THB"
            vals["trl"] = "TRL"
            vals["try"] = "TRY"
            vals["ttd"] = "TTD"
            vals["tvd"] = "TVD"
            vals["twd"] = "TWD"
            vals["uah"] = "UAH"
            vals["uyu"] = "UYU"
            vals["uzs"] = "UZS"
            vals["vef"] = "VEF"
            vals["vnd"] = "VND"
            vals["xcd"] = "XCD"
            vals["yer"] = "YER"
            vals["zar"] = "ZAR"
            vals["zwd"] = "ZWD"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `monetary_unit`'.format(value))
            value = vals[value_lower]
        self._data["Monetary Unit"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ComponentCostAdjustments(object):
    """ Corresponds to IDD object `ComponentCost:Adjustments`
        Used to perform various modifications to the construction costs to arrive at an
        estimate for total project costs. This object allows extending the line item model
        so that the overall costs of the project will reflect various profit and fees.
    
    """
    internal_name = "ComponentCost:Adjustments"
    field_count = 7
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:Adjustments`
        """
        self._data = OrderedDict()
        self._data["Miscellaneous Cost per Conditioned Area"] = None
        self._data["Design and Engineering Fees"] = None
        self._data["Contractor Fee"] = None
        self._data["Contingency"] = None
        self._data["Permits, Bonding and Insurance"] = None
        self._data["Commissioning Fee"] = None
        self._data["Regional Adjustment Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.miscellaneous_cost_per_conditioned_area = None
        else:
            self.miscellaneous_cost_per_conditioned_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_and_engineering_fees = None
        else:
            self.design_and_engineering_fees = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.contractor_fee = None
        else:
            self.contractor_fee = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.contingency = None
        else:
            self.contingency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.permits_bonding_and_insurance = None
        else:
            self.permits_bonding_and_insurance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.commissioning_fee = None
        else:
            self.commissioning_fee = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regional_adjustment_factor = None
        else:
            self.regional_adjustment_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def miscellaneous_cost_per_conditioned_area(self):
        """Get miscellaneous_cost_per_conditioned_area

        Returns:
            float: the value of `miscellaneous_cost_per_conditioned_area` or None if not set
        """
        return self._data["Miscellaneous Cost per Conditioned Area"]

    @miscellaneous_cost_per_conditioned_area.setter
    def miscellaneous_cost_per_conditioned_area(self, value=None):
        """  Corresponds to IDD Field `Miscellaneous Cost per Conditioned Area`
        based on conditioned floor area
        for cost not accounted for in current line item cost model

        Args:
            value (float): value for IDD Field `Miscellaneous Cost per Conditioned Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Design and Engineering Fees`

        Args:
            value (float): value for IDD Field `Design and Engineering Fees`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Contractor Fee`

        Args:
            value (float): value for IDD Field `Contractor Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Contingency`

        Args:
            value (float): value for IDD Field `Contingency`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Permits, Bonding and Insurance`

        Args:
            value (float): value for IDD Field `Permits, Bonding and Insurance`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Commissioning Fee`

        Args:
            value (float): value for IDD Field `Commissioning Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Regional Adjustment Factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `Regional Adjustment Factor`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `regional_adjustment_factor`'.format(value))
        self._data["Regional Adjustment Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:Reference`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.reference_building_line_item_costs = None
        else:
            self.reference_building_line_item_costs = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_miscellaneous_cost_per_conditioned_area = None
        else:
            self.reference_building_miscellaneous_cost_per_conditioned_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_design_and_engineering_fees = None
        else:
            self.reference_building_design_and_engineering_fees = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_contractor_fee = None
        else:
            self.reference_building_contractor_fee = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_contingency = None
        else:
            self.reference_building_contingency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_permits_bonding_and_insurance = None
        else:
            self.reference_building_permits_bonding_and_insurance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_commissioning_fee = None
        else:
            self.reference_building_commissioning_fee = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reference_building_regional_adjustment_factor = None
        else:
            self.reference_building_regional_adjustment_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def reference_building_line_item_costs(self):
        """Get reference_building_line_item_costs

        Returns:
            float: the value of `reference_building_line_item_costs` or None if not set
        """
        return self._data["Reference Building Line Item Costs"]

    @reference_building_line_item_costs.setter
    def reference_building_line_item_costs(self, value=None):
        """  Corresponds to IDD Field `Reference Building Line Item Costs`
        should be comparable to the components in current line item cost model

        Args:
            value (float): value for IDD Field `Reference Building Line Item Costs`
                Units: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Miscellaneous Cost per Conditioned Area`
        based on conditioned floor area
        for cost not accounted for in reference line item costs

        Args:
            value (float): value for IDD Field `Reference Building Miscellaneous Cost per Conditioned Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Design and Engineering Fees`

        Args:
            value (float): value for IDD Field `Reference Building Design and Engineering Fees`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Contractor Fee`

        Args:
            value (float): value for IDD Field `Reference Building Contractor Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Contingency`

        Args:
            value (float): value for IDD Field `Reference Building Contingency`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Permits, Bonding and Insurance`

        Args:
            value (float): value for IDD Field `Reference Building Permits, Bonding and Insurance`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Commissioning Fee`

        Args:
            value (float): value for IDD Field `Reference Building Commissioning Fee`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Reference Building Regional Adjustment Factor`
        for use with average data in line item and Misc cost models

        Args:
            value (float): value for IDD Field `Reference Building Regional Adjustment Factor`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `reference_building_regional_adjustment_factor`'.format(value))
        self._data["Reference Building Regional Adjustment Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ComponentCostLineItem(object):
    """ Corresponds to IDD object `ComponentCost:LineItem`
        Each instance of this object creates a cost line item and will contribute to the total
        for a cost estimate.
    
    """
    internal_name = "ComponentCost:LineItem"
    field_count = 13
    required_fields = ["Line Item Type", "Item Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ComponentCost:LineItem`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type = None
        else:
            self.type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.line_item_type = None
        else:
            self.line_item_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.item_name = None
        else:
            self.item_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.object_enduse_key = None
        else:
            self.object_enduse_key = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_each = None
        else:
            self.cost_per_each = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_area = None
        else:
            self.cost_per_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_unit_of_output_capacity = None
        else:
            self.cost_per_unit_of_output_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_unit_of_output_capacity_per_cop = None
        else:
            self.cost_per_unit_of_output_capacity_per_cop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_volume = None
        else:
            self.cost_per_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_volume_rate = None
        else:
            self.cost_per_volume_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_energy_per_temperature_difference = None
        else:
            self.cost_per_energy_per_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.quantity = None
        else:
            self.quantity = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Type`

        Args:
            value (str): value for IDD Field `Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Line Item Type`
        extend choice-keys as Cases are added to code

        Args:
            value (str): value for IDD Field `Line Item Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `line_item_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `line_item_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `line_item_type`')
            vals = {}
            vals["general"] = "General"
            vals["construction"] = "Construction"
            vals["coil:dx"] = "Coil:DX"
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["chiller:electric"] = "Chiller:Electric"
            vals["daylighting:controls"] = "Daylighting:Controls"
            vals["shading:zone:detailed"] = "Shading:Zone:Detailed"
            vals["lights"] = "Lights"
            vals["generator:photovoltaic"] = "Generator:Photovoltaic"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `line_item_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Item Name`
        wildcard "*" is acceptable for some components

        Args:
            value (str): value for IDD Field `Item Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `item_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `item_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Object End-Use Key`
        not yet used

        Args:
            value (str): value for IDD Field `Object End-Use Key`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `object_enduse_key`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `object_enduse_key`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Cost per Each`

        Args:
            value (float): value for IDD Field `Cost per Each`
                Units: $
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Area`

        Args:
            value (float): value for IDD Field `Cost per Area`
                Units: $/m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Unit of Output Capacity`

        Args:
            value (float): value for IDD Field `Cost per Unit of Output Capacity`
                Units: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Unit of Output Capacity per COP`
        The value is per change in COP.

        Args:
            value (float): value for IDD Field `Cost per Unit of Output Capacity per COP`
                Units: $/kW
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Volume`

        Args:
            value (float): value for IDD Field `Cost per Volume`
                Units: $/m3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Volume Rate`

        Args:
            value (float): value for IDD Field `Cost per Volume Rate`
                Units: $/(m3/s)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cost per Energy per Temperature Difference`
        as in for use with UA sizing of Coils

        Args:
            value (float): value for IDD Field `Cost per Energy per Temperature Difference`
                Units: $/(W/K)
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Quantity`
        optional for use with Cost per Each and "General" object Type

        Args:
            value (float): value for IDD Field `Quantity`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `quantity`'.format(value))
        self._data["Quantity"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Output Meter Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Tariff`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_meter_name = None
        else:
            self.output_meter_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.conversion_factor_choice = None
        else:
            self.conversion_factor_choice = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.energy_conversion_factor = None
        else:
            self.energy_conversion_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_conversion_factor = None
        else:
            self.demand_conversion_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.time_of_use_period_schedule_name = None
        else:
            self.time_of_use_period_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season_schedule_name = None
        else:
            self.season_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.month_schedule_name = None
        else:
            self.month_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_window_length = None
        else:
            self.demand_window_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.monthly_charge_or_variable_name = None
        else:
            self.monthly_charge_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_monthly_charge_or_variable_name = None
        else:
            self.minimum_monthly_charge_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.real_time_pricing_charge_schedule_name = None
        else:
            self.real_time_pricing_charge_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.customer_baseline_load_schedule_name = None
        else:
            self.customer_baseline_load_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.group_name = None
        else:
            self.group_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.buy_or_sell = None
        else:
            self.buy_or_sell = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        The name of the tariff. Tariffs are sometimes called rates. The name is used in identifying
        the output results and in associating all of the charges and other objects that make up a tariff.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Output Meter Name`
        The name of any standard meter or custom meter or but usually set to either Electricity:Facility or Gas:Facility

        Args:
            value (str): value for IDD Field `Output Meter Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_meter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Conversion Factor Choice`
        A choice that allows several different predefined conversion factors to be used; otherwise user
        defined conversion factors are used as defined in the next two fields.

        Args:
            value (str): value for IDD Field `Conversion Factor Choice`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `conversion_factor_choice`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `conversion_factor_choice`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `conversion_factor_choice`')
            vals = {}
            vals["userdefined"] = "UserDefined"
            vals["kwh"] = "kWh"
            vals["therm"] = "Therm"
            vals["mmbtu"] = "MMBtu"
            vals["mj"] = "MJ"
            vals["kbtu"] = "kBtu"
            vals["mcf"] = "MCF"
            vals["ccf"] = "CCF"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `conversion_factor_choice`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Energy Conversion Factor`
        Is a multiplier used to convert energy into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion). This field should will be used only if Conversion Factor
        Choice is set to UserDefined.  Within EnergyPlus energy always has units of J (joules).  For
        conversion from J to kWh use the value of 0.0000002778. This is also used for all objects that
        reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `Energy Conversion Factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Demand Conversion Factor`
        Is a multiplier used to convert demand into the units specified by the utility in their tariff. If
        left blank it defaults to 1 (no conversion).  This field should will be used only if Conversion
        Factor Choice is set to UserDefined.  Within EnergyPlus demand always has units of J/s (joules/sec)
        which equivalent to W (watts).  For conversion from W to kW use the value of 0.001. This is also used
        for all objects that reference the UtilityCost:Tariff.

        Args:
            value (float): value for IDD Field `Demand Conversion Factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Time of Use Period Schedule Name`
        The name of the schedule that defines the time-of-use periods that occur each day. The values for the
        different variables are: 1 for Peak. 2 for Shoulder. 3 for OffPeak. 4 for MidPeak.

        Args:
            value (str): value for IDD Field `Time of Use Period Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `time_of_use_period_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `time_of_use_period_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Season Schedule Name`
        The name of a schedule that defines the seasons.  The schedule values are: 1 for Winter. 2 for Spring.
        3 for Summer. 4 for Autumn.

        Args:
            value (str): value for IDD Field `Season Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Month Schedule Name`
        The name of the schedule that defines the billing periods of the year. Normally this entry is allowed
        to default and a schedule will be internally used that has the breaks between billing periods occurring
        at the same time as the breaks between months i.e. at midnight prior to the first day of the month.
        If other billing periods are used such as two month cycles or a single bill for an entire season such
        as some natural gas companies do in the summer then the month schedule may be used to redefine it.
        Make sure that the month schedule and season schedule are consistent otherwise an error will be issued.

        Args:
            value (str): value for IDD Field `Month Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `month_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `month_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Demand Window Length`
        The determination of demand can vary by utility. Some utilities use the peak instantaneous demand
        measured but most use a fifteen minute average demand or a one hour average demand. Some gas utilities
        measure demand as the use during the peak day or peak week.

        Args:
            value (str): value for IDD Field `Demand Window Length`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `demand_window_length`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `demand_window_length`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `demand_window_length`')
            vals = {}
            vals["quarterhour"] = "QuarterHour"
            vals["halfhour"] = "HalfHour"
            vals["fullhour"] = "FullHour"
            vals["day"] = "Day"
            vals["week"] = "Week"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `demand_window_length`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Monthly Charge or Variable Name`
        The fixed monthly service charge that many utilities have.  The entry may be numeric and gets added to
        the ServiceCharges variable or if a variable name is entered here its values for each month are used.

        Args:
            value (str): value for IDD Field `Monthly Charge or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `monthly_charge_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `monthly_charge_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Minimum Monthly Charge or Variable Name`
        The minimum total charge for the tariff or if a variable name is entered here its
        values for each month are used.

        Args:
            value (str): value for IDD Field `Minimum Monthly Charge or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_monthly_charge_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_monthly_charge_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Real Time Pricing Charge Schedule Name`
        Used with real time pricing rates. The name of a schedule that contains the cost of
        energy for that particular time period of the year. Real time rates can be modeled using a charge
        schedule with the actual real time prices entered in the schedule.

        Args:
            value (str): value for IDD Field `Real Time Pricing Charge Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `real_time_pricing_charge_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `real_time_pricing_charge_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Customer Baseline Load Schedule Name`
        Used with real time pricing rates. The name of a schedule that contains the baseline
        energy use for the customer. Many real time rates apply the charges as a credit or debit only to the
        difference between the baseline use and the actual use.

        Args:
            value (str): value for IDD Field `Customer Baseline Load Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `customer_baseline_load_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `customer_baseline_load_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Group Name`
        The group name of the tariff such as distribution transmission supplier etc. If more than one tariff
        with the same group name is present and qualifies only the lowest cost tariff is used. Usually the group
        name field is left blank which results in all tariffs using the same meter variable being compared and
        the lowest cost one being selected.

        Args:
            value (str): value for IDD Field `Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `group_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Buy Or Sell`
        Sets whether the tariff is used for buying selling or both to the utility.  This
        should be allowed to default to buyFromUtility unless a power generation system is included in the
        building that may generate more power than the building needs during the year

        Args:
            value (str): value for IDD Field `Buy Or Sell`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `buy_or_sell`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `buy_or_sell`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `buy_or_sell`')
            vals = {}
            vals["buyfromutility"] = "BuyFromUtility"
            vals["selltoutility"] = "SellToUtility"
            vals["netmetering"] = "NetMetering"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `buy_or_sell`'.format(value))
            value = vals[value_lower]
        self._data["Buy Or Sell"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Tariff Name", "Variable Name", "Threshold Value or Variable Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Qualify`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.variable_name = None
        else:
            self.variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.qualify_type = None
        else:
            self.qualify_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.threshold_value_or_variable_name = None
        else:
            self.threshold_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.threshold_test = None
        else:
            self.threshold_test = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_months = None
        else:
            self.number_of_months = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Displayed in the report if the tariff does not qualify

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Qualify.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Variable Name`
        The name of the variable used. For energy and demand the automatically created variables totalEnergy
        and totalDemand should be used respectively.

        Args:
            value (str): value for IDD Field `Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Qualify Type`

        Args:
            value (str): value for IDD Field `Qualify Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `qualify_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `qualify_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `qualify_type`')
            vals = {}
            vals["minimum"] = "Minimum"
            vals["maximum"] = "Maximum"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `qualify_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Threshold Value or Variable Name`
        The minimum or maximum value for the qualify. If the variable has values that are less than this value
        when the qualify type is minimum then the tariff may be disqualified.  If the variable has values that
        are greater than this value when the qualify type is maximum then the tariff may be disqualified.

        Args:
            value (str): value for IDD Field `Threshold Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `threshold_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `threshold_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Season`
        If the UtilityCost:Qualify only applies to a season enter the season name. If this field is left blank
        it defaults to Annual.

        Args:
            value (str): value for IDD Field `Season`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `season`')
            vals = {}
            vals["annual"] = "Annual"
            vals["summer"] = "Summer"
            vals["winter"] = "Winter"
            vals["spring"] = "Spring"
            vals["fall"] = "Fall"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `season`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Threshold Test`
        Uses the number in Number of Months in one of two different ways depending on the Threshold  Test. If
        the Threshold Test is set to Count then the qualification is based on the count of the total number
        of months per year.  If the Threshold Test is set to consecutive then the qualification is based on
        a consecutive number of months.

        Args:
            value (str): value for IDD Field `Threshold Test`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `threshold_test`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `threshold_test`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `threshold_test`')
            vals = {}
            vals["count"] = "Count"
            vals["consecutive"] = "Consecutive"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `threshold_test`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Number of Months`
        A number from 1 to 12.  If no value entered 12 is assumed when the qualify type is minimum and 1 when
        the qualify type is maximum.  This is the number of months that the threshold test applies to determine
        if the rate qualifies or not.  If the season is less than 12 months (if it is not annual) then the
        value is automatically reduced to the number of months of the seaon.

        Args:
            value (float): value for IDD Field `Number of Months`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_months`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `number_of_months`')
            if value > 12.0:
                raise ValueError('value need to be smaller 12.0 '
                                 'for field `number_of_months`')
        self._data["Number of Months"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Tariff Name", "Source Variable", "Category Variable Name", "Cost per Unit Value or Variable Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Charge:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tariff Name"] = None
        self._data["Source Variable"] = None
        self._data["Season"] = None
        self._data["Category Variable Name"] = None
        self._data["Cost per Unit Value or Variable Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_variable = None
        else:
            self.source_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.category_variable_name = None
        else:
            self.category_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost_per_unit_value_or_variable_name = None
        else:
            self.cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Simple object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Simple calculation are stored in a variable with the
        same name.  That way the results may be used for further calculation.  Spaces are not significant in
        Charge variable names. They are removed during the utility bill calculation process.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Simple.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Source Variable`
        The name of the source used by the UtilityCost:Charge:Simple.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis
        if other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Simple for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `Season`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `season`')
            vals = {}
            vals["annual"] = "Annual"
            vals["summer"] = "Summer"
            vals["winter"] = "Winter"
            vals["spring"] = "Spring"
            vals["fall"] = "Fall"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `season`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Category Variable Name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `Category Variable Name`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `category_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `category_variable_name`')
            vals = {}
            vals["energycharges"] = "EnergyCharges"
            vals["demandcharges"] = "DemandCharges"
            vals["servicecharges"] = "ServiceCharges"
            vals["basis"] = "Basis"
            vals["adjustment"] = "Adjustment"
            vals["surcharge"] = "Surcharge"
            vals["subtotal"] = "Subtotal"
            vals["taxes"] = "Taxes"
            vals["total"] = "Total"
            vals["notincluded"] = "NotIncluded"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `category_variable_name`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Cost per Unit Value or Variable Name`
        This field contains either a single number or the name of a variable.  The number is multiplied with
        all of the energy or demand or other source that is specified in the source field.  If a variable is
        used then the monthly values of the variable are multiplied against the variable specified in the
        source field.  This field makes it easy to include a simple charge without specifying block sizes.
        This is a good way to include a tax or cost adjustment.

        Args:
            value (str): value for IDD Field `Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cost_per_unit_value_or_variable_name`')
        self._data["Cost per Unit Value or Variable Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class UtilityCostChargeBlock(object):
    """ Corresponds to IDD object `UtilityCost:Charge:Block`
        Used to compute energy and demand charges (or any other charges) that are structured
        in blocks of charges. Multiple UtilityCost:Charge:Block objects may be defined for a
        single tariff and they will be added together.
    
    """
    internal_name = "UtilityCost:Charge:Block"
    field_count = 37
    required_fields = ["Name", "Tariff Name", "Source Variable", "Category Variable Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Charge:Block`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_variable = None
        else:
            self.source_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season = None
        else:
            self.season = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.category_variable_name = None
        else:
            self.category_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.remaining_into_variable = None
        else:
            self.remaining_into_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_multiplier_value_or_variable_name = None
        else:
            self.block_size_multiplier_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_1_value_or_variable_name = None
        else:
            self.block_size_1_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_1_cost_per_unit_value_or_variable_name = None
        else:
            self.block_1_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_2_value_or_variable_name = None
        else:
            self.block_size_2_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_2_cost_per_unit_value_or_variable_name = None
        else:
            self.block_2_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_3_value_or_variable_name = None
        else:
            self.block_size_3_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_3_cost_per_unit_value_or_variable_name = None
        else:
            self.block_3_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_4_value_or_variable_name = None
        else:
            self.block_size_4_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_4_cost_per_unit_value_or_variable_name = None
        else:
            self.block_4_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_5_value_or_variable_name = None
        else:
            self.block_size_5_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_5_cost_per_unit_value_or_variable_name = None
        else:
            self.block_5_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_6_value_or_variable_name = None
        else:
            self.block_size_6_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_6_cost_per_unit_value_or_variable_name = None
        else:
            self.block_6_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_7_value_or_variable_name = None
        else:
            self.block_size_7_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_7_cost_per_unit_value_or_variable_name = None
        else:
            self.block_7_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_8_value_or_variable_name = None
        else:
            self.block_size_8_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_8_cost_per_unit_value_or_variable_name = None
        else:
            self.block_8_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_9_value_or_variable_name = None
        else:
            self.block_size_9_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_9_cost_per_unit_value_or_variable_name = None
        else:
            self.block_9_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_10_value_or_variable_name = None
        else:
            self.block_size_10_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_10_cost_per_unit_value_or_variable_name = None
        else:
            self.block_10_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_11_value_or_variable_name = None
        else:
            self.block_size_11_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_11_cost_per_unit_value_or_variable_name = None
        else:
            self.block_11_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_12_value_or_variable_name = None
        else:
            self.block_size_12_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_12_cost_per_unit_value_or_variable_name = None
        else:
            self.block_12_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_13_value_or_variable_name = None
        else:
            self.block_size_13_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_13_cost_per_unit_value_or_variable_name = None
        else:
            self.block_13_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_14_value_or_variable_name = None
        else:
            self.block_size_14_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_14_cost_per_unit_value_or_variable_name = None
        else:
            self.block_14_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_size_15_value_or_variable_name = None
        else:
            self.block_size_15_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.block_15_cost_per_unit_value_or_variable_name = None
        else:
            self.block_15_cost_per_unit_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Charge Variable Name
        This is the name associated with the UtilityCost:Charge:Block object and will appear in the report.
        In addition the results of the UtilityCost:Charge:Block are stored in a variable with the same name.
        That way the results may be used for further calculation.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Block.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Source Variable`
        The name of the source used by the UtilityCost:Charge:Block.  This is usually the name of the variable
        holding the energy or demand but may also be the name of any variable including the subtotal or basis if
        other charges are based on those. Typical values include totalEnergy totalDemand EnergyCharges DemandCharges
        ServiceCharges Basis Adjustments Surcharges Subtotal Taxes and Total. If it is a time-of-use rate then
        peakEnergy peakDemand shoulderEnergy shoulderDemand offPeakEnergy offPeakDemand midPeakEnergy and midPeakDemand.
        In addition see the Tariff Report to see other native variablles that may be available. Also you can
        create additional user defined variables to model complex tariffs.

        Args:
            value (str): value for IDD Field `Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Season`
        If this is set to annual the calculations are performed for the UtilityCost:Charge:Block for the entire
        year (all months) otherwise it is calculated only for those months in the season defined.

        Args:
            value (str): value for IDD Field `Season`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `season`')
            vals = {}
            vals["annual"] = "Annual"
            vals["summer"] = "Summer"
            vals["winter"] = "Winter"
            vals["spring"] = "Spring"
            vals["fall"] = "Fall"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `season`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Category Variable Name`
        This field shows where the charge should be added. The reason to enter this field appropriately is so
        that the charge gets reported in a reasonable category.  The charge automatically gets added to the
        variable that is the category.

        Args:
            value (str): value for IDD Field `Category Variable Name`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `category_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `category_variable_name`')
            vals = {}
            vals["energycharges"] = "EnergyCharges"
            vals["demandcharges"] = "DemandCharges"
            vals["servicecharges"] = "ServiceCharges"
            vals["basis"] = "Basis"
            vals["adjustment"] = "Adjustment"
            vals["surcharge"] = "Surcharge"
            vals["subtotal"] = "Subtotal"
            vals["taxes"] = "Taxes"
            vals["total"] = "Total"
            vals["notincluded"] = "NotIncluded"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `category_variable_name`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Remaining Into Variable`
        If the blocks do not use all of the energy or demand from the source some energy and demand remains
        then the remaining amount should be assigned to a variable. If no variable is assigned and some amount
        of energy or demand is not used in the block structure a warning will be issued.

        Args:
            value (str): value for IDD Field `Remaining Into Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `remaining_into_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `remaining_into_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size Multiplier Value or Variable Name`
        The sizes of the blocks are usually used directly but if a value or a variable is entered here the block
        sizes entered in the rest of the charge are first multiplied by the entered value prior to being used.
        This is common for rates that are kWh/kW rates and in that case the variable that holds the monthly
        total electric demand would be entered.  If no value is entered a default value of one is assumed so
        that the block sizes remain exactly as entered.  This field is unusual for the EnergyPlus syntax because
        it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size Multiplier Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_multiplier_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_multiplier_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 1 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 1 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_1_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_1_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 1 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 1 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_1_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_1_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 2 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 2 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_2_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_2_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 2 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 2 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_2_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_2_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 3 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 3 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_3_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_3_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 3 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 3 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_3_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_3_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 4 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 4 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_4_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_4_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 4 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 4 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_4_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_4_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 5 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 5 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_5_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_5_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 5 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 5 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_5_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_5_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 6 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 6 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_6_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_6_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 6 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 6 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_6_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_6_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 7 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 7 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_7_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_7_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 7 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 7 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_7_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_7_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 8 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 8 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_8_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_8_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 8 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 8 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_8_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_8_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 9 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 9 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_9_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_9_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 9 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 9 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_9_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_9_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 10 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 10 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_10_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_10_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 10 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 10 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_10_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_10_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 11 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 11 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_11_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_11_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 11 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 11 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_11_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_11_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 12 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 12 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_12_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_12_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 12 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 12 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_12_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_12_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 13 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 13 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_13_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_13_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 13 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 13 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_13_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_13_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 14 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 14 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_14_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_14_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 14 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 14 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_14_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_14_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block Size 15 Value or Variable Name`
        The size of the block of the charges is entered here. For most rates that use multiple blocks this will
        be the value for the block size. Using remaining may be used when the remaining amount should be included
        in that block.  This field is unusual because it can be either a number or a name of a variable.

        Args:
            value (str): value for IDD Field `Block Size 15 Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_size_15_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_size_15_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Block 15 Cost per Unit Value or Variable Name`
        The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number
        or a name of a variable.

        Args:
            value (str): value for IDD Field `Block 15 Cost per Unit Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `block_15_cost_per_unit_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `block_15_cost_per_unit_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `block_15_cost_per_unit_value_or_variable_name`')
        self._data["Block 15 Cost per Unit Value or Variable Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class UtilityCostRatchet(object):
    """ Corresponds to IDD object `UtilityCost:Ratchet`
        Allows the modeling of tariffs that include some type of seasonal ratcheting.
        Ratchets are most common when used with electric demand charges. A ratchet is when a
        utility requires that the demand charge for a month with a low demand may be
        increased to be more consistent with a month that set a higher demand charge.
    
    """
    internal_name = "UtilityCost:Ratchet"
    field_count = 8
    required_fields = ["Name", "Tariff Name", "Baseline Source Variable", "Adjustment Source Variable"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Ratchet`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.baseline_source_variable = None
        else:
            self.baseline_source_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.adjustment_source_variable = None
        else:
            self.adjustment_source_variable = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season_from = None
        else:
            self.season_from = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.season_to = None
        else:
            self.season_to = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier_value_or_variable_name = None
        else:
            self.multiplier_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.offset_value_or_variable_name = None
        else:
            self.offset_value_or_variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Ratchet Variable Name
        The name of the ratchet and the name of the result of this single ratchet.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Ratchet.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Baseline Source Variable`
        When the ratcheted value exceeds the baseline value for a month the ratcheted value is used but when the
        baseline value is greater then the ratcheted value the baseline value is used. Usually the electric
        demand charge is used.  The baseline source variable can be the results of another ratchet object. This
        allows utility tariffs that have multiple ratchets to be modeled.

        Args:
            value (str): value for IDD Field `Baseline Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `baseline_source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `baseline_source_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Adjustment Source Variable`
        The variable that the ratchet is calculated from. It is often but not always the same as the baseline
        source variable.  The ratcheting calculations using offset and multiplier are using the values from the
        adjustment source variable. If left blank the adjustment source variable is the same as the baseline
        source variable.

        Args:
            value (str): value for IDD Field `Adjustment Source Variable`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `adjustment_source_variable`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `adjustment_source_variable`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Season From`
        The name of the season that is being examined.  The maximum value for all of the months in the named
        season is what is used with the multiplier and offset.  This is most commonly Summer or Annual.  When
        Monthly is used the adjustment source variable is used directly for all months.

        Args:
            value (str): value for IDD Field `Season From`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season_from`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_from`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `season_from`')
            vals = {}
            vals["annual"] = "Annual"
            vals["summer"] = "Summer"
            vals["winter"] = "Winter"
            vals["spring"] = "Spring"
            vals["fall"] = "Fall"
            vals["monthly"] = "Monthly"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `season_from`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Season To`
        The name of the season when the ratchet would be calculated.  This is most commonly Winter.  The ratchet
        only is applied to the months in the named season. The resulting variable for months not in the Season To
        selection will contain the values as appear in the baseline source variable.

        Args:
            value (str): value for IDD Field `Season To`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `season_to`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `season_to`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `season_to`')
            vals = {}
            vals["annual"] = "Annual"
            vals["summer"] = "Summer"
            vals["winter"] = "Winter"
            vals["spring"] = "Spring"
            vals["fall"] = "Fall"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `season_to`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Multiplier Value or Variable Name`
        Often the ratchet has a clause such as "the current month demand or 90% of the summer month demand".  For
        this case a value of 0.9 would be entered here as the multiplier.  This value may be left blank if no
        multiplier is needed and a value of one will be used as a default.

        Args:
            value (str): value for IDD Field `Multiplier Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `multiplier_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `multiplier_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Offset Value or Variable Name`
        A less common strategy is to say that the ratchet must be all demand greater than a value in this case
        an offset that is added to the demand may be entered here. If entered it is common for the offset value
        to be negative representing that the demand be reduced.   If no value is entered it is assumed to be
        zero and not affect the ratchet.

        Args:
            value (str): value for IDD Field `Offset Value or Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `offset_value_or_variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `offset_value_or_variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `offset_value_or_variable_name`')
        self._data["Offset Value or Variable Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class UtilityCostVariable(object):
    """ Corresponds to IDD object `UtilityCost:Variable`
        Allows for the direct entry of monthly values into a utility tariff variable.
    
    """
    internal_name = "UtilityCost:Variable"
    field_count = 15
    required_fields = ["Name", "Tariff Name", "Variable Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Variable`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.variable_type = None
        else:
            self.variable_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.january_value = None
        else:
            self.january_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_value = None
        else:
            self.february_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_value = None
        else:
            self.march_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_value = None
        else:
            self.april_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_value = None
        else:
            self.may_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_value = None
        else:
            self.june_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_value = None
        else:
            self.july_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_value = None
        else:
            self.august_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_value = None
        else:
            self.september_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_value = None
        else:
            self.october_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_value = None
        else:
            self.november_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_value = None
        else:
            self.december_value = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Variable Type`

        Args:
            value (str): value for IDD Field `Variable Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `variable_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `variable_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `variable_type`')
            vals = {}
            vals["energy"] = "Energy"
            vals["power"] = "Power"
            vals["dimensionless"] = "Dimensionless"
            vals["currency"] = "Currency"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `variable_type`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `January Value`

        Args:
            value (float): value for IDD Field `January Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `February Value`

        Args:
            value (float): value for IDD Field `February Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `March Value`

        Args:
            value (float): value for IDD Field `March Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `April Value`

        Args:
            value (float): value for IDD Field `April Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `May Value`

        Args:
            value (float): value for IDD Field `May Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `June Value`

        Args:
            value (float): value for IDD Field `June Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `July Value`

        Args:
            value (float): value for IDD Field `July Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `August Value`

        Args:
            value (float): value for IDD Field `August Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `September Value`

        Args:
            value (float): value for IDD Field `September Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `October Value`

        Args:
            value (float): value for IDD Field `October Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `November Value`

        Args:
            value (float): value for IDD Field `November Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `December Value`

        Args:
            value (float): value for IDD Field `December Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `december_value`'.format(value))
        self._data["December Value"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Tariff Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `UtilityCost:Computation`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tariff_name = None
        else:
            self.tariff_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_1 = None
        else:
            self.compute_step_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_2 = None
        else:
            self.compute_step_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_3 = None
        else:
            self.compute_step_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_4 = None
        else:
            self.compute_step_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_5 = None
        else:
            self.compute_step_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_6 = None
        else:
            self.compute_step_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_7 = None
        else:
            self.compute_step_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_8 = None
        else:
            self.compute_step_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_9 = None
        else:
            self.compute_step_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_10 = None
        else:
            self.compute_step_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_11 = None
        else:
            self.compute_step_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_12 = None
        else:
            self.compute_step_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_13 = None
        else:
            self.compute_step_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_14 = None
        else:
            self.compute_step_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_15 = None
        else:
            self.compute_step_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_16 = None
        else:
            self.compute_step_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_17 = None
        else:
            self.compute_step_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_18 = None
        else:
            self.compute_step_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_19 = None
        else:
            self.compute_step_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_20 = None
        else:
            self.compute_step_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_21 = None
        else:
            self.compute_step_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_22 = None
        else:
            self.compute_step_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_23 = None
        else:
            self.compute_step_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_24 = None
        else:
            self.compute_step_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_25 = None
        else:
            self.compute_step_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_26 = None
        else:
            self.compute_step_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_27 = None
        else:
            self.compute_step_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_28 = None
        else:
            self.compute_step_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_29 = None
        else:
            self.compute_step_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.compute_step_30 = None
        else:
            self.compute_step_30 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Tariff Name`
        The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.

        Args:
            value (str): value for IDD Field `Tariff Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `tariff_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tariff_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 1`
        Contain a simple language that describes the steps used in the computation process similar to a
        programming language.

        Args:
            value (str): value for IDD Field `Compute Step 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 2`

        Args:
            value (str): value for IDD Field `Compute Step 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 3`

        Args:
            value (str): value for IDD Field `Compute Step 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 4`

        Args:
            value (str): value for IDD Field `Compute Step 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 5`

        Args:
            value (str): value for IDD Field `Compute Step 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 6`

        Args:
            value (str): value for IDD Field `Compute Step 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 7`

        Args:
            value (str): value for IDD Field `Compute Step 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 8`

        Args:
            value (str): value for IDD Field `Compute Step 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 9`

        Args:
            value (str): value for IDD Field `Compute Step 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 10`

        Args:
            value (str): value for IDD Field `Compute Step 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 11`

        Args:
            value (str): value for IDD Field `Compute Step 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 12`

        Args:
            value (str): value for IDD Field `Compute Step 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 13`

        Args:
            value (str): value for IDD Field `Compute Step 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 14`

        Args:
            value (str): value for IDD Field `Compute Step 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 15`

        Args:
            value (str): value for IDD Field `Compute Step 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 16`

        Args:
            value (str): value for IDD Field `Compute Step 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 17`

        Args:
            value (str): value for IDD Field `Compute Step 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 18`

        Args:
            value (str): value for IDD Field `Compute Step 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 19`

        Args:
            value (str): value for IDD Field `Compute Step 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 20`

        Args:
            value (str): value for IDD Field `Compute Step 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 21`

        Args:
            value (str): value for IDD Field `Compute Step 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 22`

        Args:
            value (str): value for IDD Field `Compute Step 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 23`

        Args:
            value (str): value for IDD Field `Compute Step 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 24`

        Args:
            value (str): value for IDD Field `Compute Step 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 25`

        Args:
            value (str): value for IDD Field `Compute Step 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 26`

        Args:
            value (str): value for IDD Field `Compute Step 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 27`

        Args:
            value (str): value for IDD Field `Compute Step 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 28`

        Args:
            value (str): value for IDD Field `Compute Step 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 29`

        Args:
            value (str): value for IDD Field `Compute Step 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Compute Step 30`

        Args:
            value (str): value for IDD Field `Compute Step 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `compute_step_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `compute_step_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `compute_step_30`')
        self._data["Compute Step 30"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:Parameters`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discounting_convention = None
        else:
            self.discounting_convention = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inflation_approach = None
        else:
            self.inflation_approach = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.real_discount_rate = None
        else:
            self.real_discount_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_discount_rate = None
        else:
            self.nominal_discount_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inflation = None
        else:
            self.inflation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.base_date_month = None
        else:
            self.base_date_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.base_date_year = None
        else:
            self.base_date_year = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.service_date_month = None
        else:
            self.service_date_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.service_date_year = None
        else:
            self.service_date_year = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length_of_study_period_in_years = None
        else:
            self.length_of_study_period_in_years = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tax_rate = None
        else:
            self.tax_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.depreciation_method = None
        else:
            self.depreciation_method = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Discounting Convention`
        The field specifies if the discounting of future costs should be computed as occurring at the end
        of each year or the middle of each year or the beginning of each year. The most common discounting
        convention uses the end of each year.

        Args:
            value (str): value for IDD Field `Discounting Convention`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `discounting_convention`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discounting_convention`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `discounting_convention`')
            vals = {}
            vals["endofyear"] = "EndOfYear"
            vals["midyear"] = "MidYear"
            vals["beginningofyear"] = "BeginningOfYear"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `discounting_convention`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Inflation Approach`
        This field is used to determine if the analysis should use constant dollars or current dollars
        which is related to how inflation is treated. If ConstantDollar is selected then the Real Discount
        Rate input is used and it excludes the rate of inflation. If CurrentDollar is selected then the
        Nominal Discount Rate input is used and it includes the rate of inflation.

        Args:
            value (str): value for IDD Field `Inflation Approach`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `inflation_approach`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inflation_approach`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inflation_approach`')
            vals = {}
            vals["constantdollar"] = "ConstantDollar"
            vals["currentdollar"] = "CurrentDollar"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `inflation_approach`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Real Discount Rate`
        Enter the real discount rate as a decimal. For a 3% rate enter the value 0.03. This input is
        used when the Inflation Approach is ConstantDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when
        general inflation is ignored. When Inflation Approach is set to CurrentDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Real Discount Rate`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Nominal Discount Rate`
        Enter the nominal discount rate as a decimal. For a 5% rate enter the value 0.05. This input
        is used when the Inflation Approach is CurrentDollar. The real discount rate reflects the interest
        rates needed to make current and future expenditures have comparable equivalent values when general
        inflation is included. When Inflation Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Nominal Discount Rate`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Inflation`
        Enter the rate of inflation for general goods and services as a decimal. For a 2% rate enter
        the value 0.02.

        Args:
            value (float): value for IDD Field `Inflation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Base Date Month`
        Enter the month that is the beginning of study period also known as the beginning of the base period.

        Args:
            value (str): value for IDD Field `Base Date Month`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `base_date_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `base_date_month`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `base_date_month`')
            vals = {}
            vals["january"] = "January"
            vals["february"] = "February"
            vals["march"] = "March"
            vals["april"] = "April"
            vals["may"] = "May"
            vals["june"] = "June"
            vals["july"] = "July"
            vals["august"] = "August"
            vals["september"] = "September"
            vals["october"] = "October"
            vals["november"] = "November"
            vals["december"] = "December"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `base_date_month`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Base Date Year`
        Enter the four digit year that is the beginning of study period such as 2010. The study period is
        also known as the base period.

        Args:
            value (int): value for IDD Field `Base Date Year`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Service Date Month`
        Enter the month that is the beginning of building occupancy. Energy costs computed by EnergyPlus
        are assumed to occur during the year following the service date. The service date must be the
        same or later than the Base Date. This field could also be referred to as part of beneficial
        occupancy date.

        Args:
            value (str): value for IDD Field `Service Date Month`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `service_date_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `service_date_month`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `service_date_month`')
            vals = {}
            vals["january"] = "January"
            vals["february"] = "February"
            vals["march"] = "March"
            vals["april"] = "April"
            vals["may"] = "May"
            vals["june"] = "June"
            vals["july"] = "July"
            vals["august"] = "August"
            vals["september"] = "September"
            vals["october"] = "October"
            vals["november"] = "November"
            vals["december"] = "December"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `service_date_month`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Service Date Year`
        Enter the four digit year that is the beginning of occupancy such as 2010.

        Args:
            value (int): value for IDD Field `Service Date Year`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Length of Study Period in Years`
        Enter the number of years of the study period. It is the number of years that the study continues
        based on the start at the base date. The default value is 25 years. Only integers may be used
        indicating whole years.

        Args:
            value (int): value for IDD Field `Length of Study Period in Years`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Tax rate`
        Enter the overall marginal tax rate for the project costs. This does not include energy or water
        taxes. The tax rate entered should be based on the marginal tax rate for the entity and not the
        average tax rate. Enter the tax rate results in present value calculations after taxes. Most
        analyses do not factor in the impact of taxes and assume that all options under consideration
        have roughly the same tax impact. Due to this many times the tax rate can be left to default
        to zero and the present value results before taxes are used to make decisions. The value
        should be entered as a decimal value. For 15% enter 0.15. For an analysis that does not include
        tax impacts enter 0.0.

        Args:
            value (float): value for IDD Field `Tax rate`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Depreciation Method`
        For an analysis that includes income tax impacts this entry describes how capital costs are
        depreciated. Only one depreciation method may be used for an analysis and is applied to all
        capital expenditures.

        Args:
            value (str): value for IDD Field `Depreciation Method`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `depreciation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `depreciation_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `depreciation_method`')
            vals = {}
            vals["modifiedacceleratedcostrecoverysystem-3year"] = "ModifiedAcceleratedCostRecoverySystem-3year"
            vals["modifiedacceleratedcostrecoverysystem-5year"] = "ModifiedAcceleratedCostRecoverySystem-5year"
            vals["modifiedacceleratedcostrecoverysystem-7year"] = "ModifiedAcceleratedCostRecoverySystem-7year"
            vals["modifiedacceleratedcostrecoverysystem-10year"] = "ModifiedAcceleratedCostRecoverySystem-10year"
            vals["modifiedacceleratedcostrecoverysystem-15year"] = "ModifiedAcceleratedCostRecoverySystem-15year"
            vals["modifiedacceleratedcostrecoverysystem-20year"] = "ModifiedAcceleratedCostRecoverySystem-20year"
            vals["straightline-27year"] = "StraightLine-27year"
            vals["straightline-31year"] = "StraightLine-31year"
            vals["straightline-39year"] = "StraightLine-39year"
            vals["straightline-40year"] = "StraightLine-40year"
            vals["none"] = "None"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `depreciation_method`'.format(value))
            value = vals[value_lower]
        self._data["Depreciation Method"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class LifeCycleCostRecurringCosts(object):
    """ Corresponds to IDD object `LifeCycleCost:RecurringCosts`
        Recurring costs are costs that repeat over time on a regular schedule during the
        study period. If costs associated with equipment do repeat but not on a regular
        schedule, use LifeCycleCost:NonrecurringCost objects instead.
    
    """
    internal_name = "LifeCycleCost:RecurringCosts"
    field_count = 9
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:RecurringCosts`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.category = None
        else:
            self.category = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost = None
        else:
            self.cost = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_of_costs = None
        else:
            self.start_of_costs = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.years_from_start = None
        else:
            self.years_from_start = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.months_from_start = None
        else:
            self.months_from_start = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.repeat_period_years = None
        else:
            self.repeat_period_years = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.repeat_period_months = None
        else:
            self.repeat_period_months = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.annual_escalation_rate = None
        else:
            self.annual_escalation_rate = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Category`

        Args:
            value (str): value for IDD Field `Category`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `category`')
            vals = {}
            vals["maintenance"] = "Maintenance"
            vals["repair"] = "Repair"
            vals["operation"] = "Operation"
            vals["replacement"] = "Replacement"
            vals["minoroverhaul"] = "MinorOverhaul"
            vals["majoroverhaul"] = "MajorOverhaul"
            vals["otheroperational"] = "OtherOperational"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `category`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Cost`
        Enter the cost in dollars (or the appropriate monetary unit) for the recurring costs. Enter
        the cost for each time it occurs. For example if the annual maintenance cost is 500 dolllars
        enter 500 here.

        Args:
            value (float): value for IDD Field `Cost`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Start of Costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most maintenance costs the Start of Costs should be Service Period.

        Args:
            value (str): value for IDD Field `Start of Costs`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `start_of_costs`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_of_costs`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `start_of_costs`')
            vals = {}
            vals["serviceperiod"] = "ServicePeriod"
            vals["baseperiod"] = "BasePeriod"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `start_of_costs`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Years from Start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `Years from Start`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Months from Start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Costs field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `Months from Start`
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
            except ValueError:
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
    def repeat_period_years(self, value=1):
        """  Corresponds to IDD Field `Repeat Period Years`
        This field and the Repeat Period Months field indicate how much time elapses between
        reoccurrences of the cost. For costs that occur every year such the Repeat Period Years
        should be 1 and Repeat Period Months should be 0. Only integers should be entered
        representing whole years.

        Args:
            value (int): value for IDD Field `Repeat Period Years`
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
            except ValueError:
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
    def repeat_period_months(self, value=0):
        """  Corresponds to IDD Field `Repeat Period Months`
        This field and the Repeat Period Years field indicate how much time elapses between
        reoccurrences of the cost. Only integers should be entered representing whole years.
        The Repeat Period Years (times 12) and Repeat Period Months are added together.

        Args:
            value (int): value for IDD Field `Repeat Period Months`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Annual escalation rate`
        Enter the annual escalation rate as a decimal. For a 1% rate enter the value 0.01.
        This input is used when the Inflation Approach is CurrentDollar. When Inflation
        Approach is set to ConstantDollar this input is ignored.

        Args:
            value (float): value for IDD Field `Annual escalation rate`
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
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `annual_escalation_rate`'.format(value))
            if value < -0.3:
                raise ValueError('value need to be greater or equal -0.3 '
                                 'for field `annual_escalation_rate`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `annual_escalation_rate`')
        self._data["Annual escalation rate"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class LifeCycleCostNonrecurringCost(object):
    """ Corresponds to IDD object `LifeCycleCost:NonrecurringCost`
        A non-recurring cost happens only once during the study period. For costs that occur
        more than once during the study period on a regular schedule, use the
        LifeCycleCost:RecurringCost object.
    
    """
    internal_name = "LifeCycleCost:NonrecurringCost"
    field_count = 6
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:NonrecurringCost`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Category"] = None
        self._data["Cost"] = None
        self._data["Start of Costs"] = None
        self._data["Years from Start"] = None
        self._data["Months from Start"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.category = None
        else:
            self.category = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cost = None
        else:
            self.cost = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.start_of_costs = None
        else:
            self.start_of_costs = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.years_from_start = None
        else:
            self.years_from_start = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.months_from_start = None
        else:
            self.months_from_start = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Category`

        Args:
            value (str): value for IDD Field `Category`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `category`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `category`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `category`')
            vals = {}
            vals["construction"] = "Construction"
            vals["salvage"] = "Salvage"
            vals["othercapital"] = "OtherCapital"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `category`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Cost`
        Enter the non-recurring cost value. For construction and other capital costs the value
        entered is typically a positive value. For salvage costs the value entered is typically a
        negative value which represents the money paid to the investor for the equipment at the
        end of the study period.

        Args:
            value (float): value for IDD Field `Cost`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Start of Costs`
        Enter when the costs start. The First Year of Cost is based on the number of years past the
        Start of Costs. For most non-recurring costs the Start of Costs should be Base Period which
        begins at the base month and year.

        Args:
            value (str): value for IDD Field `Start of Costs`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `start_of_costs`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `start_of_costs`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `start_of_costs`')
            vals = {}
            vals["serviceperiod"] = "ServicePeriod"
            vals["baseperiod"] = "BasePeriod"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `start_of_costs`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Years from Start`
        This field and the Months From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole years.

        Args:
            value (int): value for IDD Field `Years from Start`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Months from Start`
        This field and the Years From Start field together represent the time from either the start
        of the Service Period on the service month and year or start of the Base Period on the base
        month and year (depending on the Start of Cost field) that the costs start to occur. Only
        integers should be entered representing whole months. The Years From Start (times 12) and
        Months From Start are added together.

        Args:
            value (int): value for IDD Field `Months from Start`
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
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `months_from_start`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `months_from_start`')
            if value > 1200:
                raise ValueError('value need to be smaller 1200 '
                                 'for field `months_from_start`')
        self._data["Months from Start"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class LifeCycleCostUsePriceEscalation(object):
    """ Corresponds to IDD object `LifeCycleCost:UsePriceEscalation`
        Life cycle cost escalation factors. The values for this object may be found in the
        annual supplement to NIST Handbook 135 in Tables Ca-1 to Ca-5 and are included in an
        EnergyPlus dataset file.
    
    """
    internal_name = "LifeCycleCost:UsePriceEscalation"
    field_count = 34
    required_fields = ["Name", "Resource"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:UsePriceEscalation`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.resource = None
        else:
            self.resource = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.escalation_start_year = None
        else:
            self.escalation_start_year = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.escalation_start_month = None
        else:
            self.escalation_start_month = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_1_escalation = None
        else:
            self.year_1_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_2_escalation = None
        else:
            self.year_2_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_3_escalation = None
        else:
            self.year_3_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_4_escalation = None
        else:
            self.year_4_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_5_escalation = None
        else:
            self.year_5_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_6_escalation = None
        else:
            self.year_6_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_7_escalation = None
        else:
            self.year_7_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_8_escalation = None
        else:
            self.year_8_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_9_escalation = None
        else:
            self.year_9_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_10_escalation = None
        else:
            self.year_10_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_11_escalation = None
        else:
            self.year_11_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_12_escalation = None
        else:
            self.year_12_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_13_escalation = None
        else:
            self.year_13_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_14_escalation = None
        else:
            self.year_14_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_15_escalation = None
        else:
            self.year_15_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_16_escalation = None
        else:
            self.year_16_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_17_escalation = None
        else:
            self.year_17_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_18_escalation = None
        else:
            self.year_18_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_19_escalation = None
        else:
            self.year_19_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_20_escalation = None
        else:
            self.year_20_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_21_escalation = None
        else:
            self.year_21_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_22_escalation = None
        else:
            self.year_22_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_23_escalation = None
        else:
            self.year_23_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_24_escalation = None
        else:
            self.year_24_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_25_escalation = None
        else:
            self.year_25_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_26_escalation = None
        else:
            self.year_26_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_27_escalation = None
        else:
            self.year_27_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_28_escalation = None
        else:
            self.year_28_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_29_escalation = None
        else:
            self.year_29_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_30_escalation = None
        else:
            self.year_30_escalation = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        The identifier used for the object. The name usually identifies the location (such as the
        state or region or country or census area) that the escalations apply to. In addition the
        name should identify the building class such as residential or commercial or industrial
        and the use type such as electricity or natural gas or water.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Resource`

        Args:
            value (str): value for IDD Field `Resource`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `resource`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `resource`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["electricitypurchased"] = "ElectricityPurchased"
            vals["electricityproduced"] = "ElectricityProduced"
            vals["electricitysurplussold"] = "ElectricitySurplusSold"
            vals["electricitynet"] = "ElectricityNet"
            vals["naturalgas"] = "NaturalGas"
            vals["steam"] = "Steam"
            vals["gasoline"] = "Gasoline"
            vals["diesel"] = "Diesel"
            vals["coal"] = "Coal"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["propane"] = "Propane"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["water"] = "Water"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `resource`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Escalation Start Year`
        This field and the Escalation Start Month define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Month
        define the time that escalation begins.

        Args:
            value (int): value for IDD Field `Escalation Start Year`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Escalation Start Month`
        This field and the Escalation Start Year define the time that corresponds to Year 1 Escalation
        such as 2010 when the escalation rates are applied. This field and the Escalation Start Year
        define the time that escalation begins.

        Args:
            value (str): value for IDD Field `Escalation Start Month`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `escalation_start_month`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `escalation_start_month`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `escalation_start_month`')
            vals = {}
            vals["january"] = "January"
            vals["february"] = "February"
            vals["march"] = "March"
            vals["april"] = "April"
            vals["may"] = "May"
            vals["june"] = "June"
            vals["july"] = "July"
            vals["august"] = "August"
            vals["september"] = "September"
            vals["october"] = "October"
            vals["november"] = "November"
            vals["december"] = "December"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `escalation_start_month`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Year 1 Escalation`
        The escalation in price of the energy or water use for the first year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 1 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 2 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 2 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 3 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 3 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 4 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 4 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 5 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 5 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 6 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 6 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 7 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 7 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 8 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 8 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 9 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 9 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 10 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 10 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 11 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 11 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 12 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 12 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 13 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 13 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 14 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 14 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 15 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 15 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 16 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 16 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 17 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 17 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 18 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 18 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 19 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 19 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 20 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 20 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 21 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 21 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 22 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 22 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 23 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 23 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 24 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 24 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 25 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 25 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 26 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 26 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 27 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 27 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 28 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 28 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 29 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 29 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 30 Escalation`
        The escalation in price of the energy or water use for the year expressed as a decimal.

        Args:
            value (float): value for IDD Field `Year 30 Escalation`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `year_30_escalation`'.format(value))
        self._data["Year 30 Escalation"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

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
    required_fields = ["Name", "Resource"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LifeCycleCost:UseAdjustment`
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.resource = None
        else:
            self.resource = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_1_multiplier = None
        else:
            self.year_1_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_2_multiplier = None
        else:
            self.year_2_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_3_multiplier = None
        else:
            self.year_3_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_4_multiplier = None
        else:
            self.year_4_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_5_multiplier = None
        else:
            self.year_5_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_6_multiplier = None
        else:
            self.year_6_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_7_multiplier = None
        else:
            self.year_7_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_8_multiplier = None
        else:
            self.year_8_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_9_multiplier = None
        else:
            self.year_9_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_10_multiplier = None
        else:
            self.year_10_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_11_multiplier = None
        else:
            self.year_11_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_12_multiplier = None
        else:
            self.year_12_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_13_multiplier = None
        else:
            self.year_13_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_14_multiplier = None
        else:
            self.year_14_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_15_multiplier = None
        else:
            self.year_15_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_16_multiplier = None
        else:
            self.year_16_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_17_multiplier = None
        else:
            self.year_17_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_18_multiplier = None
        else:
            self.year_18_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_19_multiplier = None
        else:
            self.year_19_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_20_multiplier = None
        else:
            self.year_20_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_21_multiplier = None
        else:
            self.year_21_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_22_multiplier = None
        else:
            self.year_22_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_23_multiplier = None
        else:
            self.year_23_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_24_multiplier = None
        else:
            self.year_24_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_25_multiplier = None
        else:
            self.year_25_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_26_multiplier = None
        else:
            self.year_26_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_27_multiplier = None
        else:
            self.year_27_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_28_multiplier = None
        else:
            self.year_28_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_29_multiplier = None
        else:
            self.year_29_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.year_30_multiplier = None
        else:
            self.year_30_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Resource`

        Args:
            value (str): value for IDD Field `Resource`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `resource`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `resource`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `resource`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["electricitypurchased"] = "ElectricityPurchased"
            vals["electricityproduced"] = "ElectricityProduced"
            vals["electricitysurplussold"] = "ElectricitySurplusSold"
            vals["electricitynet"] = "ElectricityNet"
            vals["naturalgas"] = "NaturalGas"
            vals["steam"] = "Steam"
            vals["gasoline"] = "Gasoline"
            vals["diesel"] = "Diesel"
            vals["coal"] = "Coal"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["propane"] = "Propane"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["water"] = "Water"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `resource`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Year 1 Multiplier`
        The multiplier to be applied to the end-use cost for the first year in the service period.
        The total utility costs for the selected end-use is multiplied by this value. For no change
        enter 1.0.

        Args:
            value (float): value for IDD Field `Year 1 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 2 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 2 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 3 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 3 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 4 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 4 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 5 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 5 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 6 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 6 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 7 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 7 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 8 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 8 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 9 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 9 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 10 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 10 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 11 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 11 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 12 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 12 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 13 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 13 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 14 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 14 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 15 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 15 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 16 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 16 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 17 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 17 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 18 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 18 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 19 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 19 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 20 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 20 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 21 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 21 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 22 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 22 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 23 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 23 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 24 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 24 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 25 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 25 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 26 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 26 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 27 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 27 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 28 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 28 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 29 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 29 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Year 30 Multiplier`
        The multiplier to be applied to the end-use cost for each following year. The total utility
        costs for the selected end-use is multiplied by this value. For no change enter 1.0.

        Args:
            value (float): value for IDD Field `Year 30 Multiplier`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `year_30_multiplier`'.format(value))
        self._data["Year 30 Multiplier"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])