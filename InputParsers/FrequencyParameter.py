__author__ = 'Austin Havens'

# TODO: may want to derive this from parameter to eliminate going between the two
class FrequencyParameter:

    def __init__(self, minValue, maxValue, defaultValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.defaultValue = defaultValue