# 图像生成提示词模板 (Prompt Templates)

本文件提供为每幅名画定制的图像生成提示词模板，用于将宠物自然融合到经典画作中。

---

## 通用模板结构

```
[GENERATION PURPOSE]: Create a masterpiece artwork that seamlessly blends a pet with a famous classical painting. The pet MUST be rendered in the painting's style — never photorealistic overlay.

[SCENE DESCRIPTION]: {详细描述画中场景，宠物的位置、姿态，与名画元素的互动}

[PAINTING STYLE]: {画作风格、画派、笔触特征、色彩基调、光源方向}

[PET DESCRIPTION]: Referencing the uploaded pet photo, render the pet with the following EXACT features (do NOT omit any):
- Species & breed: {petType + breed}
- Base fur color: {baseColor, 具体颜色名如 charcoal gray / tawny orange}
- Secondary fur color: {secondaryColor, 如 cream white}
- Pattern type: {patternType, 如 classic tabby / solid / tortoiseshell}
- Pattern distribution: {patternDistribution, 精确到部位, 如 "dark stripes on back and flanks, white 'gloves' on all four paws, white V-shape on chest"}
- Eye color: {eyeColor, 如 yellowish-green}
- Eye shape: {eyeShape, 如 round / almond}
- Nose color: {noseColor, 如 pink}
- Ear shape: {earShape, 如 pointed upright}
- Build: {build, 如 medium-plump}
- Fur length: {furLength, 如 short-haired}
- Fur texture: {furTexture, 如 dense plush}
- Distinctive marks: {distinctiveMarks, 如 "white tail tip / heterochromia / notched left ear" — if none, write "none"}
- Facial expression: {facialExpression, 如 calm enigmatic}

CRITICAL: The pet's fur MUST be rendered with the SAME brushwork technique as the painting ({画家的笔触特征, 如 sfumato / impasto / glazing}). The pet is placed naturally in the scene with matching lighting direction, perspective, and shadow. NO photographic sharpness — the pet must look PAINTED, not pasted.

[KEY ELEMENTS TO PRESERVE]: {必须保留的名画标志性元素列表, 3-5 项}

[QUALITY CONSTRAINTS]: 
- Oil painting texture, museum-quality masterpiece
- Pet fur rendered in the painting's brushwork style (NOT photorealistic)
- Perfect color harmony between pet and painting — no color shift on pet
- Pet lighting matches painting's light source EXACTLY (same direction, same warmth)
- No digital cutout edges — pet fully integrated into the painted scene
- Anatomically correct pet (no extra eyes/limbs, no distorted face)
- All distinctive marks preserved (white gloves, tail tip, etc.)
- Consistent light source direction
- High resolution, fine details
- Style: museum artwork, classical fine art
```

---

## 各名画专用模板

### 1. 《宫娥》Las Meninas 专用

```
[GENERATION PURPOSE]: Museum-quality classical oil painting recreating Diego Velázquez's "Las Meninas" (1656) with a pet replacing the central figure.

[SCENE DESCRIPTION]: The grand interior of the Spanish royal palace studio. A {宠物品种，如：橘色英国短毛猫} sits regally in the EXACT CENTER position where Infanta Margaret Theresa usually stands, dressed in a miniature pale silk gown with floral bodice decorations. On the pet's left and right stand the two ladies-in-waiting (meninas) in period dresses — one in greenish-bronze gown bowing offering a vessel, the other in pale silvery-white gown gently touching the pet. In the background: the large canvas on the left easel with Velázquez's self-portrait holding a brush; the mirror on the back wall reflecting King Philip IV and Queen Mariana; the doorway with a man standing; two other figures and a large dog lying in the right foreground (or replace the dog with another pet).

[PAINTING STYLE]: Spanish Baroque oil painting by Diego Velázquez, 1656. Characteristic loose brushstrokes, atmospheric chiaroscuro lighting from the right-side window, muted warm palette of taupes, greys, wine reds, deep greens, with golden highlights. Spatial depth with layers of figures. Dark ceiling beams and painted canvases on walls.

[PET DESCRIPTION]: {宠物详细描述，如：fluffy orange tabby cat with white paws, round golden eyes, chubby cheeks, soft plush fur}. The pet is positioned naturally, matching the room's cool side-lighting with soft shadows falling to the left. Its fur is rendered with the same painterly, slightly loose brushwork as Velázquez's figures — not photographically sharp, but painterly texture. The pet wears the princess's costume naturally as if born to it.

[KEY ELEMENTS TO PRESERVE]:
1. Velázquez self-portrait at left easel with paintbrush and palette, red cross on chest
2. Back wall mirror reflecting the Spanish royal couple (small but visible)
3. Two meninas flanking central pet figure with correct poses
4. Two figures in right background near doorway
5. Large dog or pet lying in lower right corner
6. Dark wooden beams on ceiling, framed paintings on back walls
7. Background doorway with man in silhouette

[QUALITY CONSTRAINTS]:
- Oil on canvas texture, visible brushstrokes, aged canvas warmth
- Pet lighting matches right-side window source
- Palette: muted warm grays, wine red, moss green, cream, gold
- Seamless integration: NO visible cutout edge around pet
- Correct Renaissance room perspective and scale
- Fine lace details on meninas' collars and cuffs
```

