import usb
RQ_SET_STATUS = 0
RQ_GET_SCORE1 = 1
RQ_GET_SCORE2 = 2
RQ_GET_STATUS = 3

####################################


def find_mcu_boards():
    '''
    Find all Practicum MCU boards attached to the machine, then return a list
    of USB device handles for all the boards

    >>> devices = find_mcu_boards()
    >>> first_board = McuBoard(devices[0])
    '''
    boards = [dev for bus in usb.busses()
              for dev in bus.devices
              if (dev.idVendor, dev.idProduct) == (0x16c0, 0x05dc)]
    return boards

####################################


class McuBoard:
    '''
    Generic class for accessing Practicum MCU board via USB connection.
    '''

    ################################
    def __init__(self, dev):
        self.device = dev
        self.handle = dev.open()

    ################################
    def usb_write(self, request, data=[], index=0, value=0):
        '''
        Send data output to the USB device (i.e., MCU board)
           request: request number to appear as bRequest field on the USB device
           index: 16-bit value to appear as wIndex field on the USB device
           value: 16-bit value to appear as wValue field on the USB device
        '''
        reqType = usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_OUT
        self.handle.controlMsg(
            reqType, request, data, value=value, index=index)

    ################################
    def usb_read(self, request, length=2, index=0, value=0):
        '''
        Request data input from the USB device (i.e., MCU board)
           request: request number to appear as bRequest field on the USB device
           length: number of bytes to read from the USB device
           index: 16-bit value to appear as wIndex field on the USB device
           value: 16-bit value to appear as wValue field on the USB device

        If successful, the method returns a tuple of length specified
        containing data returned from the MCU board.
        '''
        reqType = usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_IN
        buf = self.handle.controlMsg(
            reqType, request, length, value=value, index=index)
        return buf


####################################
class PeriBoard:

    ################################
    def __init__(self, mcu):
        self.mcu = mcu

    ################################
    def set_status(self,value):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        self.mcu.usb_write(request=RQ_SET_STATUS,value=value);

    ################################
    def get_status(self):
        '''
            Return a boolean value indicating whether the switch on the peripheral
            board is currently pressed
            '''
        status = self.mcu.usb_read(request=RQ_GET_STATUS, length=1)
        return status[0]
    
    ################################
    def get_score1(self):
        '''
            Return a boolean value indicating whether the switch on the peripheral
            board is currently pressed
            '''
        scorePlayer1 = self.mcu.usb_read(request=RQ_GET_SCORE1, length=1)
        return scorePlayer1[0]
    
    ################################
    def get_score2(self):
        '''
            Return a boolean value indicating whether the switch on the peripheral
            board is currently pressed
            '''
        scorePlayer2 = self.mcu.usb_read(request=RQ_GET_SCORE2, length=1)
        return scorePlayer2[0]

