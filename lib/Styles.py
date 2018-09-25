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

# blueLight = '#99CCFF'
# blueDark = '#66B3FF'
blueLight = '#0080FF'
blueDark = '#0174DF'
# blueHoverLight = '#0080FF'
# blueHoverDark = '#0174DF'
blueHoverLight = '#0169CB'
blueHoverDark = '#014F98'
# greenLight = '#85E085'
# greenDark = '#5DD55D'
greenLight = '#04B404'
greenDark = '#088A08'
# greenHoverLight = '#04B404'
# greenHoverDark = '#088A08'
greenHoverLight = '#099009'
greenHoverDark = '#066006'
orangeLight = '#FAAC58'
orangeDark = '#FF8000'
orangeHoverLight = '#FF8000'
orangeHoverDark = '#DF7401'

buttonLaserBig = 'QPushButton {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                 'border-radius: 4px;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                 'font: bold;' \
                 'font-size: 20px;' \
                 'color: white;' \
                 'height: 100px;' \
                 'width: 130px;' \
                 'margin-top: 8px;' \
                 '}' \
                 'QPushButton:hover {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                 '}' \
                 'QPushButton:pressed {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                 '}' \
                 'QPushButton:checked {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                 '}' \
                 'QPushButton:hover:checked {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                 '}' \
                 'QPushButton:pressed:checked {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                 '}'

buttonLaserSmall = 'QPushButton {' \
                   'border-width: 1px;' \
                   'border-style: inset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                   'border-radius: 4px;' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                   'font: bold;' \
                   'font-size: 12px;' \
                   'color: white;' \
                   'height: 70px;' \
                   'width: 80px;' \
                   '}' \
                   'QPushButton:hover {' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                   '}' \
                   'QPushButton:pressed {' \
                   'border-width: 1px;' \
                   'border-style: outset;' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                   '}' \
                   'QPushButton:checked {' \
                   'border-width: 1px;' \
                   'border-style: inset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                   '}' \
                   'QPushButton:hover:checked {' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                   '}' \
                   'QPushButton:pressed:checked {' \
                   'border-width: 1px;' \
                   'border-style: outset;' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                   '}'

buttonLaserAcquisitionSmall = 'QPushButton {' \
                              'border-width: 1px;' \
                              'border-style: inset;' \
                              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                              'border-radius: 4px;' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                              'font: bold;' \
                              'font-size: 12px;' \
                              'color: white;' \
                              'height: 80px;' \
                              'width: 80px;' \
                              '}' \
                              'QPushButton:hover {' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                              '}' \
                              'QPushButton:pressed {' \
                              'border-width: 1px;' \
                              'border-style: outset;' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                              '}' \
                              'QPushButton:checked {' \
                              'border-width: 1px;' \
                              'border-style: inset;' \
                              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                              '}' \
                              'QPushButton:hover:checked {' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                              '}' \
                              'QPushButton:pressed:checked {' \
                              'border-width: 1px;' \
                              'border-style: outset;' \
                              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                              '}'

buttonPeristaltic = 'QPushButton {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'border-radius: 4px;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'font: bold;' \
                    'font-size: 12px;' \
                    'color: white;' \
                    'height: 70px;' \
                    'width: 80px;' \
                    'margin-top: 8px;' \
                    '}' \
                    'QPushButton:hover {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:checked {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    '}' \
                    'QPushButton:hover:checked {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed:checked {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}'

buttonImpulsional = 'QPushButton {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'border-radius: 4px;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'font: bold;' \
                    'font-size: 12px;' \
                    'color: white;' \
                    'height: 70px;' \
                    'width: 80px;' \
                    'margin-top: 8px;' \
                    '}' \
                    'QPushButton:hover {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:checked {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    '}' \
                    'QPushButton:hover:checked {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed:checked {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}'

buttonImpulsionalSmall = 'QPushButton {' \
                         'border-width: 1px;' \
                         'border-style: inset;' \
                         'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                         'border-radius: 4px;' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                         'font: bold;' \
                         'font-size: 12px;' \
                         'color: white;' \
                         'height: 20px;' \
                         'width: 60px;' \
                         '}' \
                         'QPushButton:hover {' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                         '}' \
                         'QPushButton:pressed {' \
                         'border-width: 1px;' \
                         'border-style: outset;' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                         '}' \
                         'QPushButton:checked {' \
                         'border-width: 1px;' \
                         'border-style: inset;' \
                         'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                         '}' \
                         'QPushButton:hover:checked {' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                         '}' \
                         'QPushButton:pressed:checked {' \
                         'border-width: 1px;' \
                         'border-style: outset;' \
                         'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                         'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                         '}'

buttonCalibrate = 'QPushButton {' \
                  'border-width: 1px;' \
                  'border-style: inset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                  'border-radius: 4px;' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                  'font: bold;' \
                  'font-size: 12px;' \
                  'color: white;' \
                  'height: 70px;' \
                  'width: 80px;' \
                  'margin-top: 8px;' \
                  '}' \
                  'QPushButton:hover {' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                  '}' \
                  'QPushButton:pressed {' \
                  'border-width: 1px;' \
                  'border-style: outset;' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                  '}' \
                  'QPushButton:checked {' \
                  'border-width: 1px;' \
                  'border-style: inset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                  '}' \
                  'QPushButton:hover:checked {' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                  '}' \
                  'QPushButton:pressed:checked {' \
                  'border-width: 1px;' \
                  'border-style: outset;' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                  '}'

buttonCalibrateDone = 'QPushButton {' \
                      'border-width: 1px;' \
                      'border-style: inset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                      'border-radius: 4px;' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                      'font: bold;' \
                      'font-size: 12px;' \
                      'color: white;' \
                      'height: 70px;' \
                      'width: 80px;' \
                      'margin-top: 8px;' \
                      '}' \
                      'QPushButton:hover {' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                      '}' \
                      'QPushButton:pressed {' \
                      'border-width: 1px;' \
                      'border-style: outset;' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                      '}' \
                      'QPushButton:checked {' \
                      'border-width: 1px;' \
                      'border-style: inset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + orangeLight + ', stop: 1 ' + orangeDark + ');' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + orangeLight + ', stop: 1 ' + orangeDark + ');' \
                      '}' \
                      'QPushButton:hover:checked {' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + orangeHoverLight + ', stop: 1 ' + orangeHoverDark + ');' \
                      '}' \
                      'QPushButton:pressed:checked {' \
                      'border-width: 1px;' \
                      'border-style: outset;' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 ' + orangeHoverLight + ', stop: 1 ' + orangeHoverDark + ');' \
                      '}'