---

### 2. 《两个弗里达》The Two Fridas 专用

```
[GENERATION PURPOSE]: High-fidelity fine art oil painting reimagining Frida Kahlo's "The Two Fridas" (1939) with a pet shared between the two figures.

[SCENE DESCRIPTION]: Stormy dramatic cloud background in grays and deep blues. Two Frida Kahlo figures sit side-by-side on a simple wooden bench, holding hands — the Left Frida in a white lace Tehuana Mexican folk dress with puffy sleeves, the Right Frida in a European-style blue bodice with yellow trim and olive-green skirt with ruffled hem. BETWEEN THEM, in the FOREGROUND CENTER, a large {宠物品种} is lovingly embraced — both Fridas' arms wrap around the pet's body. The Left Frida holds a small pair of surgical scissors with a tiny drip of blood; the Right Frida holds a small locket miniature portrait. Both Fridas have their iconic unibrows and subtle mustache, dark hair in neat updos.

[PAINTING STYLE]: Frida Kahlo's signature naive/surrealist Mexican folk oil painting style, 1939. Flat bold colors, strong outlines, emotionally intense direct gaze. Slightly naive figure proportions. Background tempestuous cloudscape in layered storm grays and dusty blues.

[PET DESCRIPTION]: {宠物详细描述，如：chubby ginger tabby cat, thick plush fur, white chest and paws, large round amber eyes, pink nose}. The pet stands or sits between the two Fridas, arms/bodies of both women wrapped naturally around its torso. The pet faces the viewer with a calm, direct expression. Lighting is flat frontal (consistent with Kahlo's style). Pet fur is rendered with Kahlo's characteristic precise, slightly flat brushwork — not photorealistic, but stylistically consistent with the two Fridas.

[BLOOD VEIN ELEMENTS (CRITICAL)]: Two exposed anatomically-detailed hearts float over each Frida's chest (visible through open cut-outs in their bodices). A single red blood vein arches from the Left Frida's heart across behind the pet's head to the Right Frida's heart. Another red vein loops down from the Left Frida's heart, ending in the surgical scissors she holds, with a small blood drop falling onto her white skirt (which also has scattered tiny embroidered red flowers). The Right Frida's vein connects to her locket pendant. THESE VEINS MUST PASS AROUND THE PET, NOT THROUGH IT — the pet should visually unify the two Fridas.

[KEY ELEMENTS TO PRESERVE]:
1. Both Fridas with iconic unibrows, hair updos
2. Left Frida: white lace Tehuana dress, scissors in hand, scattered red flower embroidery on skirt
3. Right Frida: blue/yellow European dress, locket pendant, olive-green ruffled skirt
4. Two exposed beating hearts (anatomical, vivid red) on each chest
5. Red connecting veins (arcing over pet, not through)
6. Stormy tempestuous gray-blue cloud background
7. Both Fridas holding hands, both arms embracing the pet

[QUALITY CONSTRAINTS]:
- Oil on canvas, Kahlo's precise flat brushwork style
- Pet stylistically matched to painting (not photorealistic insert)
- Vivid red hearts and veins, clean outlines
- Uniform flat front lighting, slight yellowed aged canvas tone
- No digital compositing artifacts
- Emotionally resonant, dignified pet expression
```

---

### 3. 博斯/勃鲁盖尔 恶魔奇幻场景（人间乐园风格）专用

