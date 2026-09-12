import os

files_to_fix = {
    "app/page.tsx": "../",
    "app/layout.tsx": "../",
    "app/analyzer/page.tsx": "../../",
    "app/evidence-locker/page.tsx": "../../",
    "app/threat-intelligence/page.tsx": "../../",
    "components/Navbar.tsx": "../",
    "components/EmergencyModal.tsx": "../",
    "lib/translations.ts": "../"
}

for path, prefix in files_to_fix.items():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace("@/components", f"{prefix}components")
        content = content.replace("@/lib", f"{prefix}lib")
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {path}")
