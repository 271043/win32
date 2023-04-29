import win32api, win32con, win32gui

program_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
 
def open_program(path, amount, program_name):
    for i in range(amount):
        hwnd = win32api.ShellExecute(0, 'open', path, '', '', 1)
        if hwnd > 32:
            win32api.Sleep(500)
            window_id = win32gui.FindWindow(None, program_name)
            win32gui.ShowWindow(window_id, win32con.SW_MINIMIZE)
             
            
            
            

            
            
              
             
            
              
            
  
open_program( program_path, 2,  "แท็บใหม่ - Google Chrome")









 


 