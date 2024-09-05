from conversion import TemperatureUnit, LengthUnit, WeightUnit

temp = TemperatureUnit()

length = LengthUnit()

weight = WeightUnit()


def temp_unit_conversion(value, convert_from, convert_to):
    if convert_from == convert_to:
        return value
    if convert_to == "no-selection" or convert_from == "no-selection":
        return value

    if convert_from == "celsius" and convert_to == "fahrenheit":
        return temp.celsius_to_fahrenheit(value)
    elif convert_from == "celsius" and convert_to == "kelvin":
        return temp.celsius_to_kelvin(value)
    elif convert_from == "fahrenheit" and convert_to == "celsius":
        return temp.fahrenheit_to_celsius(value)
    elif convert_from == "fahrenheit" and convert_to == "kelvin":
        return temp.fahrenheit_to_kelvin(value)
    elif convert_from == "kelvin" and convert_to == "celsius":
        return temp.kelvin_to_celsius(value)
    elif convert_from == "kelvin" and convert_to == "fahrenheit":
        return temp.kelvin_to_fahrenheit(value)


def weight_unit_conversion(value, convert_from, convert_to):
    if convert_from == convert_to:
        return value
    elif convert_to == "no-selection" or convert_from == "no-selection":
        return value
    elif convert_from == "milligram" and convert_to == "gram":
        return weight.milligram_to_gram(value)
    elif convert_from == "milligram" and convert_to == "kilogram":
        return weight.milligram_to_kilogram(value)
    elif convert_from == "milligram" and convert_to == "ounce":
        return weight.milligram_to_ounce(value)
    elif convert_from == "milligram" and convert_to == "pound":
        return weight.milligram_to_pound(value)
    elif convert_from == "gram" and convert_to == "milligram":
        return weight.gram_to_milligram(value)
    elif convert_from == "gram" and convert_to == "kilogram":
        return weight.gram_to_kilogram(value)
    elif convert_from == "gram" and convert_to == "ounce":
        return weight.gram_to_ounce(value)
    elif convert_from == "gram" and convert_to == "pound":
        return weight.gram_to_pound(value)
    elif convert_from == "kilogram" and convert_to == "milligram":
        return weight.kilogram_to_milligram(value)
    elif convert_from == "kilogram" and convert_to == "ounce":
        return weight.kilogram_to_ounce(value)
    elif convert_from == "kilogram" and convert_to == "pound":
        return weight.kilogram_to_pound(value)
    elif convert_from == "kilogram" and convert_to == "pound":
        return weight.kilogram_to_pound(value)
    elif convert_from == "ounce" and convert_to == "milligram":
        return weight.ounce_to_milligram(value)
    elif convert_from == "ounce" and convert_to == "pound":
        return weight.ounce_to_pound(value)
    elif convert_from == "ounce" and convert_to == "kilogram":
        return weight.ounce_to_kilogram(value)
    elif convert_from == "pound" and convert_to == "milligram":
        return weight.pound_to_milligram(value)


