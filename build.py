import os
import sys
import shutil
import subprocess
from datetime import datetime

def clean_build_dirs():
    """Clean up build directories"""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

def create_version_file():
    """Create version file for the executable"""
    version = "1.0.0"  # Update this as needed
    version_info = f"""
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=({version.replace('.', ', ')}, 0),
    prodvers=({version.replace('.', ', ')}, 0),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x40004,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Your Company'),
        StringStruct(u'FileDescription', u'Clipboard Keyboard - Text Input Simulator'),
        StringStruct(u'FileVersion', u'{version}'),
        StringStruct(u'InternalName', u'ClipKeyboard'),
        StringStruct(u'LegalCopyright', u'Copyright (c) {datetime.now().year}'),
        StringStruct(u'OriginalFilename', u'ClipKeyboard.exe'),
        StringStruct(u'ProductName', u'Clipboard Keyboard'),
        StringStruct(u'ProductVersion', u'{version}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    with open('version_info.txt', 'w') as f:
        f.write(version_info)

def build_executable():
    """Build the executable using PyInstaller"""
    # Create version file
    create_version_file()
    
    # PyInstaller command
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--name=ClipKeyboard',
        '--onefile',
        '--windowed',
        '--version-file=version_info.txt',
        '--clean',
        '--noconfirm',
        'ClipKeyboard.py'  # Updated path to main script
    ]
    
    # Run PyInstaller
    subprocess.run(cmd, check=True)

def main():
    print("Starting build process...")
    
    # Clean previous builds
    print("Cleaning previous builds...")
    clean_build_dirs()
    
    # Build executable
    print("Building executable...")
    build_executable()
    
    print("\nBuild completed successfully!")
    print("Executable can be found in the 'dist' directory")

if __name__ == "__main__":
    main() 