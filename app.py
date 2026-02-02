#!/usr/bin/env python3
"""Flask server for GLTF/GLB viewer."""

import argparse
import os
import re
from pathlib import Path
from flask import Flask, send_from_directory, jsonify, abort

app = Flask(__name__, static_folder="static")

MODELS_DIR = Path(__file__).parent.resolve()


@app.after_request
def add_security_headers(response):
    """Add security headers to all responses."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


ALLOWED_MODEL_EXTENSIONS = {".glb", ".gltf"}
SAFE_FILENAME_PATTERN = re.compile(r"^[a-zA-Z0-9_\-]+\.(glb|gltf)$")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


MODEL_NAMES = {
    "1": "Wat Mahathat",
    "2": "Wat Yai Chai Mongkhon",
    "3": "Wat Chaiwatthanaram",
}


@app.route("/models")
def list_models():
    """List available GLB/GLTF files."""
    models = []
    for ext in ("*.glb", "*.gltf"):
        for f in MODELS_DIR.glob(ext):
            name = MODEL_NAMES.get(f.stem, f.stem)
            models.append({"name": name, "filename": f.name})
    return jsonify(models)


@app.route("/models/<filename>")
def serve_model(filename):
    """Serve a GLB/GLTF file."""
    # Validate filename to prevent path traversal
    if not SAFE_FILENAME_PATTERN.match(filename):
        abort(400, "Invalid filename")

    # Verify file exists and has allowed extension
    filepath = MODELS_DIR / filename
    if not filepath.suffix.lower() in ALLOWED_MODEL_EXTENSIONS:
        abort(400, "Invalid file type")

    # Ensure resolved path is within MODELS_DIR (defense in depth)
    try:
        filepath.resolve().relative_to(MODELS_DIR)
    except ValueError:
        abort(403, "Access denied")

    return send_from_directory(MODELS_DIR, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GLTF/GLB Viewer")
    parser.add_argument("-p", "--port", type=int, default=5000, help="Port to run on")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    os.makedirs("static", exist_ok=True)
    print(f"Starting GLTF Viewer at http://{args.host}:{args.port}")
    app.run(debug=args.debug, host=args.host, port=args.port)
