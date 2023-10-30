print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP10,board.GP11,board.GP12,board.GP13,)
keyboard.row_pins = (board.GP20,board.GP19,board.GP18,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

TRANS = KC.TRNS
#RAISE = KC.MO(1)
RAISE = KC.LT(1, KC.Q)
LAYER1 = KC.TO(1)
LAYER0 = KC.TO(0)

keyboard.keymap = [
    [#Layer 0: Base
     KC.MPRV,  KC.MPLY,   KC.MNXT,   LAYER1,
     KC.F16,  KC.F17,   KC.F18,   KC.H,       
     KC.F9,  KC.F13,   KC.F14,   KC.I,
    ],
    [#Layer 1: Undecided 
     KC.A,  KC.B,   KC.C,   LAYER0,
     KC.E,  KC.F,   KC.G,   KC.N,       
     KC.I,  KC.J,   KC.K,   KC.V,        
    ]
]

if __name__ == '__main__':
    keyboard.go()
