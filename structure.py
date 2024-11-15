import os

def list_files(startpath):
    with open("project_structure.txt", "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f"{subindent}{file}\n")

# Remplacez '.' par le chemin vers le dossier de votre projet si nécessaire
list_files('.')
