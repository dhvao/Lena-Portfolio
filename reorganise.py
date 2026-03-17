import os
import shutil
import sys

base = r'c:\Users\TomaKuzmic\OneDrive - ROWDEN TECHNOLOGIES LTD\Documents\Lena-Portfolio-main\Images'

# STEP 1: Create directories
dirs = [
    'hero', 'nav', '_unused',
    r'project-01-lear\intro', r'project-01-lear\own-design', r'project-01-lear\3d-models',
    r'project-01-lear\leather-case', r'project-01-lear\leather-pouch', r'project-01-lear\leather-belt',
    r'project-01-lear\development', r'project-01-lear\final', r'project-01-lear\what-else',
    r'project-02-evtol\intro', r'project-02-evtol\brand-research', r'project-02-evtol\sketches',
    r'project-02-evtol\renders', r'project-02-evtol\cmf', r'project-02-evtol\roadmap',
    r'project-02-evtol\interior', r'project-02-evtol\packaging',
    r'project-03-personal\audi'
]
for d in dirs:
    os.makedirs(os.path.join(base, d), exist_ok=True)
print('Step 1: Directories created')

# STEP 2: Move and rename files
moves = [
    # Hero
    (r'_0000001-0420.mp4', r'hero\hero-video.mp4'),
    (r'0064\Image11_000.jpg', r'hero\lena-portrait.jpg'),
    (r'Screenshot 2026-03-13 143451.png', r'hero\lena-about.png'),
    # Nav
    (r'skill development\design brief section\LEA.png', r'nav\lear-logo.png'),
    (r'contents\Screenshot 2026-03-13 143116.png', r'nav\lear-thumbnail.png'),
    (r'skill development\design brief section\6566129-Photoroom.png', r'nav\evtol-logo.png'),
    (r'contents\Screenshot 2026-03-13 143130.png', r'nav\evtol-thumbnail.png'),
    (r'contents\Screenshot 2026-03-13 143147.png', r'nav\personal-thumbnail.png'),
    # Proj01 intro
    (r'skill development\Screenshot 2026-03-13 141954.png', r'project-01-lear\intro\machine-overview.png'),
    (r'skill development\Screenshot 2026-03-13 141535.png', r'project-01-lear\intro\machine-closeup.png'),
    # Proj01 own-design
    (r'skill development\own design\71613179837__65AE876D-A07B-4719-95B5-D0E05E3FB168.jpg', r'project-01-lear\own-design\design-sketch-01.jpg'),
    (r'skill development\own design\IMG_4315.jpg', r'project-01-lear\own-design\design-sketch-02.jpg'),
    (r'skill development\own design\IMG_4421.jpg', r'project-01-lear\own-design\design-sketch-03.jpg'),
    (r'skill development\own design\IMG_4321.jpg', r'project-01-lear\own-design\design-sketch-04.jpg'),
    (r'skill development\own design\Screenshot 2026-03-13 145706.png', r'project-01-lear\own-design\design-overview.png'),
    # Proj01 3d
    (r'3d\base_basic_shaded.glb', r'project-01-lear\3d-models\model-v1.glb'),
    (r'3d\base_basic_shadeq.glb', r'project-01-lear\3d-models\model-v2.glb'),
    (r'3d\base_basic_ssshaded.glb', r'project-01-lear\3d-models\model-v3.glb'),
    # Proj01 leather-case
    (r'skill development\leather\case\DSCF1104.jpg', r'project-01-lear\leather-case\case-01.jpg'),
    (r'skill development\leather\case\DSCF1141.jpg', r'project-01-lear\leather-case\case-02.jpg'),
    (r'skill development\leather\case\DSCF1144.jpg', r'project-01-lear\leather-case\case-03.jpg'),
    (r'skill development\leather\case\DSCF1152.jpg', r'project-01-lear\leather-case\case-04.jpg'),
    # Proj01 leather-pouch
    (r'skill development\leather\pouch\DSCF1185.jpg', r'project-01-lear\leather-pouch\pouch-01.jpg'),
    (r'skill development\leather\pouch\DSCF1190.jpg', r'project-01-lear\leather-pouch\pouch-02.jpg'),
    (r'skill development\leather\pouch\DSCF1188.jpg', r'project-01-lear\leather-pouch\pouch-03.jpg'),
    (r'skill development\leather\pouch\DSCF1090.jpg', r'project-01-lear\leather-pouch\pouch-04.jpg'),
    (r'skill development\leather\pouch\DSCF1087.jpg', r'project-01-lear\leather-pouch\pouch-05.jpg'),
    # Proj01 leather-belt
    (r'skill development\leather\belt\DSCF1021.jpg', r'project-01-lear\leather-belt\belt-01.jpg'),
    (r'skill development\leather\belt\DSCF1168.jpg', r'project-01-lear\leather-belt\belt-02.jpg'),
    (r'skill development\leather\belt\DSCF1177.jpg', r'project-01-lear\leather-belt\belt-03.jpg'),
    (r'skill development\leather\belt\DSCF1016.jpg', r'project-01-lear\leather-belt\belt-04.jpg'),
    (r'skill development\leather\belt\DSCF1155.jpg', r'project-01-lear\leather-belt\belt-05.jpg'),
    # Proj01 development
    (r'skill development\final project development\Screenshot 2026-03-13 145756.png', r'project-01-lear\development\dev-01.png'),
    (r'skill development\final project development\Screenshot 2026-03-13 145830.png', r'project-01-lear\development\dev-02.png'),
    (r'skill development\final project development\Screenshot 2026-03-13 145846.png', r'project-01-lear\development\dev-03.png'),
    (r'skill development\final project development\Screenshot 2026-03-13 145910.png', r'project-01-lear\development\dev-04.png'),
    (r'skill development\final project development\Screenshot 2026-03-13 145809.png', r'project-01-lear\development\dev-05.png'),
    # Proj01 final
    (r'skill development\final project\front on mini.png', r'project-01-lear\final\front.png'),
    (r'skill development\final project\side shot mini.png', r'project-01-lear\final\side.png'),
    (r'skill development\final project\backshot test.png', r'project-01-lear\final\back.png'),
    # Proj01 what-else
    (r'skill development\what else did i learn\Screenshot 2026-03-13 150129.png', r'project-01-lear\what-else\what-else.png'),
    # Proj02 intro
    (r'skill development\design brief section\Screenshot 2026-03-13 170037.png', r'project-02-evtol\intro\brief-overview.png'),
    (r'skill development\design brief section\Screenshot 2026-03-14 172837-Photoroom.png', r'project-02-evtol\intro\system-composition.png'),
    (r'skill development\storyboard collage (1).png', r'project-02-evtol\intro\storyboard-collage.png'),
    (r'skill development\evtol collage.png', r'project-02-evtol\intro\evtol-collage.png'),
    (r'PNGs\secti2.png', r'project-02-evtol\intro\section-divider.png'),
    # Proj02 brand-research
    (u'skill development\design brief section\u2014Pngtree\u2014mute icon - no sound_23059135.png', r'project-02-evtol\brand-research\mute-icon.png'),
    (r'skill development\design brief section\unnamed.png', r'project-02-evtol\brand-research\inspiration-01.png'),
    (r'skill development\design brief section\YN5tWLwpVphAx7Ky-90wRGKF239GlscDKI18oETuw8suveYTYEJHiNDZwEqGeqLr1yQUzjWMkFG_KF31pIK4Com6.jpg', r'project-02-evtol\brand-research\reference-photo.jpg'),
    (r'skill development\design brief section\red inspo images.png', r'project-02-evtol\brand-research\inspiration-red.png'),
    (r'skill development\design brief section\unnamed (2).png', r'project-02-evtol\brand-research\inspiration-02.png'),
    # Proj02 sketches
    (r'PNGs\Untitled_Artwork.png', r'project-02-evtol\sketches\sketch-01.png'),
    (r'PNGs\Untitled_Artwork 2.png', r'project-02-evtol\sketches\sketch-02.png'),
    (r'PNGs\Untitled_Artwork 9.png', r'project-02-evtol\sketches\sketch-03.png'),
    # Proj02 interior
    (r'skill development\design brief section\unnamed1.png', r'project-02-evtol\interior\interior-sketch-01.png'),
    (r'PNGs\Untitled_Artwork 27.png', r'project-02-evtol\interior\interior-sketch-02.png'),
    (r'PNGs\Untitled_Artwork 28.png', r'project-02-evtol\interior\interior-sketch-03.png'),
    (r'PNGs\aqa.png', r'project-02-evtol\interior\interior-sketch-04.png'),
    # Proj02 renders
    (r'PNGs\PPT_EXTERIOR.png', r'project-02-evtol\renders\render-exterior.png'),
    (r'0064\LENA SUNSET 01.jpg', r'project-02-evtol\renders\render-sunset.jpg'),
    # Proj02 cmf
    (r'0064\LENA CMF O3.jpg', r'project-02-evtol\cmf\cmf-01.jpg'),
    (r'0064\lena africa 02.jpg', r'project-02-evtol\cmf\cmf-02.jpg'),
    (r'0064\LENA CMF 012.jpg', r'project-02-evtol\cmf\cmf-03.jpg'),
    (r'0064\lena mountains 02.jpg', r'project-02-evtol\cmf\cmf-04.jpg'),
    (r'0064\LENA CMF 04.jpg', r'project-02-evtol\cmf\cmf-05.jpg'),
    (r'0064\new beacxh lean.jpg', r'project-02-evtol\cmf\cmf-06.jpg'),
    # Proj02 roadmap
    (r'0064\Image11_0001111.jpg', r'project-02-evtol\roadmap\checkin-hub.jpg'),
    (r'0064\LENA FLY 011.jpg', r'project-02-evtol\roadmap\take-off.jpg'),
    (r'0064\Screenshot 2026-03-17 110710.png', r'project-02-evtol\roadmap\drop-off.png'),
    (r'0064\Image113.jpg', r'project-02-evtol\roadmap\evtol-detaches.jpg'),
    (r'0064\LENA GREEN EXT 02.jpg', r'project-02-evtol\roadmap\pick-up-pod.jpg'),
    (r'0064\LENA TOP SILLOUTTE 02.jpg', r'project-02-evtol\roadmap\recharge-pod.jpg'),
    (r'0064\LENA TOP SILLOUTTE 012.jpg', r'project-02-evtol\roadmap\recharge-pod-alt.jpg'),
    # Proj02 packaging
    (r'skill development\design brief section\WhatsApp Image 2026-03-16 at 12.31.08.jpeg', r'project-02-evtol\packaging\packaging-01.jpeg'),
    (r'skill development\design brief section\WhatsApp Image 2026-03-16 at 12.313.08.jpeg', r'project-02-evtol\packaging\packaging-02.jpeg'),
    (r'skill development\design brief section\WhatsApp Image 2026-03-16 at 12.331.08.jpeg', r'project-02-evtol\packaging\packaging-03.jpeg'),
    (r'skill development\design brief section\WhatsApp Image 12026-03-16 at 12.31.08.jpeg', r'project-02-evtol\packaging\packaging-04.jpeg'),
    # Proj03 audi
    (r'skill development\audi\audi-a3-car-emblem-logo-audi-car-logo-png-brand-image-Photoroom.png', r'project-03-personal\audi\audi-logo.png'),
]

