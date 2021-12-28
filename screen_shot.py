from PIL import ImageGrab
import tkinter as tk
import pyautogui
import win32api

class ScreenShotGUI():
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("500x250")
        root.title("ScreenShot V0.0.1")
        
        self.im = None
        self.coords = tk.StringVar()
        self.label = tk.Label(root)
        self.ScreenShotBtn = tk.Button(root, text='Screen Shot', command=lambda: self.grab_area(self.label))
        self.saveBtn = tk.Button(root, text='Save & Quit', command=lambda: self.save())
        self.ScreenShotBtn.grid(row=1, column=1)
        self.saveBtn.grid(row=1, column=5)
        self.label.grid(row=3, column=2)

    def stuff(self):
        #print("#################")
        box = self.coords.get()
        print(box)
        box = [int(bb) for bb in box.split(',')]
        try:
            im=ImageGrab.grab(bbox=(box[0],box[1],box[2],box[3]))
            im.save("temp.png", "PNG")
            return im
        except Exception as e:
            print(e)

    def grab_area(self, selflabel):
            pressed = False
            started = False
            
            winpos = (0,0)
            first = (0,0)
            last = (0,0)
            
            window = tk.Toplevel(self.root)
            state_left = win32api.GetKeyState(0x01)
            window.overrideredirect(1)
            window.wm_attributes('-alpha',0.5)
            window.geometry("100x100")
            
            while True:
                
                a = win32api.GetKeyState(0x01)
                mouse = pyautogui.position()

                if a != state_left:  # Button state changed
                    state_left = a
                    if a < 0:
                        pressed = True
                    else:
                        pressed = False
                        
                try:        
                    if pressed:
                        if not started:
                            first = mouse
                        started = True
                        winposdif = (mouse[0] - winpos[0], mouse[1] - winpos[1])
                        winsize = str(winposdif[0])+ "x" + str(winposdif[1])
                        window.geometry(winsize)
                        
                    elif not pressed:
                        if started:
                            last = mouse # end of square
                            self.coords.set(str(first[0]) + str(",") + str(first[1]) +  str(",") +\
                                    str(last[0]) + str(",") + str(last[1]))
                            window.destroy()
                            self.im = self.stuff()

                            selflabel.image = tk.PhotoImage(file="temp.png")
                            # selflabel.image = tk.PhotoImage(self.im)
                            selflabel['image'] = selflabel.image
                            selflabel.grid()

                            break
                        
                        winpos = (mouse[0], mouse[1])
                        window.geometry("+" + str(mouse[0])+ "+" + str(mouse[1]))
                        started = False
                        
                except Exception as e:
                    print(e)
                    break
                    
                window.update_idletasks()
                window.update()

    def save(self):
        if self.im == None:
            print('Screen shot is empty.')
        else:
            self.im.save('./ScreenShot/image.png', 'PNG')
            print('Image has been saved in ./ScreenShot/image.png.')
            self.root.destroy()