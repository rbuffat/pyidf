from collections import OrderedDict

class CurrencyType(object):
    """ Corresponds to IDD object `CurrencyType`
        If CurrencyType is not specified, it will default to USD and produce $ in the reports.
    """
    internal_name = "CurrencyType"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CurrencyType`
        """
        self._data = OrderedDict()
        self._data["Monetary Unit"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.monetary_unit = None
        else:
            self.monetary_unit = vals[i]
        i += 1

    @property
    def monetary_unit(self):
        """Get monetary_unit

        Returns:
            str: the value of `monetary_unit` or None if not set
        """
        return self._data["Monetary Unit"]

    @monetary_unit.setter
    def monetary_unit(self, value=None):
        """  Corresponds to IDD Field `monetary_unit`
        The commonly used three letter currency code for the units of money for the country or region.
        Based on ISO 4217 currency codes.  Common currency codes are USD for $ and EUR for Euros.

        Args:
            value (str): value for IDD Field `monetary_unit`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `monetary_unit`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `monetary_unit`')
            vals = set()
            vals.add("USD")
            vals.add("AFN")
            vals.add("ALL")
            vals.add("ANG")
            vals.add("ARS")
            vals.add("AUD")
            vals.add("AWG")
            vals.add("AZN")
            vals.add("BAM")
            vals.add("BBD")
            vals.add("BGN")
            vals.add("BMD")
            vals.add("BND")
            vals.add("BOB")
            vals.add("BRL")
            vals.add("BSD")
            vals.add("BWP")
            vals.add("BYR")
            vals.add("BZD")
            vals.add("CAD")
            vals.add("CHF")
            vals.add("CLP")
            vals.add("CNY")
            vals.add("COP")
            vals.add("CRC")
            vals.add("CUP")
            vals.add("CZK")
            vals.add("DKK")
            vals.add("DOP")
            vals.add("EEK")
            vals.add("EGP")
            vals.add("EUR")
            vals.add("FJD")
            vals.add("GBP")
            vals.add("GHC")
            vals.add("GIP")
            vals.add("GTQ")
            vals.add("GYD")
            vals.add("HKD")
            vals.add("HNL")
            vals.add("HRK")
            vals.add("HUF")
            vals.add("IDR")
            vals.add("ILS")
            vals.add("IMP")
            vals.add("INR")
            vals.add("IRR")
            vals.add("ISK")
            vals.add("JEP")
            vals.add("JMD")
            vals.add("JPY")
            vals.add("KGS")
            vals.add("KHR")
            vals.add("KPW")
            vals.add("KRW")
            vals.add("KYD")
            vals.add("KZT")
            vals.add("LAK")
            vals.add("LBP")
            vals.add("LKR")
            vals.add("LRD")
            vals.add("LTL")
            vals.add("LVL")
            vals.add("MKD")
            vals.add("MNT")
            vals.add("MUR")
            vals.add("MXN")
            vals.add("MYR")
            vals.add("MZN")
            vals.add("NAD")
            vals.add("NGN")
            vals.add("NIO")
            vals.add("NOK")
            vals.add("NPR")
            vals.add("NZD")
            vals.add("OMR")
            vals.add("PAB")
            vals.add("PEN")
            vals.add("PHP")
            vals.add("PKR")
            vals.add("PLN")
            vals.add("PYG")
            vals.add("QAR")
            vals.add("RON")
            vals.add("RSD")
            vals.add("RUB")
            vals.add("SAR")
            vals.add("SBD")
            vals.add("SCR")
            vals.add("SEK")
            vals.add("SGD")
            vals.add("SHP")
            vals.add("SOS")
            vals.add("SRD")
            vals.add("SVC")
            vals.add("SYP")
            vals.add("THB")
            vals.add("TRL")
            vals.add("TRY")
            vals.add("TTD")
            vals.add("TVD")
            vals.add("TWD")
            vals.add("UAH")
            vals.add("UYU")
            vals.add("UZS")
            vals.add("VEF")
            vals.add("VND")
            vals.add("XCD")
            vals.add("YER")
            vals.add("ZAR")
            vals.add("ZWD")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `monetary_unit`'.format(value))

        self._data["Monetary Unit"] = value

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
        out.append(self._to_str(self.monetary_unit))
        return ",".join(out)