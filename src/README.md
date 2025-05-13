# HLS36USB API Documentation

This document describes the functions available in the HLS36USB API based on the header file `hls36usb.h`.

## Error Codes

| Code | Constant | Description |
|------|----------|-------------|
| 0 | `HLS_SUCCESS` | Normal termination |
| 1 | `HLS_ERR_DEVICENOTEXIST` | Device does not exist |
| 2 | `HLS_ERR_ALREADYOPENED` | Device is already opened |
| 3 | `HLS_ERR_CLOSED` | `HlsOpenHandle` has never been called |
| 4 | `HLS_ERR_INVALIDPARAM` | Function called with invalid parameters |
| 5 | `HLS_ERR_NORESOUCE` | Insufficient resources for execution |
| 6 | `HLS_ERR_FAILED` | Processing was not completed due to unknown cause |
| 7 | `HLS_ERR_AUTO_TRANS_ALREADY_START` | Periodic update has already started |
| 8 | `HLS_ERR_AUTO_TRANS_STOP` | Periodic update has not started |
| 9 | `HLS_ERR_USB_TIMEOUT_SUCCESS_STOP_HLS` | Timeout occurred during USB communication, HLS communication stop succeeded |
| 10 | `HLS_ERR_USB_TIMEOUT_FAILED_STOP_HLS` | Timeout occurred during USB communication, HLS communication stop failed |
| 11 | `HLS_ERR_REACQUISITION_OF_HANDLE` | Handle has not been reacquired |
| 12 | `HLS_ERR_NOT_SUPPORT_FIRM_VERSION` | Unsupported firmware version detected |
| 13 | `HLS_ERR_INVALID_SEQUENCE_NUMBER` | Invalid sequence number |
| 99 | `HLS_NOTCALLYET` | API function has never been called |

## Functions

### HlsGetVersion

```c
UINT HLSAPI HlsGetVersion(void);
```

**Description:**  
Retrieves the version of the HLS API.

**Parameters:**  
None

**Returns:**  
`UINT` - Version number of the HLS API.

---

### HlsGetLastError

```c
UINT HLSAPI HlsGetLastError(void);
```

**Description:**  
Retrieves the error code of the last operation.

**Parameters:**  
None

**Returns:**  
`UINT` - Error code of the last operation (see Error Codes table).

---

### HlsCountDevice

```c
INT HLSAPI HlsCountDevice(void);
```

**Description:**  
Counts the number of connected HLS devices.

**Parameters:**  
None

**Returns:**  
`INT` - Number of connected HLS devices.

---

### HlsStartAutoTrans

```c
BOOL HLSAPI HlsStartAutoTrans(HANDLE HLSHandle, WORD MfCnt);
```

**Description:**  
Starts periodic updates for the specified device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `MfCnt` - Frequency count for updates.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsStopAutoTrans

```c
BOOL HLSAPI HlsStopAutoTrans(HANDLE HLSHandle);
```

**Description:**  
Stops periodic updates for the specified device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsOpenHandle

```c
HANDLE HLSAPI HlsOpenHandle(int Instance);
```

**Description:**  
Opens a handle to an HLS device.

**Parameters:**  
- `Instance` - Index of the device to open.

**Returns:**  
`HANDLE` - Handle to the HLS device if successful, `NULL` otherwise.

---

### HlsCloseHandle

```c
BOOL HLSAPI HlsCloseHandle(HANDLE HLSHandle);
```

**Description:**  
Closes a previously opened handle to an HLS device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsReadWord

```c
BOOL HLSAPI HlsReadWord(HANDLE HLSHandle, const ULONG Adr, WORD* Dat);
```

**Description:**  
Reads a word from the specified address.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Adr` - Address to read from.
- `Dat` - Pointer to a buffer that receives the read data.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsWriteWord

```c
BOOL HLSAPI HlsWriteWord(HANDLE HLSHandle, const ULONG Adr, const WORD Dat);
```

**Description:**  
Writes a word to the specified address.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Adr` - Address to write to.
- `Dat` - Data to write.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsReadCTL

```c
BOOL HLSAPI HlsReadCTL(HANDLE HLSHandle, void* Data);
```

**Description:**  
Reads control information from the device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Data` - Pointer to a buffer that receives the control data.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsReadDI

```c
BOOL HLSAPI HlsReadDI(HANDLE HLSHandle, void* Data);
```

**Description:**  
Reads digital input data from the device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Data` - Pointer to a buffer that receives the digital input data.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsReadDRC

```c
BOOL HLSAPI HlsReadDRC(HANDLE HLSHandle, void* Data);
```

**Description:**  
Reads DRC (Digital Remote Control) data from the device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Data` - Pointer to a buffer that receives the DRC data.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsReadData

```c
BOOL HLSAPI HlsReadData(HANDLE HLSHandle, WORD Adr, WORD WordLen, void* Data);
```

**Description:**  
Reads a block of data from the specified address.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Adr` - Starting address to read from.
- `WordLen` - Number of words to read.
- `Data` - Pointer to a buffer that receives the read data.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsWriteData

```c
BOOL HLSAPI HlsWriteData(HANDLE HLSHandle, WORD Adr, WORD WordLen, void* Data);
```

**Description:**  
Writes a block of data to the specified address.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.
- `Adr` - Starting address to write to.
- `WordLen` - Number of words to write.
- `Data` - Pointer to the data to write.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsBoardID

```c
INT HLSAPI HlsBoardID(HANDLE HLSHandle);
```

**Description:**  
Retrieves the ID of the board associated with the handle.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.

**Returns:**  
`INT` - Board ID if successful, error code otherwise.

---

### HlsSearchBoard

```c
BOOL HLSAPI HlsSearchBoard(BYTE *board_num, BYTE *board_id_list);
```

**Description:**  
Searches for available boards and retrieves their IDs.

**Parameters:**  
- `board_num` - Pointer to receive the number of boards found.
- `board_id_list` - Pointer to a buffer that receives the list of board IDs.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsResetMKY36

```c
BOOL HLSAPI HlsResetMKY36(HANDLE HLSHandle);
```

**Description:**  
Resets the MKY36 device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.

**Returns:**  
`BOOL` - `TRUE` if successful, `FALSE` otherwise.

---

### HlsGetFirmwareVersion

```c
INT HLSAPI HlsGetFirmwareVersion(HANDLE HLSHandle);
```

**Description:**  
Retrieves the firmware version of the device.

**Parameters:**  
- `HLSHandle` - Handle to the HLS device obtained from `HlsOpenHandle`.

**Returns:**  
`INT` - Firmware version if successful, error code otherwise.
