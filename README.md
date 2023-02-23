# DeGourou (DeDRM + libgourou)

### Automate the process of getting decrypted ebook from [InternetArchive](https://archive.org/) without the need for [Adobe Digital Editions](https://www.adobe.com/in/solutions/ebook/digital-editions/download.html) and [Calibre](https://calibre-ebook.com/) with DeDRM Plugins.

---

## Things you need

1. ACSM file from the book page you borrowded from Internet Archive
2. Adobe Account (optional) (dummy account recommended)
3. Python v3.x.x Installed with pip (not required for normal users)

---

## Guide

*It uses dummy account for ADE, you can also use your own account*
### For Normal Users

1. Download binary file according to your operating system from [Releases Section](https://github.com/bipinkrish/DeGourou/releases)
2. Run the binary according to operating system

    A. Windows user's can just simply run the DeGourou-windows.exe

    B. Linux user's need to change the file permission and then can run

    ```
    chmod 777 DeGourou-linux
    ./DeGourou-linux
    ```

    C. MacOS user's accordingly

### For Developers

1. Clone the repositary or Download zip file and extract it
2. Install requirements using pip
3. Run "DeGourou.py" file


```
git clone https://github.com/bipinkrish/DeGourou.git
cd DeGourou
pip install -r requirements.txt
python DeGourou.py
```

---

## Usage

```
usage: DeGourou [-h] [-l] [file]

Download and Decrypt an encrypted PDF or EPUB file. It uses Dummy account for ADE, you can overide using --login

positional arguments:
  file         Path to the ACSM file

optional arguments:
  -h, --help   show this help message and exit
  -l, --login  Login to your ADE account. (optional)
```

---

## Credits

This project is highly inspired from these projects, thanks to them

1. [DeDrm](https://github.com/apprenticeharper/DeDRM_tools) tools for ebooks
2. [Standalone Version of DeDrm Tools](https://github.com/noDRM/DeDRM_tools)
3. [libgourou](https://indefero.soutade.fr//p/libgourou/) is a free implementation of Adobe's ADEPT protocol
4. [ACSM Input plugin + standalone](https://github.com/Leseratte10/acsm-calibre-plugin)