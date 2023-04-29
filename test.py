import win32gui
import win32con
import win32api

# หา ID ของหน้าต่าง notepad
window_id = win32gui.FindWindow(None, 'Untitled - Notepad')

# เปิดหน้าต่าง notepad ถ้ายังไม่เปิด
if not window_id:
    win32gui.ShellExecute(0, 'open', 'notepad.exe', None, None, 1)

# ส่ง keybd_event ให้กับ notepad
win32gui.SetForegroundWindow(window_id)
win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
