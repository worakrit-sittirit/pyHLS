#pragma once 
#define HLSAPI __stdcall 

#define HLS_SUCCESS                             0   /* 正常終了                                               */
#define HLS_ERR_DEVICENOTEXIST                  1   /* デバイスが存在しない                                   */
#define HLS_ERR_ALREADYOPENED                   2   /* すでにオープンされている                               */
#define HLS_ERR_CLOSED                          3   /* HlsOpenHandle が一度もコールされていない               */
#define HLS_ERR_INVALIDPARAM                    4   /* 無効なパラメータでコールされた                         */
#define HLS_ERR_NORESOUCE                       5   /* 実行に必要なリソースが足りない                         */
#define HLS_ERR_FAILED                          6   /* 原因不明により処理が遂行されなかった                   */
#define HLS_ERR_AUTO_TRANS_ALREADY_START        7   /* 定期更新がすでに開始されている                         */
#define HLS_ERR_AUTO_TRANS_STOP                 8   /* 定期更新が開始されていない                             */
#define HLS_ERR_USB_TIMEOUT_SUCCESS_STOP_HLS    9   /* USB通信中にタイムアウトが発生、HLS通信の停止に成功     */
#define HLS_ERR_USB_TIMEOUT_FAILED_STOP_HLS     10  /* USB通信中にタイムアウトが発生、HLS通信の停止にも失敗   */
#define HLS_ERR_REACQUISITION_OF_HANDLE         11  /* ハンドルの再取得が行われていない                       */
#define HLS_ERR_NOT_SUPPORT_FIRM_VERSION        12  /* サポートされてないファームウェアバージョンを確認       */
#define HLS_ERR_INVALID_SEQUENCE_NUMBER         13  /* シーケンス番号が無効                                   */
#define HLS_NOTCALLYET                          99  /* API関数が一度もコールされていない                      */

#ifdef __cplusplus 
extern "C" {
#endif
UINT   HLSAPI HlsGetVersion(void);
UINT   HLSAPI HlsGetLastError(void);
INT    HLSAPI HlsCountDevice(void);
BOOL   HLSAPI HlsStartAutoTrans(HANDLE HLSHandle, WORD MfCnt);
BOOL   HLSAPI HlsStopAutoTrans(HANDLE HLSHandle);
HANDLE HLSAPI HlsOpenHandle(int Instance);
BOOL   HLSAPI HlsCloseHandle(HANDLE HLSHandle);
BOOL   HLSAPI HlsReadWord(HANDLE HLSHandle, const ULONG Adr, WORD* Dat);
BOOL   HLSAPI HlsWriteWord(HANDLE HLSHandle, const ULONG Adr, const WORD Dat);
BOOL   HLSAPI HlsReadCTL(HANDLE HLSHandle, void* Data);
BOOL   HLSAPI HlsReadDI(HANDLE HLSHandle, void* Data);
BOOL   HLSAPI HlsReadDRC(HANDLE HLSHandle, void* Data);
BOOL   HLSAPI HlsReadData(HANDLE HLSHandle, WORD Adr, WORD WordLen, void* Data);
BOOL   HLSAPI HlsWriteData(HANDLE HLSHandle, WORD Adr, WORD WordLen, void* Data);
INT    HLSAPI HlsBoardID(HANDLE HLSHandle);
BOOL   HLSAPI HlsSearchBoard(BYTE *board_num, BYTE *board_id_list);
BOOL   HLSAPI HlsResetMKY36(HANDLE HLSHandle);
INT    HLSAPI HlsGetFirmwareVersion(HANDLE HLSHandle);

#ifdef __cplusplus
}
#endif
