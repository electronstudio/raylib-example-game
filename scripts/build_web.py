#!/usr/bin/env python3
"""Web build script that creates a temporary workspace and builds with pygbag."""

import argparse
import subprocess
import sys
import os
import shutil
import tempfile
import urllib.request
import zipfile
from pathlib import Path


def main():
    """Build raylib-example-game for web using pygbag."""
    parser = argparse.ArgumentParser(description="Build raylib-example-game for web using pygbag")
    parser.add_argument("--build", action="store_true", 
                       help="Build only (no web server)")
    args = parser.parse_args()
    
    mode = "build only" if args.build else "build and serve"
    print(f"Building raylib-example-game for web with pygbag ({mode})...")
    
    project_root = Path.cwd()
    temp_dir = Path("/tmp/raylib_example_game_web_build")
    wheel_url = "https://github.com/electronstudio/pygbag-raylib/releases/download/v5.5.0.3/raylib-5.5.0.3-cp310-abi3-wasm32_bi_emscripten.whl"
    
    try:
        # Step 1: Create temporary folder (delete if exists)
        print("🗂️  Creating temporary build directory...")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        temp_dir.mkdir()
        os.chdir(temp_dir)
        print(f"📁 Working in: {temp_dir}")
        
        # Step 2: Copy raylib_example_game folder
        print("📂 Copying raylib_example_game folder...")
        source_game_dir = project_root / "raylib_example_game"
        dest_game_dir = temp_dir / "raylib_example_game"
        shutil.copytree(source_game_dir, dest_game_dir)
        
        # Step 3: Copy __main__.py to main.py
        print("📄 Copying __main__.py to main.py...")
        main_src = dest_game_dir / "__main__.py"
        main_dest = temp_dir / "main.py"
        shutil.copy2(main_src, main_dest)
        
        # Step 4: Download raylib wheel
        print("⬇️  Downloading raylib wheel...")
        wheel_filename = "raylib.whl"
        urllib.request.urlretrieve(wheel_url, wheel_filename)
        print(f"✅ Downloaded: {wheel_filename}")
        
        # Step 5: Extract wheel
        print("📦 Extracting wheel...")
        with zipfile.ZipFile(wheel_filename, 'r') as zip_ref:
            zip_ref.extractall()
        print("✅ Wheel extracted")
        
        # Step 6: Delete wheel file
        print("🗑️  Cleaning up wheel file...")
        os.remove(wheel_filename)
        
        # Step 7: Run pygbag
        build_type = "🔧 build only" if args.build else "🌐 build and serve"
        print(f"{build_type} Running pygbag...")
        pygbag_cmd = [
            "python3", "-m", "pygbag",
            "--PYBUILD", "3.12",
            "--ume_block", "0", 
            "--template", "noctx.tmpl",
            "--git"
        ]
        
        if args.build:
            pygbag_cmd.append("--build")
            
        pygbag_cmd.append("main.py")
        
        print(f"Running command: {' '.join(pygbag_cmd)}")
        result = subprocess.run(pygbag_cmd, check=True)
        
        print("✅ Web build completed successfully!")
        print(f"📁 Build artifacts should be in: {temp_dir}")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with exit code {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"❌ Build failed with error: {e}")
        sys.exit(1)
    finally:
        # Return to original directory
        os.chdir(project_root)
        print(f"📂 Returned to: {project_root}")


if __name__ == "__main__":
    main()