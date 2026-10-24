# Bloom Where You Are Planted

a Chris Grissette Vibe Coded Pomodoro Timer Project

An anime-inspired, local Pomodoro garden prototype with original Blender scenery.

Open this folder in VS Code. Run `npm run dev` in its terminal, then visit http://127.0.0.1:5174. No dependency installation needed. Python 3 and Node are required for the development commands.

Focus defaults to 25 minutes, short break to 5, and long break to 15 after each fourth focus session. Pause, resume, reset, task labels, adjustable durations and completed-session history are supported. Sessions are saved in this browser's local storage. Changing mode or saving durations resets the current timer. An active countdown uses wall-clock time, so background tab throttling does not slow it; keep the tab open. Reloading discards the active countdown, but retains completed sessions.

Growth milestones: seed (0 completed sessions), sprout (1), tree (4), forest (12). Explore growth previews the art without adding sessions. To try a full completion, set focus to 1 minute in Adjust timer. Breaks do not add progress.

Original 3D source: `blender/garden.blend`. Rebuild all four transparent renders with Blender: `blender -b -t 6 --python blender/garden.py`. The scene uses faceted canopies, an orthographic floating island and soft lighting. The web prototype displays those renders rather than a live 3D viewport. Google Fonts are optional; local serif/sans fallbacks work offline.

This is a local prototype: no account, cloud sync, notifications or background service. Clearing browser data removes saved sessions. Keep the same local address and browser to retain your garden.

## License

MIT — copyright 2026 Chris Grissette. The original code, Blender scene, and garden renders are included under this license. Google Fonts are loaded from their external service and retain their own licenses.
