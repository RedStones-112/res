import time, win32con, win32api, win32gui
from pywinauto import clipboard



# # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_opentalk_name = '메모장'
chat_command = ['음소거','음소거 취소','로아']
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
text = "테스트텍스트"
kakao_sendtext(text)
PostKeyEx(hwndListControl, ord('A'), [w.VK_CONTROL], False)
time.sleep(1)
PostKeyEx(hwndListControl, ord('C'), [w.VK_CONTROL], False)
ctext = clipboard.GetData()
print(ctext)