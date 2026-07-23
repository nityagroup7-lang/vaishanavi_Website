import re

html_file = 'c:/Users/HP/Desktop/Nitya_Group/vaishnavi-website/Vaishnavi/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Animate card wrappers
def replace_col(match):
    # Just to add reveal to the column if not there
    inner = match.group(0)
    if 'reveal-' not in inner:
        # We will do this manually or skip, let's just animate the elements inside.
        pass
    return inner

# Animate inner elements of faculty cards
content = re.sub(r'<div class="fc-img-wrap">', r'<div class="fc-img-wrap reveal-top" data-delay="100">', content)
content = re.sub(r'<div class="fc-meta">', r'<div class="fc-meta reveal-left" data-delay="250">', content)
content = re.sub(r'<h3>(Faculty of Engineering Admissions|Arts and Humanities Admissions|Social And Sciences Admissions|Computer Science Admissions|Medicine and Health Sciences Admissions|Business and Economics Admissions)</h3>', r'<h3 class="reveal-right" data-delay="400">\1</h3>', content)
content = re.sub(r'<div class="fc-features">', r'<div class="fc-features reveal-bottom" data-delay="550">', content)
content = re.sub(r'<a href="#" class="fc-apply">', r'<a href="#" class="fc-apply reveal-left" data-delay="700">', content)

# Animate the columns themselves for a staggered entry
# Card 1, 4
content = content.replace('<div class="col-lg-4 col-md-6">\n                <div class="faculty-card">', '<div class="col-lg-4 col-md-6 reveal-bottom" data-delay="200">\n                <div class="faculty-card">')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
