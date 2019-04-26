# -*- coding: utf-8 -*-

import rabird.winio
import time
import atexit

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

__winio = None

def __get_winio():
    global __winio

    if __winio is None:
            __winio = rabird.winio.WinIO()
            def __clear_winio():
                    global __winio
                    __winio = None
            atexit.register(__clear_winio)

    return __winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80);

def key_press(scancode, press_time = 0.2):
    key_down( scancode )
    time.sleep( press_time )
    key_up( scancode )

def password_type(password):
    #for c in password:
     #   key_press(c)
    key_press(0x08)
    key_press(0x0b)
    key_press(0x05)
    key_press(0x0a)
    key_press(0x04)
    key_press(0x08)
    key_press(0x07)
    key_press(0x04)
    key_press(0x02)
    key_press(0x07)
    key_down(0x2a)
    key_press(0x19)
    key_up(0x2a)
    key_press(0x30)
    key_press(0x2e)
    key_press(0x2e)
    key_press(0x13)
    key_press(0x2e)
    
    
    

# Press 'A' key
# Scancodes references : https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
# key_press(0x1E)