import os
import re

tpl_dir = r'c:\Users\yashw\Desktop\electricity\main\templates'
idx_path = os.path.join(tpl_dir, 'index.html')

with open(idx_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find the main content block
pattern = re.compile(r'(<div class="-mt-12 mx-6 mb-6.*?)<footer', re.DOTALL)

# Blogs
bg_content = '''<div class="-mt-12 mx-6 mb-6">
  <div class="card shadow p-6">
    <h3 class="text-xl font-bold mb-4" style="margin-left: 20px; padding-top: 20px;">Internal Blogs</h3>
    <div class="text-gray-700" style="margin: 20px;">
      <p>The blogs feature is currently under construction. Please check back later.</p>
    </div>
  </div>
</div>
'''

new_bg = pattern.sub(bg_content + '<footer', content)

with open(os.path.join(tpl_dir, 'blogs.html'), 'w', encoding='utf-8') as f:
    f.write(new_bg)

print("Created blogs.html")

# Fix navigations across all templates to point to /blogs
for fname in os.listdir(tpl_dir):
    if not fname.endswith('.html'): continue
    path = os.path.join(tpl_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # The sidebar HTML might have: 
    # href="#!" ... aria-controls="navComponents"> ... Blogs Page
    # We essentially want to replace anything looking like Blogs Page link to href="/blogs"
    # Looking at how fix_nav.py did it:
    file_content = file_content.replace('href="./logs.html"', 'href="/blogs"')
    file_content = file_content.replace('href="#!" data-bs-toggle="collapse" data-bs-target="#navComponents"\n                aria-expanded="false" aria-controls="navComponents">\n                <i data-feather="package" class="w-4 h-4 mr-2"></i>\n                Blogs Page',
                              'href="/blogs">\n                <i data-feather="file-text" class="w-4 h-4 mr-2"></i>\n                Blogs Page')
    file_content = file_content.replace('href="#!" data-bs-toggle="collapse" data-bs-target="#navComponents" aria-expanded="false" aria-controls="navComponents">\n                <i data-feather="package" class="w-4 h-4 mr-2"></i>\n                Blogs Page',
                              'href="/blogs">\n                <i data-feather="file-text" class="w-4 h-4 mr-2"></i>\n                Blogs Page')

    # Catch-all if it's slightly different
    file_content = re.sub(r'href="[^"]*"\s*[^>]*>\s*<i[^>]*>\s*</i>\s*Blogs Page', r'href="/blogs">\n                <i data-feather="file-text" class="w-4 h-4 mr-2"></i>\n                Blogs Page', file_content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(file_content)

print("Navigation fixed")
