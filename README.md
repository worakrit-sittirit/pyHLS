# pyHLS

## Overview
pyHLS is a Python library designed to provide access to HLS USB Board functionality through a convenient Python interface. It wraps the HLS USB Board's DLL (Dynamic Link Library) to enable easy interaction with the hardware.

## Features
- Comprehensive wrapper for HLS USB Board DLL functions
- Support for various hardware interactions including:
  - Device discovery and management
  - Reading and writing data
  - Firmware version retrieval
  - Error handling
- Simple Python interface to low-level hardware operations

## Installation

### Prerequisites
- Windows operating system
- Python 3.6+
- Compatible HLS USB Board
- Included `hls36usb.dll` library

### Install via pip
```bash
pip install pyHLS
```

## Usage Example

```python
import pyHLS
import ctypes

# Count available HLS devices
device_count = pyHLS.HlsCountDevice()
print(f"Number of HLS devices: {device_count}")

# Open a handle to the first device
handle = pyHLS.HlsOpenHandle(0)

# Read firmware version
firmware_version = pyHLS.HlsGetFirmwareVersion(handle)
print(f"Firmware Version: {firmware_version}")

# Perform read/write operations
result_data = ctypes.c_int()
pyHLS.HlsReadWord(handle, read_address, ctypes.byref(result_data))

# Close the handle when done
pyHLS.HlsCloseHandle(handle)
```

## Supported Operations
- Device Discovery
  - `HlsCountDevice()`: Count available devices
  - `HlsSearchBoard()`: Search for specific boards

- Device Handle Management
  - `HlsOpenHandle()`: Open a device handle
  - `HlsCloseHandle()`: Close a device handle
  - `HlsResetMKY36()`: Reset the device

- Data Operations
  - `HlsReadWord()`: Read a single word
  - `HlsWriteWord()`: Write a single word
  - `HlsReadData()`: Read multiple words
  - `HlsWriteData()`: Write multiple words

- Diagnostic Functions
  - `HlsGetVersion()`: Get library version
  - `HlsGetLastError()`: Retrieve last error code
  - `HlsGetFirmwareVersion()`: Get device firmware version

## Error Handling
The library provides predefined error codes through the `HLS_ERROR` class:
- `HLS_SUCCESS`: Operation completed successfully
- `HLS_ERR_DEVICENOTEXIST`: Device not found
- `HLS_ERR_ALREADYOPENED`: Device already in use
- And more... (see source code for full list)

## System Requirements
- Operating System: Windows
- Python Version: 3.6+
- Hardware: HLS USB Board (MKY36)

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Worakrit Sittirit - kritsitti.coe@gmail.com

Project Link: [https://github.com/worakrit-sittirit/pyHLS](https://github.com/worakrit-sittirit/pyHLS)

## Acknowledgments
- Special thanks to the HLS USB Board developers
- Python ctypes library for enabling low-level hardware interactions

## Disclaimer
This library is a Python wrapper for the HLS USB Board DLL. Ensure proper hardware and driver compatibility before use.