buttonReset = 'QPushButton {' \
              'border-width: 1px;' \
              'border-style: inset;' \
              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
              'border-radius: 4px;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
              'font: bold;' \
              'font-size: 12px;' \
              'color: white;' \
              'height: 50px;' \
              'width: 80px;' \
              '}' \
              'QPushButton:hover {' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
              '}' \
              'QPushButton:pressed {' \
              'border-width: 1px;' \
              'border-style: outset;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
              '}' \
              'QPushButton:checked {' \
              'border-width: 1px;' \
              'border-style: inset;' \
              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
              '}' \
              'QPushButton:hover:checked {' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
              '}' \
              'QPushButton:pressed:checked {' \
              'border-width: 1px;' \
              'border-style: outset;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
              '}'

buttonAutoAcquisition = 'QPushButton {' \
                        'border-width: 1px;' \
                        'border-style: inset;' \
                        'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                        'border-radius: 4px;' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                        'font: bold;' \
                        'font-size: 12px;' \
                        'color: white;' \
                        'height: 50px;' \
                        'width: 80px;' \
                        '}' \
                        'QPushButton:hover {' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                        '}' \
                        'QPushButton:pressed {' \
                        'border-width: 1px;' \
                        'border-style: outset;' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                        '}' \
                        'QPushButton:checked {' \
                        'border-width: 1px;' \
                        'border-style: inset;' \
                        'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                        '}' \
                        'QPushButton:hover:checked {' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                        '}' \
                        'QPushButton:pressed:checked {' \
                        'border-width: 1px;' \
                        'border-style: outset;' \
                        'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                        'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                        '}'

buttonAutoAcquisitionInProcess = 'QPushButton {' \
                                 'border-width: 1px;' \
                                 'border-style: inset;' \
                                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                                 'border-radius: 4px;' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                                 'font: bold;' \
                                 'font-size: 12px;' \
                                 'color: white;' \
                                 'height: 50px;' \
                                 'width: 80px;' \
                                 '}' \
                                 'QPushButton:hover {' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                                 '}' \
                                 'QPushButton:pressed {' \
                                 'border-width: 1px;' \
                                 'border-style: outset;' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                                 '}' \
                                 'QPushButton:checked {' \
                                 'border-width: 1px;' \
                                 'border-style: inset;' \
                                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + orangeLight + ', stop: 1 ' + orangeDark + ');' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + orangeLight + ', stop: 1 ' + orangeDark + ');' \
                                 '}' \
                                 'QPushButton:hover:checked {' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + orangeHoverLight + ', stop: 1 ' + orangeHoverDark + ');' \
                                 '}' \
                                 'QPushButton:pressed:checked {' \
                                 'border-width: 1px;' \
                                 'border-style: outset;' \
                                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                                 'stop: 0 ' + orangeHoverLight + ', stop: 1 ' + orangeHoverDark + ');' \
                                 '}'

buttonInit = 'QPushButton {' \
             'border-width: 1px;' \
             'border-style: inset;' \
             'border-radius: 4px;' \
             'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
             'font: bold;' \
             'font-size: 12px;' \
             'color: white;' \
             'height: 215px;' \
             'width: 90px;' \
             'margin-top: 8px;' \
             '}' \
             'QPushButton:hover {' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
             '}' \
             'QPushButton:pressed {' \
             'border-width: 1px;' \
             'border-style: outset;' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
             '}' \
             'QPushButton:checked {' \
             'border-width: 1px;' \
             'border-style: inset;' \
             'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
             'border-radius: 4px;' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
             '}' \
             'QPushButton:hover:checked {' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
             '}' \
             'QPushButton:pressed:checked {' \
             'border-width: 1px;' \
             'border-style: outset;' \
             'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
             'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
             '}'

buttonFreeRunning = 'QPushButton {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'border-radius: 4px;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                    'font: bold;' \
                    'font-size: 12px;' \
                    'color: white;' \
                    'height: 20px;' \
                    'min-width: 220px;' \
                    '}' \
                    'QPushButton:hover {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                    '}' \
                    'QPushButton:checked {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                    '}' \
                    'QPushButton:hover:checked {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}' \
                    'QPushButton:pressed:checked {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                    '}'

