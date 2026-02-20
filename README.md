# 🗂️ File Organizer / Folder Structuring Script

A **Python script** to automatically organize the contents of any folder into structured categories based on file types. This tool helps you **clean up messy folders** and categorize files like images, documents, media, code, software, and more.  

---

## Features

- ✅ Automatically detects file types based on extensions.  
- ✅ Categorizes files into folders:  
  - Images, Documents, Audio, Video, Archives  
  - Scripts / Code, Fonts, HTML/CSS, JSON/XML  
  - Database, Executables, Software, Vector, 3D Models  
  - Others (catch-all for unknown file types)  
- ✅ Creates folders if they don’t exist.  
- ✅ Safely moves files to corresponding folders.  
- ✅ Supports a wide variety of extensions and programming languages.  

---

## How It Works

1. The script asks for the path of the folder you want to organize.  
2. It reads all files in the folder.  
3. For each file, it checks the extension and matches it to a predefined category.  
4. It creates a folder for that category (if it doesn’t exist) and moves the file into it.  
5. Files with unknown extensions are moved to the `Others` folder.  

---

## Supported Categories and Extensions

- **Image:** jpeg, jpg, png, gif, bmp, tiff, webp, heic, svg  
- **Documents:** txt, docx, doc, pdf, ppt, pptx, xls, xlsx, odt, rtf, md  
- **Audio:** mp3, wav, aac, flac, ogg, m4a, wma, aiff, alac  
- **Video:** mp4, mkv, avi, mov, wmv, flv, webm, m4v, mpeg  
- **Archives:** zip, rar, 7z, tar, gz, bz2, xz  
- **Scripts / Code:** py, js, ts, java, c, cpp, cs, go, rb, php, pl, swift, kt, kts, scala, rs, lua, dart, m, r, jl, hs, sh, bat, ps1, sql, html, htm, css, scss, less, xhtml, xml, json, yaml, yml, toml, ini  
- **Fonts:** ttf, otf, woff, woff2, eot  
- **HTML/CSS:** html, htm, css, scss, less, xhtml  
- **JSON/XML:** json, xml, yaml, yml, toml, ini  
- **Database:** sql, db, sqlite, mdb, accdb  
- **Executables:** exe, msi, bat, com, jar, app  
- **Software:** exe, msi, dmg, apk, appx, deb, rpm, pkg, jar  
- **Vector:** svg, eps, ai, cdr  
- **3D Models:** stl, obj, fbx, dae, 3ds  
- **Others:** All files that do not match above categories  

---

## Usage

1. Clone the repository:  

```bash
