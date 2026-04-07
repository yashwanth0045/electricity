import os
import re

tpl_dir = r'c:\Users\yashw\Desktop\electricity\main\templates'
idx_path = os.path.join(tpl_dir, 'index.html')

with open(idx_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find the main content block
pattern = re.compile(r'(<div class="-mt-12 mx-6 mb-6.*?)<footer', re.DOTALL)

# Feedback
fb_content = '''<div class="-mt-12 mx-6 mb-6">
  <div class="card shadow p-6">
    <h3 class="text-xl font-bold mb-4" style="margin-left: 20px; padding-top: 20px;">Feedback</h3>
    <form action="/feedback" method="post" style="margin: 20px;">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Subject</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700" type="text" placeholder="Subject">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2">Message</label>
        <textarea class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 h-32" placeholder="Your feedback..."></textarea>
      </div>
      <br>
      <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded" type="button">Submit Feedback</button>
    </form>
  </div>
</div>
'''

new_fb = pattern.sub(fb_content + '<footer', content)

with open(os.path.join(tpl_dir, 'feedback.html'), 'w', encoding='utf-8') as f:
    f.write(new_fb)

# Settings
st_content = '''<div class="-mt-12 mx-6 mb-6">
  <div class="card shadow p-6">
    <h3 class="text-xl font-bold mb-4" style="margin-left: 20px; padding-top: 20px;">Settings</h3>
    <div class="mb-4" style="margin-left: 20px;">
      <label class="flex items-center space-x-3">
        <input type="checkbox" class="form-checkbox h-5 w-5 text-indigo-600" checked>
        <span class="text-gray-700 font-medium">Enable Email Notifications</span>
      </label>
    </div>
    <div class="mb-4" style="margin-left: 20px;">
      <label class="flex items-center space-x-3">
        <input type="checkbox" class="form-checkbox h-5 w-5 text-indigo-600">
        <span class="text-gray-700 font-medium">Dark Mode Appearance</span>
      </label>
    </div>
    <br>
    <button style="margin-left: 20px;" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded" type="button">Save Settings</button>
  </div>
</div>
'''

new_st = pattern.sub(st_content + '<footer', content)

with open(os.path.join(tpl_dir, 'settings.html'), 'w', encoding='utf-8') as f:
    f.write(new_st)

print("Created feedback.html and settings.html")
