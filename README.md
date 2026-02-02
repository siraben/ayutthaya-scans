# Ayutthaya GLTF Viewer

3D viewer for photogrammetry scans of temples from Ayutthaya, Thailand.

## Models

- Wat Mahathat
- Wat Yai Chai Mongkhon
- Wat Chaiwatthanaram

## Run

```bash
nix develop
python app.py
```

Or: `pip install flask && python app.py`

Open http://localhost:5000

## Controls

- **Mouse**: Rotate, pan, zoom
- **WASD**: Move
- **Space/Shift**: Up/down
- **H**: Toggle panel

## Deploy to GitHub Pages

Settings → Pages → Source: `master` branch, `/ (root)`
