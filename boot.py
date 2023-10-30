import board
import digitalio
import storage
import usb_cdc
import usb_hid

#This is from the base kmk boot.py / causes code below to not function
#supervisor.set_next_stack_limit(4096 + 4096)

# If key (Top/Left) is held down during boot, don't run code to hide storage
col = digitalio.DigitalInOut(board.GP10)
row = digitalio.DigitalInOut(board.GP20)

col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()
