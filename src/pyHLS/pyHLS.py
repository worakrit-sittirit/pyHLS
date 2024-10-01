import ctypes,os

# Load DLL into memory.

currentPath = os.path.dirname(__file__)
hlsDll = ctypes.cdll.LoadLibrary(os.path.join(currentPath, "hls36usb.dll"))

def HlsGetVersion():
    tmp_rslt = hlsDll.HlsGetVersion()
    return tmp_rslt.value

class HLS_ERROR:
    HLS_SUCCESS = 0
    HLS_ERR_DEVICENOTEXIST = 1
    HLS_ERR_ALREADYOPENED = 2
    HLS_ERR_CLOSED = 3
    HLS_ERR_INVALIDPARAM = 4
    HLS_ERR_NORESOUCE = 5
    HLS_ERR_FAILED = 6
    HLS_ERR_AUTO_TRANS_ALREADY_START = 7
    HLS_ERR_AUTO_TRANS_STOP = 8
    HLS_ERR_USB_TIMEOUT_SUCCESS_STOP_HLS = 9
    HLS_ERR_USB_TIMEOUT_FAILED_STOP_HLS = 10
    HLS_ERR_REACQUISTION_OF_ANDLE = 11
    HLS_ERR_NOT_SUPPORT_FIRM_VERSION = 12
    HLS_ERR_INVALID_SEQUENCE_NUMER = 13
    HLS_NOCALLYET = 99


def HlsGetLastError():
    tmp_rslt = hlsDll.HlsGetLastError()
    return tmp_rslt.value

def HlsCountDevice():
    tmp_rslt = hlsDll.HlsCountDevice()
    return tmp_rslt.value

def HlsBoardID(handleObject):
    tmp_rslt = hlsDll.HlsBoardID(ctypes.byref(handleObject))
    return tmp_rslt.value

def HlsSearchBoard(board_num, board_id_list):
    tmp_rslt = hlsDll.HlsSearchBoard(ctypes.byref(board_num), ctypes.byref(board_id_list))
    return tmp_rslt.value

def HlsStartAutoTrans(handleObject, MfCnt):
    tmp_rslt = hlsDll.HlsStartAutoTrans(ctypes.byref(handleObject), MfCnt)
    return tmp_rslt.value

def HlsStopAutoTrans(handleObject):
    tmp_rslt = hlsDll.HlsStopAutoTrans(ctypes.byref(handleObject))
    return tmp_rslt.value

def HlsOpenHandle(index_no):
    tmp_rslt = hlsDll.HlsOpenHandle(index_no)
    return tmp_rslt

def HlsCloseHandle(handleObject):
    tmp_rslt = hlsDll.HlsCloseHandle(ctypes.byref(handleObject))
    return tmp_rslt.value

def HlsResetMKY36(handleObject):
    tmp_rslt = hlsDll.HlsResetMKY36(ctypes.byref(handleObject))
    return tmp_rslt.value

def HlsReadWord(handleObject, readAdr, rsltData):
    tmp_rslt = hlsDll.HlsReadWord(ctypes.byref(handleObject), readAdr, ctypes.byref(rsltData))
    return tmp_rslt.value

def HlsWriteWord(handleObject, writeAdr, writeData):
    tmp_rslt = hlsDll.HlsWriteWord(ctypes.byref(handleObject), writeAdr, writeData)
    return tmp_rslt.value

def HlsReadCTL(handleObject, rsltData):
    '''
        rsltData size 128
    '''
    tmp_rslt = hlsDll.HlsReadCTL(ctypes.byref(handleObject), ctypes.byref(rsltData))
    return tmp_rslt.value

def HlsReadDI(handleObject, rsltData):
    '''
        rsltData size 128
    '''
    tmp_rslt = hlsDll.HlsReadDI(ctypes.byref(handleObject), ctypes.byref(rsltData))
    return tmp_rslt.value

def HlsReadDRC(handleObject, rsltData):
    '''
        rsltData size 128
    '''
    tmp_rslt = hlsDll.HlsReadDRC(ctypes.byref(handleObject), ctypes.byref(rsltData))
    return tmp_rslt.value


def HlsReadData(handleObject, readAdr, wordLen, rsltData):
    tmp_rslt = hlsDll.HlsReadData(ctypes.byref(handleObject), readAdr, wordLen, ctypes.byref(rsltData))
    return tmp_rslt.value

def HlsWriteData(handleObject, writeAdr, wordLen, writeData):
    tmp_rslt = hlsDll.HlsWriteData(ctypes.byref(handleObject), writeAdr, wordLen, writeData)
    return tmp_rslt.value

def HlsGetFirmwareVersion(handleObject):
    tmp_rslt = hlsDll.HlsGetFirmwareVersion(ctypes.byref(handleObject))
    return tmp_rslt.value
