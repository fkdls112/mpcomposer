"""
Build script for mpcomposer using PyInstaller
"""
import PyInstaller.__main__
import os
import sys


def build():
    """Build executable"""
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Main script path
    main_script = os.path.join(project_dir, 'run.py')
    
    if not os.path.exists(main_script):
        print(f"Error: {main_script} not found")
        return False
    
    # PyInstaller arguments
    args = [
        main_script,
        '--name=MPComposer',
        '--windowed',
        '--onefile',
        '--clean',
        '--noconfirm',
    ]
    
    # Add icon if exists
    icon_path = os.path.join(project_dir, 'resources', 'icon.ico')
    if os.path.exists(icon_path):
        args.append(f'--icon={icon_path}')
    
    # Hidden imports for tkinter
    args.extend([
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.messagebox',
        '--hidden-import=tkinter.ttk',
    ])
    
    print("Starting build for mpcomposer...")
    print(f"Project dir: {project_dir}")
    print(f"Main script: {main_script}")
    
    try:
        PyInstaller.__main__.run(args)
        print("Build complete!")
        print("Output: dist/")
        
        # Check output
        exe_path = os.path.join(project_dir, 'dist', 'MPComposer.exe')
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"File size: {size_mb:.2f} MB")
        
        return True
        
    except Exception as e:
        print(f"Build failed: {str(e)}")
        return False


if __name__ == "__main__":
    success = build()
    sys.exit(0 if success else 1)
