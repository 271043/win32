import win32api
import win32con
import win32gui

def get_all_windows():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            # print(hex(hwnd), win32gui.GetWindowText(hwnd))
            # หา ID ของหน้าต่างโปรแกรม
            window_id = win32gui.FindWindow(
                None,  win32gui.GetWindowText(hwnd))
            print(window_id, win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)