```
[GENERATION PURPOSE]: Epic surreal masterpiece oil painting in the style of Hieronymus Bosch / Pieter Bruegel the Elder, with a pet as the central saint-like figure surrounded by fantastical demons.

[SCENE DESCRIPTION]: Dramatic visionary landscape composition (vertical format). A glorified {宠物品种} is ELEVATED CENTER STAGE, standing or hovering regally, paws posed, with a beatific upward gaze — like a saint in ecstasy or a deity being carried aloft. The pet is surrounded by a swirling throng of at least 8-12 grotesque fantastical demon creatures ALL DIRECTING THEIR ATTENTION TO THE PET (offering things, holding it up, gesturing toward it): a spiky feathered fish-monster with rooster head; a hairy horned bat-winged demon holding up a roasted chicken leg and a silver fish like offerings; a red lobster/demon hybrid with wings; a green frog-legged imp holding a small silver plate of food toward the pet; a red horned demon with fan-like spiky tail gesturing; another demon holding a shallow bowl of brown liquid; other hybrid creatures with human-animal parts, claws, horns, wings. The background shows a panoramic wild mountainous rocky landscape on the left with bare twisted trees, a wide winding river or estuary with a tiny sailing ship below, distant castle/church spires on the horizon under a hazy blue-green gradient sky.

[PAINTING STYLE]: Late 15th/early 16th century Northern Renaissance oil on oak panel in the style of Hieronymus Bosch (The Garden of Earthly Delights) and Pieter Bruegel. Meticulously detailed tiny brushwork, opaque tempera-oil layering, muted but vivid jewel-tone palette of teal, sea-green, ochre, cinnabar red, deep brown. Atmospheric aerial perspective (distant blues/hazes). Slight horror vacui (richly populated space). Glazed luminous colors.

[PET DESCRIPTION]: {宠物详细描述，如：massive chubby orange tabby cat, extremely round fluffy body, bright white front paws and back socks, golden-yellow alert eyes, pink nose, soft plush fur rendered in microscopic detail}. The pet is visually the LARGEST single figure (heroic scale, slightly larger than surrounding demons). It stands with front paws held prayer-like, or one paw resting elegantly on a small tray being offered. Lighting on the pet is DRAMATIC — focused soft holy radiance, catching the tops of its fur like rim lighting, making it the obvious focal point amid the darker demons. Fur is rendered with impossibly fine tiny brushstrokes (Bosch's miniaturist technique). Shadows fall consistently downward-left.

[DEMON CREATURE DETAILS]: 
- Spiky porcupine-finned fish body with rooster/beak head reaching toward pet
- Brown hairy satyr-demon with horns and bat wings, standing behind pet holding aloft a silver fish (airborne) and a roasted golden chicken leg
- Red-skinned demon woman with horns and bat wings, arched body
- Red dragon-demon with wings and long scaly spiky tail curling around
- Green imp with frog legs and feathered peplum skirt, kneeling holding silver plate
- Other gargoyle hybrids: donkey ears, goat legs, bird claws

[KEY ELEMENTS TO PRESERVE]:
1. Panoramic distant landscape (left rocks, river with ship, spires on right)
2. Blue-green gradient hazy sky (lighter at top, darker toward horizon)
3. Bare twisted leafless tree on left rock
4. 8+ distinct Boschian hybrid monsters/demons
5. Various "offerings" (fish, chicken leg, plate, bowl) being presented TO the pet
6. Pet has beatific, upward-looking saintly expression

[QUALITY CONSTRAINTS]:
- Oil on oak panel texture, fine miniaturist brushwork, aged varnish warmth
- Pet lighting is dramatic focal glow, consistent with rest of scene
- Seamless fur integration with painterly environment
- Atmospheric perspective correct (backgrounds bluer/hazier)
- NO photographic pet overlay, fully redrawn in Bosch/Bruegel technique
- Rich with tiny surreal details (demons can hide tiny instruments, fruits, objects)
```

---

### 4. 荷兰胖男孩抱着宠物肖像（范德赫尔斯特风格）专用

