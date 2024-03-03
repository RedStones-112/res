import time, win32con, win32api, win32gui
from pywinauto import clipboard
import ctypes
import os
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# # 카톡창 이름 (열려있는 상태, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_opentalk_name = '메모장'

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# # 핸들
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)


hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

# # 채팅 전송
#text = "테스트"
#kakao_sendtext(text)

#####################################
PBYTE256 = ctypes.c_ubyte * 256
_user32 = ctypes.WinDLL("user32")
GetKeyboardState = _user32.GetKeyboardState
SetKeyboardState = _user32.SetKeyboardState
PostMessage = win32api.PostMessage
SendMessage = win32gui.SendMessage
FindWindow = win32gui.FindWindow
IsWindow = win32gui.IsWindow
GetCurrentThreadId = win32api.GetCurrentThreadId
GetWindowThreadProcessId = _user32.GetWindowThreadProcessId
AttachThreadInput = _user32.AttachThreadInput

MapVirtualKeyA = _user32.MapVirtualKeyA
MapVirtualKeyW = _user32.MapVirtualKeyW

MakeLong = win32api.MAKELONG
w = win32con

device = AudioUtilities.GetSpeakers()## 오디오 설정 ##조금더 이해필요
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
current = volume.GetMasterVolumeLevel()

# 조합키 쓰기 위해
def PostKeyEx(hwnd, key, shift, specialkey):
    if IsWindow(hwnd):

        ThreadId = GetWindowThreadProcessId(hwnd, None)

        lparam = MakeLong(0, MapVirtualKeyA(key, 0))
        msg_down = w.WM_KEYDOWN
        msg_up = w.WM_KEYUP

        if specialkey:
            lparam = lparam | 0x1000000

        if len(shift) > 0:  
            pKeyBuffers = PBYTE256()
            pKeyBuffers_old = PBYTE256()

            SendMessage(hwnd, w.WM_ACTIVATE, w.WA_ACTIVE, 0)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, True)
            GetKeyboardState(ctypes.byref(pKeyBuffers_old))

            for modkey in shift:
                if modkey == w.VK_MENU:
                    lparam = lparam | 0x20000000
                    msg_down = w.WM_SYSKEYDOWN
                    msg_up = w.WM_SYSKEYUP
                pKeyBuffers[modkey] |= 128

            SetKeyboardState(ctypes.byref(pKeyBuffers))
            time.sleep(0.01)
            PostMessage(hwnd, msg_down, key, lparam)
            time.sleep(0.01)
            PostMessage(hwnd, msg_up, key, lparam | 0xC0000000)
            time.sleep(0.01)
            SetKeyboardState(ctypes.byref(pKeyBuffers_old))
            time.sleep(0.01)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, False)

        else:
            SendMessage(hwnd, msg_down, key, lparam)
            SendMessage(hwnd, msg_up, key, lparam | 0xC0000000)


def main():

    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
    hwndListControl = win32gui.FindWindowEx(hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

    # #조합키, 본문을 클립보드에 복사 ( ctl + A , C )
    PostKeyEx(hwndListControl, ord('A'), [w.VK_CONTROL], False)
    time.sleep(1)
    PostKeyEx(hwndListControl, ord('C'), [w.VK_CONTROL], False)
    ctext = clipboard.GetData()
    command = ctext[ len(ctext) - ctext[::-1].find(']',2) + 1 : len(ctext) - ctext[::-1].find('\r',1) - 1] # 클립보드에서 마지막 명령어 파츠만 슬라이싱
    #카카오톡 메세지가 [이름] [시간] "채팅내역\r\n" 형식이므로 뒤에서 첫번째 ]와 \r 사이의 내용만 슬라이싱
    
    command_list = ('pc종료', '볼륨조절', "음악", "음악종료", '프로그램종료')#커멘드 리스트
    
    if (command == command_list[0]):#이후 print문은 카카오톡 출력으로 변경
        text = "pc종료 실행"
        kakao_sendtext(text)
        os.system('shutdown -s -t 1')
        
    elif(command.find(command_list[1]) != -1):##볼륨조절이 지수함수 형태를 띄어 추후 조정필요
        try:
            current = 5 + (100 - int(command[command.rfind(command_list[1])+len(command_list[1]):])) * -13 // 20
            volume.SetMasterVolumeLevel(current, None)
            text = "볼륨" + command[command.rfind(command_list[1])+len(command_list[1]):] + "으로 설정"
            kakao_sendtext(text)
        except:
            text = "ERROR : 볼륨조절 실패"
            kakao_sendtext(text)
        
        
    elif(command == '음악'):
        text = "음악 실행"
        kakao_sendtext(text)
        
    elif(command == '음악종료'):
        text = "음악종료 실행"
        kakao_sendtext(text)
        
    elif(command == '프로그램종료'):
        text = "프로그램종료 실행"
        kakao_sendtext(text)
        
    else:
        pass
    

if __name__ == '__main__':
    main()




'''
PostKeyEx(hwndListControl, ord('A'), [win32con.VK_CONTROL], False)
time.sleep(1)   
PostKeyEx(hwndListControl, ord('C'), [win32con.VK_CONTROL], False)
ctext = clipboard.GetData()
print(ctext)

'''