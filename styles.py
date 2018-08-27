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

buttonLaserBig = 'QPushButton {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #00ff00, stop: 1 #04b404);' \
                 'border-radius: 4px;' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #00ff00, stop: 1 #04b404);' \
                 'font: bold;' \
                 'font-size: 20px;' \
                 'color: white;' \
                 'height: 100px;' \
                 'margin-top: 8px;' \
                 '}' \
                 'QPushButton:hover {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #04b404, stop: 1 #088a08);' \
                 '}' \
                 'QPushButton:pressed {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #00ff00, stop: 1 #04b404);' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #04b404, stop: 1 #088a08);' \
                 '}' \
                 'QPushButton:checked {' \
                 'border-width: 1px;' \
                 'border-style: inset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #fa5858, stop: 1 #ff0000);' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #fa5858, stop: 1 #ff0000);' \
                 '}' \
                 'QPushButton:hover:checked {' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #ff0000, stop: 1 #df0101);' \
                 '}' \
                 'QPushButton:pressed:checked {' \
                 'border-width: 1px;' \
                 'border-style: outset;' \
                 'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #fa5858, stop: 1 #ff0000);' \
                 'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                 'stop: 0 #ff0000, stop: 1 #df0101);' \
                 '}'

buttonLaserSmall = 'QPushButton {' \
                   'border-width: 1px;' \
                   'border-style: inset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #00ff00, stop: 1 #04b404);' \
                   'border-radius: 4px;' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #00ff00, stop: 1 #04b404);' \
                   'font: bold;' \
                   'font-size: 12px;' \
                   'color: white;' \
                   'height: 70px;' \
                   'width: 80px;' \
                   '}' \
                   'QPushButton:hover {' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #04b404, stop: 1 #088a08);' \
                   '}' \
                   'QPushButton:pressed {' \
                   'border-width: 1px;' \
                   'border-style: outset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #00ff00, stop: 1 #04b404);' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #04b404, stop: 1 #088a08);' \
                   '}' \
                   'QPushButton:checked {' \
                   'border-width: 1px;' \
                   'border-style: inset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #fa5858, stop: 1 #ff0000);' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #fa5858, stop: 1 #ff0000);' \
                   '}' \
                   'QPushButton:hover:checked {' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #ff0000, stop: 1 #df0101);' \
                   '}' \
                   'QPushButton:pressed:checked {' \
                   'border-width: 1px;' \
                   'border-style: outset;' \
                   'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #fa5858, stop: 1 #ff0000);' \
                   'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                   'stop: 0 #ff0000, stop: 1 #df0101);' \
                   '}'

buttonPeristaltic = 'QPushButton {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'border-radius: 4px;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'font: bold;' \
                    'font-size: 12px;' \
                    'color: white;' \
                    'height: 70px;' \
                    'width: 80px;' \
                    'margin-top: 8px;' \
                    '}' \
                    'QPushButton:hover {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #0080ff, stop: 1 #0174df);' \
                    '}' \
                    'QPushButton:pressed {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #0080ff, stop: 1 #0174df);' \
                    '}' \
                    'QPushButton:checked {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #faac58, stop: 1 #ff8000);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #faac58, stop: 1 #ff8000);' \
                    '}' \
                    'QPushButton:hover:checked {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #ff8000, stop: 1 #df7401);' \
                    '}' \
                    'QPushButton:pressed:checked {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #faac58, stop: 1 #ff8000);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #ff8000, stop: 1 #df7401);' \
                    '}'

buttonImpulsional = 'QPushButton {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'border-radius: 4px;' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'font: bold;' \
                    'font-size: 12px;' \
                    'color: white;' \
                    'height: 70px;' \
                    'width: 80px;' \
                    'margin-top: 8px;' \
                    '}' \
                    'QPushButton:hover {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #0080ff, stop: 1 #0174df);' \
                    '}' \
                    'QPushButton:pressed {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #58acfa, stop: 1 #0080ff);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #0080ff, stop: 1 #0174df);' \
                    '}' \
                    'QPushButton:checked {' \
                    'border-width: 1px;' \
                    'border-style: inset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #00ff00, stop: 1 #04b404);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #00ff00, stop: 1 #04b404);' \
                    '}' \
                    'QPushButton:hover:checked {' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #04b404, stop: 1 #088a08);' \
                    '}' \
                    'QPushButton:pressed:checked {' \
                    'border-width: 1px;' \
                    'border-style: outset;' \
                    'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #00ff00, stop: 1 #04b404);' \
                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                    'stop: 0 #04b404, stop: 1 #088a08);' \
                    '}'

buttonCalibrate = 'QPushButton {' \
                  'border-width: 1px;' \
                  'border-style: inset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #58acfa, stop: 1 #0080ff);' \
                  'border-radius: 4px;' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #58acfa, stop: 1 #0080ff);' \
                  'font: bold;' \
                  'font-size: 12px;' \
                  'color: white;' \
                  'height: 70px;' \
                  'width: 80px;' \
                  'margin-top: 8px;' \
                  '}' \
                  'QPushButton:hover {' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #0080ff, stop: 1 #0174df);' \
                  '}' \
                  'QPushButton:pressed {' \
                  'border-width: 1px;' \
                  'border-style: outset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #58acfa, stop: 1 #0080ff);' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #0080ff, stop: 1 #0174df);' \
                  '}' \
                  'QPushButton:checked {' \
                  'border-width: 1px;' \
                  'border-style: inset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #faac58, stop: 1 #ff8000);' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #faac58, stop: 1 #ff8000);' \
                  '}' \
                  'QPushButton:hover:checked {' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #ff8000, stop: 1 #df7401);' \
                  '}' \
                  'QPushButton:pressed:checked {' \
                  'border-width: 1px;' \
                  'border-style: outset;' \
                  'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #faac58, stop: 1 #ff8000);' \
                  'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                  'stop: 0 #ff8000, stop: 1 #df7401);' \
                  '}'

buttonCalibrateDone = 'QPushButton {' \
                      'border-width: 1px;' \
                      'border-style: inset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #00ff00, stop: 1 #04b404);' \
                      'border-radius: 4px;' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #00ff00, stop: 1 #04b404);' \
                      'font: bold;' \
                      'font-size: 12px;' \
                      'color: white;' \
                      'height: 70px;' \
                      'width: 80px;' \
                      'margin-top: 8px;' \
                      '}' \
                      'QPushButton:hover {' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #04b404, stop: 1 #088a08);' \
                      '}' \
                      'QPushButton:pressed {' \
                      'border-width: 1px;' \
                      'border-style: outset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #00ff00, stop: 1 #04b404);' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #04b404, stop: 1 #088a08);' \
                      '}' \
                      'QPushButton:checked {' \
                      'border-width: 1px;' \
                      'border-style: inset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #faac58, stop: 1 #ff8000);' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #faac58, stop: 1 #ff8000);' \
                      '}' \
                      'QPushButton:hover:checked {' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #ff8000, stop: 1 #df7401);' \
                      '}' \
                      'QPushButton:pressed:checked {' \
                      'border-width: 1px;' \
                      'border-style: outset;' \
                      'border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #faac58, stop: 1 #ff8000);' \
                      'background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      'stop: 0 #ff8000, stop: 1 #df7401);' \
                      '}'