import gymnasium as gym
import numpy as np
import time
import win32gui
import win32ui
import win32con
import win32api
import ctypes
from stable_baselines3 import PPO

class BackgroundTerrariaEnv(gym.Env):
    def __init__(self):
        super(BackgroundTerrariaEnv, self).__init__()
        # The AI has 3 basic choices: 0=Left, 1=Right, 2=Jump
        self.action_space = gym.spaces.Discrete(3)
        # The observation space pixel window shape
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(200, 200, 3), dtype=np.uint8)
        
        # Advanced Scanning Loop: Check every open program name running on Windows
        self.hwnd = None
        def winEnumHandler(hwnd, ctx):
            window_text = win32gui.GetWindowText(hwnd)
            # Match any active window containing the word terraria or modloader
            if "terraria" in window_text.lower() or "modloader" in window_text.lower():
                self.hwnd = hwnd
                
        win32gui.EnumWindows(winEnumHandler, None)

        # Safety Fallback
        if not self.hwnd:
            raise RuntimeError("Terraria window not found! Make sure the game application is booted up.")

    def _get_background_screenshot(self):
        # Grabs graphics memory buffer data from the target game process handle
        w, h = 800, 600 
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        
        # Fixed: Using universal ctypes call to bypass pywin32 library restrictions
        ctypes.windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 3)
        
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        img = np.frombuffer(bmpstr, dtype='uint8')
        img.shape = (bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)
        
        # Free allocated GDI system handles to prevent desktop freezing memory leaks
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)
        
        # Crop down to a standard 200x200 pixel block centered on the main player frame
        cropped_img = img[200:400, 300:500, :3] 
        return cropped_img

    def _send_background_key(self, key_code):
        # Posts direct background messaging commands to the target application thread
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key_code, 0)
        time.sleep(0.05)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, key_code, 0)

    def step(self, action):
        # Map reinforcement choices to virtual hardware parameters
        if action == 0: self._send_background_key(0x41)   # Move Left (A)
        elif action == 1: self._send_background_key(0x44) # Move Right (D)
        elif action == 2: self._send_background_key(0x20) # Jump (Space)

        # Retrieve the updated state observation
        obs = self._get_background_screenshot()

        # Temporary uniform baseline score parameters
        reward = 1.0
        done = False

        return obs, reward, done, False, {}

    def reset(self, seed=None):
        return self._get_background_screenshot(), {}

# --- EXECUTIVE AGENT LOOP ---
env = BackgroundTerrariaEnv()

# Build the PPO model architecture brain
model = PPO("CnnPolicy", env, verbose=1)

print("Starting background training! The loop will bypass your screen configurations now.")
model.learn(total_timesteps=10000)

# Save progress to disk
model.save("terraria_background_brain")
print("Training complete! Brain file exported safely.")
