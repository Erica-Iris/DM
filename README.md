# DeGourou (DeDRM + libgourou)

### Automate the process of getting decrypted book from [InternetArchive](https://archive.org/) without the need for [Adobe Digital Editions](https://www.adobe.com/in/solutions/ebook/digital-editions/download.html) and [Calibre](https://calibre-ebook.com/) with DeDRM Plugins.

---

## Things you need

1. Adobe Account (dummy account recommended)
2. Internet Archive Account
3. ACSM file from the book page you borrowded from Internet Archive
4. Python v3.x.x Installed with pip

---

## Guide

1. Clone the repositary or Downlaod zip file and extract it
2. Install requirements using pip
3. Run "DeGourou" file


```
git clone https://github.com/bipinkrish/DeGourou.git
cd DeGourou
pip install -r requirements.txt
python DeGourou.py
```

---

## Credits

This project is highly inspired from these projects, thanks to them

1. [DeDrm](https://github.com/apprenticeharper/DeDRM_tools) tools for ebooks
2. [Standalone Version of DeDrm Tools](https://github.com/noDRM/DeDRM_tools)
3. [libgourou](https://indefero.soutade.fr//p/libgourou/) is a free implementation of Adobe's ADEPT protocol]
4. [ACSM Input plugin + standalone](https://github.com/Leseratte10/acsm-calibre-plugin)