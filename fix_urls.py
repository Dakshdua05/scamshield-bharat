import glob
import os

files = glob.glob('app/api/**/*.ts', recursive=True)
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace single quotes
    content = content.replace("'http://localhost:8000", "`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}")
    # Replace double quotes
    content = content.replace('"http://localhost:8000', "`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}")
    
    # Fix the trailing quote issue by ensuring we don't end up with `url'` or `url"`
    content = content.replace("/api/emergency/incidents'", "/api/emergency/incidents`")
    content = content.replace("/api/threats'", "/api/threats`")
    content = content.replace("/api/analyze/audio'", "/api/analyze/audio`")
    content = content.replace("/api/emergency/draft'", "/api/emergency/draft`")
    content = content.replace("/api/analyze/text\"", "/api/analyze/text`")
    content = content.replace("/api/analyze/url'", "/api/analyze/url`")
    content = content.replace("/api/analyze/qr'", "/api/analyze/qr`")
    content = content.replace("/api/admin/stats'", "/api/admin/stats`")
    content = content.replace("/api/analyze/image'", "/api/analyze/image`")
    
    with open(f, 'w') as file:
        file.write(content)
print("Done fixing URLs")