buttonSaveFile = 'QPushButton {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                 'border-radius: 4px;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
                 'font: bold;' \
                 'font-size: 12px;' \
                 'color: white;' \
                 'height: 30px;' \
                 '}' \
                 'QPushButton:hover {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                 '}' \
                 'QPushButton:pressed {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
                 '}' \
                 'QPushButton:checked {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
                 '}' \
                 'QPushButton:hover:checked {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                 '}' \
                 'QPushButton:pressed:checked {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
                 '}'

buttonChart = 'QPushButton {' \
              'border-width: 1px;' \
              'border-style: inset;' \
              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
              'border-radius: 4px;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueLight + ', stop: 1 ' + blueDark + ');' \
              'font: bold;' \
              'font-size: 12px;' \
              'color: white;' \
              'padding: 3px 8px 3px 8px;' \
              '}' \
              'QPushButton:hover {' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
              '}' \
              'QPushButton:pressed {' \
              'border-width: 1px;' \
              'border-style: outset;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + blueHoverLight + ', stop: 1 ' + blueHoverDark + ');' \
              '}' \
              'QPushButton:checked {' \
              'border-width: 1px;' \
              'border-style: inset;' \
              'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenLight + ', stop: 1 ' + greenDark + ');' \
              '}' \
              'QPushButton:hover:checked {' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
              '}' \
              'QPushButton:pressed:checked {' \
              'border-width: 1px;' \
              'border-style: outset;' \
              'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
              'stop: 0 ' + greenHoverLight + ', stop: 1 ' + greenHoverDark + ');' \
              '}'

buttonExit = 'QPushButton {' \
             'font: bold;' \
             '}'

"""
    Different border style:
        - dotted
        - dashed
        - solid
        - double
        - groove
        - ridge
        - inset
        - outset
        - none
        - hidden
"""

groupBoxGeneral = 'QGroupBox {' \
                  'border: 2px outset #737373;' \
                  'border-radius: 5px;' \
                  'margin-top: 7px;' \
                  '}' \
                  'QGroupBox:title {' \
                  'top: -7 ex;' \
                  'left: 10px;' \
                  '}'

groupBoxGeneralWithoutBorder = 'QGroupBox {' \
                               'border: 0px outset #948682;' \
                               'border-radius: 5px;' \
                               'margin-top: 7px;' \
                               '}' \
                               'QGroupBox:title {' \
                               'top: -7 ex;' \
                               'left: 10px;' \
                               '}'

groupBoxAutoAcquisition = 'QGroupBox {' \
                          'border: 2px outset #948682;' \
                          'border-radius: 5px;' \
                          '}'

groupBoxFilled = 'QGroupBox {' \
                 'border: 2px solid red;' \
                 '}'

spinBoxGeneral = 'QSpinBox {' \
                 'height: 20px;' \
                 'font-size: 14px;' \
                 '}'

doubleSpinBoxGeneral = 'QDoubleSpinBox {' \
                       'height: 20px;' \
                       'font-size: 14px;' \
                       '}'

lineEditGeneral = 'QLineEdit {' \
                  'height: 20px;' \
                  'font-size: 14px;' \
                  '}'

labelBtnInit = 'QLabel {' \
               'font: bold;' \
               'font-size: 12px;' \
               'color: white;' \
               '}'

labelBtnPeristaltic = 'QLabel {' \
                      'font: bold;' \
                      'font-size: 8px;' \
                      'color: black;' \
                      '}'

qTabBar = 'QTabWidget:pane {' \
          'border-width: 1px;' \
          'border-style: solid;' \
          'border-color: #737373;' \
          'background: #d8d8d8;' \
          '}' \
          'QTabWidget:tab-bar:top {' \
          'top: 1px;' \
          '}' \
          'QTabWidget:tab-bar:bottom {' \
          'bottom: 1px;' \
          '}' \
          'QTabWidget:tab-bar:left {' \
          'right: 1px;' \
          '}' \
          'QTabWidget:tab-bar:right {' \
          'left: 1px;' \
          '}' \
          'QTabBar:tab {' \
          'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f2f2f2, stop: 1 #a4a4a4);' \
          'border-width: 1px;' \
          'border-style: solid;' \
          'border-color: #737373;' \
          'min-height: 15px;' \
          'min-width: 100px;' \
          'padding: 2px;' \
          '}' \
          'QTabBar:tab:selected {' \
          'background-color: #d8d8d8;' \
          'border-left-width: 1px;' \
          'border-top-width: 1px;' \
          'border-right-width: 1px;' \
          'border-bottom-width: 0px;' \
          '}'
