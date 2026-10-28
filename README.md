# 🎮 Project: Self-Learning Autonomous AI Framework for Video Games
### Developed by: Ivan Reyes
### Category: Machine Learning, Computer Vision, and Data Science (STEM Fest 2026 Lisa Academy)

---

## 📌 Project Overview
This repository provides a concrete system-level blueprint and proof-of-concept for training autonomous video game agents entirely through **Deep Reinforcement Learning (RL)**. Instead of coding strict algorithmic rules (such as `if player close to wall, press jump`), these scripts construct an ecosystem where a digital brain learns entirely through continuous trial-and-error using raw visual pixels—mirroring human sensory workflows.

This project demonstrates two distinct architectural solutions for game automation:
1. **`terraria_ai.py` (Process-Specific Background Agent):** An advanced system pipeline utilizing low-level Windows API memory hooks to capture frames and inject keystrokes into a game window silently in the background.
2. **`universal_ai.py` (General-Purpose Computer Vision Framework):** A broad-spectrum Artificial General Intelligence (AGI) model that treats the entire computer display as its environment, controlling any game on Monitor 1 via hardware level virtualization.

---

## 🔬 Scientific Framework

### The Hypothesis
> *If a deep reinforcement learning model (PPO Algorithm) is linked to a standard computer display buffer and an active hardware input simulator, then increasing total training iterations ('timesteps') will cause a direct exponential correlation in agent survival efficiency and target pattern recognition without reading any internal game source files.*

### Variables
* **Independent Variable:** Total training time and environmental exposure (measured in mathematical engine `timesteps`).
* **Dependent Variable:** The chronological survival timeline length of the game character before taking environmental damage.
* **Controlled Parameters:** Display capture dimensions (200x200 pixel observation field), PPO learning rates, and action availability indices.

---

## 🛠️ The Architecture Stack

### 1. The Brain (The Learning Engine)
Both scripts are anchored by **Stable-Baselines3** using the **PPO (Proximal Policy Optimization)** algorithm. The model structures a Convolutional Neural Network (CNN) that processes images (`CnnPolicy`), calculates action reward probabilities, and continuously alters its internal mathematical weights via backpropagation based on environmental feedback.

### 2. The Eyes (Computer Vision)
* **Dedicated Route (`terraria_ai.py`):** Utilizes `win32gui.EnumWindows` to scan running operating system processes dynamically. It extracts live frame buffers directly from hidden background window handles using low-level `ctypes.windll.user32.PrintWindow` routines.
* **Universal Route (`universal_ai.py`):** Uses high-performance screen-scraping pipelines (`mss`) combined with OpenCV (`cv2`) to capture, center-crop, and downscale primary monitor visual arrays into a compact `200x200x3` pixel matrix.

### 3. The Hands (Input Virtualization)
* **Background Injections:** Uses `win32api.PostMessage` threads combined with `WM_ACTIVATE` focus-override flags to force DirectInput video games to accept keystrokes while out of focus, leaving the computer free for other multitasking chores.
* **Hardware-Level Virtualization:** Uses `pydirectinput` to simulate raw hardware-level OS commands, bypassing advanced input rejection filters across standard modern game engines (Unity, Unreal Engine, Source, etc.).

---

## 📂 Repository Contents & Structure

* 📄 `terraria_ai.py` - The advanced, process-isolated background training pipeline for Terraria.
* 📄 `universal_ai.py` - The multi-game computer vision and DirectInput hardware simulation script.
* 📄 `Terraria_AI_Presentation.md` - Complete transcript layout, analogies, and research notes for the physical display board.

---

## 🚀 How Future Researchers Can Build It

To implement or scale this architecture on a personal workstation, execute the following system setup:

### 1. Environment Installation
Ensure a standard Python environment is configured, then open a shell and fetch the dependencies:
```bash
# Install PyTorch Deep Learning core components
pip install torch torchvision --no-cache-dir

# Install the Machine Learning Brain library
pip install stable-baselines3[extra]

# Fetch the Visual Capture, Automation, and Math toolkits
pip install mss pydirectinput opencv-python gymnasium pywin32
```

### 2. Running the Pipelines
* To launch the dedicated background worker, ensure your target game window is active on the desktop and execute:
  ```bash
  python terraria_ai.py
  ```
* To launch the general-purpose vision engine, ensure your chosen game is set to fullscreen mode on your primary monitor and run:
  ```bash
  python universal_ai.py
  ```

---

## 🐈 The Theoretical Analogy: Thorndike's Puzzle Box
To explain this complex code in simple human terms for our presentation, this model mimics **Edward Thorndike's classic 1898 Psychology experiment**:
1. **The Chaos Phase (Step 0):** A cat placed inside a unfamiliar dark box scratches and moves completely at random because it does not understand how its environment works. This matches our AI's "Dumb Phase" where it frantically mashes arbitrary keys.
2. **The Accident (The Breakthrough):** By sheer probability, the cat bumps its paw into a hidden lever that opens the door to a treat. In our script, surviving a timestamp rewards the model with a `+1.0` value spike.
3. **The Brain Update (Optimization):** Upon repeated trials, the biological brain discards useless actions (scratching walls) and favors rewarding actions (the lever). Our PPO neural network dynamically updates its weight matrices to permanently eliminate erratic fumbles and lock in mastery.
