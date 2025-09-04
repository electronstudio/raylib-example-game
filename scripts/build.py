#!/usr/bin/env python3
"""Build script that uses uv with specific Python version for Nuitka compilation."""

import subprocess
import sys
import os


def main():
    """Build using uv with CPython 3.13 for Nuitka compilation."""
    print("Building raylib-example-game with uv + Nuitka (CPython 3.13)...")
    
    # Use uv run with specific Python version
    cmd = [
        "uv", "run", "--python", "python3.13",
        "python", "-m", "nuitka",
        "--onefile",
        "--assume-yes-for-downloads",
        "--output-filename=raylib-example-game",
        "--enable-plugin=anti-bloat",
        "--show-progress",
        "--prefer-source-code",
        "--remove-output",
        "--include-package-data=raylib_example_game.resources",
        "--main=raylib_example_game"
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, cwd=os.getcwd())
        print("\n[SUCCESS] Build completed successfully!")
        
        # Check if binary was created
        binary_name = "raylib-example-game"
        if os.path.exists(binary_name):
            print(f"[BINARY] Binary created: {binary_name}")
            print(f"[SIZE] Size: {os.path.getsize(binary_name) / 1024 / 1024:.1f} MB")
        else:
            print("[WARNING] Binary not found at expected location")
            
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Build failed with exit code {e.returncode}")
        sys.exit(e.returncode)
    except FileNotFoundError:
        print("[ERROR] uv not found. Make sure it's installed and in PATH")
        sys.exit(1)


if __name__ == "__main__":
    main()