moved = []
not_found = []

for src_rel, dst_rel in moves:
    src = os.path.join(base, src_rel)
    dst = os.path.join(base, dst_rel)
    if os.path.exists(src):
        shutil.move(src, dst)
        moved.append(dst_rel)
        print(f'  OK: {src_rel}  ->  {dst_rel}')
    else:
        not_found.append(src_rel)
        print(f'  MISSING: {src_rel}')

print(f'\nStep 2: Moved {len(moved)} files. Not found: {len(not_found)}')

# STEP 3: Move unused files
unused = [
    r'Copy of website draft .png',
    r'0064\0064.png', r'0064\0132.png', r'0064\Image11.jpg', r'0064\Image12_000.jpg',
    r'0064\Image13.jpg', r'0064\Image14.jpg',
    r'0064\LENA 07.jpg', r'0064\LENA 08.jpg', r'0064\LENA BEACH FLY 01.jpg',
    r'0064\LENA BLUE 05.jpg', r'0064\LENA BLUE NEW 01.jpg',
    r'0064\LENA CMF 01.jpg', r'0064\LENA CMF 02.jpg', r'0064\LENA CMF 042.jpg',
    r'0064\LENA EXTERIOR 01.jpg', r'0064\LENA FLY 01.jpg', r'0064\LENA GREEN FLY 03.jpg',
    r'0064\LENA NEW RED INTERIOR 01.jpg', r'0064\LENA NEW RED INTERIOR 02.jpg',
    r'0064\lena blue 01.jpg', r'0064\lena blue 02.jpg', r'0064\lena blue 03.jpg',
    r'0064\lena blue 04.jpg', r'0064\lena blue side 05.jpg',
    r'0064\lena green 001.jpg', r'0064\lena green 01 (1).jpg', r'0064\lena green 02 (1).jpg',
    r'0064\lena green 03 (1).jpg', r'0064\lena green 09.jpg', r'0064\lena green sparkles.jpg',
    r'0064\lena red 05.jpg', r'0064\lena red kitchen 002.jpg', r'0064\lena red side 04.jpg',
    r'contents\example.png',
    r'PNGs\People at table .png', r'PNGs\unnamed.png',
    r'PNGs\Untitled_Artwork 3.png', r'PNGs\Untitled_Artwork 4.png', r'PNGs\Untitled_Artwork 5.png',
    r'PNGs\Untitled_Artwork 6.png', r'PNGs\Untitled_Artwork 7.png', r'PNGs\Untitled_Artwork 8.png',
    r'PNGs\Untitled_Artwork 10.png', r'PNGs\Untitled_Artwork 11.png', r'PNGs\Untitled_Artwork 12.png',
    r'PNGs\Untitled_Artwork 13.png', r'PNGs\Untitled_Artwork 14.png', r'PNGs\Untitled_Artwork 15.png',
    r'PNGs\Untitled_Artwork 16.png', r'PNGs\Untitled_Artwork 17.png', r'PNGs\Untitled_Artwork 18.png',
    r'PNGs\Untitled_Artwork 19.png', r'PNGs\Untitled_Artwork 20.png', r'PNGs\Untitled_Artwork 21.png',
    r'PNGs\Untitled_Artwork 22.png', r'PNGs\Untitled_Artwork 23.png', r'PNGs\Untitled_Artwork 24.png',
    r'PNGs\Untitled_Artwork 25.png', r'PNGs\Untitled_Artwork 26.png',
    r'PNGs\Untitled_Artwork 29.png', r'PNGs\Untitled_Artwork 30.png', r'PNGs\Untitled_Artwork 32.png',
    r'PNGs\Untitled_Artwork 33.png', r'PNGs\Untitled_Artwork 34.png', r'PNGs\Untitled_Artwork 35.png',
    r'PNGs\Untitled_Artwork 36.png', r'PNGs\Untitled_Artwork 37.png', r'PNGs\Untitled_Artwork 38.png',
    r'PNGs\Untitled_Artwork 39.png', r'PNGs\Untitled_Artwork 40.png',
]

