import os
import re

tpl_dir = r'c:\Users\yashw\Desktop\electricity\main\templates'
for fname in os.listdir(tpl_dir):
    if not fname.endswith('.html'): continue
    path = os.path.join(tpl_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace specific nav links in the sidebar
    content = content.replace('href="#!" data-bs-toggle="collapse" data-bs-target="#navComponents"\n                aria-expanded="false" aria-controls="navComponents">\n                <i data-feather="package" class="w-4 h-4 mr-2"></i>\n                Feedback',
                              'href="/feedback">\n                <i data-feather="message-square" class="w-4 h-4 mr-2"></i>\n                Feedback')

    content = content.replace('href="#!" data-bs-toggle="collapse" data-bs-target="#navComponents"\n                aria-expanded="false" aria-controls="navComponents">\n                <i data-feather="package" class="w-4 h-4 mr-2"></i>\n                Settings',
                              'href="/settings">\n                <i data-feather="settings" class="w-4 h-4 mr-2"></i>\n                Settings')

    content = content.replace('href="./settings.html"', 'href="/settings"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