```
[GENERATION PURPOSE]: Museum-quality Dutch Golden Age oil portrait of a plump child holding a pet, in the style of Bartholomeus van der Helst, c. 1650s.

[SCENE DESCRIPTION]: Half-length formal portrait against a very dark near-black studio background, lit dramatically from upper left. A rosy-cheeked chubby young boy (about 6 years old) with a serious solemn expression sits facing the viewer, his short wavy auburn hair parted, double chin visible. His arms cradle a large {宠物品种} across his lap/chest. The boy wears: a rich deep wine-red satin velvet doublet slashed with puffings, a wide flat white lace collar (millstone ruff) with delicate scalloped bobbin lace edging, elaborate lace cuffs on both sleeves (right cuff has intricate reticella needlelace with tiny pearl beads embroidered along the edge), draped over his lap a heavy charcoal-gray wool skirt or tabard with an ornate band of black-and-gold Venetian gros-point needlelace running horizontally near the bottom hem. A small golden sash tassel hangs near the pet's paw.

[PAINTING STYLE]: Dutch Golden Age Baroque portrait, c. 1645-1660, manner of Bartholomeus van der Helst / Jacob Adriaensz. Backer. Extremely smooth, glazing oil technique. Strong chiaroscuro from upper left (Rembrandtesque). Hyper-realistic skin texture (rosy cheeks, subtle skin fuzz). Satin fabrics rendered with precise white highlights showing silk sheen. Lace done with microscopic individual thread detail. Dark neutral brown-black studio background, slightly lighter behind the head for silhouette.

[PET DESCRIPTION]: {宠物详细描述，如：adult orange tabby cat with white chin, chest, and "socks" on all four paws, long white whiskers, bright green attentive eyes}. The pet is being held securely across the boy's chest — its front paws dangle relaxed over the boy's left arm, back legs across the boy's right hand. The cat looks DIRECTLY AT the viewer with a slightly grumpy but dignified expression. Lighting on pet follows the same upper-left dramatic key light — top of head and left shoulder are bright, right side falls into soft shadow. Fur is rendered with Dutch Masters precision: individual soft hairs visible, especially around the fluffy white paws. Shadow of the cat falls softly onto the boy's red doublet.

[KEY ELEMENTS TO PRESERVE]:
1. Very dark, near-black neutral studio background (slightly graded warmer behind the head)
2. Rosy chubby child with solemn, serious gaze, double chin
3. Wavy auburn medium-length period hairstyle
4. Wine-red satin velvet doublet with authentic period cut
5. White lace collar + incredibly detailed lace cuffs (especially right cuff with tiny pearls/needlelace)
6. Gray draped skirt/tabard with wide band of intricate black-and-gold lace near hem
7. Correct period anatomy (boy's chubby hand resting on pet)

[QUALITY CONSTRAINTS]:
- Smooth glazed oil technique, no visible brushstrokes on skin
- Absolute lighting consistency (upper left only)
- Pet fur is rendered as carefully as the boy's skin
- Satin fabric sheen highlights are accurate
- Lace is exquisitely detailed (individual holes visible)
- No cutout look — pet shadows fall on clothing, boy's hands press into fur realistically
- Canvas slightly warm/yellowed with age (varnish patina)
```

---

### 5. 埃尔·格列柯 绅士抱宠物肖像专用

```
[GENERATION PURPOSE]: Mannerist Spanish Renaissance oil portrait of a nobleman with a pet, in the style of El Greco, c. 1580s-90s.

[SCENE DESCRIPTION]: Half-length portrait, vertical format, against a warm deep umber brown textured studio background. A severe, gaunt Spanish nobleman in late 16th century dress faces the viewer with a piercing, intense gaze. His face is characteristically EL GRECO-ELONGATED: pale olive skin, high forehead, deeply-set intense eyes (slanted, almost Asian-influenced), long thin nose, dark full beard and mustache neatly trimmed, dark short receding hair. He wears a completely plain black velvet period doublet (high neck, no ornament) that absorbs light — but at his neck is a SPECTACULAR, voluminous white linen cartwheel ruff (millstone ruff) of lace with intricate scalloped openwork reticella needlelace edge, standing stiffly wired open. His unusually long, slender pale fingers (typical El Greco mannerist elongation) rest on the chest/body of a large {宠物品种} that he holds across his torso — one hand on the pet's chest, the other supporting its belly. His fingers also have an identical matching miniature lace ruff (cuff) around the wrist. At his left hip, the ornate gilded brass hilt of a rapier sword peeks out (showing cup-hilt, knuckle-bow, intricately pierced).

[PAINTING STYLE]: El Greco (Domenikos Theotokopoulos) Byzantine-influenced Spanish Mannerism, c. 1580-1600. Characteristic features: greatly elongated face/hands/fingers; cool pallid olive skin tones with cool gray-blue shadows; highly expressive intense spiritual gaze; rich deep umber studio background with subtle painterly texture; white lace rendered with dazzling tiny highlights against the black costume; loose, visible, almost flickering brushstrokes on the background and velvet but smoother glazing on the face. Slightly distorted, ethereal proportions.

[PET DESCRIPTION]: {宠物详细描述，如：robust orange tabby cat with white chin, chest, and all four white paws, fluffy whiskers, enormous round copper-colored eyes}. The pet lies across the nobleman's torso at a slight angle, looking alertly and directly at the viewer with a slightly stunned/wide-eyed expression. Its body stretches diagonally. The pet is rendered in El Greco's stylized manner — its fur has the same cool-toned shadows and warm highlights as the man's skin. The lighting on the pet comes from the upper front-left: top of the pet's head and white paws catch the light brightly, matching the same light source that gilds the ruff's lace edges and the man's forehead. The pet's fur is slightly "painterly" (smoother than background but with visible El Greco characteristic flickering stroke quality).

[KEY ELEMENTS TO PRESERVE]:
1. Elongated gaunt face with intense eyes, full dark beard/mustache — unmistakably El Greco type
2. Huge, intricate white reticella cartwheel Ruff around the man's neck
3. Matching miniature lace Ruff (cuff) around the man's wrist (visible on the hand that holds pet's chest)
4. Plain black velvet doublet (high neck) — no decoration
5. Ornate pierced gilded rapier hilt at lower left (cup hilt, quillons, etc.)
6. Elongated slender fingers (mannerist exaggeration) resting on the pet
7. Warm deep umber textured painterly background

[QUALITY CONSTRAINTS]:
- Clear El Greco stylistic mannerism (elongation, pallor, intense gaze, flickering strokes)
- Pet rendered IN STYLE, NOT photorealistic overlay
- Lighting strictly front-left, highlights on lace, forehead, pet paws
- Lace on ruff and wrist cuff rendered with same intricate detail level
- Cool shadows on skin and pet (slate-blue undertones)
- No sign of digital compositing; pet and figure share a single pictorial space
```

