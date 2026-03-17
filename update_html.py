import os

path = r'c:\Users\TomaKuzmic\OneDrive - ROWDEN TECHNOLOGIES LTD\Documents\Lena-Portfolio-main\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

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
    ('Images/skill development/design brief section/\u2014Pngtree\u2014mute icon - no sound_23059135.png', 'Images/project-02-evtol/brand-research/mute-icon.png'),
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

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'  Replaced: {old}  ->  {new}')
    else:
        print(f'  NOT FOUND in HTML: {old}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone. {count} path(s) replaced in index.html.')
