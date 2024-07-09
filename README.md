# image-crop

Simple image crop (white border space) write in pthony and complied to exe, game project

# Setup enviroment (with venv->virtualenviroment)

For windows or Unix-like:

## venv Windows

```sh
python -m venv venv
venv\Scripts\activate.ps1 #Powershell
venv\Scripts\activate.bat # with cmd
```

## venv Linux

```sh
python3 -m venv
source venv/bin/activate
```

## Save dependencies (for development)

```sh
pip freeze > requirements.txt
```

## Install dependencies (for development)

```sh
pip install -r requirements.txt
```

Explanation: -r, --requirement <filename>

# Example of test/(usage with python)

```sh
python app.py path/img.jpg
python app.py path/img.png
python app.py path/img.svg
```

# Compile for Windows / Make an exe

edit the medatada.py

```sh
pyinstaller --onefile --name=ic ./src/app.py # to create an exe and .spec (template)
```

# or edit the compiler_pyinstaller.py and execute it by the command:

```python
py compiler_pyinstaller.py
```

# edit .spec file with ./spec/\*.spec.tempalte, add metadata

```sh
pyinstaller ic.spec # to re-compile adding the metadata to the exe
```