unused_moved = 0
unused_dst = os.path.join(base, '_unused')
for f in unused:
    src = os.path.join(base, f)
    if os.path.exists(src):
        shutil.move(src, unused_dst)
        unused_moved += 1

# Move entire Canva format folder contents
canva_dir = os.path.join(base, 'Canva format')
if os.path.isdir(canva_dir):
    for item in os.listdir(canva_dir):
        src = os.path.join(canva_dir, item)
        if os.path.isfile(src):
            shutil.move(src, unused_dst)
            unused_moved += 1

print(f'Step 3: Moved {unused_moved} unused files to _unused/')

# STEP 4: Update index.html
html_path = r'c:\Users\TomaKuzmic\OneDrive - ROWDEN TECHNOLOGIES LTD\Documents\Lena-Portfolio-main\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('Images/_0000001-0420.mp4', 'Images/hero/hero-video.mp4'),
    ('Images/0064/Image11_000.jpg', 'Images/hero/lena-portrait.jpg'),
    ('Images/Screenshot 2026-03-13 143451.png', 'Images/hero/lena-about.png'),
    ('Images/skill development/design brief section/LEA.png', 'Images/nav/lear-logo.png'),
    ('Images/contents/Screenshot 2026-03-13 143116.png', 'Images/nav/lear-thumbnail.png'),
    ('Images/skill development/design brief section/6566129-Photoroom.png', 'Images/nav/evtol-logo.png'),
    ('Images/contents/Screenshot 2026-03-13 143130.png', 'Images/nav/evtol-thumbnail.png'),
    ('Images/contents/Screenshot 2026-03-13 143147.png', 'Images/nav/personal-thumbnail.png'),
    ('Images/skill development/Screenshot 2026-03-13 141954.png', 'Images/project-01-lear/intro/machine-overview.png'),
    ('Images/skill development/Screenshot 2026-03-13 141535.png', 'Images/project-01-lear/intro/machine-closeup.png'),
    ('Images/skill development/own design/71613179837__65AE876D-A07B-4719-95B5-D0E05E3FB168.jpg', 'Images/project-01-lear/own-design/design-sketch-01.jpg'),
    ('Images/skill development/own design/IMG_4315.jpg', 'Images/project-01-lear/own-design/design-sketch-02.jpg'),
    ('Images/skill development/own design/IMG_4421.jpg', 'Images/project-01-lear/own-design/design-sketch-03.jpg'),
    ('Images/skill development/own design/IMG_4321.jpg', 'Images/project-01-lear/own-design/design-sketch-04.jpg'),
    ('Images/skill development/own design/Screenshot 2026-03-13 145706.png', 'Images/project-01-lear/own-design/design-overview.png'),
    ('Images/3d/base_basic_shaded.glb', 'Images/project-01-lear/3d-models/model-v1.glb'),
    ('Images/3d/base_basic_shadeq.glb', 'Images/project-01-lear/3d-models/model-v2.glb'),
    ('Images/3d/base_basic_ssshaded.glb', 'Images/project-01-lear/3d-models/model-v3.glb'),
    ('Images/skill development/leather/case/DSCF1104.jpg', 'Images/project-01-lear/leather-case/case-01.jpg'),
    ('Images/skill development/leather/case/DSCF1141.jpg', 'Images/project-01-lear/leather-case/case-02.jpg'),
    ('Images/skill development/leather/case/DSCF1144.jpg', 'Images/project-01-lear/leather-case/case-03.jpg'),
    ('Images/skill development/leather/case/DSCF1152.jpg', 'Images/project-01-lear/leather-case/case-04.jpg'),
    ('Images/skill development/leather/pouch/DSCF1185.jpg', 'Images/project-01-lear/leather-pouch/pouch-01.jpg'),
    ('Images/skill development/leather/pouch/DSCF1190.jpg', 'Images/project-01-lear/leather-pouch/pouch-02.jpg'),
    ('Images/skill development/leather/pouch/DSCF1188.jpg', 'Images/project-01-lear/leather-pouch/pouch-03.jpg'),
    ('Images/skill development/leather/pouch/DSCF1090.jpg', 'Images/project-01-lear/leather-pouch/pouch-04.jpg'),
    ('Images/skill development/leather/pouch/DSCF1087.jpg', 'Images/project-01-lear/leather-pouch/pouch-05.jpg'),
    ('Images/skill development/leather/belt/DSCF1021.jpg', 'Images/project-01-lear/leather-belt/belt-01.jpg'),
    ('Images/skill development/leather/belt/DSCF1168.jpg', 'Images/project-01-lear/leather-belt/belt-02.jpg'),
    ('Images/skill development/leather/belt/DSCF1177.jpg', 'Images/project-01-lear/leather-belt/belt-03.jpg'),
    ('Images/skill development/leather/belt/DSCF1016.jpg', 'Images/project-01-lear/leather-belt/belt-04.jpg'),
    ('Images/skill development/leather/belt/DSCF1155.jpg', 'Images/project-01-lear/leather-belt/belt-05.jpg'),
    ('Images/skill development/final project development/Screenshot 2026-03-13 145756.png', 'Images/project-01-lear/development/dev-01.png'),
    ('Images/skill development/final project development/Screenshot 2026-03-13 145830.png', 'Images/project-01-lear/development/dev-02.png'),
    ('Images/skill development/final project development/Screenshot 2026-03-13 145846.png', 'Images/project-01-lear/development/dev-03.png'),
    ('Images/skill development/final project development/Screenshot 2026-03-13 145910.png', 'Images/project-01-lear/development/dev-04.png'),
    ('Images/skill development/final project development/Screenshot 2026-03-13 145809.png', 'Images/project-01-lear/development/dev-05.png'),
    ('Images/skill development/final project/front on mini.png', 'Images/project-01-lear/final/front.png'),
    ('Images/skill development/final project/side shot mini.png', 'Images/project-01-lear/final/side.png'),
    ('Images/skill development/final project/backshot test.png', 'Images/project-01-lear/final/back.png'),
    ('Images/skill development/what else did i learn/Screenshot 2026-03-13 150129.png', 'Images/project-01-lear/what-else/what-else.png'),
    ('Images/skill development/design brief section/Screenshot 2026-03-13 170037.png', 'Images/project-02-evtol/intro/brief-overview.png'),
    ('Images/skill development/design brief section/Screenshot 2026-03-14 172837-Photoroom.png', 'Images/project-02-evtol/intro/system-composition.png'),
    ('Images/skill development/storyboard collage (1).png', 'Images/project-02-evtol/intro/storyboard-collage.png'),
    ('Images/skill development/evtol collage.png', 'Images/project-02-evtol/intro/evtol-collage.png'),
    ('Images/PNGs/secti2.png', 'Images/project-02-evtol/intro/section-divider.png'),
    (u'Images/skill development/design brief section/\u2014Pngtree\u2014mute icon - no sound_23059135.png', 'Images/project-02-evtol/brand-research/mute-icon.png'),
    ('Images/skill development/design brief section/unnamed.png', 'Images/project-02-evtol/brand-research/inspiration-01.png'),
    ('Images/skill development/design brief section/YN5tWLwpVphAx7Ky-90wRGKF239GlscDKI18oETuw8suveYTYEJHiNDZwEqGeqLr1yQUzjWMkFG_KF31pIK4Com6.jpg', 'Images/project-02-evtol/brand-research/reference-photo.jpg'),
    ('Images/skill development/design brief section/red inspo images.png', 'Images/project-02-evtol/brand-research/inspiration-red.png'),
    ('Images/skill development/design brief section/unnamed (2).png', 'Images/project-02-evtol/brand-research/inspiration-02.png'),
    ('Images/skill development/design brief section/unnamed1.png', 'Images/project-02-evtol/interior/interior-sketch-01.png'),
    ('Images/PNGs/Untitled_Artwork.png', 'Images/project-02-evtol/sketches/sketch-01.png'),
    ('Images/PNGs/Untitled_Artwork 2.png', 'Images/project-02-evtol/sketches/sketch-02.png'),
    ('Images/PNGs/Untitled_Artwork 9.png', 'Images/project-02-evtol/sketches/sketch-03.png'),
    ('Images/PNGs/Untitled_Artwork 27.png', 'Images/project-02-evtol/interior/interior-sketch-02.png'),
    ('Images/PNGs/Untitled_Artwork 28.png', 'Images/project-02-evtol/interior/interior-sketch-03.png'),
    ('Images/PNGs/aqa.png', 'Images/project-02-evtol/interior/interior-sketch-04.png'),
    ('Images/PNGs/PPT_EXTERIOR.png', 'Images/project-02-evtol/renders/render-exterior.png'),
    ('Images/0064/LENA SUNSET 01.jpg', 'Images/project-02-evtol/renders/render-sunset.jpg'),
    ('Images/0064/LENA CMF O3.jpg', 'Images/project-02-evtol/cmf/cmf-01.jpg'),
    ('Images/0064/lena africa 02.jpg', 'Images/project-02-evtol/cmf/cmf-02.jpg'),
    ('Images/0064/LENA CMF 012.jpg', 'Images/project-02-evtol/cmf/cmf-03.jpg'),
    ('Images/0064/lena mountains 02.jpg', 'Images/project-02-evtol/cmf/cmf-04.jpg'),
    ('Images/0064/LENA CMF 04.jpg', 'Images/project-02-evtol/cmf/cmf-05.jpg'),
    ('Images/0064/new beacxh lean.jpg', 'Images/project-02-evtol/cmf/cmf-06.jpg'),
    ('Images/0064/Image11_0001111.jpg', 'Images/project-02-evtol/roadmap/checkin-hub.jpg'),
    ('Images/0064/LENA FLY 011.jpg', 'Images/project-02-evtol/roadmap/take-off.jpg'),
    ('Images/0064/Screenshot 2026-03-17 110710.png', 'Images/project-02-evtol/roadmap/drop-off.png'),
    ('Images/0064/Image113.jpg', 'Images/project-02-evtol/roadmap/evtol-detaches.jpg'),
    ('Images/0064/LENA GREEN EXT 02.jpg', 'Images/project-02-evtol/roadmap/pick-up-pod.jpg'),
    ('Images/0064/LENA TOP SILLOUTTE 02.jpg', 'Images/project-02-evtol/roadmap/recharge-pod.jpg'),
    ('Images/0064/LENA TOP SILLOUTTE 012.jpg', 'Images/project-02-evtol/roadmap/recharge-pod-alt.jpg'),
    ('Images/skill development/design brief section/WhatsApp Image 2026-03-16 at 12.31.08.jpeg', 'Images/project-02-evtol/packaging/packaging-01.jpeg'),
    ('Images/skill development/design brief section/WhatsApp Image 2026-03-16 at 12.313.08.jpeg', 'Images/project-02-evtol/packaging/packaging-02.jpeg'),
    ('Images/skill development/design brief section/WhatsApp Image 2026-03-16 at 12.331.08.jpeg', 'Images/project-02-evtol/packaging/packaging-03.jpeg'),
    ('Images/skill development/design brief section/WhatsApp Image 12026-03-16 at 12.31.08.jpeg', 'Images/project-02-evtol/packaging/packaging-04.jpeg'),
    ('Images/skill development/audi/audi-a3-car-emblem-logo-audi-car-logo-png-brand-image-Photoroom.png', 'Images/project-03-personal/audi/audi-logo.png'),
]

html_count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        html_count += 1
        print(f'  HTML replaced: {old}')
    else:
        print(f'  HTML not found: {old}')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nStep 4: {html_count} path replacements made in index.html')
print('\nAll done!')