def length_unit_conversion(value, convert_from, convert_to):
    if convert_from == convert_to:
        return value
    elif convert_to == "no-selection" or convert_from == "no-selection":
        return value

    elif convert_from == "millimeter" and convert_to == "centimeter":
        return length.millimeter_to_centimeter(value)
    elif convert_from == "millimeter" and convert_to == "meter":
        return length.millimeter_to_meter(value)
    elif convert_from == "millimeter" and convert_to == "kilometer":
        return length.millimeter_to_kilometer(value)
    elif convert_from == "millimeter" and convert_to == "inch":
        return length.millimeter_to_inch(value)
    elif convert_from == "millimeter" and convert_to == "foot":
        return length.millimeter_to_foot(value)
    elif convert_from == "millimeter" and convert_to == "yard":
        return length.millimeter_to_yard(value)
    elif convert_from == "millimeter" and convert_to == "mile":
        return length.millimeter_to_mile(value)

    elif convert_from == "centimeter" and convert_to == "millimeter":
        return length.centimeter_to_millimeter(value)
    elif convert_from == "centimeter" and convert_to == "meter":
        return length.centimeter_to_meter(value)
    elif convert_from == "centimeter" and convert_to == "kilometer":
        return length.centimeter_to_kilometer(value)
    elif convert_from == "centimeter" and convert_to == "inch":
        return length.centimeter_to_inch(value)
    elif convert_from == "centimeter" and convert_to == "foot":
        return length.centimeter_to_foot(value)
    elif convert_from == "centimeter" and convert_to == "yard":
        return length.centimeter_to_yard(value)
    elif convert_from == "centimeter" and convert_to == "mile":
        return length.centimeter_to_mile(value)

    elif convert_from == "meter" and convert_to == "millimeter":
        return length.meter_to_millimeter(value)
    elif convert_from == "meter" and convert_to == "centimeter":
        return length.meter_to_centimeter(value)
    elif convert_from == "meter" and convert_to == "kilometer":
        return length.meter_to_kilometer(value)
    elif convert_from == "meter" and convert_to == "inch":
        return length.meter_to_inch(value)
    elif convert_from == "meter" and convert_to == "foot":
        return length.meter_to_foot(value)
    elif convert_from == "meter" and convert_to == "yard":
        return length.meter_to_yard(value)
    elif convert_from == "meter" and convert_to == "mile":
        return length.meter_to_mile(value)

    elif convert_from == "kilometer" and convert_to == "millimeter":
        return length.kilometer_to_millimeter(value)
    elif convert_from == "kilometer" and convert_to == "centimeter":
        return length.kilometer_to_centimeter(value)
    elif convert_from == "kilometer" and convert_to == "meter":
        return length.kilometer_to_meter(value)
    elif convert_from == "kilometer" and convert_to == "inch":
        return length.kilometer_to_inch(value)
    elif convert_from == "kilometer" and convert_to == "foot":
        return length.kilometer_to_foot(value)
    elif convert_from == "kilometer" and convert_to == "yard":
        return length.kilometer_to_yard(value)
    elif convert_from == "kilometer" and convert_to == "mile":
        return length.kilometer_to_mile(value)

    elif convert_from == "inch" and convert_to == "millimeter":
        return length.inch_to_millimeter(value)
    elif convert_from == "inch" and convert_to == "centimeter":
        return length.inch_to_centimeter(value)
    elif convert_from == "inch" and convert_to == "meter":
        return length.inch_to_meter(value)
    elif convert_from == "inch" and convert_to == "kilometer":
        return length.inch_to_kilometer(value)
    elif convert_from == "inch" and convert_to == "foot":
        return length.inch_to_foot(value)
    elif convert_from == "inch" and convert_to == "yard":
        return length.inch_to_yard(value)
    elif convert_from == "inch" and convert_to == "mile":
        return length.inch_to_mile(value)

    elif convert_from == "foot" and convert_to == "millimeter":
        return length.foot_to_millimeter(value)
    elif convert_from == "foot" and convert_to == "centimeter":
        return length.foot_to_centimeter(value)
    elif convert_from == "foot" and convert_to == "meter":
        return length.foot_to_meter(value)
    elif convert_from == "foot" and convert_to == "kilometer":
        return length.foot_to_kilometer(value)
    elif convert_from == "foot" and convert_to == "inch":
        return length.foot_to_inch(value)
    elif convert_from == "foot" and convert_to == "yard":
        return length.foot_to_yard(value)
    elif convert_from == "foot" and convert_to == "mile":
        return length.foot_to_mile(value)

    elif convert_from == "yard" and convert_to == "millimeter":
        return length.yard_to_millimeter(value)
    elif convert_from == "yard" and convert_to == "centimeter":
        return length.yard_to_centimeter(value)
    elif convert_from == "yard" and convert_to == "meter":
        return length.yard_to_meter(value)
    elif convert_from == "yard" and convert_to == "kilometer":
        return length.yard_to_kilometer(value)
    elif convert_from == "yard" and convert_to == "inch":
        return length.yard_to_inch(value)
    elif convert_from == "yard" and convert_to == "foot":
        return length.yard_to_foot(value)
    elif convert_from == "yard" and convert_to == "mile":
        return length.yard_to_mile(value)

    elif convert_from == "mile" and convert_to == "millimeter":
        return length.mile_to_millimeter(value)
    elif convert_from == "mile" and convert_to == "centimeter":
        return length.mile_to_centimeter(value)
    elif convert_from == "mile" and convert_to == "meter":
        return length.mile_to_meter(value)
    elif convert_from == "mile" and convert_to == "kilometer":
        return length.mile_to_kilometer(value)
    elif convert_from == "mile" and convert_to == "inch":
        return length.mile_to_inch(value)
    elif convert_from == "mile" and convert_to == "foot":
        return length.mile_to_foot(value)
    elif convert_from == "mile" and convert_to == "yard":
        return length.mile_to_yard(value)
