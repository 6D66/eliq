#!/usr/bin/env python
#
#  A library for Eliq Online API
#  Copyright (C) 2015 Magnus F <magnus@fet.nu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import unittest
import sys
from .unittools import UnitTools

sys.path.append('.')

import eliqonline


class ToolTest(unittest.TestCase):

    unit_tools = None

    eliq_online = None
    token_string = None

    def setUp(self):
        self.unit_tools = UnitTools()
        self.token_string = self.unit_tools.get_random_string()
        self.eliq_online = eliqonline.API(self.token_string)

    def test_init(self):
        self.assertEquals(
            self.token_string,
            self.eliq_online.tools.ACCESS_TOKEN
        )

    def test_maybe_to_date(self):
        str_date = "2015-01-01"
        str_time = "T12:00:00"
        str_datetime = "%s%s" % (str_date, str_time)
        date = self.eliq_online.tools.maybe_to_date(str_datetime)
        self.assertEqual(str_date, str(date.date()))

    def test_maybe_to_date_none(self):
        date = self.eliq_online.tools.maybe_to_date(None)
        self.assertEqual(None, date)

    def test_to_date(self):
        str_date = "2015-01-01"
        str_time = "12:00:00"
        str_datetime = "%sT%s" % (str_date, str_time)
        date_value = self.eliq_online.tools.to_date(str_datetime)
        self.assertEqual(str_date, str(date_value.date()))
        self.assertEqual(str_time, str(date_value.time()))

    def test_maybe_to_float(self):
        str_float = str(self.unit_tools.get_random_float())
        value = self.eliq_online.tools.maybe_to_float(str_float)

        self.assertEqual(
            float(str_float),
            value
        )

    def test_maybe_to_float_none(self):
        value = self.eliq_online.tools.maybe_to_float(None)
        self.assertEqual(None, value)

if __name__ == '__main__':
        unittest.main()