---

### 6. 《戴珍珠耳环的少女》专用

```
[GENERATION PURPOSE]: Tronie-style Dutch Golden Age masterpiece — a pet with the pearl earring and blue turban, in the style of Vermeer.

[SCENE DESCRIPTION]: Close-up bust portrait (tronie) against a deep velvety almost-black studio background. A {宠物品种} is turned in a THREE-QUARTER VIEW, glancing back over its shoulder directly at the viewer with an enigmatic expression. The pet wears: a voluminous draped turban/headwrap of rich deep ULTRAMARINE BLUE fabric (Vermeer's signature costly lapis lazuli pigment) with a soft yellow-gold silk scarf hanging down at the back. Dangling from the pet's ear region is a SINGLE, enormous, luminous tear-drop-shaped NATURAL PEARL, catching the light with a distinct specular highlight. The pet's skin/fur is illuminated by a soft cool window light from the left.

[PAINTING STYLE]: Johannes Vermeer, c. 1665, Dutch Delft School. Luminous glazing technique. Characteristic "pearl-like" smooth skin/fur rendering. Exquisitely subtle soft diffused window light. Atmospheric muted palette: deep ultramarine, yellow ochre, warm ivory flesh tones, deep black-brown background. Subtle soft edges and lost-and-found outlines.

[PET DESCRIPTION]: {宠物详细描述}. Three-quarter back turned, head rotated back to look directly at viewer. Soft cool left-side lighting. Fur/skin rendered with Vermeer's characteristic luminous glazes — smooth transitions, no harsh lines. The pearl earring is the key focal accent: perfect translucent luster, one distinct bright white specular highlight, subtle reflected ambient light. Blue turban fabric has a visible fabric weave texture and soft folds.

[KEY ELEMENTS TO PRESERVE]:
1. Iconic deep ultramarine blue turban with yellow hanging scarf
2. Single enormous luminous pearl drop earring (with highlight!)
3. Three-quarter pose, head turned back, direct enigmatic gaze
4. Deep near-black background (Vermeer's characteristic dark studio)
5. Soft, diffused, cool window light from the left

[QUALITY CONSTRAINTS]:
- Luminous oil glaze technique, not photographic
- Pearl catchlight is correct (key feature)
- Turban blue is saturated deep ultramarine (lapis lazuli pigment)
- Pet features soft-edged Vermeer quality, not sharp
- No cutout edges, fully integrated lighting
```

---

## 输出格式规范

生成图像后，必须按以下格式展示名画信息：

```markdown
## 🎨 作品信息

| 项目 | 内容 |
|------|------|
| **画作名称** | {中英文名称} |
| **原文名称** | {原文名称，如 Las Meninas / The Two Fridas} |
| **作者** | {艺术家姓名，生卒年} |
| **创作时间** | {精确年份或时期} |
| **艺术流派** | {画派/风格} |
| **现藏地点** | {博物馆及城市} |
| **原作尺寸** | {高×宽 cm} |

---

### ✨ 创作故事
{3-5句话介绍这幅画的背景、创作故事或艺术价值，让用户了解作品的历史意义}

### 🖌️ 融合说明
{描述宠物在画中的角色位置、替换了原作中的哪个元素，以及设计此融合的巧思}
```
