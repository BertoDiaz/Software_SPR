"""
Copyright (C) 2018  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class Queue:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) > 0:
            value = self.data[0]
            del self.data[0]

        else:
            value = -1

        return value
