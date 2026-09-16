# Ubot Initial GUI

A Kivy-based Graphical User Interface (GUI) application designed for controlling and interacting with **Ubot**. This project provides a multi-screen interface to access different robotic functionalities such as manual control, remote control, and mapping.

## Features

* **Multi-Screen Interface**: Uses multiple scripts and `.kv` files to manage different views.
* **Core Functions**:
  * Manual Control
  * Remote Control
  * Mapping capabilities
* **Interactive UI Elements**: Custom buttons, volume control sliders, and popups.

## Project Structure

The GUI is modularized into several Python scripts and corresponding Kivy (`.kv`) design files:

* `main.py`: The entry point for the application. Launches the main menu/interface.
* `s2.py`: A secondary screen that handles navigation to specific modules.
* `manual.py`: Interface for manual control of Ubot.
* `remote.py`: Interface for remote control functionality.
* `map.py`: Interface for mapping and navigation features.
* `*.kv` files (`my1.kv`, `my2.kv`, `mym.kv`, `mymp.kv`, `myr.kv`): Kivy design language files that define the layout and styling for the corresponding Python scripts.

## Prerequisites

* **Python 3.x**
* **Kivy**: The application relies on the Kivy framework for the GUI.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BavanPrabahar/initial_gui.git
   cd initial_gui
   ```

2. Install the required dependencies:
   ```bash
   pip install Kivy
   ```

## Usage

To start the Ubot GUI, run the main entry point:

```bash
python3 main.py
```

From the main menu, you can navigate to other functionalities like mapping or remote control as needed.

## License

This project is licensed under the MIT License - see the LICENSE file for details (if applicable).
