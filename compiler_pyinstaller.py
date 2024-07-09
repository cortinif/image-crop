import os
import PyInstaller.__main__

package_name= "image2metadata"

PyInstaller.__main__.run([
    '--onefile',
    '--name=ic',
    './src/app.py',
])