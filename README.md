# Ayutthaya 3D

3D viewer for interior scans from Ayutthaya, Thailand.

## Models

- Wat Chaiwatthanaram
- Wat Mahathat
- Wat Yai Chai Mongkhon

## Features

- **URL sharing**: Full camera state encoded in URL (24 chars)
- **PWA**: Works offline after first load
- **Loading progress**: Shows download percentage for slow connections

## Controls

| Input | Action |
|-------|--------|
| Mouse drag | Rotate view |
| Right-drag / Two-finger | Pan |
| Scroll | Zoom |
| Ctrl+Click | Set pivot point on surface |
| WASD | Move camera |
| Space / Shift | Move up / down |
| H | Toggle control panel |

## Display Options

- Wireframe, Grid, Axes helper, Bounding box
- Auto-rotate
- Background color
- Model transform (position, rotation, scale)
- Lighting (ambient/directional intensity, colors, shadows)
- Camera FOV and clip planes

## Run Locally

```bash
nix develop && python app.py
```

Or: `pip install flask && python app.py`

Open http://localhost:5000

## Deploy

GitHub Pages: Settings → Pages → Source: `master` branch, `/ (root)`
