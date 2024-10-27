# Keylogger
Basic keylogger for educational purposes, capturing keystrokes and storing them in a file. This should only be used in secure, ethical, and legal ways.

## Run the Keylogger
1. Install Dependencies:
  ```bash
  pip install -r requirements.txt
  ```
2. Run the Keylogger:
  ```bash
  python keylogger.py
  ```
  This will start the keylogger, which will capture and log keystrokes to `key_log.txt` in your home directory.

## Explanation of Code
- **Keylogger Class:** Initializes logging with `pynput`, listens for keystrokes, and logs them.
- **Logging Special Keys:** Keys like `Enter`, `Shift`, and `Backspace` are logged as `[ENTER]`, `[SHIFT]`, and `[BACKSPACE]`.
- **Start Listener:** Starts a listener that continuously monitors for keystrokes until you terminate it (e.g., with `Ctrl+C)`.

## Log File Output Example
The log file (`key_log.txt`) will contain entries like:

```yaml
2024-10-27 10:30:15: h
2024-10-27 10:30:16: e
2024-10-27 10:30:17: l
2024-10-27 10:30:18: l
2024-10-27 10:30:19: o
2024-10-27 10:30:20: [SPACE]
2024-10-27 10:30:21: w
2024-10-27 10:30:22: o
2024-10-27 10:30:23: r
2024-10-27 10:30:24: l
2024-10-27 10:30:25: d
```

## Stopping the Keylogger
To stop the keylogger, press `Ctrl+C` in the terminal where it's running, or close the terminal window.

## Note
This keylogger is a basic tool and does not hide itself, nor does it run as a background service. You can enhance it by adding features like:

- Running in the background
- Emailing logs at specified intervals
- Capturing screenshots (requires additional libraries)

**⚠️ Reminder: Please use this only for ethical, educational, and authorized purposes. Unauthorized use is illegal and unethical.**
