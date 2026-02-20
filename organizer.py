import os
import shutil

path = input("Enter the path of folder which you want to make structured: ")

categories = {
    "Image": ["jpeg", "jpg", "png", "gif", "bmp", "tiff", "webp", "heic", "svg"],
    "Documents": [
        "txt",
        "docx",
        "doc",
        "pdf",
        "ppt",
        "pptx",
        "xls",
        "xlsx",
        "odt",
        "rtf",
        "md",
    ],
    "Audio": ["mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "aiff", "alac"],
    "Video": ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "m4v", "mpeg"],
    "Archives": ["zip", "rar", "7z", "tar", "gz", "bz2", "xz"],
    "Scripts / Code": [
        "py",
        "js",
        "ts",
        "java",
        "c",
        "cpp",
        "cs",
        "go",
        "rb",
        "php",
        "pl",
        "swift",
        "kt",
        "kts",
        "scala",
        "rs",
        "lua",
        "dart",
        "m",
        "r",
        "jl",
        "hs",
        "sh",
        "bat",
        "ps1",
        "sql",
        "html",
        "htm",
        "css",
        "scss",
        "less",
        "xhtml",
        "xml",
        "json",
        "yaml",
        "yml",
        "toml",
        "ini",
    ],
    "Fonts": ["ttf", "otf", "woff", "woff2", "eot"],
    "HTML/CSS": ["html", "htm", "css", "scss", "less", "xhtml"],
    "JSON/XML": ["json", "xml", "yaml", "yml", "toml", "ini"],
    "Database": ["sql", "db", "sqlite", "mdb", "accdb"],
    "Executables": ["exe", "msi", "bat", "com", "jar", "app"],
    "Software": ["exe", "msi", "dmg", "apk", "appx", "deb", "rpm", "pkg", "jar"],
    "Vector": ["svg", "eps", "ai", "cdr"],
    "3D Models": ["stl", "obj", "fbx", "dae", "3ds"],
    "Others": [],
}

if os.path.exists(path=path) == True:
    files = os.listdir(path=path)
    for file in files:
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):
            continue
        ext = file.split(".")[-1].lower()
        for category, ext_list in categories.items():
            if ext in ext_list:
                category_folder = os.path.join(path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, file))
                print("You folder is now structured.")

else:
    print("File not exsist! in your system.")
