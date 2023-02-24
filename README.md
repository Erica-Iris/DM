# DeGourou (DeDRM + libgourou)

### Automate the process of getting decrypted ebook from [InternetArchive](https://archive.org/) without the need for [Adobe Digital Editions](https://www.adobe.com/in/solutions/ebook/digital-editions/download.html) and [Calibre](https://calibre-ebook.com/) with DeDRM Plugins.

---

## Things you need

1. ACSM file from the book page you borrowded from Internet Archive
2. Adobe Account (optional) (dummy account recommended)
3. Python v3.x.x Installed with pip (not required for normal users)

---

## Usage

```
usage: DeGourou.xxx [-h] [-l] [-o OUTPUT] [file]

Download and Decrypt an encrypted PDF or EPUB file. It uses Dummy account for ADE, you can overide using --login

positional arguments:
  file                  Path to the ACSM file

optional arguments:
  -h, --help            show this help message and exit
  -l, --login           Login to your ADE account. (optional)
  -o OUTPUT             Output file name. (optional)
```

---

## Guide

*By default it uses dummy account for ADE, you can also use your own account*
### For Normal Users

1. Download binary file according to your operating system from [Releases Section](https://github.com/bipinkrish/DeGourou/releases)
2. Run the binary according to operating system

    A. Windows user's can just open Command Prompt and use based on the [USAGE](https://github.com/bipinkrish/DeGourou#usage)

    B. Linux user's need to change the file permission and then can run

    ```
    chmod 777 DeGourou-linux
    ./DeGourou-linux
    ```

    C. MacOS user's accordingly with name ```DeGourou.bin```

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

## Credits

This project is based on the following projects:

1. [DeDrm](https://github.com/apprenticeharper/DeDRM_tools) tools for ebooks by Apprentice Harper et al.
2. [Standalone Version of DeDrm Tools](https://github.com/noDRM/DeDRM_tools) by noDRM
3. [libgourou](https://indefero.soutade.fr//p/libgourou/) is a free implementation of Adobe's ADEPT protocol, by Grégory Soutadé
4. [Calibre ACSM Input plugin](https://github.com/Leseratte10/acsm-calibre-plugin), by Leseratte10

## Copyright notices

```
ACSM Input Plugin for Calibre - Copyright (c) 2021-2023 Leseratte10
ACSM Input Plugin for Calibre / acsm-calibre-plugin
Formerly known as "DeACSM"
Copyright (c) 2021-2023 Leseratte10

This software is based on a Python reimplementation of the C++ library 
"libgourou" by Grégory Soutadé which is under the LGPLv3 or later 
license (http://indefero.soutade.fr/p/libgourou/).

I have no idea whether a reimplementation in another language counts 
as "derivative use", so just in case it does, I'm putting this project 
under the GPLv3 (which is allowed in the LGPLv3 license) to prevent any 
licensing issues. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

See the "LICENSE" file for a full copy of the GNU GPL v3.

========================================================================

libgourou:
Copyright 2021 Grégory Soutadé

This file is part of libgourou.

libgourou is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

libgourou is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with libgourou. If not, see <http://www.gnu.org/licenses/>.


```
