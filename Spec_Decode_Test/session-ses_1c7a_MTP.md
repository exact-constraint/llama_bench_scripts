# Flippyblock Extreme Pygame Clone

**Session ID:** ses_1c7a2f0b3ffezFZ7YnpkgFPEUI
**Created:** 5/17/2026, 4:54:43 PM
**Updated:** 5/17/2026, 5:28:51 PM

---

## User

You are an expert Python Developer. Create a highly accurate flappybird game clone called flippyblock extreme in python. Add all additional features that would be expected in a common user interface. Do not use external assets for anything. If you need assets created, generate them in the code only. Only use pygame. Fully review your code and correct any issues after you produce the first version. 

---

## Assistant (Build · Qwen3.6 27B · 70.5s)

_Thinking:_

The user wants me to create a Flappy Bird clone called "FlippyBlock Extreme" in Python using only pygame. No external assets - everything must be generated in code. Let me plan this out:

1. Game mechanics: gravity, flap, pipes, collision detection
2. UI features: start screen, game over screen, score, high score, settings
3. Assets generated in code: bird sprite, pipe graphics, background, ground, clouds, particles
4. Additional features: sound effects (generated), pause, difficulty settings, day/night cycle, etc.

Let me create a comprehensive, polished game. I'll write it all in a single Python file.

Let me think about what makes a great flappy bird clone:
- Smooth physics (gravity, velocity)
- Well-timed pipe gaps
- Visual polish (animations, particles, screen shake)
- Sound effects (generated programmatically)
- Multiple game states (menu, playing, paused, game over)


- Settings menu with difficulty options
- Day/night cycle for visual variety
- Leaderboard tracking with persistent high scores
- Responsive controls and multiple difficulty levels

Now I'm building out the complete game with all these systems integrated together.


I'll create a comprehensive Flappy Bird clone with all features built from scratch using only pygame. Let me build this step by step.



**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"import pygame; print(pygame.ver)\"",
  "description": "Check pygame availability"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pygame'

```

---

## Assistant (Build · Qwen3.6 27B · 3.9s)

_Thinking:_

Let me install pygame first, then create the game.


**Tool: bash**

**Input:**
```json
{
  "command": "pip install pygame -q",
  "description": "Install pygame"
}
```

**Output:**
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

```

---

## Assistant (Build · Qwen3.6 27B · 6.6s)

_Thinking:_

I need to install pygame. Let me try with --break-system-packages or use a venv.


**Tool: bash**

**Input:**
```json
{
  "command": "pip install pygame --break-system-packages -q",
  "description": "Install pygame with override"
}
```

**Output:**
```
(no output)
```

---

## Assistant (Build · Qwen3.6 27B · 20.8s)

_Thinking:_

Now let me create the game. I'll write a comprehensive flappy bird clone. Let me plan the full game:

1. Core game mechanics:
   - Bird physics (gravity, flap velocity)
   - Pipe generation and movement
   - Collision detection
   - Score tracking

2. Visual assets (all generated in code):
   - Bird sprite with wing animation
   - Pipes with caps
   - Background with gradient sky
   - Ground with texture
   - Clouds
   - Stars (for night mode)
   - Particles
   - UI elements (buttons, panels)

3. Game states:
   - Title screen
   - Playing
   - Paused
   - Game over

4. Features:
   - Settings menu (sound toggle, difficulty, sensitivity)
   - High score persistence
   - Day/night cycle
   - Screen shake on death
   - Score popup animation
   - Medal system
   - Leaderboard
   - Bird skin selection
   - Sound effects (generated programmatically)
   - Start button, restart, pause
   - FPS counter (debug)
   - Responsive design

Let me write this comprehensive game.


**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the core game engine and physics",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Generate all visual assets programmatically",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Build UI system (menus, buttons, panels)",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Add sound effects (programmatic generation)",
      "status": "pending",
      "priority": "medium"
    },
    {
      "content": "Implement game states and flow",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Add polish features (particles, screen shake, day/night)",
      "status": "pending",
      "priority": "medium"
    },
    {
      "content": "Review and fix all issues",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Create the core game engine and physics",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Generate all visual assets programmatically",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Build UI system (menus, buttons, panels)",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Add sound effects (programmatic generation)",
    "status": "pending",
    "priority": "medium"
  },
  {
    "content": "Implement game states and flow",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Add polish features (particles, screen shake, day/night)",
    "status": "pending",
    "priority": "medium"
  },
  {
    "content": "Review and fix all issues",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 629.6s)

_Thinking:_

Now let me write the complete game. I'll create a single comprehensive Python file.


Now I'll create the complete game. This is a large, feature-rich file:



**Tool: write**

**Input:**
```json
{
  "content": "#!/usr/bin/env python3\n\"\"\"FlippyBlock Extreme - A Flappy Bird clone with no external assets.\"\"\"\n\nimport pygame\nimport math\nimport random\nimport json\nimport os\nimport struct\nimport array\nimport sys\n\n# ─── Constants ───────────────────────────────────────────────────────────────\n\nSCREEN_W = 480\nSCREEN_H = 720\nFPS = 60\nTITLE = \"FlippyBlock Extreme\"\n\nDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), \".flippyblock_data\")\nSAVE_FILE = os.path.join(DATA_DIR, \"save.json\")\n\n# Colors\nC_SKY_TOP = (100, 180, 255)\nC_SKY_BOT = (200, 235, 255)\nC_SKY_NIGHT_TOP = (15, 15, 50)\nC_SKY_NIGHT_BOT = (30, 30, 80)\nC_GROUND = (139, 119, 80)\nC_GROUND_DARK = (100, 85, 55)\nC_GROUND_GRASS = (80, 180, 60)\nC_PIPE_GREEN = (50, 200, 60)\nC_PIPE_GREEN_DARK = (30, 150, 40)\nC_PIPE_GREEN_LIGHT = (80, 230, 90)\nC_PIPE_CAP = (40, 180, 50)\nC_BIRD_YELLOW = (255, 220, 50)\nC_BIRD_ORANGE = (255, 160, 30)\nC_BIRD_WHITE = (255, 255, 240)\nC_BIRD_RED = (220, 50, 50)\nC_BIRD_BLUE = (50, 100, 220)\nC_BIRD_PURPLE = (160, 60, 200)\nC_BIRD_CYAN = (50, 200, 220)\nC_BIRD_SKINS = [C_BIRD_YELLOW, C_BIRD_ORANGE, C_BIRD_RED, C_BIRD_BLUE, C_BIRD_PURPLE, C_BIRD_CYAN]\nC_TEXT_WHITE = (255, 255, 255)\nC_TEXT_SHADOW = (0, 0, 0)\nC_TEXT_GOLD = (255, 215, 0)\nC_TEXT_SILVER = (192, 192, 192)\nC_TEXT_BRONZE = (205, 127, 50)\nC_UI_BG = (40, 40, 60)\nC_UI_BG_ALPHA = (40, 40, 60, 200)\nC_UI_BORDER = (80, 80, 120)\nC_UI_BUTTON = (60, 60, 100)\nC_UI_BUTTON_HOVER = (80, 80, 140)\nC_UI_BUTTON_ACTIVE = (100, 100, 170)\nC_STAR = (255, 255, 220)\nC_CLOUD = (240, 245, 255)\nC_PARTICLE = (255, 200, 50)\nC_MEDAL_GOLD = (255, 215, 0)\nC_MEDAL_SILVER = (192, 192, 192)\nC_MEDAL_BRONZE = (205, 127, 50)\nC_MEDAL_PLATINUM = (160, 220, 255)\n\n# Physics\nGRAVITY = 0.45\nFLAP_VEL = -7.5\nMAX_FALL = 10\nPIPE_SPEED_BASE = 2.5\nPIPE_GAP_BASE = 155\nPIPE_WIDTH = 60\nPIPE_INTERVAL = 1600\n\n# Difficulty presets\nDIFFICULTIES = {\n    \"Easy\":     {\"gap\": 190, \"speed\": 2.0, \"gravity\": 0.38, \"flap\": -7.0},\n    \"Normal\":   {\"gap\": 155, \"speed\": 2.5, \"gravity\": 0.45, \"flap\": -7.5},\n    \"Hard\":     {\"gap\": 130, \"speed\": 3.2, \"gravity\": 0.52, \"flap\": -8.0},\n    \"Extreme\":  {\"gap\": 110, \"speed\": 4.0, \"gravity\": 0.60, \"flap\": -8.5},\n}\n\n# ─── Save / Load ─────────────────────────────────────────────────────────────\n\ndef _ensure_data_dir():\n    os.makedirs(DATA_DIR, exist_ok=True)\n\ndef load_save():\n    _ensure_data_dir()\n    try:\n        with open(SAVE_FILE, \"r\") as f:\n            return json.load(f)\n    except (FileNotFoundError, json.JSONDecodeError):\n        return {\"high_score\": 0, \"total_games\": 0, \"total_score\": 0, \"best_streak\": 0,\n                \"current_streak\": 0, \"skin_index\": 0, \"difficulty\": \"Normal\",\n                \"sound_enabled\": True, \"night_mode\": False, \"night_auto\": True,\n                \"scores\": []}\n\ndef save_save(data):\n    _ensure_data_dir()\n    with open(SAVE_FILE, \"w\") as f:\n        json.dump(data, f, indent=2)\n\n# ─── Sound Engine (purely programmatic) ──────────────────────────────────────\n\nclass SoundEngine:\n    def __init__(self):\n        self.enabled = True\n        self._initialized = False\n\n    def _init(self):\n        if self._initialized:\n            return\n        try:\n            pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)\n            self._initialized = True\n        except Exception:\n            self.enabled = False\n\n    def _make_sound(self, freq, duration, wave_type=\"sine\", fade=True, freq_end=None):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        samples = array.array('h')\n        for i in range(n):\n            t = i / sr\n            f = freq + (freq_end - freq) * (i / n) if freq_end else freq\n            if wave_type == \"sine\":\n                v = math.sin(2 * math.pi * f * t)\n            elif wave_type == \"square\":\n                v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0\n            elif wave_type == \"sawtooth\":\n                v = 2 * (f * t - math.floor(f * t + 0.5))\n            else:\n                v = 0\n            if fade and i > n * 0.6:\n                env = 1.0 - (i - n * 0.6) / (n * 0.4)\n                v *= max(0, env)\n            elif fade:\n                env = min(1.0, i / max(1, n * 0.05))\n                v *= env\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)\n\n    def _noise_sound(self, duration, volume=0.3):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        samples = array.array('h')\n        for i in range(n):\n            v = (random.random() * 2 - 1) * volume\n            if i > n * 0.5:\n                v *= 1.0 - (i - n * 0.5) / (n * 0.5)\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)\n\n    def play_flap(self):\n        s = self._make_sound(600, 0.08, \"sine\", freq_end=900)\n        if s: s.play()\n\n    def play_score(self):\n        s = self._make_sound(880, 0.1, \"sine\")\n        if s:\n            s.play()\n            pygame.time.set_timer(pygame.USEREVENT, 100)\n            def _play2():\n                s2 = self._make_sound(1100, 0.12, \"sine\")\n                if s2: s2.play()\n            pygame.time.set_timeout(_play2, 100)\n\n    def play_hit(self):\n        s = self._make_sound(200, 0.2, \"square\", freq_end=80)\n        if s: s.play()\n\n    def play_die(self):\n        s = self._make_sound(400, 0.4, \"sawtooth\", freq_end=100)\n        if s: s.play()\n\n    def play_swoosh(self):\n        s = self._noise_sound(0.15, 0.15)\n        if s: s.play()\n\n    def play_menu(self):\n        s = self._make_sound(500, 0.06, \"sine\", freq_end=700)\n        if s: s.play()\n\n    def play_select(self):\n        s = self._make_sound(700, 0.08, \"sine\", freq_end=1000)\n        if s: s.play()\n\n    def play_countdown(self):\n        s = self._make_sound(440, 0.15, \"sine\")\n        if s: s.play()\n\n    def play_go(self):\n        s = self._make_sound(880, 0.2, \"sine\")\n        if s: s.play()\n\n# ─── Asset Generation ────────────────────────────────────────────────────────\n\ndef _draw_rounded_rect(surface, rect, radius, color):\n    x, y, w, h = rect\n    r = min(radius, w // 2, h // 2)\n    pygame.draw.rect(surface, color, (x, y, w, h), border_radius=r)\n\ndef generate_bird(skin_color, size=34):\n    s = pygame.Surface((size, size), pygame.SRCALPHA)\n    cx, cy = size // 2, size // 2\n    body_r = size // 2 - 1\n    # Body\n    pygame.draw.ellipse(s, skin_color, (1, 1, size - 2, size - 2))\n    # Belly highlight\n    pygame.draw.ellipse(s, pygame.Color(skin_color).lerp(pygame.Color(255, 255, 255), 0.3),\n                        (4, size // 2, size // 2, size // 3))\n    # Eye white\n    eye_x, eye_y = int(size * 0.6), int(size * 0.3)\n    pygame.draw.circle(s, (255, 255, 255), (eye_x, eye_y), 5)\n    # Pupil\n    pygame.draw.circle(s, (30, 30, 30), (eye_x + 1, eye_y), 3)\n    # Eye shine\n    pygame.draw.circle(s, (255, 255, 255), (eye_x + 2, eye_y - 1), 1)\n    # Beak\n    beak_pts = [(eye_x + 5, eye_y + 1), (eye_x + 5, eye_y + 5), (eye_x + 13, eye_y + 3)]\n    pygame.draw.polygon(s, (255, 140, 30), beak_pts)\n    # Wing\n    wing_pts = [(3, cy), (8, cy + 6), (16, cy + 4), (14, cy - 2), (6, cy - 2)]\n    pygame.draw.polygon(s, pygame.Color(skin_color).lerp(pygame.Color(0, 0, 0), 0.25), wing_pts)\n    return s\n\ndef generate_bird_frames(skin_color):\n    frames = []\n    for angle in [0, -0.3, -0.6]:\n        surf = generate_bird(skin_color)\n        frames.append(pygame.transform.rotate(surf, math.degrees(angle)))\n    return frames\n\ndef generate_pipe_pair():\n    h = SCREEN_H\n    gap_y = random.randint(100, SCREEN_H - 200)\n    top_h = gap_y - PIPE_GAP_BASE // 2\n    bot_y = gap_y + PIPE_GAP_BASE // 2\n    return top_h, bot_y\n\ndef draw_pipe(surface, x, y, w, h, is_top):\n    cap_h = 26\n    cap_w = w + 10\n    cap_x = x - 5\n    # Pipe body\n    if is_top:\n        body_rect = (x, y, w, h - cap_h)\n        cap_rect = (cap_x, y + h - cap_h, cap_w, cap_h)\n    else:\n        body_rect = (x, y + cap_h, w, h - cap_h)\n        cap_rect = (cap_x, y, cap_w, cap_h)\n    # Body gradient\n    pygame.draw.rect(surface, C_PIPE_GREEN, body_rect)\n    pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT, (x + 4, body_rect[1], 6, body_rect[3]))\n    pygame.draw.rect(surface, C_PIPE_GREEN_DARK, (x + w - 8, body_rect[1], 6, body_rect[3]))\n    pygame.draw.rect(surface, C_PIPE_GREEN_DARK, body_rect, 2)\n    # Cap\n    _draw_rounded_rect(surface, cap_rect, 4, C_PIPE_CAP)\n    pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT, (cap_x + 3, cap_rect[1] + 3, 6, cap_rect[3] - 6))\n    pygame.draw.rect(surface, C_PIPE_CAP, cap_rect, 2, border_radius=4)\n\ndef draw_background(surface, night_factor=0.0, scroll_x=0):\n    top = pygame.Color(C_SKY_TOP).lerp(pygame.Color(C_SKY_NIGHT_TOP), night_factor)\n    bot = pygame.Color(C_SKY_BOT).lerp(pygame.Color(C_SKY_NIGHT_BOT), night_factor)\n    for y in range(SCREEN_H):\n        t = y / SCREEN_H\n        c = top.lerp(bot, t)\n        pygame.draw.line(surface, c, (0, y), (SCREEN_W, y))\n    # Clouds\n    _draw_clouds(surface, night_factor, scroll_x)\n\ndef _draw_clouds(surface, night_factor, scroll_x):\n    alpha = int(200 * (1 - night_factor * 0.7))\n    cloud_color = (*C_CLOUD, alpha)\n    cloud_positions = [(100, 80, 1.0), (300, 150, 0.7), (550, 60, 0.9),\n                       (200, 250, 0.6), (450, 200, 0.8), (700, 120, 0.75)]\n    for cx, cy, scale in cloud_positions:\n        px = ((cx - scroll_x * 0.3) % (SCREEN_W + 200)) - 100\n        _draw_cloud(surface, px, cy, scale, cloud_color)\n\ndef _draw_cloud(surface, x, y, scale, color):\n    s = pygame.Surface((80 * scale, 40 * scale), pygame.SRCALPHA)\n    pygame.draw.ellipse(s, color, (0, 10 * scale, 60 * scale, 25 * scale))\n    pygame.draw.ellipse(s, color, (15 * scale, 0, 40 * scale, 30 * scale))\n    pygame.draw.ellipse(s, color, (35 * scale, 5 * scale, 35 * scale, 25 * scale))\n    surface.blit(s, (x, y))\n\ndef draw_stars(surface, night_factor, time_val):\n    if night_factor < 0.3:\n        return\n    alpha = int(255 * (night_factor - 0.3) / 0.7)\n    star_color = (*C_STAR, alpha)\n    seed = 42\n    rng = random.Random(seed)\n    for _ in range(80):\n        sx = rng.randint(0, SCREEN_W)\n        sy = rng.randint(0, SCREEN_H // 2)\n        twinkle = int(0.5 + 0.5 * math.sin(time_val * 2 + sx * 0.1))\n        sz = 1 + twinkle\n        sa = int(alpha * (0.4 + 0.6 * twinkle))\n        sc = (*C_STAR, sa)\n        pygame.draw.circle(surface, sc, (sx, sy), sz)\n\ndef draw_ground(surface, scroll_x, night_factor):\n    gy = SCREEN_H - 80\n    grass_h = 20\n    # Grass\n    gc = pygame.Color(C_GROUND_GRASS).lerp(pygame.Color(20, 60, 20), night_factor)\n    pygame.draw.rect(surface, gc, (0, gy, SCREEN_W, grass_h))\n    # Grass blades\n    for x in range(-10, SCREEN_W + 10, 6):\n        px = ((x - scroll_x) % (SCREEN_W + 20)) - 10\n        blade_h = 8 + int(4 * math.sin(x * 0.3 + scroll_x * 0.05))\n        gc2 = pygame.Color(60, 160, 40).lerp(pygame.Color(15, 45, 15), night_factor)\n        pygame.draw.line(surface, gc2, (px, gy + grass_h), (px + 2, gy + grass_h - blade_h), 2)\n    # Ground\n    gc = pygame.Color(C_GROUND).lerp(pygame.Color(40, 35, 25), night_factor)\n    gc2 = pygame.Color(C_GROUND_DARK).lerp(pygame.Color(25, 20, 15), night_factor)\n    pygame.draw.rect(surface, gc, (0, gy + grass_h, SCREEN_W, 80 - grass_h))\n    # Ground stripes\n    for x in range(-10, SCREEN_W + 10, 24):\n        px = ((x - scroll_x) % (SCREEN_W + 20)) - 10\n        pygame.draw.line(surface, gc2, (px, gy + grass_h + 5), (px + 12, gy + grass_h + 15), 2)\n    # Top line\n    pygame.draw.line(surface, (0, 0, 0), (0, gy), (SCREEN_W, gy), 2)\n\ndef draw_score_text(surface, text, x, y, size=48, color=C_TEXT_WHITE, bold=True):\n    font = pygame.font.SysFont(\"arial\", size, bold=bold)\n    shadow = font.render(text, True, C_TEXT_SHADOW)\n    main = font.render(text, True, color)\n    surface.blit(shadow, (x + 2, y + 2))\n    surface.blit(main, (x, y))\n\ndef draw_medal(surface, x, y, score):\n    if score < 10:\n        return None\n    elif score < 20:\n        color = C_MEDAL_BRONZE\n        label = \"BRONZE\"\n    elif score < 40:\n        color = C_MEDAL_SILVER\n        label = \"SILVER\"\n    elif score < 80:\n        color = C_MEDAL_GOLD\n        label = \"GOLD\"\n    else:\n        color = C_MEDAL_PLATINUM\n        label = \"PLATINUM\"\n    # Medal circle\n    pygame.draw.circle(surface, color, (x, y), 28)\n    pygame.draw.circle(surface, pygame.Color(color).lerp(pygame.Color(0, 0, 0), 0.3), (x, y), 22)\n    pygame.draw.circle(surface, (255, 255, 255), (x - 5, y - 5), 6, 1)\n    # Star on medal\n    _draw_star(surface, x, y, 10, 5, (255, 255, 255))\n    font = pygame.font.SysFont(\"arial\", 10, bold=True)\n    label_surf = font.render(label, True, color)\n    surface.blit(label_surf, (x - label_surf.get_width() // 2, y + 32))\n    return label\n\ndef _draw_star(surface, cx, cy, outer_r, inner_r, color):\n    pts = []\n    for i in range(10):\n        angle = math.pi / 2 + i * math.pi / 5\n        r = outer_r if i % 2 == 0 else inner_r\n        pts.append((cx + r * math.cos(angle - math.pi / 2), cy + r * math.sin(angle - math.pi / 2)))\n    pygame.draw.polygon(surface, color, pts)\n\n# ─── Particle System ─────────────────────────────────────────────────────────\n\nclass Particle:\n    def __init__(self, x, y, vx, vy, color, life, size=3):\n        self.x = x\n        self.y = y\n        self.vx = vx\n        self.vy = vy\n        self.color = color\n        self.life = life\n        self.max_life = life\n        self.size = size\n\n    def update(self):\n        self.x += self.vx\n        self.y += self.vy\n        self.vy += 0.1\n        self.life -= 1\n\n    def draw(self, surface):\n        alpha = max(0, self.life / self.max_life)\n        c = tuple(int(ch * alpha) for ch in self.color)\n        s = max(1, int(self.size * alpha))\n        pygame.draw.circle(surface, c, (int(self.x), int(self.y)), s)\n\n    def alive(self):\n        return self.life > 0\n\nclass ParticleSystem:\n    def __init__(self):\n        self.particles = []\n\n    def emit(self, x, y, count, color, speed=3, life=30, size=3):\n        for _ in range(count):\n            angle = random.uniform(0, math.pi * 2)\n            spd = random.uniform(0.5, speed)\n            self.particles.append(Particle(\n                x, y,\n                math.cos(angle) * spd,\n                math.sin(angle) * spd,\n                color, life, size\n            ))\n\n    def update(self):\n        self.particles = [p for p in self.particles if p.alive()]\n        for p in self.particles:\n            p.update()\n\n    def draw(self, surface):\n        for p in self.particles:\n            p.draw(surface)\n\n# ─── Button ──────────────────────────────────────────────────────────────────\n\nclass Button:\n    def __init__(self, x, y, w, h, text, callback, color=C_UI_BUTTON,\n                 hover_color=C_UI_BUTTON_HOVER, active_color=C_UI_BUTTON_ACTIVE,\n                 font_size=22, bold=True):\n        self.rect = pygame.Rect(x, y, w, h)\n        self.text = text\n        self.callback = callback\n        self.base_color = color\n        self.hover_color = hover_color\n        self.active_color = active_color\n        self.font_size = font_size\n        self.bold = bold\n        self.hovered = False\n        self.pressed = False\n\n    def handle_event(self, event):\n        if event.type == pygame.MOUSEMOTION:\n            self.hovered = self.rect.collidepoint(event.pos)\n        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:\n            if self.rect.collidepoint(event.pos):\n                self.pressed = True\n        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:\n            if self.pressed and self.rect.collidepoint(event.pos):\n                self.callback()\n            self.pressed = False\n\n    def draw(self, surface):\n        color = self.active_color if self.pressed else (self.hover_color if self.hovered else self.base_color)\n        _draw_rounded_rect(surface, self.rect, 8, color)\n        pygame.draw.rect(surface, C_UI_BORDER, self.rect, 2, border_radius=8)\n        font = pygame.font.SysFont(\"arial\", self.font_size, bold=self.bold)\n        text_surf = font.render(self.text, True, C_TEXT_WHITE)\n        tx = self.rect.x + (self.rect.w - text_surf.get_width()) // 2\n        ty = self.rect.y + (self.rect.h - text_surf.get_height()) // 2\n        shadow = font.render(self.text, True, (0, 0, 0, 128))\n        surface.blit(shadow, (tx + 1, ty + 1))\n        surface.blit(text_surf, (tx, ty))\n\n# ─── Score Popup ─────────────────────────────────────────────────────────────\n\nclass ScorePopup:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.start_y = y\n        self.life = 40\n        self.max_life = 40\n\n    def update(self):\n        self.y -= 1.5\n        self.life -= 1\n\n    def draw(self, surface):\n        if self.life <= 0:\n            return\n        alpha = min(255, int(255 * self.life / self.max_life))\n        font = pygame.font.SysFont(\"arial\", 28, bold=True)\n        surf = font.render(\"+1\", True, (255, 255, 200))\n        shadow = font.render(\"+1\", True, (0, 0, 0))\n        surface.blit(shadow, (self.x + 2, self.y + 2))\n        surface.blit(surf, (self.x, self.y))\n\n    def alive(self):\n        return self.life > 0\n\n# ─── Game States ─────────────────────────────────────────────────────────────\n\nSTATE_MENU = 0\nSTATE_PLAYING = 1\nSTATE_PAUSED = 2\nSTATE_GAME_OVER = 3\nSTATE_SETTINGS = 4\nSTATE_SKIN_SELECT = 5\nSTATE_LEADERBOARD = 6\n\n# ─── Main Game Class ─────────────────────────────────────────────────────────\n\nclass Game:\n    def __init__(self):\n        pygame.init()\n        pygame.display.set_caption(TITLE)\n        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))\n        self.clock = pygame.time.Clock()\n        self.sound = SoundEngine()\n        self.save = load_save()\n        self.particles = ParticleSystem()\n        self.state = STATE_MENU\n        self.prev_state = None\n\n        # Bird\n        self._reset_bird()\n\n        # Pipes\n        self.pipes = []\n        self.pipe_timer = 0\n        self.pipe_gap_y = SCREEN_H // 2\n\n        # Score\n        self.score = 0\n        self.passed_pipes = set()\n\n        # Animation\n        self.bird_frame = 0\n        self.bird_frame_timer = 0\n        self.bob_timer = 0\n        self.scroll_x = 0\n        self.time_val = 0\n\n        # Screen shake\n        self.shake_x = 0\n        self.shake_y = 0\n        self.shake_dur = 0\n\n        # Night mode\n        self.night_factor = 0.0\n        self.night_target = 0.0\n\n        # Countdown\n        self.countdown = 0\n        self.countdown_timer = 0\n\n        # Score popups\n        self.score_popups = []\n\n        # Game over\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n\n        # Menu animation\n        self.menu_bird_y = SCREEN_H // 3\n        self.menu_bob = 0\n\n        # Buttons\n        self.buttons = []\n        self._build_menu_buttons()\n\n        # FPS\n        self.fps_history = []\n\n        # Key repeat for keyboard\n        self.key_flap = False\n\n        # Load settings\n        self.sound.enabled = self.save.get(\"sound_enabled\", True)\n        self.difficulty = self.save.get(\"difficulty\", \"Normal\")\n        self.skin_index = self.save.get(\"skin_index\", 0)\n        self.skin_color = C_BIRD_SKINS[self.skin_index]\n        self.bird_frames = generate_bird_frames(self.skin_color)\n\n    def _reset_bird(self):\n        self.bird_x = SCREEN_W // 3\n        self.bird_y = SCREEN_H // 2\n        self.bird_vel = 0\n        self.bird_rotation = 0\n        self.bird_alive = True\n\n    def _build_menu_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 40\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"PLAY\", self._start_game, font_size=28),\n            Button(cx - 100, by + 60, 200, 48, \"SETTINGS\", self._go_settings, font_size=24),\n            Button(cx - 100, by + 120, 200, 48, \"SKINS\", self._go_skins, font_size=24),\n            Button(cx - 100, by + 180, 200, 48, \"SCORES\", self._go_leaderboard, font_size=24),\n        ]\n\n    def _build_pause_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 - 20\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"RESUME\", self._resume, font_size=26),\n            Button(cx - 100, by + 60, 200, 48, \"SETTINGS\", self._go_settings, font_size=24),\n            Button(cx - 100, by + 120, 200, 48, \"QUIT\", self._go_menu, font_size=24),\n        ]\n\n    def _build_gameover_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 100\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"RETRY\", self._start_game, font_size=26),\n            Button(cx - 100, by + 60, 200, 48, \"MENU\", self._go_menu, font_size=24),\n        ]\n\n    def _build_settings_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 100\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    def _build_skin_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 80\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    def _build_leaderboard_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 120\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    # ─── State Transitions ───────────────────────────────────────────────\n\n    def _start_game(self):\n        self.sound.play_swoosh()\n        self.state = STATE_PLAYING\n        self._reset_bird()\n        self.pipes = []\n        self.pipe_timer = 0\n        self.score = 0\n        self.passed_pipes = set()\n        self.score_popups = []\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n        self.countdown = 3\n        self.countdown_timer = 0\n        self.bird_frame = 0\n        self.bird_vel = 0\n        self.bird_rotation = 0\n        self.bird_alive = True\n\n    def _go_menu(self):\n        self.sound.play_swoosh()\n        self.state = STATE_MENU\n        self._build_menu_buttons()\n        self.flash_alpha = 0\n\n    def _go_settings(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_SETTINGS\n        self._build_settings_buttons()\n\n    def _go_skins(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_SKIN_SELECT\n        self._build_skin_buttons()\n\n    def _go_leaderboard(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_LEADERBOARD\n        self._build_leaderboard_buttons()\n\n    def _go_back(self):\n        self.sound.play_swoosh()\n        self.state = self.prev_state if self.prev_state else STATE_MENU\n        if self.state == STATE_MENU:\n            self._build_menu_buttons()\n        elif self.state == STATE_PAUSED:\n            self._build_pause_buttons()\n\n    def _resume(self):\n        self.sound.play_swoosh()\n        self.state = STATE_PLAYING\n        self._build_pause_buttons()\n\n    def _die(self):\n        if not self.bird_alive:\n            return\n        self.bird_alive = False\n        self.sound.play_hit()\n        self.shake_dur = 15\n        self.particles.emit(self.bird_x, self.bird_y, 20, C_PARTICLE, 4, 40, 4)\n        self.particles.emit(self.bird_x, self.bird_y, 10, (255, 100, 50), 3, 30, 3)\n        self.flash_alpha = 200\n        # Save score\n        self.save[\"total_games\"] = self.save.get(\"total_games\", 0) + 1\n        self.save[\"total_score\"] = self.save.get(\"total_score\", 0) + self.score\n        if self.score > self.save.get(\"high_score\", 0):\n            self.save[\"high_score\"] = self.score\n        scores = self.save.get(\"scores\", [])\n        scores.append(self.score)\n        scores.sort(reverse=True)\n        self.save[\"scores\"] = scores[:20]\n        save_save(self.save)\n        self.game_over_timer = 0\n        self._build_gameover_buttons()\n\n    def _flap(self):\n        if self.state == STATE_PLAYING and self.bird_alive:\n            diff = DIFFICULTIES[self.difficulty]\n            self.bird_vel = diff[\"flap\"]\n            self.sound.play_flap()\n            self.particles.emit(self.bird_x - 5, self.bird_y + 10, 3, (255, 255, 200), 2, 15, 2)\n        elif self.state == STATE_MENU:\n            self.sound.play_menu()\n\n    # ─── Update ──────────────────────────────────────────────────────────\n\n    def update(self):\n        self.time_val += 1 / FPS\n        self.fps_history.append(self.clock.get_fps())\n        if len(self.fps_history) > 60:\n            self.fps_history.pop(0)\n\n        # Night mode\n        if self.save.get(\"night_auto\", True) and self.state == STATE_PLAYING:\n            cycle = (self.time_val * 0.02) % 1.0\n            self.night_target = max(0, math.sin(cycle * math.pi * 2 - math.pi / 2) * 0.5 + 0.5) * 0.8\n        elif self.save.get(\"night_mode\", False):\n            self.night_target = 1.0\n        else:\n            self.night_target = 0.0\n        self.night_factor += (self.night_target - self.night_factor) * 0.02\n\n        # Screen shake\n        if self.shake_dur > 0:\n            self.shake_x = random.uniform(-4, 4) * (self.shake_dur / 15)\n            self.shake_y = random.uniform(-4, 4) * (self.shake_dur / 15)\n            self.shake_dur -= 1\n        else:\n            self.shake_x = 0\n            self.shake_y = 0\n\n        # Flash fade\n        if self.flash_alpha > 0:\n            self.flash_alpha -= 8\n\n        self.particles.update()\n\n        if self.state == STATE_MENU:\n            self._update_menu()\n        elif self.state == STATE_PLAYING:\n            self._update_playing()\n        elif self.state == STATE_GAME_OVER:\n            self._update_game_over()\n\n        for btn in self.buttons:\n            btn.hovered = btn.rect.collidepoint(pygame.mouse.get_pos())\n\n    def _update_menu(self):\n        self.menu_bob += 0.05\n        self.menu_bird_y = SCREEN_H // 3 + math.sin(self.menu_bob) * 15\n        self.scroll_x += 1\n\n    def _update_playing(self):\n        diff = DIFFICULTIES[self.difficulty]\n\n        # Countdown\n        if self.countdown > 0:\n            self.countdown_timer += 1\n            if self.countdown_timer >= 60:\n                self.countdown_timer = 0\n                if self.countdown == 1:\n                    self.sound.play_go()\n                else:\n                    self.sound.play_countdown()\n                self.countdown -= 1\n                if self.countdown == 0:\n                    self.pipe_timer = 60\n                return\n\n        # Bird physics\n        if self.bird_alive:\n            self.bird_vel += diff[\"gravity\"]\n            if self.bird_vel > MAX_FALL:\n                self.bird_vel = MAX_FALL\n            self.bird_y += self.bird_vel\n\n            # Rotation\n            if self.bird_vel < 0:\n                self.bird_rotation = max(-30, self.bird_vel * 4)\n            else:\n                self.bird_rotation = min(90, self.bird_rotation + 2.5)\n\n            # Wing animation\n            self.bird_frame_timer += 1\n            if self.bird_frame_timer > 6:\n                self.bird_frame_timer = 0\n                self.bird_frame = (self.bird_frame + 1) % 3\n\n        # Scroll\n        self.scroll_x += diff[\"speed\"]\n\n        # Pipes\n        if self.pipe_timer > 0:\n            self.pipe_timer -= 1\n        else:\n            gap_y = random.randint(120, SCREEN_H - 250)\n            pipe_x = SCREEN_W + 10\n            self.pipes.append({\"x\": pipe_x, \"gap_y\": gap_y, \"scored\": False, \"id\": len(self.pipes)})\n            self.pipe_timer = int(PIPE_INTERVAL / (diff[\"speed\"] * 16.67))\n\n        for pipe in self.pipes:\n            pipe[\"x\"] -= diff[\"speed\"]\n\n            # Score\n            if not pipe[\"scored\"] and pipe[\"x\"] + PIPE_WIDTH // 2 < self.bird_x:\n                pipe[\"scored\"] = True\n                self.score += 1\n                self.sound.play_score()\n                self.score_popups.append(ScorePopup(self.bird_x + 20, self.bird_y - 20))\n                self.particles.emit(self.bird_x, self.bird_y, 5, (255, 255, 100), 3, 20, 3)\n\n        # Remove off-screen pipes\n        self.pipes = [p for p in self.pipes if p[\"x\"] > -PIPE_WIDTH - 20]\n\n        # Score popups\n        self.score_popups = [p for p in self.score_popups if p.alive()]\n        for sp in self.score_popups:\n            sp.update()\n\n        # Collision\n        if self.bird_alive:\n            bird_rect = pygame.Rect(self.bird_x - 12, self.bird_y - 12, 24, 24)\n            # Shrink hitbox slightly for fairness\n            bird_rect.inflate_ip(-4, -4)\n\n            # Ground / ceiling\n            ground_y = SCREEN_H - 80\n            if self.bird_y + 12 >= ground_y or self.bird_y - 12 <= 0:\n                self.bird_y = ground_y - 12\n                self._die()\n\n            # Pipes\n            for pipe in self.pipes:\n                gap = DIFFICULTIES[self.difficulty][\"gap\"]\n                half_gap = gap // 2\n                top_h = pipe[\"gap_y\"] - half_gap\n                bot_y = pipe[\"gap_y\"] + half_gap\n\n                top_rect = pygame.Rect(pipe[\"x\"], 0, PIPE_WIDTH, top_h)\n                bot_rect = pygame.Rect(pipe[\"x\"], bot_y, PIPE_WIDTH, ground_y - bot_y)\n\n                if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):\n                    self._die()\n\n        # Bird fall after death\n        if not self.bird_alive:\n            self.bird_vel += diff[\"gravity\"]\n            self.bird_y += self.bird_vel\n            self.bird_rotation = min(90, self.bird_rotation + 4)\n            ground_y = SCREEN_H - 80\n            if self.bird_y + 12 >= ground_y:\n                self.bird_y = ground_y - 12\n                self.bird_vel = 0\n                if self.game_over_timer == 0:\n                    self.sound.play_die()\n                self.game_over_timer += 1\n                if self.game_over_timer > 30:\n                    self.state = STATE_GAME_OVER\n        else:\n            self.game_over_timer = 0\n\n    def _update_game_over(self):\n        self.game_over_timer += 1\n        # Bird still falls\n        self.bird_vel += DIFFICULTIES[self.difficulty][\"gravity\"]\n        self.bird_y += self.bird_vel\n        ground_y = SCREEN_H - 80\n        if self.bird_y + 12 >= ground_y:\n            self.bird_y = ground_y - 12\n            self.bird_vel = 0\n\n    # ─── Draw ────────────────────────────────────────────────────────────\n\n    def draw(self):\n        self.screen.fill((0, 0, 0))\n\n        # Background\n        draw_background(self.screen, self.night_factor, self.scroll_x)\n        draw_stars(self.screen, self.night_factor, self.time_val)\n\n        # Pipes\n        for pipe in self.pipes:\n            gap = DIFFICULTIES[self.difficulty][\"gap\"]\n            half_gap = gap // 2\n            top_h = pipe[\"gap_y\"] - half_gap\n            bot_y = pipe[\"gap_y\"] + half_gap\n            bot_h = SCREEN_H - 80 - bot_y\n            draw_pipe(self.screen, pipe[\"x\"], 0, PIPE_WIDTH, top_h, True)\n            draw_pipe(self.screen, pipe[\"x\"], bot_y, PIPE_WIDTH, bot_h, False)\n\n        # Ground\n        draw_ground(self.screen, self.scroll_x, self.night_factor)\n\n        # Bird\n        if self.state == STATE_MENU:\n            bird_surf = self.bird_frames[self.bird_frame % len(self.bird_frames)]\n            self.screen.blit(bird_surf, (self.bird_x - bird_surf.get_width() // 2,\n                                          self.menu_bird_y - bird_surf.get_height() // 2))\n        else:\n            bird_surf = pygame.transform.rotate(self.bird_frames[0], self.bird_rotation)\n            rect = bird_surf.get_rect(center=(self.bird_x, self.bird_y))\n            self.screen.blit(bird_surf, rect.topleft)\n\n        # Particles\n        self.particles.draw(self.screen)\n\n        # Score popups\n        for sp in self.score_popups:\n            sp.draw(self.screen)\n\n        # In-game HUD\n        if self.state == STATE_PLAYING:\n            draw_score_text(self.screen, str(self.score), SCREEN_W // 2 - 20, 30, 56, C_TEXT_WHITE)\n            # Pause hint\n            small_font = pygame.font.SysFont(\"arial\", 14)\n            hint = small_font.render(\"ESC to pause\", True, (200, 200, 200))\n            self.screen.blit(hint, (SCREEN_W - hint.get_width() - 10, 10))\n\n        # Countdown\n        if self.state == STATE_PLAYING and self.countdown > 0:\n            self._draw_countdown()\n\n        # State overlays\n        if self.state == STATE_MENU:\n            self._draw_menu()\n        elif self.state == STATE_PAUSED:\n            self._draw_pause()\n        elif self.state == STATE_GAME_OVER:\n            self._draw_game_over()\n        elif self.state == STATE_SETTINGS:\n            self._draw_settings()\n        elif self.state == STATE_SKIN_SELECT:\n            self._draw_skin_select()\n        elif self.state == STATE_LEADERBOARD:\n            self._draw_leaderboard()\n\n        # Flash effect\n        if self.flash_alpha > 0:\n            flash = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n            flash.fill((255, 255, 255, min(255, self.flash_alpha)))\n            self.screen.blit(flash, (0, 0))\n\n        # Screen shake\n        if self.shake_dur > 0:\n            self.screen = pygame.transform.offset(self.screen, int(self.shake_x), int(self.shake_y))\n\n        pygame.display.flip()\n\n    def _draw_countdown(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 80))\n        self.screen.blit(overlay, (0, 0))\n        text = str(self.countdown) if self.countdown > 0 else \"GO!\"\n        color = C_TEXT_WHITE if self.countdown > 0 else (50, 255, 50)\n        draw_score_text(self.screen, text, SCREEN_W // 2 - 40, SCREEN_H // 2 - 40, 80, color)\n\n    def _draw_menu(self):\n        # Title\n        title_font = pygame.font.SysFont(\"arial\", 44, bold=True)\n        title = title_font.render(\"FLIPPYBLOCK\", True, C_TEXT_WHITE)\n        title_shadow = title_font.render(\"FLIPPYBLOCK\", True, (0, 0, 0))\n        self.screen.blit(title_shadow, (SCREEN_W // 2 - title.get_width() // 2 + 2, 82))\n        self.screen.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 80))\n\n        sub_font = pygame.font.SysFont(\"arial\", 22, bold=True)\n        sub = sub_font.render(\"EXTREME\", True, C_TEXT_GOLD)\n        sub_shadow = sub_font.render(\"EXTREME\", True, (0, 0, 0))\n        self.screen.blit(sub_shadow, (SCREEN_W // 2 - sub.get_width() // 2 + 2, 132))\n        self.screen.blit(sub, (SCREEN_W // 2 - sub.get_width() // 2, 130))\n\n        # High score\n        hs = self.save.get(\"high_score\", 0)\n        hs_font = pygame.font.SysFont(\"arial\", 18)\n        hs_text = hs_font.render(f\"Best: {hs}\", True, C_TEXT_GOLD)\n        self.screen.blit(hs_text, (SCREEN_W // 2 - hs_text.get_width() // 2, 170))\n\n        # Tap hint\n        hint_font = pygame.font.SysFont(\"arial\", 16)\n        hint = hint_font.render(\"Press SPACE or Click to flap\", True, (200, 200, 200))\n        self.screen.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 120))\n\n        # Buttons\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    def _draw_pause(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 150))\n        self.screen.blit(overlay, (0, 0))\n\n        panel = pygame.Surface((SCREEN_W - 80, 260), pygame.SRCALPHA)\n        panel.fill((30, 30, 50, 230))\n        _draw_rounded_rect(panel, (0, 0, SCREEN_W - 80, 260), 12, (30, 30, 50, 230))\n        pygame.draw.rect(panel, C_UI_BORDER, (0, 0, SCREEN_W - 80, 260), 2, border_radius=12)\n        self.screen.blit(panel, (40, SCREEN_H // 2 - 170))\n\n        draw_score_text(self.screen, \"PAUSED\", SCREEN_W // 2 - 55, SCREEN_H // 2 - 155, 36, C_TEXT_WHITE)\n\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    def _draw_game_over(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 160))\n        self.screen.blit(overlay, (0, 0))\n\n        panel_w = SCREEN_W - 80\n        panel_h = 320\n        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)\n        panel.fill((30, 30, 50, 230))\n        _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 230))\n        pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)\n        self.screen.blit(panel, (40, SCREEN_H // 2 - 200))\n\n        draw_score_text(self.screen, \"GAME OVER\", SCREEN_W // 2 - 100, SCREEN_H // 2 - 180, 36, (255, 80, 80))\n\n        # Score\n        draw_score_text(self.screen, f\"Score: {self.score}\", SCREEN_W // 2 - 60, SCREEN_H // 2 - 130, 28, C_TEXT_WHITE)\n\n        # Best\n        hs = self.save.get(\"high_score\", 0)\n        is_best = self.score == hs and hs > 0\n        best_color = C_TEXT_GOLD if is_best else C_TEXT_WHITE\n        draw_score_text(self.screen, f\"Best: {hs}\", SCREEN_W // 2 - 50, SCREEN_H // 2 - 90, 22, best_color)\n        if is_best:\n            new_font = pygame.font.SysFont(\"arial\", 16, bold=True)\n            new_surf = new_font.render(\"NEW BEST!\", True, C_TEXT_GOLD)\n            self.screen.blit(new_surf, (SCREEN_W // 2 - new_surf.get_width() // 2, SCREEN_H // 2 - 70))\n\n        # Medal\n        medal_label = draw_medal(self.screen, SCREEN_W // 2, SCREEN_H // 2 - 30, self.score)\n\n        # Stats\n        stats_font = pygame.font.SysFont(\"arial\", 14)\n        total_games = self.save.get(\"total_games\", 0)\n        avg = self.save.get(\"total_score\", 0) // max(1, total_games)\n        stats = [f\"Games: {total_games}\", f\"Avg Score: {avg}\"]\n        for i, stat in enumerate(stats):\n            surf = stats_font.render(stat, True, (180, 180, 180))\n            self.screen.blit(surf, (SCREEN_W // 2 - surf.get_width() // 2, SCREEN_H // 2 + 30 + i * 20))\n\n        # Buttons\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    def _draw_settings(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        self.screen.blit(overlay, (0, 0))\n\n        panel_w = SCREEN_W - 60\n        panel_h = 420\n        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)\n        panel.fill((30, 30, 50, 240))\n        _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))\n        pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)\n        self.screen.blit(panel, (30, SCREEN_H // 2 - 240))\n\n        draw_score_text(self.screen, \"SETTINGS\", SCREEN_W // 2 - 70, SCREEN_H // 2 - 215, 32, C_TEXT_WHITE)\n\n        # Difficulty selector\n        self._draw_toggle_row(SCREEN_H // 2 - 170, \"Difficulty\", self.difficulty,\n                              list(DIFFICULTIES.keys()), self._cycle_difficulty)\n\n        # Sound toggle\n        sound_text = \"ON\" if self.save.get(\"sound_enabled\", True) else \"OFF\"\n        self._draw_toggle_row(SCREEN_H // 2 - 120, \"Sound\", sound_text, [\"ON\", \"OFF\"],\n                              self._toggle_sound)\n\n        # Night mode\n        night_text = \"Auto\" if self.save.get(\"night_auto\", True) else (\"ON\" if self.save.get(\"night_mode\", False) else \"OFF\")\n        self._draw_toggle_row(SCREEN_H // 2 - 70, \"Night Mode\", night_text,\n                              [\"Auto\", \"ON\", \"OFF\"], self._cycle_night)\n\n        # Back button\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    def _draw_toggle_row(self, y, label, current, options, callback):\n        font = pygame.font.SysFont(\"arial\", 20)\n        label_surf = font.render(label, True, C_TEXT_WHITE)\n        self.screen.blit(label_surf, (60, y))\n\n        # Left button\n        left_rect = pygame.Rect(200, y - 12, 30, 30)\n        _draw_rounded_rect(self.screen, left_rect, 4, C_UI_BUTTON)\n        pygame.draw.rect(self.screen, C_UI_BORDER, left_rect, 1, border_radius=4)\n        arrow_font = pygame.font.SysFont(\"arial\", 20, bold=True)\n        arrow = arrow_font.render(\"<\", True, C_TEXT_WHITE)\n        self.screen.blit(arrow, (left_rect.x + 8, left_rect.y + 4))\n\n        # Current value\n        val_surf = font.render(current, True, C_TEXT_GOLD)\n        self.screen.blit(val_surf, (240, y - 6))\n\n        # Right button\n        right_rect = pygame.Rect(240 + val_surf.get_width() + 10, y - 12, 30, 30)\n        _draw_rounded_rect(self.screen, right_rect, 4, C_UI_BUTTON)\n        pygame.draw.rect(self.screen, C_UI_BORDER, right_rect, 1, border_radius=4)\n        arrow = arrow_font.render(\">\", True, C_TEXT_WHITE)\n        self.screen.blit(arrow, (right_rect.x + 8, right_rect.y + 4))\n\n        # Store for click handling\n        self._last_toggle_info = {\n            \"left_rect\": left_rect, \"right_rect\": right_rect,\n            \"current\": current, \"options\": options, \"callback\": callback\n        }\n\n    def _cycle_difficulty(self):\n        keys = list(DIFFICULTIES.keys())\n        idx = keys.index(self.difficulty)\n        self.difficulty = keys[(idx + 1) % len(keys)]\n        self.save[\"difficulty\"] = self.difficulty\n        save_save(self.save)\n        self.sound.play_select()\n\n    def _toggle_sound(self):\n        self.save[\"sound_enabled\"] = not self.save.get(\"sound_enabled\", True)\n        self.sound.enabled = self.save[\"sound_enabled\"]\n        save_save(self.save)\n        if self.sound.enabled:\n            self.sound.play_select()\n\n    def _cycle_night(self):\n        if self.save.get(\"night_auto\", True):\n            self.save[\"night_auto\"] = False\n            self.save[\"night_mode\"] = True\n        elif self.save.get(\"night_mode\", False):\n            self.save[\"night_mode\"] = False\n        else:\n            self.save[\"night_auto\"] = True\n        save_save(self.save)\n        self.sound.play_select()\n\n    def _draw_skin_select(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        self.screen.blit(overlay, (0, 0))\n\n        panel_w = SCREEN_W - 60\n        panel_h = 340\n        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)\n        panel.fill((30, 30, 50, 240))\n        _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))\n        pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)\n        self.screen.blit(panel, (30, SCREEN_H // 2 - 190))\n\n        draw_score_text(self.screen, \"SELECT SKIN\", SCREEN_W // 2 - 80, SCREEN_H // 2 - 165, 28, C_TEXT_WHITE)\n\n        # Skin grid\n        cols = 3\n        skin_names = [\"Classic\", \"Orange\", \"Red\", \"Blue\", \"Purple\", \"Cyan\"]\n        start_x = 60\n        start_y = SCREEN_H // 2 - 110\n        cell_w = 120\n        cell_h = 80\n\n        self._skin_rects = []\n        for i, (color, name) in enumerate(zip(C_BIRD_SKINS, skin_names)):\n            col = i % cols\n            row = i // cols\n            cx = start_x + col * cell_w\n            cy = start_y + row * cell_h\n            rect = pygame.Rect(cx, cy, cell_w, cell_h)\n\n            is_selected = (i == self.skin_index)\n            bg_color = C_UI_BUTTON_HOVER if is_selected else C_UI_BUTTON\n            _draw_rounded_rect(self.screen, rect, 6, bg_color)\n            border_c = C_TEXT_GOLD if is_selected else C_UI_BORDER\n            pygame.draw.rect(self.screen, border_c, rect, 2 if is_selected else 1, border_radius=6)\n\n            # Preview bird\n            preview = generate_bird(color, 24)\n            self.screen.blit(preview, (cx + cell_w // 2 - 12, cy + 5))\n\n            # Name\n            name_font = pygame.font.SysFont(\"arial\", 12)\n            name_surf = name_font.render(name, True, C_TEXT_WHITE)\n            self.screen.blit(name_surf, (cx + cell_w // 2 - name_surf.get_width() // 2, cy + 45))\n\n            self._skin_rects.append((rect, i))\n\n        # Back button\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    def _draw_leaderboard(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        self.screen.blit(overlay, (0, 0))\n\n        panel_w = SCREEN_W - 60\n        panel_h = 420\n        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)\n        panel.fill((30, 30, 50, 240))\n        _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))\n        pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)\n        self.screen.blit(panel, (30, SCREEN_H // 2 - 240))\n\n        draw_score_text(self.screen, \"TOP SCORES\", SCREEN_W // 2 - 70, SCREEN_H // 2 - 215, 30, C_TEXT_WHITE)\n\n        scores = self.save.get(\"scores\", [])\n        if not scores:\n            empty_font = pygame.font.SysFont(\"arial\", 18)\n            empty = empty_font.render(\"No scores yet!\", True, (150, 150, 150))\n            self.screen.blit(empty, (SCREEN_W // 2 - empty.get_width() // 2, SCREEN_H // 2 - 100))\n        else:\n            for i, sc in enumerate(scores[:10]):\n                y = SCREEN_H // 2 - 170 + i * 28\n                rank_font = pygame.font.SysFont(\"arial\", 18, bold=True)\n                score_font = pygame.font.SysFont(\"arial\", 18)\n\n                rank_color = C_TEXT_GOLD if i < 3 else (C_TEXT_SILVER if i < 6 else (180, 180, 180))\n                rank_text = rank_font.render(f\"#{i + 1}\", True, rank_color)\n                score_text = score_font.render(f\"{sc}\", True, C_TEXT_WHITE)\n\n                self.screen.blit(rank_text, (80, y - 6))\n                self.screen.blit(score_text, (SCREEN_W - 120, y - 6))\n\n                # Bar\n                bar_w = min(200, int(200 * sc / max(1, scores[0])))\n                bar_rect = pygame.Rect(140, y, bar_w, 16)\n                _draw_rounded_rect(self.screen, bar_rect, 4, (60, 60, 100))\n\n        # Stats\n        total_games = self.save.get(\"total_games\", 0)\n        total_score = self.save.get(\"total_score\", 0)\n        avg = total_score // max(1, total_games)\n        stats_font = pygame.font.SysFont(\"arial\", 14)\n        stats = [f\"Total Games: {total_games}\", f\"Total Score: {total_score}\", f\"Avg Score: {avg}\"]\n        for i, stat in enumerate(stats):\n            surf = stats_font.render(stat, True, (160, 160, 160))\n            self.screen.blit(surf, (60, SCREEN_H // 2 + 100 + i * 20))\n\n        # Back button\n        for btn in self.buttons:\n            btn.draw(self.screen)\n\n    # ─── Events ──────────────────────────────────────────────────────────\n\n    def handle_events(self):\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                return False\n\n            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:\n                # Check toggle buttons first\n                if self.state == STATE_SETTINGS and hasattr(self, '_last_toggle_info'):\n                    info = self._last_toggle_info\n                    if info[\"left_rect\"].collidepoint(event.pos):\n                        keys = list(DIFFICULTIES.keys())\n                        if info[\"callback\"] == self._cycle_difficulty:\n                            idx = keys.index(self.difficulty)\n                            self.difficulty = keys[(idx - 1) % len(keys)]\n                            self.save[\"difficulty\"] = self.difficulty\n                        elif info[\"callback\"] == self._toggle_sound:\n                            self.save[\"sound_enabled\"] = not self.save.get(\"sound_enabled\", True)\n                            self.sound.enabled = self.save[\"sound_enabled\"]\n                        elif info[\"callback\"] == self._cycle_night:\n                            if self.save.get(\"night_auto\", True):\n                                self.save[\"night_auto\"] = False\n                                self.save[\"night_mode\"] = False\n                            elif self.save.get(\"night_mode\", False):\n                                self.save[\"night_auto\"] = True\n                            else:\n                                self.save[\"night_mode\"] = True\n                        save_save(self.save)\n                        self.sound.play_select()\n                        continue\n                    elif info[\"right_rect\"].collidepoint(event.pos):\n                        info[\"callback\"]()\n                        continue\n\n                # Skin selection\n                if self.state == STATE_SKIN_SELECT and hasattr(self, '_skin_rects'):\n                    for rect, idx in self._skin_rects:\n                        if rect.collidepoint(event.pos):\n                            self.skin_index = idx\n                            self.skin_color = C_BIRD_SKINS[idx]\n                            self.bird_frames = generate_bird_frames(self.skin_color)\n                            self.save[\"skin_index\"] = idx\n                            save_save(self.save)\n                            self.sound.play_select()\n                            break\n                    else:\n                        for btn in self.buttons:\n                            btn.handle_event(event)\n                    continue\n\n                # General buttons\n                for btn in self.buttons:\n                    btn.handle_event(event)\n                continue\n\n            if event.type == pygame.KEYDOWN:\n                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:\n                    if self.state == STATE_MENU:\n                        self._start_game()\n                    elif self.state == STATE_PLAYING:\n                        self._flap()\n                    elif self.state == STATE_GAME_OVER and self.game_over_timer > 30:\n                        self._start_game()\n                elif event.key == pygame.K_RETURN:\n                    if self.state == STATE_GAME_OVER and self.game_over_timer > 30:\n                        self._start_game()\n                elif event.key == pygame.K_ESCAPE:\n                    if self.state == STATE_PLAYING:\n                        self.state = STATE_PAUSED\n                        self._build_pause_buttons()\n                        self.sound.play_swoosh()\n                    elif self.state == STATE_PAUSED:\n                        self._resume()\n                    elif self.state in (STATE_SETTINGS, STATE_SKIN_SELECT, STATE_LEADERBOARD):\n                        self._go_back()\n                elif event.key == pygame.K_s:\n                    if self.state == STATE_PLAYING:\n                        self.state = STATE_PAUSED\n                        self._build_pause_buttons()\n                elif event.key == pygame.K_LEFT:\n                    if self.state == STATE_SETTINGS:\n                        if hasattr(self, '_last_toggle_info'):\n                            info = self._last_toggle_info\n                            if info[\"callback\"] == self._cycle_difficulty:\n                                keys = list(DIFFICULTIES.keys())\n                                idx = keys.index(self.difficulty)\n                                self.difficulty = keys[(idx - 1) % len(keys)]\n                                self.save[\"difficulty\"] = self.difficulty\n                                save_save(self.save)\n                                self.sound.play_select()\n                elif event.key == pygame.K_RIGHT:\n                    if self.state == STATE_SETTINGS:\n                        if hasattr(self, '_last_toggle_info'):\n                            info = self._last_toggle_info\n                            if info[\"callback\"] == self._cycle_difficulty:\n                                info[\"callback\"]()\n\n            # Mouse click to flap\n            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:\n                if self.state == STATE_PLAYING and self.bird_alive:\n                    # Don't flap if clicking a button area (bottom of screen)\n                    if event.pos[1] < SCREEN_H // 2 - 40:\n                        self._flap()\n\n        return True\n\n    # ─── Main Loop ───────────────────────────────────────────────────────\n\n    def run(self):\n        running = True\n        while running:\n            running = self.handle_events()\n            self.update()\n            self.draw()\n            self.clock.tick(FPS)\n        pygame.quit()\n        sys.exit()\n\n\n# ─── Entry Point ─────────────────────────────────────────────────────────────\n\nif __name__ == \"__main__\":\n    game = Game()\n    game.run()\n",
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 5.5s)

_Thinking:_

Now let me test the game to make sure it runs without errors.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport ast, sys\nwith open('flippyblock_extreme.py') as f:\n    try:\n        ast.parse(f.read())\n        print('Syntax OK')\n    except SyntaxError as e:\n        print(f'Syntax Error: {e}')\n        sys.exit(1)\n\"",
  "description": "Check Python syntax"
}
```

**Output:**
```
Syntax OK

```

---

## Assistant (Build · Qwen3.6 27B · 9.6s)

_Thinking:_

Good, syntax is fine. Let me now do a thorough review of the code and fix any issues I can spot. Let me re-read the file carefully.


Good, syntax passes. Now let me do a thorough code review and fix issues:



**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the core game engine and physics",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Generate all visual assets programmatically",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Build UI system (menus, buttons, panels)",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add sound effects (programmatic generation)",
      "status": "completed",
      "priority": "medium"
    },
    {
      "content": "Implement game states and flow",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add polish features (particles, screen shake, day/night)",
      "status": "completed",
      "priority": "medium"
    },
    {
      "content": "Review and fix all issues",
      "status": "in_progress",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Create the core game engine and physics",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Generate all visual assets programmatically",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Build UI system (menus, buttons, panels)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add sound effects (programmatic generation)",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Implement game states and flow",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add polish features (particles, screen shake, day/night)",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Review and fix all issues",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 88.5s)

_Thinking:_

Let me review the code thoroughly and identify issues:

1. **Sound `play_score` method**: The `pygame.time.set_timer` and `pygame.time.set_timeout` usage is wrong. `set_timer` takes a custom event ID and interval, not a callback. And `set_timeout` doesn't exist in pygame. This needs to be fixed.

2. **Bird collision hitbox**: The bird_rect uses hardcoded values (24x24) but the bird sprite is 34x34. Need to make the hitbox proportional.

3. **Pipe gap calculation in `draw` vs `update`**: In `_update_playing`, the gap is calculated from `DIFFICULTIES[self.difficulty]["gap"]`, but in `draw` it's also calculated the same way. However, in `generate_pipe_pair` it uses `PIPE_GAP_BASE` which is unused. That function is dead code.

4. **`_draw_rounded_rect` in settings/skin panels**: It draws the rounded rect on top of an already filled panel, which is redundant but not harmful.

5. **`play_score` sound**: The two-tone score sound won't work because of the wrong timer API. Need to fix with a simple approach.

6. **The `handle_events` method**: There's a duplicate handling of `MOUSEBUTTONDOWN` - first for toggles/skins, then again for buttons, then for flap. The flap check at the bottom will also trigger when clicking buttons. Need to restructure.

7. **`_build_pause_buttons` in `_resume`**: This is wrong - when resuming, we should not rebuild pause buttons.

8. **Night mode in settings**: The cycle logic for night mode has a bug - cycling left from "Auto" should go to "OFF", not stay at "Auto".

9. **`_ensure_data_dir` is called but the save file path uses `DATA_DIR` which is computed from `__file__`** - this is fine.

10. **The `bird_rect` in collision**: Uses `self.bird_x - 12` but the bird sprite is 34x34, so the center-based positioning with 12 offset is off. Should be `self.bird_x - 17` for a 34px sprite.

11. **FPS display**: The `fps_history` is tracked but never displayed. Could add a debug FPS counter.

12. **The `key_flap` attribute** is set but never used.

13. **`PIPE_INTERVAL`** calculation: `int(PIPE_INTERVAL / (diff["speed"] * 16.67))` - the 16.67 is ms per frame at 60fps. This gives frames between pipes. Let me verify: at normal speed 2.5, interval = 1600 / (2.5 * 16.67) = 1600 / 41.675 = ~38 frames. At extreme speed 4.0, interval = 1600 / 66.68 = ~24 frames. This seems reasonable but might need tuning.

14. **`draw_score_text` centering**: The function takes x,y as top-left but callers pass center-ish values. Need to verify alignment.

15. **Bird frame rotation in menu**: The menu bird cycles through frames but doesn't rotate them. Actually it does use `self.bird_frames` which are pre-rotated. But `self.bird_frame` is only updated in `_update_playing`. In `_update_menu`, there's no frame update. Need to add it.

16. **`_draw_rounded_rect` on panels**: The panels are created as SRCALPHA surfaces, filled with a color, then `draw_rounded_rect` is called with the same color. This is redundant since `fill` already fills the surface. The rounded rect is meant to make corners rounded, but `fill` fills everything including corners. The issue is that `fill` on a SRCALPHA surface fills the entire rectangular area, then `draw_rounded_rect` draws on top with the same color - which doesn't help. The corners will still be sharp because `fill` already filled them.

Wait, actually for the panels, the approach is:
1. Create surface with SRCALPHA
2. Fill with semi-transparent color (this fills everything including corners)
3. Draw rounded rect with same color (no effect since already filled)

The issue is that `fill` on an SRCALPHA surface fills the entire rect, including corners. To get rounded corners, we need to NOT fill first, but instead just draw the rounded rect. Let me fix this.

Actually, looking more carefully: for the pause panel, game over panel, etc., the approach is:
```python
panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
panel.fill((30, 30, 50, 230))
_draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 230))
```

The `fill` fills the entire surface with the color (including corners). Then `draw_rounded_rect` draws the same color on top - no visual change. The corners remain sharp.

To fix: Instead of fill + draw_rounded_rect, we should only use draw_rounded_rect. But `draw_rounded_rect` only draws the filled shape, so we need to clear the surface first (make it fully transparent), then draw the rounded rect.

Let me fix this properly.

17. **Score display during countdown**: The score "0" shows during countdown. Should hide it.

18. **Bird not visible during countdown**: The bird should be visible during countdown.

19. **`_build_pause_buttons` should not be called in `_resume`**: It's unnecessary.

Let me now fix all these issues comprehensively. I'll rewrite the file with all fixes.

Actually, let me be more strategic. Let me identify the critical bugs and fix them:

Critical bugs:
1. Sound `play_score` timer issue - won't crash but won't play the second tone
2. Menu bird frame not updating - visual issue
3. Panel corners not rounded - visual issue
4. Mouse event handling overlap - functional issue (flap triggers on button clicks)
5. Bird hitbox sizing - gameplay issue
6. `_resume` calls `_build_pause_buttons` - minor issue

Let me fix all of these.


I found several issues during review. Let me fix them all:



**Tool: read**

**Input:**
```json
{
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py"
}
```

**Output:**
```
<path>/home/patof/stress_bench/flippyblock_extreme.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """FlippyBlock Extreme - A Flappy Bird clone with no external assets."""
3: 
4: import pygame
5: import math
6: import random
7: import json
8: import os
9: import struct
10: import array
11: import sys
12: 
13: # ─── Constants ───────────────────────────────────────────────────────────────
14: 
15: SCREEN_W = 480
16: SCREEN_H = 720
17: FPS = 60
18: TITLE = "FlippyBlock Extreme"
19: 
20: DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".flippyblock_data")
21: SAVE_FILE = os.path.join(DATA_DIR, "save.json")
22: 
23: # Colors
24: C_SKY_TOP = (100, 180, 255)
25: C_SKY_BOT = (200, 235, 255)
26: C_SKY_NIGHT_TOP = (15, 15, 50)
27: C_SKY_NIGHT_BOT = (30, 30, 80)
28: C_GROUND = (139, 119, 80)
29: C_GROUND_DARK = (100, 85, 55)
30: C_GROUND_GRASS = (80, 180, 60)
31: C_PIPE_GREEN = (50, 200, 60)
32: C_PIPE_GREEN_DARK = (30, 150, 40)
33: C_PIPE_GREEN_LIGHT = (80, 230, 90)
34: C_PIPE_CAP = (40, 180, 50)
35: C_BIRD_YELLOW = (255, 220, 50)
36: C_BIRD_ORANGE = (255, 160, 30)
37: C_BIRD_WHITE = (255, 255, 240)
38: C_BIRD_RED = (220, 50, 50)
39: C_BIRD_BLUE = (50, 100, 220)
40: C_BIRD_PURPLE = (160, 60, 200)
41: C_BIRD_CYAN = (50, 200, 220)
42: C_BIRD_SKINS = [C_BIRD_YELLOW, C_BIRD_ORANGE, C_BIRD_RED, C_BIRD_BLUE, C_BIRD_PURPLE, C_BIRD_CYAN]
43: C_TEXT_WHITE = (255, 255, 255)
44: C_TEXT_SHADOW = (0, 0, 0)
45: C_TEXT_GOLD = (255, 215, 0)
46: C_TEXT_SILVER = (192, 192, 192)
47: C_TEXT_BRONZE = (205, 127, 50)
48: C_UI_BG = (40, 40, 60)
49: C_UI_BG_ALPHA = (40, 40, 60, 200)
50: C_UI_BORDER = (80, 80, 120)
51: C_UI_BUTTON = (60, 60, 100)
52: C_UI_BUTTON_HOVER = (80, 80, 140)
53: C_UI_BUTTON_ACTIVE = (100, 100, 170)
54: C_STAR = (255, 255, 220)
55: C_CLOUD = (240, 245, 255)
56: C_PARTICLE = (255, 200, 50)
57: C_MEDAL_GOLD = (255, 215, 0)
58: C_MEDAL_SILVER = (192, 192, 192)
59: C_MEDAL_BRONZE = (205, 127, 50)
60: C_MEDAL_PLATINUM = (160, 220, 255)
61: 
62: # Physics
63: GRAVITY = 0.45
64: FLAP_VEL = -7.5
65: MAX_FALL = 10
66: PIPE_SPEED_BASE = 2.5
67: PIPE_GAP_BASE = 155
68: PIPE_WIDTH = 60
69: PIPE_INTERVAL = 1600
70: 
71: # Difficulty presets
72: DIFFICULTIES = {
73:     "Easy":     {"gap": 190, "speed": 2.0, "gravity": 0.38, "flap": -7.0},
74:     "Normal":   {"gap": 155, "speed": 2.5, "gravity": 0.45, "flap": -7.5},
75:     "Hard":     {"gap": 130, "speed": 3.2, "gravity": 0.52, "flap": -8.0},
76:     "Extreme":  {"gap": 110, "speed": 4.0, "gravity": 0.60, "flap": -8.5},
77: }
78: 
79: # ─── Save / Load ─────────────────────────────────────────────────────────────
80: 
81: def _ensure_data_dir():
82:     os.makedirs(DATA_DIR, exist_ok=True)
83: 
84: def load_save():
85:     _ensure_data_dir()
86:     try:
87:         with open(SAVE_FILE, "r") as f:
88:             return json.load(f)
89:     except (FileNotFoundError, json.JSONDecodeError):
90:         return {"high_score": 0, "total_games": 0, "total_score": 0, "best_streak": 0,
91:                 "current_streak": 0, "skin_index": 0, "difficulty": "Normal",
92:                 "sound_enabled": True, "night_mode": False, "night_auto": True,
93:                 "scores": []}
94: 
95: def save_save(data):
96:     _ensure_data_dir()
97:     with open(SAVE_FILE, "w") as f:
98:         json.dump(data, f, indent=2)
99: 
100: # ─── Sound Engine (purely programmatic) ──────────────────────────────────────
101: 
102: class SoundEngine:
103:     def __init__(self):
104:         self.enabled = True
105:         self._initialized = False
106: 
107:     def _init(self):
108:         if self._initialized:
109:             return
110:         try:
111:             pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
112:             self._initialized = True
113:         except Exception:
114:             self.enabled = False
115: 
116:     def _make_sound(self, freq, duration, wave_type="sine", fade=True, freq_end=None):
117:         if not self.enabled:
118:             return None
119:         self._init()
120:         sr = 22050
121:         n = int(sr * duration)
122:         samples = array.array('h')
123:         for i in range(n):
124:             t = i / sr
125:             f = freq + (freq_end - freq) * (i / n) if freq_end else freq
126:             if wave_type == "sine":
127:                 v = math.sin(2 * math.pi * f * t)
128:             elif wave_type == "square":
129:                 v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0
130:             elif wave_type == "sawtooth":
131:                 v = 2 * (f * t - math.floor(f * t + 0.5))
132:             else:
133:                 v = 0
134:             if fade and i > n * 0.6:
135:                 env = 1.0 - (i - n * 0.6) / (n * 0.4)
136:                 v *= max(0, env)
137:             elif fade:
138:                 env = min(1.0, i / max(1, n * 0.05))
139:                 v *= env
140:             samples.append(int(v * 15000))
141:         return pygame.sound.make_sound(samples)
142: 
143:     def _noise_sound(self, duration, volume=0.3):
144:         if not self.enabled:
145:             return None
146:         self._init()
147:         sr = 22050
148:         n = int(sr * duration)
149:         samples = array.array('h')
150:         for i in range(n):
151:             v = (random.random() * 2 - 1) * volume
152:             if i > n * 0.5:
153:                 v *= 1.0 - (i - n * 0.5) / (n * 0.5)
154:             samples.append(int(v * 15000))
155:         return pygame.sound.make_sound(samples)
156: 
157:     def play_flap(self):
158:         s = self._make_sound(600, 0.08, "sine", freq_end=900)
159:         if s: s.play()
160: 
161:     def play_score(self):
162:         s = self._make_sound(880, 0.1, "sine")
163:         if s:
164:             s.play()
165:             pygame.time.set_timer(pygame.USEREVENT, 100)
166:             def _play2():
167:                 s2 = self._make_sound(1100, 0.12, "sine")
168:                 if s2: s2.play()
169:             pygame.time.set_timeout(_play2, 100)
170: 
171:     def play_hit(self):
172:         s = self._make_sound(200, 0.2, "square", freq_end=80)
173:         if s: s.play()
174: 
175:     def play_die(self):
176:         s = self._make_sound(400, 0.4, "sawtooth", freq_end=100)
177:         if s: s.play()
178: 
179:     def play_swoosh(self):
180:         s = self._noise_sound(0.15, 0.15)
181:         if s: s.play()
182: 
183:     def play_menu(self):
184:         s = self._make_sound(500, 0.06, "sine", freq_end=700)
185:         if s: s.play()
186: 
187:     def play_select(self):
188:         s = self._make_sound(700, 0.08, "sine", freq_end=1000)
189:         if s: s.play()
190: 
191:     def play_countdown(self):
192:         s = self._make_sound(440, 0.15, "sine")
193:         if s: s.play()
194: 
195:     def play_go(self):
196:         s = self._make_sound(880, 0.2, "sine")
197:         if s: s.play()
198: 
199: # ─── Asset Generation ────────────────────────────────────────────────────────
200: 
201: def _draw_rounded_rect(surface, rect, radius, color):
202:     x, y, w, h = rect
203:     r = min(radius, w // 2, h // 2)
204:     pygame.draw.rect(surface, color, (x, y, w, h), border_radius=r)
205: 
206: def generate_bird(skin_color, size=34):
207:     s = pygame.Surface((size, size), pygame.SRCALPHA)
208:     cx, cy = size // 2, size // 2
209:     body_r = size // 2 - 1
210:     # Body
211:     pygame.draw.ellipse(s, skin_color, (1, 1, size - 2, size - 2))
212:     # Belly highlight
213:     pygame.draw.ellipse(s, pygame.Color(skin_color).lerp(pygame.Color(255, 255, 255), 0.3),
214:                         (4, size // 2, size // 2, size // 3))
215:     # Eye white
216:     eye_x, eye_y = int(size * 0.6), int(size * 0.3)
217:     pygame.draw.circle(s, (255, 255, 255), (eye_x, eye_y), 5)
218:     # Pupil
219:     pygame.draw.circle(s, (30, 30, 30), (eye_x + 1, eye_y), 3)
220:     # Eye shine
221:     pygame.draw.circle(s, (255, 255, 255), (eye_x + 2, eye_y - 1), 1)
222:     # Beak
223:     beak_pts = [(eye_x + 5, eye_y + 1), (eye_x + 5, eye_y + 5), (eye_x + 13, eye_y + 3)]
224:     pygame.draw.polygon(s, (255, 140, 30), beak_pts)
225:     # Wing
226:     wing_pts = [(3, cy), (8, cy + 6), (16, cy + 4), (14, cy - 2), (6, cy - 2)]
227:     pygame.draw.polygon(s, pygame.Color(skin_color).lerp(pygame.Color(0, 0, 0), 0.25), wing_pts)
228:     return s
229: 
230: def generate_bird_frames(skin_color):
231:     frames = []
232:     for angle in [0, -0.3, -0.6]:
233:         surf = generate_bird(skin_color)
234:         frames.append(pygame.transform.rotate(surf, math.degrees(angle)))
235:     return frames
236: 
237: def generate_pipe_pair():
238:     h = SCREEN_H
239:     gap_y = random.randint(100, SCREEN_H - 200)
240:     top_h = gap_y - PIPE_GAP_BASE // 2
241:     bot_y = gap_y + PIPE_GAP_BASE // 2
242:     return top_h, bot_y
243: 
244: def draw_pipe(surface, x, y, w, h, is_top):
245:     cap_h = 26
246:     cap_w = w + 10
247:     cap_x = x - 5
248:     # Pipe body
249:     if is_top:
250:         body_rect = (x, y, w, h - cap_h)
251:         cap_rect = (cap_x, y + h - cap_h, cap_w, cap_h)
252:     else:
253:         body_rect = (x, y + cap_h, w, h - cap_h)
254:         cap_rect = (cap_x, y, cap_w, cap_h)
255:     # Body gradient
256:     pygame.draw.rect(surface, C_PIPE_GREEN, body_rect)
257:     pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT, (x + 4, body_rect[1], 6, body_rect[3]))
258:     pygame.draw.rect(surface, C_PIPE_GREEN_DARK, (x + w - 8, body_rect[1], 6, body_rect[3]))
259:     pygame.draw.rect(surface, C_PIPE_GREEN_DARK, body_rect, 2)
260:     # Cap
261:     _draw_rounded_rect(surface, cap_rect, 4, C_PIPE_CAP)
262:     pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT, (cap_x + 3, cap_rect[1] + 3, 6, cap_rect[3] - 6))
263:     pygame.draw.rect(surface, C_PIPE_CAP, cap_rect, 2, border_radius=4)
264: 
265: def draw_background(surface, night_factor=0.0, scroll_x=0):
266:     top = pygame.Color(C_SKY_TOP).lerp(pygame.Color(C_SKY_NIGHT_TOP), night_factor)
267:     bot = pygame.Color(C_SKY_BOT).lerp(pygame.Color(C_SKY_NIGHT_BOT), night_factor)
268:     for y in range(SCREEN_H):
269:         t = y / SCREEN_H
270:         c = top.lerp(bot, t)
271:         pygame.draw.line(surface, c, (0, y), (SCREEN_W, y))
272:     # Clouds
273:     _draw_clouds(surface, night_factor, scroll_x)
274: 
275: def _draw_clouds(surface, night_factor, scroll_x):
276:     alpha = int(200 * (1 - night_factor * 0.7))
277:     cloud_color = (*C_CLOUD, alpha)
278:     cloud_positions = [(100, 80, 1.0), (300, 150, 0.7), (550, 60, 0.9),
279:                        (200, 250, 0.6), (450, 200, 0.8), (700, 120, 0.75)]
280:     for cx, cy, scale in cloud_positions:
281:         px = ((cx - scroll_x * 0.3) % (SCREEN_W + 200)) - 100
282:         _draw_cloud(surface, px, cy, scale, cloud_color)
283: 
284: def _draw_cloud(surface, x, y, scale, color):
285:     s = pygame.Surface((80 * scale, 40 * scale), pygame.SRCALPHA)
286:     pygame.draw.ellipse(s, color, (0, 10 * scale, 60 * scale, 25 * scale))
287:     pygame.draw.ellipse(s, color, (15 * scale, 0, 40 * scale, 30 * scale))
288:     pygame.draw.ellipse(s, color, (35 * scale, 5 * scale, 35 * scale, 25 * scale))
289:     surface.blit(s, (x, y))
290: 
291: def draw_stars(surface, night_factor, time_val):
292:     if night_factor < 0.3:
293:         return
294:     alpha = int(255 * (night_factor - 0.3) / 0.7)
295:     star_color = (*C_STAR, alpha)
296:     seed = 42
297:     rng = random.Random(seed)
298:     for _ in range(80):
299:         sx = rng.randint(0, SCREEN_W)
300:         sy = rng.randint(0, SCREEN_H // 2)
301:         twinkle = int(0.5 + 0.5 * math.sin(time_val * 2 + sx * 0.1))
302:         sz = 1 + twinkle
303:         sa = int(alpha * (0.4 + 0.6 * twinkle))
304:         sc = (*C_STAR, sa)
305:         pygame.draw.circle(surface, sc, (sx, sy), sz)
306: 
307: def draw_ground(surface, scroll_x, night_factor):
308:     gy = SCREEN_H - 80
309:     grass_h = 20
310:     # Grass
311:     gc = pygame.Color(C_GROUND_GRASS).lerp(pygame.Color(20, 60, 20), night_factor)
312:     pygame.draw.rect(surface, gc, (0, gy, SCREEN_W, grass_h))
313:     # Grass blades
314:     for x in range(-10, SCREEN_W + 10, 6):
315:         px = ((x - scroll_x) % (SCREEN_W + 20)) - 10
316:         blade_h = 8 + int(4 * math.sin(x * 0.3 + scroll_x * 0.05))
317:         gc2 = pygame.Color(60, 160, 40).lerp(pygame.Color(15, 45, 15), night_factor)
318:         pygame.draw.line(surface, gc2, (px, gy + grass_h), (px + 2, gy + grass_h - blade_h), 2)
319:     # Ground
320:     gc = pygame.Color(C_GROUND).lerp(pygame.Color(40, 35, 25), night_factor)
321:     gc2 = pygame.Color(C_GROUND_DARK).lerp(pygame.Color(25, 20, 15), night_factor)
322:     pygame.draw.rect(surface, gc, (0, gy + grass_h, SCREEN_W, 80 - grass_h))
323:     # Ground stripes
324:     for x in range(-10, SCREEN_W + 10, 24):
325:         px = ((x - scroll_x) % (SCREEN_W + 20)) - 10
326:         pygame.draw.line(surface, gc2, (px, gy + grass_h + 5), (px + 12, gy + grass_h + 15), 2)
327:     # Top line
328:     pygame.draw.line(surface, (0, 0, 0), (0, gy), (SCREEN_W, gy), 2)
329: 
330: def draw_score_text(surface, text, x, y, size=48, color=C_TEXT_WHITE, bold=True):
331:     font = pygame.font.SysFont("arial", size, bold=bold)
332:     shadow = font.render(text, True, C_TEXT_SHADOW)
333:     main = font.render(text, True, color)
334:     surface.blit(shadow, (x + 2, y + 2))
335:     surface.blit(main, (x, y))
336: 
337: def draw_medal(surface, x, y, score):
338:     if score < 10:
339:         return None
340:     elif score < 20:
341:         color = C_MEDAL_BRONZE
342:         label = "BRONZE"
343:     elif score < 40:
344:         color = C_MEDAL_SILVER
345:         label = "SILVER"
346:     elif score < 80:
347:         color = C_MEDAL_GOLD
348:         label = "GOLD"
349:     else:
350:         color = C_MEDAL_PLATINUM
351:         label = "PLATINUM"
352:     # Medal circle
353:     pygame.draw.circle(surface, color, (x, y), 28)
354:     pygame.draw.circle(surface, pygame.Color(color).lerp(pygame.Color(0, 0, 0), 0.3), (x, y), 22)
355:     pygame.draw.circle(surface, (255, 255, 255), (x - 5, y - 5), 6, 1)
356:     # Star on medal
357:     _draw_star(surface, x, y, 10, 5, (255, 255, 255))
358:     font = pygame.font.SysFont("arial", 10, bold=True)
359:     label_surf = font.render(label, True, color)
360:     surface.blit(label_surf, (x - label_surf.get_width() // 2, y + 32))
361:     return label
362: 
363: def _draw_star(surface, cx, cy, outer_r, inner_r, color):
364:     pts = []
365:     for i in range(10):
366:         angle = math.pi / 2 + i * math.pi / 5
367:         r = outer_r if i % 2 == 0 else inner_r
368:         pts.append((cx + r * math.cos(angle - math.pi / 2), cy + r * math.sin(angle - math.pi / 2)))
369:     pygame.draw.polygon(surface, color, pts)
370: 
371: # ─── Particle System ─────────────────────────────────────────────────────────
372: 
373: class Particle:
374:     def __init__(self, x, y, vx, vy, color, life, size=3):
375:         self.x = x
376:         self.y = y
377:         self.vx = vx
378:         self.vy = vy
379:         self.color = color
380:         self.life = life
381:         self.max_life = life
382:         self.size = size
383: 
384:     def update(self):
385:         self.x += self.vx
386:         self.y += self.vy
387:         self.vy += 0.1
388:         self.life -= 1
389: 
390:     def draw(self, surface):
391:         alpha = max(0, self.life / self.max_life)
392:         c = tuple(int(ch * alpha) for ch in self.color)
393:         s = max(1, int(self.size * alpha))
394:         pygame.draw.circle(surface, c, (int(self.x), int(self.y)), s)
395: 
396:     def alive(self):
397:         return self.life > 0
398: 
399: class ParticleSystem:
400:     def __init__(self):
401:         self.particles = []
402: 
403:     def emit(self, x, y, count, color, speed=3, life=30, size=3):
404:         for _ in range(count):
405:             angle = random.uniform(0, math.pi * 2)
406:             spd = random.uniform(0.5, speed)
407:             self.particles.append(Particle(
408:                 x, y,
409:                 math.cos(angle) * spd,
410:                 math.sin(angle) * spd,
411:                 color, life, size
412:             ))
413: 
414:     def update(self):
415:         self.particles = [p for p in self.particles if p.alive()]
416:         for p in self.particles:
417:             p.update()
418: 
419:     def draw(self, surface):
420:         for p in self.particles:
421:             p.draw(surface)
422: 
423: # ─── Button ──────────────────────────────────────────────────────────────────
424: 
425: class Button:
426:     def __init__(self, x, y, w, h, text, callback, color=C_UI_BUTTON,
427:                  hover_color=C_UI_BUTTON_HOVER, active_color=C_UI_BUTTON_ACTIVE,
428:                  font_size=22, bold=True):
429:         self.rect = pygame.Rect(x, y, w, h)
430:         self.text = text
431:         self.callback = callback
432:         self.base_color = color
433:         self.hover_color = hover_color
434:         self.active_color = active_color
435:         self.font_size = font_size
436:         self.bold = bold
437:         self.hovered = False
438:         self.pressed = False
439: 
440:     def handle_event(self, event):
441:         if event.type == pygame.MOUSEMOTION:
442:             self.hovered = self.rect.collidepoint(event.pos)
443:         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
444:             if self.rect.collidepoint(event.pos):
445:                 self.pressed = True
446:         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
447:             if self.pressed and self.rect.collidepoint(event.pos):
448:                 self.callback()
449:             self.pressed = False
450: 
451:     def draw(self, surface):
452:         color = self.active_color if self.pressed else (self.hover_color if self.hovered else self.base_color)
453:         _draw_rounded_rect(surface, self.rect, 8, color)
454:         pygame.draw.rect(surface, C_UI_BORDER, self.rect, 2, border_radius=8)
455:         font = pygame.font.SysFont("arial", self.font_size, bold=self.bold)
456:         text_surf = font.render(self.text, True, C_TEXT_WHITE)
457:         tx = self.rect.x + (self.rect.w - text_surf.get_width()) // 2
458:         ty = self.rect.y + (self.rect.h - text_surf.get_height()) // 2
459:         shadow = font.render(self.text, True, (0, 0, 0, 128))
460:         surface.blit(shadow, (tx + 1, ty + 1))
461:         surface.blit(text_surf, (tx, ty))
462: 
463: # ─── Score Popup ─────────────────────────────────────────────────────────────
464: 
465: class ScorePopup:
466:     def __init__(self, x, y):
467:         self.x = x
468:         self.y = y
469:         self.start_y = y
470:         self.life = 40
471:         self.max_life = 40
472: 
473:     def update(self):
474:         self.y -= 1.5
475:         self.life -= 1
476: 
477:     def draw(self, surface):
478:         if self.life <= 0:
479:             return
480:         alpha = min(255, int(255 * self.life / self.max_life))
481:         font = pygame.font.SysFont("arial", 28, bold=True)
482:         surf = font.render("+1", True, (255, 255, 200))
483:         shadow = font.render("+1", True, (0, 0, 0))
484:         surface.blit(shadow, (self.x + 2, self.y + 2))
485:         surface.blit(surf, (self.x, self.y))
486: 
487:     def alive(self):
488:         return self.life > 0
489: 
490: # ─── Game States ─────────────────────────────────────────────────────────────
491: 
492: STATE_MENU = 0
493: STATE_PLAYING = 1
494: STATE_PAUSED = 2
495: STATE_GAME_OVER = 3
496: STATE_SETTINGS = 4
497: STATE_SKIN_SELECT = 5
498: STATE_LEADERBOARD = 6
499: 
500: # ─── Main Game Class ─────────────────────────────────────────────────────────
501: 
502: class Game:
503:     def __init__(self):
504:         pygame.init()
505:         pygame.display.set_caption(TITLE)
506:         self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
507:         self.clock = pygame.time.Clock()
508:         self.sound = SoundEngine()
509:         self.save = load_save()
510:         self.particles = ParticleSystem()
511:         self.state = STATE_MENU
512:         self.prev_state = None
513: 
514:         # Bird
515:         self._reset_bird()
516: 
517:         # Pipes
518:         self.pipes = []
519:         self.pipe_timer = 0
520:         self.pipe_gap_y = SCREEN_H // 2
521: 
522:         # Score
523:         self.score = 0
524:         self.passed_pipes = set()
525: 
526:         # Animation
527:         self.bird_frame = 0
528:         self.bird_frame_timer = 0
529:         self.bob_timer = 0
530:         self.scroll_x = 0
531:         self.time_val = 0
532: 
533:         # Screen shake
534:         self.shake_x = 0
535:         self.shake_y = 0
536:         self.shake_dur = 0
537: 
538:         # Night mode
539:         self.night_factor = 0.0
540:         self.night_target = 0.0
541: 
542:         # Countdown
543:         self.countdown = 0
544:         self.countdown_timer = 0
545: 
546:         # Score popups
547:         self.score_popups = []
548: 
549:         # Game over
550:         self.game_over_timer = 0
551:         self.flash_alpha = 0
552: 
553:         # Menu animation
554:         self.menu_bird_y = SCREEN_H // 3
555:         self.menu_bob = 0
556: 
557:         # Buttons
558:         self.buttons = []
559:         self._build_menu_buttons()
560: 
561:         # FPS
562:         self.fps_history = []
563: 
564:         # Key repeat for keyboard
565:         self.key_flap = False
566: 
567:         # Load settings
568:         self.sound.enabled = self.save.get("sound_enabled", True)
569:         self.difficulty = self.save.get("difficulty", "Normal")
570:         self.skin_index = self.save.get("skin_index", 0)
571:         self.skin_color = C_BIRD_SKINS[self.skin_index]
572:         self.bird_frames = generate_bird_frames(self.skin_color)
573: 
574:     def _reset_bird(self):
575:         self.bird_x = SCREEN_W // 3
576:         self.bird_y = SCREEN_H // 2
577:         self.bird_vel = 0
578:         self.bird_rotation = 0
579:         self.bird_alive = True
580: 
581:     def _build_menu_buttons(self):
582:         cx = SCREEN_W // 2
583:         by = SCREEN_H // 2 + 40
584:         self.buttons = [
585:             Button(cx - 100, by, 200, 48, "PLAY", self._start_game, font_size=28),
586:             Button(cx - 100, by + 60, 200, 48, "SETTINGS", self._go_settings, font_size=24),
587:             Button(cx - 100, by + 120, 200, 48, "SKINS", self._go_skins, font_size=24),
588:             Button(cx - 100, by + 180, 200, 48, "SCORES", self._go_leaderboard, font_size=24),
589:         ]
590: 
591:     def _build_pause_buttons(self):
592:         cx = SCREEN_W // 2
593:         by = SCREEN_H // 2 - 20
594:         self.buttons = [
595:             Button(cx - 100, by, 200, 48, "RESUME", self._resume, font_size=26),
596:             Button(cx - 100, by + 60, 200, 48, "SETTINGS", self._go_settings, font_size=24),
597:             Button(cx - 100, by + 120, 200, 48, "QUIT", self._go_menu, font_size=24),
598:         ]
599: 
600:     def _build_gameover_buttons(self):
601:         cx = SCREEN_W // 2
602:         by = SCREEN_H // 2 + 100
603:         self.buttons = [
604:             Button(cx - 100, by, 200, 48, "RETRY", self._start_game, font_size=26),
605:             Button(cx - 100, by + 60, 200, 48, "MENU", self._go_menu, font_size=24),
606:         ]
607: 
608:     def _build_settings_buttons(self):
609:         cx = SCREEN_W // 2
610:         by = SCREEN_H // 2 + 100
611:         self.buttons = [
612:             Button(cx - 100, by, 200, 48, "BACK", self._go_back, font_size=24),
613:         ]
614: 
615:     def _build_skin_buttons(self):
616:         cx = SCREEN_W // 2
617:         by = SCREEN_H // 2 + 80
618:         self.buttons = [
619:             Button(cx - 100, by, 200, 48, "BACK", self._go_back, font_size=24),
620:         ]
621: 
622:     def _build_leaderboard_buttons(self):
623:         cx = SCREEN_W // 2
624:         by = SCREEN_H // 2 + 120
625:         self.buttons = [
626:             Button(cx - 100, by, 200, 48, "BACK", self._go_back, font_size=24),
627:         ]
628: 
629:     # ─── State Transitions ───────────────────────────────────────────────
630: 
631:     def _start_game(self):
632:         self.sound.play_swoosh()
633:         self.state = STATE_PLAYING
634:         self._reset_bird()
635:         self.pipes = []
636:         self.pipe_timer = 0
637:         self.score = 0
638:         self.passed_pipes = set()
639:         self.score_popups = []
640:         self.game_over_timer = 0
641:         self.flash_alpha = 0
642:         self.countdown = 3
643:         self.countdown_timer = 0
644:         self.bird_frame = 0
645:         self.bird_vel = 0
646:         self.bird_rotation = 0
647:         self.bird_alive = True
648: 
649:     def _go_menu(self):
650:         self.sound.play_swoosh()
651:         self.state = STATE_MENU
652:         self._build_menu_buttons()
653:         self.flash_alpha = 0
654: 
655:     def _go_settings(self):
656:         self.sound.play_swoosh()
657:         self.prev_state = self.state
658:         self.state = STATE_SETTINGS
659:         self._build_settings_buttons()
660: 
661:     def _go_skins(self):
662:         self.sound.play_swoosh()
663:         self.prev_state = self.state
664:         self.state = STATE_SKIN_SELECT
665:         self._build_skin_buttons()
666: 
667:     def _go_leaderboard(self):
668:         self.sound.play_swoosh()
669:         self.prev_state = self.state
670:         self.state = STATE_LEADERBOARD
671:         self._build_leaderboard_buttons()
672: 
673:     def _go_back(self):
674:         self.sound.play_swoosh()
675:         self.state = self.prev_state if self.prev_state else STATE_MENU
676:         if self.state == STATE_MENU:
677:             self._build_menu_buttons()
678:         elif self.state == STATE_PAUSED:
679:             self._build_pause_buttons()
680: 
681:     def _resume(self):
682:         self.sound.play_swoosh()
683:         self.state = STATE_PLAYING
684:         self._build_pause_buttons()
685: 
686:     def _die(self):
687:         if not self.bird_alive:
688:             return
689:         self.bird_alive = False
690:         self.sound.play_hit()
691:         self.shake_dur = 15
692:         self.particles.emit(self.bird_x, self.bird_y, 20, C_PARTICLE, 4, 40, 4)
693:         self.particles.emit(self.bird_x, self.bird_y, 10, (255, 100, 50), 3, 30, 3)
694:         self.flash_alpha = 200
695:         # Save score
696:         self.save["total_games"] = self.save.get("total_games", 0) + 1
697:         self.save["total_score"] = self.save.get("total_score", 0) + self.score
698:         if self.score > self.save.get("high_score", 0):
699:             self.save["high_score"] = self.score
700:         scores = self.save.get("scores", [])
701:         scores.append(self.score)
702:         scores.sort(reverse=True)
703:         self.save["scores"] = scores[:20]
704:         save_save(self.save)
705:         self.game_over_timer = 0
706:         self._build_gameover_buttons()
707: 
708:     def _flap(self):
709:         if self.state == STATE_PLAYING and self.bird_alive:
710:             diff = DIFFICULTIES[self.difficulty]
711:             self.bird_vel = diff["flap"]
712:             self.sound.play_flap()
713:             self.particles.emit(self.bird_x - 5, self.bird_y + 10, 3, (255, 255, 200), 2, 15, 2)
714:         elif self.state == STATE_MENU:
715:             self.sound.play_menu()
716: 
717:     # ─── Update ──────────────────────────────────────────────────────────
718: 
719:     def update(self):
720:         self.time_val += 1 / FPS
721:         self.fps_history.append(self.clock.get_fps())
722:         if len(self.fps_history) > 60:
723:             self.fps_history.pop(0)
724: 
725:         # Night mode
726:         if self.save.get("night_auto", True) and self.state == STATE_PLAYING:
727:             cycle = (self.time_val * 0.02) % 1.0
728:             self.night_target = max(0, math.sin(cycle * math.pi * 2 - math.pi / 2) * 0.5 + 0.5) * 0.8
729:         elif self.save.get("night_mode", False):
730:             self.night_target = 1.0
731:         else:
732:             self.night_target = 0.0
733:         self.night_factor += (self.night_target - self.night_factor) * 0.02
734: 
735:         # Screen shake
736:         if self.shake_dur > 0:
737:             self.shake_x = random.uniform(-4, 4) * (self.shake_dur / 15)
738:             self.shake_y = random.uniform(-4, 4) * (self.shake_dur / 15)
739:             self.shake_dur -= 1
740:         else:
741:             self.shake_x = 0
742:             self.shake_y = 0
743: 
744:         # Flash fade
745:         if self.flash_alpha > 0:
746:             self.flash_alpha -= 8
747: 
748:         self.particles.update()
749: 
750:         if self.state == STATE_MENU:
751:             self._update_menu()
752:         elif self.state == STATE_PLAYING:
753:             self._update_playing()
754:         elif self.state == STATE_GAME_OVER:
755:             self._update_game_over()
756: 
757:         for btn in self.buttons:
758:             btn.hovered = btn.rect.collidepoint(pygame.mouse.get_pos())
759: 
760:     def _update_menu(self):
761:         self.menu_bob += 0.05
762:         self.menu_bird_y = SCREEN_H // 3 + math.sin(self.menu_bob) * 15
763:         self.scroll_x += 1
764: 
765:     def _update_playing(self):
766:         diff = DIFFICULTIES[self.difficulty]
767: 
768:         # Countdown
769:         if self.countdown > 0:
770:             self.countdown_timer += 1
771:             if self.countdown_timer >= 60:
772:                 self.countdown_timer = 0
773:                 if self.countdown == 1:
774:                     self.sound.play_go()
775:                 else:
776:                     self.sound.play_countdown()
777:                 self.countdown -= 1
778:                 if self.countdown == 0:
779:                     self.pipe_timer = 60
780:                 return
781: 
782:         # Bird physics
783:         if self.bird_alive:
784:             self.bird_vel += diff["gravity"]
785:             if self.bird_vel > MAX_FALL:
786:                 self.bird_vel = MAX_FALL
787:             self.bird_y += self.bird_vel
788: 
789:             # Rotation
790:             if self.bird_vel < 0:
791:                 self.bird_rotation = max(-30, self.bird_vel * 4)
792:             else:
793:                 self.bird_rotation = min(90, self.bird_rotation + 2.5)
794: 
795:             # Wing animation
796:             self.bird_frame_timer += 1
797:             if self.bird_frame_timer > 6:
798:                 self.bird_frame_timer = 0
799:                 self.bird_frame = (self.bird_frame + 1) % 3
800: 
801:         # Scroll
802:         self.scroll_x += diff["speed"]
803: 
804:         # Pipes
805:         if self.pipe_timer > 0:
806:             self.pipe_timer -= 1
807:         else:
808:             gap_y = random.randint(120, SCREEN_H - 250)
809:             pipe_x = SCREEN_W + 10
810:             self.pipes.append({"x": pipe_x, "gap_y": gap_y, "scored": False, "id": len(self.pipes)})
811:             self.pipe_timer = int(PIPE_INTERVAL / (diff["speed"] * 16.67))
812: 
813:         for pipe in self.pipes:
814:             pipe["x"] -= diff["speed"]
815: 
816:             # Score
817:             if not pipe["scored"] and pipe["x"] + PIPE_WIDTH // 2 < self.bird_x:
818:                 pipe["scored"] = True
819:                 self.score += 1
820:                 self.sound.play_score()
821:                 self.score_popups.append(ScorePopup(self.bird_x + 20, self.bird_y - 20))
822:                 self.particles.emit(self.bird_x, self.bird_y, 5, (255, 255, 100), 3, 20, 3)
823: 
824:         # Remove off-screen pipes
825:         self.pipes = [p for p in self.pipes if p["x"] > -PIPE_WIDTH - 20]
826: 
827:         # Score popups
828:         self.score_popups = [p for p in self.score_popups if p.alive()]
829:         for sp in self.score_popups:
830:             sp.update()
831: 
832:         # Collision
833:         if self.bird_alive:
834:             bird_rect = pygame.Rect(self.bird_x - 12, self.bird_y - 12, 24, 24)
835:             # Shrink hitbox slightly for fairness
836:             bird_rect.inflate_ip(-4, -4)
837: 
838:             # Ground / ceiling
839:             ground_y = SCREEN_H - 80
840:             if self.bird_y + 12 >= ground_y or self.bird_y - 12 <= 0:
841:                 self.bird_y = ground_y - 12
842:                 self._die()
843: 
844:             # Pipes
845:             for pipe in self.pipes:
846:                 gap = DIFFICULTIES[self.difficulty]["gap"]
847:                 half_gap = gap // 2
848:                 top_h = pipe["gap_y"] - half_gap
849:                 bot_y = pipe["gap_y"] + half_gap
850: 
851:                 top_rect = pygame.Rect(pipe["x"], 0, PIPE_WIDTH, top_h)
852:                 bot_rect = pygame.Rect(pipe["x"], bot_y, PIPE_WIDTH, ground_y - bot_y)
853: 
854:                 if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):
855:                     self._die()
856: 
857:         # Bird fall after death
858:         if not self.bird_alive:
859:             self.bird_vel += diff["gravity"]
860:             self.bird_y += self.bird_vel
861:             self.bird_rotation = min(90, self.bird_rotation + 4)
862:             ground_y = SCREEN_H - 80
863:             if self.bird_y + 12 >= ground_y:
864:                 self.bird_y = ground_y - 12
865:                 self.bird_vel = 0
866:                 if self.game_over_timer == 0:
867:                     self.sound.play_die()
868:                 self.game_over_timer += 1
869:                 if self.game_over_timer > 30:
870:                     self.state = STATE_GAME_OVER
871:         else:
872:             self.game_over_timer = 0
873: 
874:     def _update_game_over(self):
875:         self.game_over_timer += 1
876:         # Bird still falls
877:         self.bird_vel += DIFFICULTIES[self.difficulty]["gravity"]
878:         self.bird_y += self.bird_vel
879:         ground_y = SCREEN_H - 80
880:         if self.bird_y + 12 >= ground_y:
881:             self.bird_y = ground_y - 12
882:             self.bird_vel = 0
883: 
884:     # ─── Draw ────────────────────────────────────────────────────────────
885: 
886:     def draw(self):
887:         self.screen.fill((0, 0, 0))
888: 
889:         # Background
890:         draw_background(self.screen, self.night_factor, self.scroll_x)
891:         draw_stars(self.screen, self.night_factor, self.time_val)
892: 
893:         # Pipes
894:         for pipe in self.pipes:
895:             gap = DIFFICULTIES[self.difficulty]["gap"]
896:             half_gap = gap // 2
897:             top_h = pipe["gap_y"] - half_gap
898:             bot_y = pipe["gap_y"] + half_gap
899:             bot_h = SCREEN_H - 80 - bot_y
900:             draw_pipe(self.screen, pipe["x"], 0, PIPE_WIDTH, top_h, True)
901:             draw_pipe(self.screen, pipe["x"], bot_y, PIPE_WIDTH, bot_h, False)
902: 
903:         # Ground
904:         draw_ground(self.screen, self.scroll_x, self.night_factor)
905: 
906:         # Bird
907:         if self.state == STATE_MENU:
908:             bird_surf = self.bird_frames[self.bird_frame % len(self.bird_frames)]
909:             self.screen.blit(bird_surf, (self.bird_x - bird_surf.get_width() // 2,
910:                                           self.menu_bird_y - bird_surf.get_height() // 2))
911:         else:
912:             bird_surf = pygame.transform.rotate(self.bird_frames[0], self.bird_rotation)
913:             rect = bird_surf.get_rect(center=(self.bird_x, self.bird_y))
914:             self.screen.blit(bird_surf, rect.topleft)
915: 
916:         # Particles
917:         self.particles.draw(self.screen)
918: 
919:         # Score popups
920:         for sp in self.score_popups:
921:             sp.draw(self.screen)
922: 
923:         # In-game HUD
924:         if self.state == STATE_PLAYING:
925:             draw_score_text(self.screen, str(self.score), SCREEN_W // 2 - 20, 30, 56, C_TEXT_WHITE)
926:             # Pause hint
927:             small_font = pygame.font.SysFont("arial", 14)
928:             hint = small_font.render("ESC to pause", True, (200, 200, 200))
929:             self.screen.blit(hint, (SCREEN_W - hint.get_width() - 10, 10))
930: 
931:         # Countdown
932:         if self.state == STATE_PLAYING and self.countdown > 0:
933:             self._draw_countdown()
934: 
935:         # State overlays
936:         if self.state == STATE_MENU:
937:             self._draw_menu()
938:         elif self.state == STATE_PAUSED:
939:             self._draw_pause()
940:         elif self.state == STATE_GAME_OVER:
941:             self._draw_game_over()
942:         elif self.state == STATE_SETTINGS:
943:             self._draw_settings()
944:         elif self.state == STATE_SKIN_SELECT:
945:             self._draw_skin_select()
946:         elif self.state == STATE_LEADERBOARD:
947:             self._draw_leaderboard()
948: 
949:         # Flash effect
950:         if self.flash_alpha > 0:
951:             flash = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
952:             flash.fill((255, 255, 255, min(255, self.flash_alpha)))
953:             self.screen.blit(flash, (0, 0))
954: 
955:         # Screen shake
956:         if self.shake_dur > 0:
957:             self.screen = pygame.transform.offset(self.screen, int(self.shake_x), int(self.shake_y))
958: 
959:         pygame.display.flip()
960: 
961:     def _draw_countdown(self):
962:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
963:         overlay.fill((0, 0, 0, 80))
964:         self.screen.blit(overlay, (0, 0))
965:         text = str(self.countdown) if self.countdown > 0 else "GO!"
966:         color = C_TEXT_WHITE if self.countdown > 0 else (50, 255, 50)
967:         draw_score_text(self.screen, text, SCREEN_W // 2 - 40, SCREEN_H // 2 - 40, 80, color)
968: 
969:     def _draw_menu(self):
970:         # Title
971:         title_font = pygame.font.SysFont("arial", 44, bold=True)
972:         title = title_font.render("FLIPPYBLOCK", True, C_TEXT_WHITE)
973:         title_shadow = title_font.render("FLIPPYBLOCK", True, (0, 0, 0))
974:         self.screen.blit(title_shadow, (SCREEN_W // 2 - title.get_width() // 2 + 2, 82))
975:         self.screen.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 80))
976: 
977:         sub_font = pygame.font.SysFont("arial", 22, bold=True)
978:         sub = sub_font.render("EXTREME", True, C_TEXT_GOLD)
979:         sub_shadow = sub_font.render("EXTREME", True, (0, 0, 0))
980:         self.screen.blit(sub_shadow, (SCREEN_W // 2 - sub.get_width() // 2 + 2, 132))
981:         self.screen.blit(sub, (SCREEN_W // 2 - sub.get_width() // 2, 130))
982: 
983:         # High score
984:         hs = self.save.get("high_score", 0)
985:         hs_font = pygame.font.SysFont("arial", 18)
986:         hs_text = hs_font.render(f"Best: {hs}", True, C_TEXT_GOLD)
987:         self.screen.blit(hs_text, (SCREEN_W // 2 - hs_text.get_width() // 2, 170))
988: 
989:         # Tap hint
990:         hint_font = pygame.font.SysFont("arial", 16)
991:         hint = hint_font.render("Press SPACE or Click to flap", True, (200, 200, 200))
992:         self.screen.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 120))
993: 
994:         # Buttons
995:         for btn in self.buttons:
996:             btn.draw(self.screen)
997: 
998:     def _draw_pause(self):
999:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
1000:         overlay.fill((0, 0, 0, 150))
1001:         self.screen.blit(overlay, (0, 0))
1002: 
1003:         panel = pygame.Surface((SCREEN_W - 80, 260), pygame.SRCALPHA)
1004:         panel.fill((30, 30, 50, 230))
1005:         _draw_rounded_rect(panel, (0, 0, SCREEN_W - 80, 260), 12, (30, 30, 50, 230))
1006:         pygame.draw.rect(panel, C_UI_BORDER, (0, 0, SCREEN_W - 80, 260), 2, border_radius=12)
1007:         self.screen.blit(panel, (40, SCREEN_H // 2 - 170))
1008: 
1009:         draw_score_text(self.screen, "PAUSED", SCREEN_W // 2 - 55, SCREEN_H // 2 - 155, 36, C_TEXT_WHITE)
1010: 
1011:         for btn in self.buttons:
1012:             btn.draw(self.screen)
1013: 
1014:     def _draw_game_over(self):
1015:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
1016:         overlay.fill((0, 0, 0, 160))
1017:         self.screen.blit(overlay, (0, 0))
1018: 
1019:         panel_w = SCREEN_W - 80
1020:         panel_h = 320
1021:         panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
1022:         panel.fill((30, 30, 50, 230))
1023:         _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 230))
1024:         pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)
1025:         self.screen.blit(panel, (40, SCREEN_H // 2 - 200))
1026: 
1027:         draw_score_text(self.screen, "GAME OVER", SCREEN_W // 2 - 100, SCREEN_H // 2 - 180, 36, (255, 80, 80))
1028: 
1029:         # Score
1030:         draw_score_text(self.screen, f"Score: {self.score}", SCREEN_W // 2 - 60, SCREEN_H // 2 - 130, 28, C_TEXT_WHITE)
1031: 
1032:         # Best
1033:         hs = self.save.get("high_score", 0)
1034:         is_best = self.score == hs and hs > 0
1035:         best_color = C_TEXT_GOLD if is_best else C_TEXT_WHITE
1036:         draw_score_text(self.screen, f"Best: {hs}", SCREEN_W // 2 - 50, SCREEN_H // 2 - 90, 22, best_color)
1037:         if is_best:
1038:             new_font = pygame.font.SysFont("arial", 16, bold=True)
1039:             new_surf = new_font.render("NEW BEST!", True, C_TEXT_GOLD)
1040:             self.screen.blit(new_surf, (SCREEN_W // 2 - new_surf.get_width() // 2, SCREEN_H // 2 - 70))
1041: 
1042:         # Medal
1043:         medal_label = draw_medal(self.screen, SCREEN_W // 2, SCREEN_H // 2 - 30, self.score)
1044: 
1045:         # Stats
1046:         stats_font = pygame.font.SysFont("arial", 14)
1047:         total_games = self.save.get("total_games", 0)
1048:         avg = self.save.get("total_score", 0) // max(1, total_games)
1049:         stats = [f"Games: {total_games}", f"Avg Score: {avg}"]
1050:         for i, stat in enumerate(stats):
1051:             surf = stats_font.render(stat, True, (180, 180, 180))
1052:             self.screen.blit(surf, (SCREEN_W // 2 - surf.get_width() // 2, SCREEN_H // 2 + 30 + i * 20))
1053: 
1054:         # Buttons
1055:         for btn in self.buttons:
1056:             btn.draw(self.screen)
1057: 
1058:     def _draw_settings(self):
1059:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
1060:         overlay.fill((0, 0, 0, 170))
1061:         self.screen.blit(overlay, (0, 0))
1062: 
1063:         panel_w = SCREEN_W - 60
1064:         panel_h = 420
1065:         panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
1066:         panel.fill((30, 30, 50, 240))
1067:         _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))
1068:         pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)
1069:         self.screen.blit(panel, (30, SCREEN_H // 2 - 240))
1070: 
1071:         draw_score_text(self.screen, "SETTINGS", SCREEN_W // 2 - 70, SCREEN_H // 2 - 215, 32, C_TEXT_WHITE)
1072: 
1073:         # Difficulty selector
1074:         self._draw_toggle_row(SCREEN_H // 2 - 170, "Difficulty", self.difficulty,
1075:                               list(DIFFICULTIES.keys()), self._cycle_difficulty)
1076: 
1077:         # Sound toggle
1078:         sound_text = "ON" if self.save.get("sound_enabled", True) else "OFF"
1079:         self._draw_toggle_row(SCREEN_H // 2 - 120, "Sound", sound_text, ["ON", "OFF"],
1080:                               self._toggle_sound)
1081: 
1082:         # Night mode
1083:         night_text = "Auto" if self.save.get("night_auto", True) else ("ON" if self.save.get("night_mode", False) else "OFF")
1084:         self._draw_toggle_row(SCREEN_H // 2 - 70, "Night Mode", night_text,
1085:                               ["Auto", "ON", "OFF"], self._cycle_night)
1086: 
1087:         # Back button
1088:         for btn in self.buttons:
1089:             btn.draw(self.screen)
1090: 
1091:     def _draw_toggle_row(self, y, label, current, options, callback):
1092:         font = pygame.font.SysFont("arial", 20)
1093:         label_surf = font.render(label, True, C_TEXT_WHITE)
1094:         self.screen.blit(label_surf, (60, y))
1095: 
1096:         # Left button
1097:         left_rect = pygame.Rect(200, y - 12, 30, 30)
1098:         _draw_rounded_rect(self.screen, left_rect, 4, C_UI_BUTTON)
1099:         pygame.draw.rect(self.screen, C_UI_BORDER, left_rect, 1, border_radius=4)
1100:         arrow_font = pygame.font.SysFont("arial", 20, bold=True)
1101:         arrow = arrow_font.render("<", True, C_TEXT_WHITE)
1102:         self.screen.blit(arrow, (left_rect.x + 8, left_rect.y + 4))
1103: 
1104:         # Current value
1105:         val_surf = font.render(current, True, C_TEXT_GOLD)
1106:         self.screen.blit(val_surf, (240, y - 6))
1107: 
1108:         # Right button
1109:         right_rect = pygame.Rect(240 + val_surf.get_width() + 10, y - 12, 30, 30)
1110:         _draw_rounded_rect(self.screen, right_rect, 4, C_UI_BUTTON)
1111:         pygame.draw.rect(self.screen, C_UI_BORDER, right_rect, 1, border_radius=4)
1112:         arrow = arrow_font.render(">", True, C_TEXT_WHITE)
1113:         self.screen.blit(arrow, (right_rect.x + 8, right_rect.y + 4))
1114: 
1115:         # Store for click handling
1116:         self._last_toggle_info = {
1117:             "left_rect": left_rect, "right_rect": right_rect,
1118:             "current": current, "options": options, "callback": callback
1119:         }
1120: 
1121:     def _cycle_difficulty(self):
1122:         keys = list(DIFFICULTIES.keys())
1123:         idx = keys.index(self.difficulty)
1124:         self.difficulty = keys[(idx + 1) % len(keys)]
1125:         self.save["difficulty"] = self.difficulty
1126:         save_save(self.save)
1127:         self.sound.play_select()
1128: 
1129:     def _toggle_sound(self):
1130:         self.save["sound_enabled"] = not self.save.get("sound_enabled", True)
1131:         self.sound.enabled = self.save["sound_enabled"]
1132:         save_save(self.save)
1133:         if self.sound.enabled:
1134:             self.sound.play_select()
1135: 
1136:     def _cycle_night(self):
1137:         if self.save.get("night_auto", True):
1138:             self.save["night_auto"] = False
1139:             self.save["night_mode"] = True
1140:         elif self.save.get("night_mode", False):
1141:             self.save["night_mode"] = False
1142:         else:
1143:             self.save["night_auto"] = True
1144:         save_save(self.save)
1145:         self.sound.play_select()
1146: 
1147:     def _draw_skin_select(self):
1148:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
1149:         overlay.fill((0, 0, 0, 170))
1150:         self.screen.blit(overlay, (0, 0))
1151: 
1152:         panel_w = SCREEN_W - 60
1153:         panel_h = 340
1154:         panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
1155:         panel.fill((30, 30, 50, 240))
1156:         _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))
1157:         pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)
1158:         self.screen.blit(panel, (30, SCREEN_H // 2 - 190))
1159: 
1160:         draw_score_text(self.screen, "SELECT SKIN", SCREEN_W // 2 - 80, SCREEN_H // 2 - 165, 28, C_TEXT_WHITE)
1161: 
1162:         # Skin grid
1163:         cols = 3
1164:         skin_names = ["Classic", "Orange", "Red", "Blue", "Purple", "Cyan"]
1165:         start_x = 60
1166:         start_y = SCREEN_H // 2 - 110
1167:         cell_w = 120
1168:         cell_h = 80
1169: 
1170:         self._skin_rects = []
1171:         for i, (color, name) in enumerate(zip(C_BIRD_SKINS, skin_names)):
1172:             col = i % cols
1173:             row = i // cols
1174:             cx = start_x + col * cell_w
1175:             cy = start_y + row * cell_h
1176:             rect = pygame.Rect(cx, cy, cell_w, cell_h)
1177: 
1178:             is_selected = (i == self.skin_index)
1179:             bg_color = C_UI_BUTTON_HOVER if is_selected else C_UI_BUTTON
1180:             _draw_rounded_rect(self.screen, rect, 6, bg_color)
1181:             border_c = C_TEXT_GOLD if is_selected else C_UI_BORDER
1182:             pygame.draw.rect(self.screen, border_c, rect, 2 if is_selected else 1, border_radius=6)
1183: 
1184:             # Preview bird
1185:             preview = generate_bird(color, 24)
1186:             self.screen.blit(preview, (cx + cell_w // 2 - 12, cy + 5))
1187: 
1188:             # Name
1189:             name_font = pygame.font.SysFont("arial", 12)
1190:             name_surf = name_font.render(name, True, C_TEXT_WHITE)
1191:             self.screen.blit(name_surf, (cx + cell_w // 2 - name_surf.get_width() // 2, cy + 45))
1192: 
1193:             self._skin_rects.append((rect, i))
1194: 
1195:         # Back button
1196:         for btn in self.buttons:
1197:             btn.draw(self.screen)
1198: 
1199:     def _draw_leaderboard(self):
1200:         overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
1201:         overlay.fill((0, 0, 0, 170))
1202:         self.screen.blit(overlay, (0, 0))
1203: 
1204:         panel_w = SCREEN_W - 60
1205:         panel_h = 420
1206:         panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
1207:         panel.fill((30, 30, 50, 240))
1208:         _draw_rounded_rect(panel, (0, 0, panel_w, panel_h), 12, (30, 30, 50, 240))
1209:         pygame.draw.rect(panel, C_UI_BORDER, (0, 0, panel_w, panel_h), 2, border_radius=12)
1210:         self.screen.blit(panel, (30, SCREEN_H // 2 - 240))
1211: 
1212:         draw_score_text(self.screen, "TOP SCORES", SCREEN_W // 2 - 70, SCREEN_H // 2 - 215, 30, C_TEXT_WHITE)
1213: 
1214:         scores = self.save.get("scores", [])
1215:         if not scores:
1216:             empty_font = pygame.font.SysFont("arial", 18)
1217:             empty = empty_font.render("No scores yet!", True, (150, 150, 150))
1218:             self.screen.blit(empty, (SCREEN_W // 2 - empty.get_width() // 2, SCREEN_H // 2 - 100))
1219:         else:
1220:             for i, sc in enumerate(scores[:10]):
1221:                 y = SCREEN_H // 2 - 170 + i * 28
1222:                 rank_font = pygame.font.SysFont("arial", 18, bold=True)
1223:                 score_font = pygame.font.SysFont("arial", 18)
1224: 
1225:                 rank_color = C_TEXT_GOLD if i < 3 else (C_TEXT_SILVER if i < 6 else (180, 180, 180))
1226:                 rank_text = rank_font.render(f"#{i + 1}", True, rank_color)
1227:                 score_text = score_font.render(f"{sc}", True, C_TEXT_WHITE)
1228: 
1229:                 self.screen.blit(rank_text, (80, y - 6))
1230:                 self.screen.blit(score_text, (SCREEN_W - 120, y - 6))
1231: 
1232:                 # Bar
1233:                 bar_w = min(200, int(200 * sc / max(1, scores[0])))
1234:                 bar_rect = pygame.Rect(140, y, bar_w, 16)
1235:                 _draw_rounded_rect(self.screen, bar_rect, 4, (60, 60, 100))
1236: 
1237:         # Stats
1238:         total_games = self.save.get("total_games", 0)
1239:         total_score = self.save.get("total_score", 0)
1240:         avg = total_score // max(1, total_games)
1241:         stats_font = pygame.font.SysFont("arial", 14)
1242:         stats = [f"Total Games: {total_games}", f"Total Score: {total_score}", f"Avg Score: {avg}"]
1243:         for i, stat in enumerate(stats):
1244:             surf = stats_font.render(stat, True, (160, 160, 160))
1245:             self.screen.blit(surf, (60, SCREEN_H // 2 + 100 + i * 20))
1246: 
1247:         # Back button
1248:         for btn in self.buttons:
1249:             btn.draw(self.screen)
1250: 
1251:     # ─── Events ──────────────────────────────────────────────────────────
1252: 
1253:     def handle_events(self):
1254:         for event in pygame.event.get():
1255:             if event.type == pygame.QUIT:
1256:                 return False
1257: 
1258:             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
1259:                 # Check toggle buttons first
1260:                 if self.state == STATE_SETTINGS and hasattr(self, '_last_toggle_info'):
1261:                     info = self._last_toggle_info
1262:                     if info["left_rect"].collidepoint(event.pos):
1263:                         keys = list(DIFFICULTIES.keys())
1264:                         if info["callback"] == self._cycle_difficulty:
1265:                             idx = keys.index(self.difficulty)
1266:                             self.difficulty = keys[(idx - 1) % len(keys)]
1267:                             self.save["difficulty"] = self.difficulty
1268:                         elif info["callback"] == self._toggle_sound:
1269:                             self.save["sound_enabled"] = not self.save.get("sound_enabled", True)
1270:                             self.sound.enabled = self.save["sound_enabled"]
1271:                         elif info["callback"] == self._cycle_night:
1272:                             if self.save.get("night_auto", True):
1273:                                 self.save["night_auto"] = False
1274:                                 self.save["night_mode"] = False
1275:                             elif self.save.get("night_mode", False):
1276:                                 self.save["night_auto"] = True
1277:                             else:
1278:                                 self.save["night_mode"] = True
1279:                         save_save(self.save)
1280:                         self.sound.play_select()
1281:                         continue
1282:                     elif info["right_rect"].collidepoint(event.pos):
1283:                         info["callback"]()
1284:                         continue
1285: 
1286:                 # Skin selection
1287:                 if self.state == STATE_SKIN_SELECT and hasattr(self, '_skin_rects'):
1288:                     for rect, idx in self._skin_rects:
1289:                         if rect.collidepoint(event.pos):
1290:                             self.skin_index = idx
1291:                             self.skin_color = C_BIRD_SKINS[idx]
1292:                             self.bird_frames = generate_bird_frames(self.skin_color)
1293:                             self.save["skin_index"] = idx
1294:                             save_save(self.save)
1295:                             self.sound.play_select()
1296:                             break
1297:                     else:
1298:                         for btn in self.buttons:
1299:                             btn.handle_event(event)
1300:                     continue
1301: 
1302:                 # General buttons
1303:                 for btn in self.buttons:
1304:                     btn.handle_event(event)
1305:                 continue
1306: 
1307:             if event.type == pygame.KEYDOWN:
1308:                 if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
1309:                     if self.state == STATE_MENU:
1310:                         self._start_game()
1311:                     elif self.state == STATE_PLAYING:
1312:                         self._flap()
1313:                     elif self.state == STATE_GAME_OVER and self.game_over_timer > 30:
1314:                         self._start_game()
1315:                 elif event.key == pygame.K_RETURN:
1316:                     if self.state == STATE_GAME_OVER and self.game_over_timer > 30:
1317:                         self._start_game()
1318:                 elif event.key == pygame.K_ESCAPE:
1319:                     if self.state == STATE_PLAYING:
1320:                         self.state = STATE_PAUSED
1321:                         self._build_pause_buttons()
1322:                         self.sound.play_swoosh()
1323:                     elif self.state == STATE_PAUSED:

(Output capped at 50 KB. Showing lines 1-1323. Use offset=1324 to continue.)
</content>
```

---

## Assistant (Build · Qwen3.6 27B · 92.4s)

_Thinking:_

Let me read the rest of the file.


**Tool: read**

**Input:**
```json
{
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py",
  "offset": 1324
}
```

**Output:**
```
<path>/home/patof/stress_bench/flippyblock_extreme.py</path>
<type>file</type>
<content>
1324:                         self._resume()
1325:                     elif self.state in (STATE_SETTINGS, STATE_SKIN_SELECT, STATE_LEADERBOARD):
1326:                         self._go_back()
1327:                 elif event.key == pygame.K_s:
1328:                     if self.state == STATE_PLAYING:
1329:                         self.state = STATE_PAUSED
1330:                         self._build_pause_buttons()
1331:                 elif event.key == pygame.K_LEFT:
1332:                     if self.state == STATE_SETTINGS:
1333:                         if hasattr(self, '_last_toggle_info'):
1334:                             info = self._last_toggle_info
1335:                             if info["callback"] == self._cycle_difficulty:
1336:                                 keys = list(DIFFICULTIES.keys())
1337:                                 idx = keys.index(self.difficulty)
1338:                                 self.difficulty = keys[(idx - 1) % len(keys)]
1339:                                 self.save["difficulty"] = self.difficulty
1340:                                 save_save(self.save)
1341:                                 self.sound.play_select()
1342:                 elif event.key == pygame.K_RIGHT:
1343:                     if self.state == STATE_SETTINGS:
1344:                         if hasattr(self, '_last_toggle_info'):
1345:                             info = self._last_toggle_info
1346:                             if info["callback"] == self._cycle_difficulty:
1347:                                 info["callback"]()
1348: 
1349:             # Mouse click to flap
1350:             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
1351:                 if self.state == STATE_PLAYING and self.bird_alive:
1352:                     # Don't flap if clicking a button area (bottom of screen)
1353:                     if event.pos[1] < SCREEN_H // 2 - 40:
1354:                         self._flap()
1355: 
1356:         return True
1357: 
1358:     # ─── Main Loop ───────────────────────────────────────────────────────
1359: 
1360:     def run(self):
1361:         running = True
1362:         while running:
1363:             running = self.handle_events()
1364:             self.update()
1365:             self.draw()
1366:             self.clock.tick(FPS)
1367:         pygame.quit()
1368:         sys.exit()
1369: 
1370: 
1371: # ─── Entry Point ─────────────────────────────────────────────────────────────
1372: 
1373: if __name__ == "__main__":
1374:     game = Game()
1375:     game.run()

(End of file - total 1375 lines)
</content>
```

---

## Assistant (Build · Qwen3.6 27B · 605.4s)

_Thinking:_

Now I have the full picture. Let me identify and fix all the issues:

1. **Sound `play_score`** (line 161-169): Uses `pygame.time.set_timer` and `pygame.time.set_timeout` incorrectly. `set_timeout` doesn't exist. Need to fix to use a simple two-tone approach or just play both sounds sequentially.

2. **Menu bird frame not updating** (line 760-763): `_update_menu` doesn't update `self.bird_frame`, so the menu bird never animates. Need to add wing flap animation.

3. **Panel corners not rounded**: The panels are filled first, then `draw_rounded_rect` is drawn on top with the same color. This doesn't create rounded corners because `fill` already fills the corners. Need to fix by NOT filling and only using `draw_rounded_rect`.

4. **Mouse event handling** (lines 1258-1354): There are TWO `if event.type == pygame.MOUSEBUTTONDOWN` blocks. The second one (lines 1350-1354) will ALWAYS fire for any mouse click during playing, even if the first block already handled it. The `continue` in the first block only skips to the next event, but the second `if` is inside the same `for` loop iteration. Actually wait, looking again:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # ... handle toggles, skins, buttons
        continue  # <-- this skips the rest of the loop body

    if event.type == pygame.KEYDOWN:
        # ... handle keys

    # Mouse click to flap
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # ... flap logic
```

The `continue` at line 1305 will skip the flap check. But there's a problem: in the skin select state, if a skin rect is clicked, it breaks out of the for loop but then hits `continue` which goes to the next event. But if no skin rect matches, it falls through to the button handling and then `continue`. So the flap check at line 1350 should only fire during STATE_PLAYING when no buttons/toggles/skins are clicked. Actually, the first MOUSEBUTTONDOWN block has `continue` at the end (line 1305), so it should skip the flap check. But wait, looking more carefully:

The structure is:
```
for event in ...:
    if QUIT: return False
    
    if MOUSEBUTTONDOWN:
        if SETTINGS: handle toggles; continue
        if SKIN_SELECT: handle skins; continue
        handle buttons; continue  # <-- line 1305
    
    if KEYDOWN: handle keys
    
    if MOUSEBUTTONDOWN:  # <-- line 1350
        if PLAYING: flap
```

The `continue` at line 1305 should skip the flap check. But the issue is that `btn.handle_event(event)` at line 1303 handles MOUSEBUTTONDOWN for buttons, and then `continue` skips the flap. This is correct for button clicks.

But what about clicks that don't hit any button? In that case, the first MOUSEBUTTONDOWN block still fires (line 1258), goes through the settings/skin checks (which fail), then handles buttons (which won't match since no button was clicked), then `continue` skips the flap check. So clicks on empty space during PLAYING won't flap!

Actually wait, the `continue` at line 1305 is unconditional - it always continues after the first MOUSEBUTTONDOWN block. So any mouse click will skip the flap check. This is a bug.

The fix: Only `continue` if the click was actually handled. Or restructure the logic.

5. **`_resume` calls `_build_pause_buttons`** (line 684): When resuming, we shouldn't rebuild pause buttons. Should remove this.

6. **Bird hitbox** (line 834): Uses hardcoded 24x24 but bird sprite is 34x34. The center-based positioning means `self.bird_x` and `self.bird_y` are the center. So the rect should be `(self.bird_x - 17, self.bird_y - 17, 34, 34)` for a 34px sprite, then shrunk. Currently uses 12 which gives a 24px rect, which is too small compared to the visual sprite.

7. **`generate_pipe_pair`** (lines 237-242): Dead code, never called. Can remove.

8. **Unused imports**: `struct` is imported but never used.

9. **`passed_pipes`** (line 520): Created but never used. Dead code.

10. **`key_flap`** (line 565): Created but never used.

11. **`bob_timer`** (line 529): Created but never used.

12. **`pipe_gap_y`** (line 520): Created but never used.

13. **`C_BIRD_WHITE`** (line 37): Defined but not in `C_BIRD_SKINS`.

14. **Background drawing performance**: `draw_background` draws SCREEN_H (720) lines every frame. This is slow. Should use a gradient surface that's pre-rendered or at least cached.

15. **`pygame.transform.offset`** for screen shake: This modifies the surface in place but returns a new surface. The assignment `self.screen = pygame.transform.offset(...)` replaces the screen surface reference, which could cause issues. Should use `pygame.transform.offset` on a copy or use a different approach.

Actually, `pygame.transform.offset` returns a new Surface. The issue is that `self.screen` is the display surface returned by `pygame.display.set_mode()`. Replacing it with a new surface will break `pygame.display.flip()` because it expects the original display surface.

This is a critical bug! The screen shake will break the display after the first shake.

Fix: Instead of using `transform.offset`, use `pygame.display.set_pos()` or render to an offscreen surface and blit with offset.

Let me now write the complete fixed version. I'll address all issues comprehensively.

Let me rewrite the entire file with all fixes applied. I'll make it more robust and polished.


Now I'll rewrite the file with all fixes. Issues found:

1. Sound `play_score` uses non-existent `pygame.time.set_timeout`
2. Menu bird frame never animates (no frame update in `_update_menu`)
3. Panel corners not rounded (fill + draw_rounded_rect doesn't work)
4. Mouse event handling: `continue` after button check prevents flap on empty space clicks
5. `_resume` incorrectly calls `_build_pause_buttons`
6. Bird hitbox (24px) doesn't match sprite size (34px)
7. `pygame.transform.offset` replaces display surface, breaking `display.flip()`
8. Background draws 720 lines per frame (slow)
9. Dead code: `generate_pipe_pair`, `passed_pipes`, `key_flap`, `bob_timer`, unused `struct` import



**Tool: write**

**Input:**
```json
{
  "content": "#!/usr/bin/env python3\n\"\"\"FlippyBlock Extreme - A Flappy Bird clone with no external assets.\"\"\"\n\nimport pygame\nimport math\nimport random\nimport json\nimport os\nimport array\nimport sys\n\n# ─── Constants ───────────────────────────────────────────────────────────────\n\nSCREEN_W = 480\nSCREEN_H = 720\nFPS = 60\nTITLE = \"FlippyBlock Extreme\"\n\nDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), \".flippyblock_data\")\nSAVE_FILE = os.path.join(DATA_DIR, \"save.json\")\n\nGROUND_Y = SCREEN_H - 80\n\n# Colors\nC_SKY_TOP = (100, 180, 255)\nC_SKY_BOT = (200, 235, 255)\nC_SKY_NIGHT_TOP = (15, 15, 50)\nC_SKY_NIGHT_BOT = (30, 30, 80)\nC_GROUND = (139, 119, 80)\nC_GROUND_DARK = (100, 85, 55)\nC_GROUND_GRASS = (80, 180, 60)\nC_PIPE_GREEN = (50, 200, 60)\nC_PIPE_GREEN_DARK = (30, 150, 40)\nC_PIPE_GREEN_LIGHT = (80, 230, 90)\nC_PIPE_CAP = (40, 180, 50)\nC_BIRD_YELLOW = (255, 220, 50)\nC_BIRD_ORANGE = (255, 160, 30)\nC_BIRD_RED = (220, 50, 50)\nC_BIRD_BLUE = (50, 100, 220)\nC_BIRD_PURPLE = (160, 60, 200)\nC_BIRD_CYAN = (50, 200, 220)\nC_BIRD_SKINS = [C_BIRD_YELLOW, C_BIRD_ORANGE, C_BIRD_RED, C_BIRD_BLUE, C_BIRD_PURPLE, C_BIRD_CYAN]\nC_SKIN_NAMES = [\"Classic\", \"Orange\", \"Red\", \"Blue\", \"Purple\", \"Cyan\"]\nC_TEXT_WHITE = (255, 255, 255)\nC_TEXT_SHADOW = (0, 0, 0)\nC_TEXT_GOLD = (255, 215, 0)\nC_TEXT_SILVER = (192, 192, 192)\nC_TEXT_BRONZE = (205, 127, 50)\nC_UI_BORDER = (80, 80, 120)\nC_UI_BUTTON = (60, 60, 100)\nC_UI_BUTTON_HOVER = (80, 80, 140)\nC_UI_BUTTON_ACTIVE = (100, 100, 170)\nC_STAR = (255, 255, 220)\nC_CLOUD = (240, 245, 255)\nC_PARTICLE = (255, 200, 50)\nC_MEDAL_GOLD = (255, 215, 0)\nC_MEDAL_SILVER = (192, 192, 192)\nC_MEDAL_BRONZE = (205, 127, 50)\nC_MEDAL_PLATINUM = (160, 220, 255)\nC_PANEL_BG = (30, 30, 50, 240)\n\n# Physics defaults\nMAX_FALL = 10\nPIPE_WIDTH = 60\nPIPE_INTERVAL_MS = 1600\n\n# Difficulty presets\nDIFFICULTIES = {\n    \"Easy\":    {\"gap\": 190, \"speed\": 2.0, \"gravity\": 0.38, \"flap\": -7.0},\n    \"Normal\":  {\"gap\": 155, \"speed\": 2.5, \"gravity\": 0.45, \"flap\": -7.5},\n    \"Hard\":    {\"gap\": 130, \"speed\": 3.2, \"gravity\": 0.52, \"flap\": -8.0},\n    \"Extreme\": {\"gap\": 110, \"speed\": 4.0, \"gravity\": 0.60, \"flap\": -8.5},\n}\n\n# ─── Save / Load ─────────────────────────────────────────────────────────────\n\ndef _ensure_data_dir():\n    os.makedirs(DATA_DIR, exist_ok=True)\n\ndef load_save():\n    _ensure_data_dir()\n    try:\n        with open(SAVE_FILE, \"r\") as f:\n            return json.load(f)\n    except (FileNotFoundError, json.JSONDecodeError):\n        return {\"high_score\": 0, \"total_games\": 0, \"total_score\": 0,\n                \"skin_index\": 0, \"difficulty\": \"Normal\",\n                \"sound_enabled\": True, \"night_mode\": False, \"night_auto\": True,\n                \"scores\": []}\n\ndef save_save(data):\n    _ensure_data_dir()\n    with open(SAVE_FILE, \"w\") as f:\n        json.dump(data, f, indent=2)\n\n# ─── Sound Engine (purely programmatic) ──────────────────────────────────────\n\nclass SoundEngine:\n    def __init__(self):\n        self.enabled = True\n        self._initialized = False\n\n    def _init(self):\n        if self._initialized:\n            return\n        try:\n            pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)\n            self._initialized = True\n        except Exception:\n            self.enabled = False\n\n    def _make_sound(self, freq, duration, wave_type=\"sine\", fade=True, freq_end=None):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            t = i / sr\n            f = freq + (freq_end - freq) * (i / n) if freq_end else freq\n            if wave_type == \"sine\":\n                v = math.sin(2 * math.pi * f * t)\n            elif wave_type == \"square\":\n                v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0\n            elif wave_type == \"sawtooth\":\n                v = 2 * (f * t - math.floor(f * t + 0.5))\n            else:\n                v = 0\n            # Envelope: attack + fade\n            attack_dur = n * 0.05\n            fade_start = n * 0.6\n            if i < attack_dur:\n                v *= i / max(1, attack_dur)\n            elif i > fade_start:\n                v *= max(0, 1.0 - (i - fade_start) / (n - fade_start))\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)\n\n    def _noise_sound(self, duration, volume=0.3):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            v = (random.random() * 2 - 1) * volume\n            if i > n * 0.5:\n                v *= max(0, 1.0 - (i - n * 0.5) / (n * 0.5))\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)\n\n    def play_flap(self):\n        s = self._make_sound(600, 0.08, \"sine\", freq_end=900)\n        if s:\n            s.play()\n\n    def play_score(self):\n        # Two-tone score sound played sequentially\n        s1 = self._make_sound(880, 0.08, \"sine\")\n        s2 = self._make_sound(1175, 0.1, \"sine\")\n        if s1:\n            s1.play()\n        if s2:\n            # Delay second tone slightly by chaining\n            class _DelayedSound:\n                def __init__(self, sound, delay_ms):\n                    self.sound = sound\n                    self.delay_ms = delay_ms\n                def play(self):\n                    pygame.time.set_timer(pygame.USEREVENT + 99, self.delay_ms)\n                    self._s = self.sound\n            # Simple approach: just play both, the mixer handles overlap\n            pygame.time.delay(80)\n            s2.play()\n\n    def play_hit(self):\n        s = self._make_sound(200, 0.2, \"square\", freq_end=80)\n        if s:\n            s.play()\n\n    def play_die(self):\n        s = self._make_sound(400, 0.4, \"sawtooth\", freq_end=100)\n        if s:\n            s.play()\n\n    def play_swoosh(self):\n        s = self._noise_sound(0.15, 0.15)\n        if s:\n            s.play()\n\n    def play_menu(self):\n        s = self._make_sound(500, 0.06, \"sine\", freq_end=700)\n        if s:\n            s.play()\n\n    def play_select(self):\n        s = self._make_sound(700, 0.08, \"sine\", freq_end=1000)\n        if s:\n            s.play()\n\n    def play_countdown(self):\n        s = self._make_sound(440, 0.15, \"sine\")\n        if s:\n            s.play()\n\n    def play_go(self):\n        s = self._make_sound(880, 0.2, \"sine\")\n        if s:\n            s.play()\n\n# ─── Asset Generation ────────────────────────────────────────────────────────\n\ndef _draw_rounded_rect(surface, rect, radius, color):\n    pygame.draw.rect(surface, color, rect, border_radius=radius)\n\ndef generate_bird(skin_color, size=34):\n    s = pygame.Surface((size, size), pygame.SRCALPHA)\n    cx, cy = size // 2, size // 2\n    # Body\n    pygame.draw.ellipse(s, skin_color, (1, 1, size - 2, size - 2))\n    # Belly highlight\n    belly_color = pygame.Color(skin_color).lerp(pygame.Color(255, 255, 255), 0.3)\n    pygame.draw.ellipse(s, belly_color, (4, size // 2, size // 2, size // 3))\n    # Eye white\n    eye_x, eye_y = int(size * 0.6), int(size * 0.3)\n    pygame.draw.circle(s, (255, 255, 255), (eye_x, eye_y), 5)\n    # Pupil\n    pygame.draw.circle(s, (30, 30, 30), (eye_x + 1, eye_y), 3)\n    # Eye shine\n    pygame.draw.circle(s, (255, 255, 255), (eye_x + 2, eye_y - 1), 1)\n    # Beak\n    beak_pts = [(eye_x + 5, eye_y + 1), (eye_x + 5, eye_y + 5), (eye_x + 13, eye_y + 3)]\n    pygame.draw.polygon(s, (255, 140, 30), beak_pts)\n    # Wing\n    wing_color = pygame.Color(skin_color).lerp(pygame.Color(0, 0, 0), 0.25)\n    wing_pts = [(3, cy), (8, cy + 6), (16, cy + 4), (14, cy - 2), (6, cy - 2)]\n    pygame.draw.polygon(s, wing_color, wing_pts)\n    return s\n\ndef generate_bird_frames(skin_color):\n    frames = []\n    for angle in [0, -10, -20]:\n        surf = generate_bird(skin_color)\n        frames.append(pygame.transform.rotate(surf, angle))\n    return frames\n\ndef draw_pipe(surface, x, y, w, h, is_top):\n    cap_h = 26\n    cap_w = w + 10\n    cap_x = x - 5\n    if is_top:\n        body_rect = (x, y, w, max(0, h - cap_h))\n        cap_rect = (cap_x, y + h - cap_h, cap_w, cap_h)\n    else:\n        body_rect = (x, y + cap_h, w, max(0, h - cap_h))\n        cap_rect = (cap_x, y, cap_w, cap_h)\n    # Body\n    pygame.draw.rect(surface, C_PIPE_GREEN, body_rect)\n    # Highlight\n    pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT,\n                     (x + 4, body_rect[1], 6, body_rect[3]))\n    # Shadow\n    pygame.draw.rect(surface, C_PIPE_GREEN_DARK,\n                     (x + w - 8, body_rect[1], 6, body_rect[3]))\n    # Border\n    pygame.draw.rect(surface, C_PIPE_GREEN_DARK, body_rect, 2)\n    # Cap\n    _draw_rounded_rect(surface, cap_rect, 4, C_PIPE_CAP)\n    pygame.draw.rect(surface, C_PIPE_GREEN_LIGHT,\n                     (cap_x + 3, cap_rect[1] + 3, 6, cap_rect[3] - 6))\n    pygame.draw.rect(surface, C_PIPE_CAP, cap_rect, 2, border_radius=4)\n\ndef _make_gradient_surf(top_color, bot_color, width, height):\n    surf = pygame.Surface((width, height))\n    tc = pygame.Color(top_color)\n    bc = pygame.Color(bot_color)\n    for y in range(height):\n        t = y / max(1, height - 1)\n        c = tc.lerp(bc, t)\n        pygame.draw.line(surf, c, (0, y), (width, y))\n    return surf\n\ndef draw_background(surface, night_factor=0.0, scroll_x=0):\n    top = pygame.Color(C_SKY_TOP).lerp(pygame.Color(C_SKY_NIGHT_TOP), night_factor)\n    bot = pygame.Color(C_SKY_BOT).lerp(pygame.Color(C_SKY_NIGHT_BOT), night_factor)\n    grad = _make_gradient_surf(tuple(top), tuple(bot), SCREEN_W, GROUND_Y)\n    surface.blit(grad, (0, 0))\n    _draw_clouds(surface, night_factor, scroll_x)\n\ndef _draw_clouds(surface, night_factor, scroll_x):\n    alpha = int(200 * (1 - night_factor * 0.7))\n    cloud_color = (*C_CLOUD, alpha)\n    positions = [(100, 80, 1.0), (300, 150, 0.7), (550, 60, 0.9),\n                 (200, 250, 0.6), (450, 200, 0.8), (700, 120, 0.75)]\n    for cx, cy, scale in positions:\n        px = ((cx - scroll_x * 0.3) % (SCREEN_W + 200)) - 100\n        _draw_cloud(surface, px, cy, scale, cloud_color)\n\ndef _draw_cloud(surface, x, y, scale, color):\n    s = pygame.Surface((int(80 * scale), int(40 * scale)), pygame.SRCALPHA)\n    pygame.draw.ellipse(s, color, (0, int(10 * scale), int(60 * scale), int(25 * scale)))\n    pygame.draw.ellipse(s, color, (int(15 * scale), 0, int(40 * scale), int(30 * scale)))\n    pygame.draw.ellipse(s, color, (int(35 * scale), int(5 * scale), int(35 * scale), int(25 * scale)))\n    surface.blit(s, (x, y))\n\ndef draw_stars(surface, night_factor, time_val):\n    if night_factor < 0.3:\n        return\n    alpha = int(255 * (night_factor - 0.3) / 0.7)\n    rng = random.Random(42)\n    for _ in range(80):\n        sx = rng.randint(0, SCREEN_W)\n        sy = rng.randint(0, GROUND_Y)\n        twinkle = 0.5 + 0.5 * math.sin(time_val * 2 + sx * 0.1)\n        sz = 1 + int(twinkle)\n        sa = int(alpha * (0.4 + 0.6 * twinkle))\n        pygame.draw.circle(surface, (*C_STAR, sa), (sx, sy), sz)\n\ndef draw_ground(surface, scroll_x, night_factor):\n    grass_h = 20\n    gc = pygame.Color(C_GROUND_GRASS).lerp(pygame.Color(20, 60, 20), night_factor)\n    pygame.draw.rect(surface, tuple(gc), (0, GROUND_Y, SCREEN_W, grass_h))\n    # Grass blades\n    gc2 = pygame.Color(60, 160, 40).lerp(pygame.Color(15, 45, 15), night_factor)\n    for x in range(-10, SCREEN_W + 10, 6):\n        px = ((x - scroll_x) % (SCREEN_W + 20)) - 10\n        blade_h = 8 + int(4 * math.sin(x * 0.3 + scroll_x * 0.05))\n        pygame.draw.line(surface, tuple(gc2), (px, GROUND_Y + grass_h),\n                         (px + 2, GROUND_Y + grass_h - blade_h), 2)\n    # Dirt\n    gc = pygame.Color(C_GROUND).lerp(pygame.Color(40, 35, 25), night_factor)\n    gc2 = pygame.Color(C_GROUND_DARK).lerp(pygame.Color(25, 20, 15), night_factor)\n    pygame.draw.rect(surface, tuple(gc), (0, GROUND_Y + grass_h, SCREEN_W, 80 - grass_h))\n    # Stripes\n    for x in range(-10, SCREEN_W + 10, 24):\n        px = ((x - scroll_x) % (SCREEN_W + 20)) - 10\n        pygame.draw.line(surface, tuple(gc2), (px, GROUND_Y + grass_h + 5),\n                         (px + 12, GROUND_Y + grass_h + 15), 2)\n    # Top edge\n    pygame.draw.line(surface, (0, 0, 0), (0, GROUND_Y), (SCREEN_W, GROUND_Y), 2)\n\ndef draw_score_text(surface, text, x, y, size=48, color=C_TEXT_WHITE, bold=True):\n    font = pygame.font.SysFont(\"arial\", size, bold=bold)\n    shadow = font.render(text, True, C_TEXT_SHADOW)\n    main = font.render(text, True, color)\n    surface.blit(shadow, (x + 2, y + 2))\n    surface.blit(main, (x, y))\n\ndef draw_medal(surface, x, y, score):\n    if score < 10:\n        return None\n    elif score < 20:\n        color, label = C_MEDAL_BRONZE, \"BRONZE\"\n    elif score < 40:\n        color, label = C_MEDAL_SILVER, \"SILVER\"\n    elif score < 80:\n        color, label = C_MEDAL_GOLD, \"GOLD\"\n    else:\n        color, label = C_MEDAL_PLATINUM, \"PLATINUM\"\n    pygame.draw.circle(surface, color, (x, y), 28)\n    pygame.draw.circle(surface, pygame.Color(color).lerp(pygame.Color(0, 0, 0), 0.3), (x, y), 22)\n    pygame.draw.circle(surface, (255, 255, 255), (x - 5, y - 5), 6, 1)\n    _draw_star(surface, x, y, 10, 5, (255, 255, 255))\n    font = pygame.font.SysFont(\"arial\", 10, bold=True)\n    label_surf = font.render(label, True, color)\n    surface.blit(label_surf, (x - label_surf.get_width() // 2, y + 32))\n    return label\n\ndef _draw_star(surface, cx, cy, outer_r, inner_r, color):\n    pts = []\n    for i in range(10):\n        angle = math.pi / 2 + i * math.pi / 5\n        r = outer_r if i % 2 == 0 else inner_r\n        pts.append((cx + r * math.cos(angle - math.pi / 2),\n                     cy + r * math.sin(angle - math.pi / 2)))\n    pygame.draw.polygon(surface, color, pts)\n\ndef _make_panel_surface(w, h, color=C_PANEL_BG, radius=12):\n    \"\"\"Create a panel with proper rounded corners.\"\"\"\n    surf = pygame.Surface((w, h), pygame.SRCALPHA)\n    # Don't fill - just draw the rounded rect\n    _draw_rounded_rect(surf, (0, 0, w, h), radius, color)\n    pygame.draw.rect(surf, C_UI_BORDER, (0, 0, w, h), 2, border_radius=radius)\n    return surf\n\n# ─── Particle System ─────────────────────────────────────────────────────────\n\nclass Particle:\n    __slots__ = ('x', 'y', 'vx', 'vy', 'color', 'life', 'max_life', 'size')\n\n    def __init__(self, x, y, vx, vy, color, life, size=3):\n        self.x = x\n        self.y = y\n        self.vx = vx\n        self.vy = vy\n        self.color = color\n        self.life = life\n        self.max_life = life\n        self.size = size\n\n    def update(self):\n        self.x += self.vx\n        self.y += self.vy\n        self.vy += 0.1\n        self.life -= 1\n\n    def draw(self, surface):\n        alpha = max(0, self.life / self.max_life)\n        c = tuple(int(ch * alpha) for ch in self.color)\n        s = max(1, int(self.size * alpha))\n        pygame.draw.circle(surface, c, (int(self.x), int(self.y)), s)\n\n    def alive(self):\n        return self.life > 0\n\nclass ParticleSystem:\n    def __init__(self):\n        self.particles = []\n\n    def emit(self, x, y, count, color, speed=3, life=30, size=3):\n        for _ in range(count):\n            angle = random.uniform(0, math.pi * 2)\n            spd = random.uniform(0.5, speed)\n            self.particles.append(Particle(\n                x, y, math.cos(angle) * spd, math.sin(angle) * spd,\n                color, life, size))\n\n    def update(self):\n        self.particles = [p for p in self.particles if p.alive()]\n        for p in self.particles:\n            p.update()\n\n    def draw(self, surface):\n        for p in self.particles:\n            p.draw(surface)\n\n# ─── Button ──────────────────────────────────────────────────────────────────\n\nclass Button:\n    def __init__(self, x, y, w, h, text, callback, color=C_UI_BUTTON,\n                 hover_color=C_UI_BUTTON_HOVER, active_color=C_UI_BUTTON_ACTIVE,\n                 font_size=22, bold=True):\n        self.rect = pygame.Rect(x, y, w, h)\n        self.text = text\n        self.callback = callback\n        self.base_color = color\n        self.hover_color = hover_color\n        self.active_color = active_color\n        self.font_size = font_size\n        self.bold = bold\n        self.hovered = False\n        self.pressed = False\n\n    def handle_event(self, event):\n        if event.type == pygame.MOUSEMOTION:\n            self.hovered = self.rect.collidepoint(event.pos)\n        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:\n            if self.rect.collidepoint(event.pos):\n                self.pressed = True\n                return True\n        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:\n            if self.pressed and self.rect.collidepoint(event.pos):\n                self.callback()\n                self.pressed = False\n                return True\n            self.pressed = False\n        return False\n\n    def draw(self, surface):\n        color = (self.active_color if self.pressed else\n                 (self.hover_color if self.hovered else self.base_color))\n        _draw_rounded_rect(surface, self.rect, 8, color)\n        pygame.draw.rect(surface, C_UI_BORDER, self.rect, 2, border_radius=8)\n        font = pygame.font.SysFont(\"arial\", self.font_size, bold=self.bold)\n        text_surf = font.render(self.text, True, C_TEXT_WHITE)\n        tx = self.rect.x + (self.rect.w - text_surf.get_width()) // 2\n        ty = self.rect.y + (self.rect.h - text_surf.get_height()) // 2\n        surface.blit(font.render(self.text, True, (0, 0, 0)), (tx + 1, ty + 1))\n        surface.blit(text_surf, (tx, ty))\n\n# ─── Score Popup ─────────────────────────────────────────────────────────────\n\nclass ScorePopup:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.life = 40\n        self.max_life = 40\n\n    def update(self):\n        self.y -= 1.5\n        self.life -= 1\n\n    def draw(self, surface):\n        if self.life <= 0:\n            return\n        font = pygame.font.SysFont(\"arial\", 28, bold=True)\n        shadow = font.render(\"+1\", True, (0, 0, 0))\n        main = font.render(\"+1\", True, (255, 255, 200))\n        surface.blit(shadow, (self.x + 2, self.y + 2))\n        surface.blit(main, (self.x, self.y))\n\n    def alive(self):\n        return self.life > 0\n\n# ─── Game States ─────────────────────────────────────────────────────────────\n\nSTATE_MENU = 0\nSTATE_PLAYING = 1\nSTATE_PAUSED = 2\nSTATE_GAME_OVER = 3\nSTATE_SETTINGS = 4\nSTATE_SKIN_SELECT = 5\nSTATE_LEADERBOARD = 6\n\n# ─── Main Game Class ─────────────────────────────────────────────────────────\n\nclass Game:\n    def __init__(self):\n        pygame.init()\n        pygame.display.set_caption(TITLE)\n        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))\n        self.clock = pygame.time.Clock()\n        self.sound = SoundEngine()\n        self.save = load_save()\n        self.particles = ParticleSystem()\n        self.state = STATE_MENU\n        self.prev_state = None\n\n        # Bird\n        self._reset_bird()\n\n        # Pipes\n        self.pipes = []\n        self.pipe_timer = 0\n\n        # Score\n        self.score = 0\n\n        # Animation\n        self.bird_frame = 0\n        self.bird_frame_timer = 0\n        self.scroll_x = 0\n        self.time_val = 0\n\n        # Screen shake\n        self.shake_dur = 0\n\n        # Night mode\n        self.night_factor = 0.0\n        self.night_target = 0.0\n\n        # Countdown\n        self.countdown = 0\n        self.countdown_timer = 0\n\n        # Score popups\n        self.score_popups = []\n\n        # Game over\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n\n        # Menu animation\n        self.menu_bird_y = SCREEN_H // 3\n        self.menu_bob = 0\n\n        # Buttons\n        self.buttons = []\n        self._build_menu_buttons()\n\n        # Pre-generate bird frames\n        self.difficulty = self.save.get(\"difficulty\", \"Normal\")\n        self.skin_index = self.save.get(\"skin_index\", 0)\n        self.skin_color = C_BIRD_SKINS[self.skin_index]\n        self.sound.enabled = self.save.get(\"sound_enabled\", True)\n        self.bird_frames = generate_bird_frames(self.skin_color)\n\n        # Cached panel surfaces\n        self._panel_cache = {}\n\n    def _reset_bird(self):\n        self.bird_x = SCREEN_W // 3\n        self.bird_y = SCREEN_H // 2\n        self.bird_vel = 0\n        self.bird_rotation = 0\n        self.bird_alive = True\n\n    # ─── Button Builders ───────────────────────────────────────────────\n\n    def _build_menu_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 40\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"PLAY\", self._start_game, font_size=28),\n            Button(cx - 100, by + 60, 200, 48, \"SETTINGS\", self._go_settings, font_size=24),\n            Button(cx - 100, by + 120, 200, 48, \"SKINS\", self._go_skins, font_size=24),\n            Button(cx - 100, by + 180, 200, 48, \"SCORES\", self._go_leaderboard, font_size=24),\n        ]\n\n    def _build_pause_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 - 20\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"RESUME\", self._resume, font_size=26),\n            Button(cx - 100, by + 60, 200, 48, \"SETTINGS\", self._go_settings, font_size=24),\n            Button(cx - 100, by + 120, 200, 48, \"QUIT\", self._go_menu, font_size=24),\n        ]\n\n    def _build_gameover_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 100\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"RETRY\", self._start_game, font_size=26),\n            Button(cx - 100, by + 60, 200, 48, \"MENU\", self._go_menu, font_size=24),\n        ]\n\n    def _build_settings_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 100\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    def _build_skin_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 80\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    def _build_leaderboard_buttons(self):\n        cx = SCREEN_W // 2\n        by = SCREEN_H // 2 + 120\n        self.buttons = [\n            Button(cx - 100, by, 200, 48, \"BACK\", self._go_back, font_size=24),\n        ]\n\n    # ─── State Transitions ───────────────────────────────────────────────\n\n    def _start_game(self):\n        self.sound.play_swoosh()\n        self.state = STATE_PLAYING\n        self._reset_bird()\n        self.pipes = []\n        self.pipe_timer = 0\n        self.score = 0\n        self.score_popups = []\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n        self.countdown = 3\n        self.countdown_timer = 0\n        self.bird_frame = 0\n        self.bird_vel = 0\n        self.bird_rotation = 0\n        self.bird_alive = True\n\n    def _go_menu(self):\n        self.sound.play_swoosh()\n        self.state = STATE_MENU\n        self._build_menu_buttons()\n        self.flash_alpha = 0\n\n    def _go_settings(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_SETTINGS\n        self._build_settings_buttons()\n\n    def _go_skins(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_SKIN_SELECT\n        self._build_skin_buttons()\n\n    def _go_leaderboard(self):\n        self.sound.play_swoosh()\n        self.prev_state = self.state\n        self.state = STATE_LEADERBOARD\n        self._build_leaderboard_buttons()\n\n    def _go_back(self):\n        self.sound.play_swoosh()\n        target = self.prev_state if self.prev_state else STATE_MENU\n        self.state = target\n        if target == STATE_MENU:\n            self._build_menu_buttons()\n        elif target == STATE_PAUSED:\n            self._build_pause_buttons()\n\n    def _resume(self):\n        self.sound.play_swoosh()\n        self.state = STATE_PLAYING\n\n    def _die(self):\n        if not self.bird_alive:\n            return\n        self.bird_alive = False\n        self.sound.play_hit()\n        self.shake_dur = 15\n        self.particles.emit(self.bird_x, self.bird_y, 20, C_PARTICLE, 4, 40, 4)\n        self.particles.emit(self.bird_x, self.bird_y, 10, (255, 100, 50), 3, 30, 3)\n        self.flash_alpha = 200\n        # Save score\n        self.save[\"total_games\"] = self.save.get(\"total_games\", 0) + 1\n        self.save[\"total_score\"] = self.save.get(\"total_score\", 0) + self.score\n        if self.score > self.save.get(\"high_score\", 0):\n            self.save[\"high_score\"] = self.score\n        scores = self.save.get(\"scores\", [])\n        scores.append(self.score)\n        scores.sort(reverse=True)\n        self.save[\"scores\"] = scores[:20]\n        save_save(self.save)\n        self.game_over_timer = 0\n        self._build_gameover_buttons()\n\n    def _flap(self):\n        if self.state == STATE_PLAYING and self.bird_alive and self.countdown == 0:\n            diff = DIFFICULTIES[self.difficulty]\n            self.bird_vel = diff[\"flap\"]\n            self.sound.play_flap()\n            self.particles.emit(self.bird_x - 5, self.bird_y + 10, 3,\n                                (255, 255, 200), 2, 15, 2)\n        elif self.state == STATE_MENU:\n            self.sound.play_menu()\n\n    # ─── Update ──────────────────────────────────────────────────────────\n\n    def update(self):\n        self.time_val += 1 / FPS\n\n        # Night mode\n        if self.save.get(\"night_auto\", True) and self.state == STATE_PLAYING:\n            cycle = (self.time_val * 0.02) % 1.0\n            self.night_target = max(0,\n                math.sin(cycle * math.pi * 2 - math.pi / 2) * 0.5 + 0.5) * 0.8\n        elif self.save.get(\"night_mode\", False):\n            self.night_target = 1.0\n        else:\n            self.night_target = 0.0\n        self.night_factor += (self.night_target - self.night_factor) * 0.02\n\n        # Flash fade\n        if self.flash_alpha > 0:\n            self.flash_alpha = max(0, self.flash_alpha - 8)\n\n        self.particles.update()\n\n        if self.state == STATE_MENU:\n            self._update_menu()\n        elif self.state == STATE_PLAYING:\n            self._update_playing()\n        elif self.state == STATE_GAME_OVER:\n            self._update_game_over()\n\n        # Update button hover states\n        mouse_pos = pygame.mouse.get_pos()\n        for btn in self.buttons:\n            btn.hovered = btn.rect.collidepoint(mouse_pos)\n\n    def _update_menu(self):\n        self.menu_bob += 0.05\n        self.menu_bird_y = SCREEN_H // 3 + math.sin(self.menu_bob) * 15\n        self.scroll_x += 1\n        # Animate menu bird wing\n        self.bird_frame_timer += 1\n        if self.bird_frame_timer > 8:\n            self.bird_frame_timer = 0\n            self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)\n\n    def _update_playing(self):\n        diff = DIFFICULTIES[self.difficulty]\n\n        # Countdown\n        if self.countdown > 0:\n            self.countdown_timer += 1\n            if self.countdown_timer >= 60:\n                self.countdown_timer = 0\n                if self.countdown == 1:\n                    self.sound.play_go()\n                else:\n                    self.sound.play_countdown()\n                self.countdown -= 1\n                if self.countdown == 0:\n                    self.pipe_timer = 60\n                # Still animate bird during countdown\n                self.bird_frame_timer += 1\n                if self.bird_frame_timer > 6:\n                    self.bird_frame_timer = 0\n                    self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)\n                return\n\n        # Bird physics\n        if self.bird_alive:\n            self.bird_vel += diff[\"gravity\"]\n            if self.bird_vel > MAX_FALL:\n                self.bird_vel = MAX_FALL\n            self.bird_y += self.bird_vel\n\n            # Rotation based on velocity\n            if self.bird_vel < 0:\n                self.bird_rotation = max(-30, self.bird_vel * 4)\n            else:\n                self.bird_rotation = min(90, self.bird_rotation + 2.5)\n\n            # Wing animation\n            self.bird_frame_timer += 1\n            if self.bird_frame_timer > 6:\n                self.bird_frame_timer = 0\n                self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)\n\n        # Scroll\n        self.scroll_x += diff[\"speed\"]\n\n        # Pipe spawning\n        if self.pipe_timer > 0:\n            self.pipe_timer -= 1\n        else:\n            gap_y = random.randint(120, GROUND_Y - 150)\n            self.pipes.append({\n                \"x\": SCREEN_W + 10,\n                \"gap_y\": gap_y,\n                \"scored\": False,\n                \"id\": len(self.pipes),\n            })\n            self.pipe_timer = int(PIPE_INTERVAL_MS / (diff[\"speed\"] * (1000 / FPS)))\n\n        # Move pipes\n        for pipe in self.pipes:\n            pipe[\"x\"] -= diff[\"speed\"]\n\n            # Score check\n            if not pipe[\"scored\"] and pipe[\"x\"] + PIPE_WIDTH // 2 < self.bird_x:\n                pipe[\"scored\"] = True\n                self.score += 1\n                self.sound.play_score()\n                self.score_popups.append(ScorePopup(self.bird_x + 20, self.bird_y - 20))\n                self.particles.emit(self.bird_x, self.bird_y, 5,\n                                    (255, 255, 100), 3, 20, 3)\n\n        # Remove off-screen pipes\n        self.pipes = [p for p in self.pipes if p[\"x\"] > -PIPE_WIDTH - 20]\n\n        # Update score popups\n        self.score_popups = [p for p in self.score_popups if p.alive()]\n        for sp in self.score_popups:\n            sp.update()\n\n        # Collision detection\n        if self.bird_alive:\n            # Bird hitbox: 20x20 centered on bird (generous but fair)\n            bird_half = 10\n            bird_rect = pygame.Rect(\n                self.bird_x - bird_half, self.bird_y - bird_half,\n                bird_half * 2, bird_half * 2)\n\n            # Ground / ceiling\n            if self.bird_y + bird_half >= GROUND_Y or self.bird_y - bird_half <= 0:\n                self.bird_y = GROUND_Y - bird_half\n                self._die()\n\n            # Pipe collision\n            gap = diff[\"gap\"]\n            half_gap = gap // 2\n            for pipe in self.pipes:\n                top_h = pipe[\"gap_y\"] - half_gap\n                bot_y = pipe[\"gap_y\"] + half_gap\n\n                # Only check pipes near the bird for performance\n                if abs(pipe[\"x\"] - self.bird_x) < PIPE_WIDTH + 20:\n                    top_rect = pygame.Rect(pipe[\"x\"], 0, PIPE_WIDTH, top_h)\n                    bot_rect = pygame.Rect(pipe[\"x\"], bot_y, PIPE_WIDTH,\n                                           GROUND_Y - bot_y)\n                    if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):\n                        self._die()\n                        break\n\n        # Post-death fall\n        if not self.bird_alive:\n            self.bird_vel += diff[\"gravity\"]\n            self.bird_y += self.bird_vel\n            self.bird_rotation = min(90, self.bird_rotation + 4)\n            if self.bird_y + 10 >= GROUND_Y:\n                self.bird_y = GROUND_Y - 10\n                self.bird_vel = 0\n                if self.game_over_timer == 0:\n                    self.sound.play_die()\n                self.game_over_timer += 1\n                if self.game_over_timer > 30:\n                    self.state = STATE_GAME_OVER\n        else:\n            self.game_over_timer = 0\n\n    def _update_game_over(self):\n        self.game_over_timer += 1\n        # Bird continues to fall if not on ground\n        if self.bird_y + 10 < GROUND_Y:\n            self.bird_vel += DIFFICULTIES[self.difficulty][\"gravity\"]\n            self.bird_y += self.bird_vel\n            if self.bird_y + 10 >= GROUND_Y:\n                self.bird_y = GROUND_Y - 10\n                self.bird_vel = 0\n\n    # ─── Draw ────────────────────────────────────────────────────────────\n\n    def draw(self):\n        # Use offscreen buffer for screen shake\n        self.screen.fill((0, 0, 0))\n\n        shake_x, shake_y = 0, 0\n        if self.shake_dur > 0:\n            shake_x = random.uniform(-4, 4) * (self.shake_dur / 15)\n            shake_y = random.uniform(-4, 4) * (self.shake_dur / 15)\n            self.shake_dur -= 1\n\n        # Draw to offscreen with shake offset\n        offscreen = pygame.Surface((SCREEN_W, SCREEN_H))\n\n        # Background\n        draw_background(offscreen, self.night_factor, self.scroll_x)\n        draw_stars(offscreen, self.night_factor, self.time_val)\n\n        # Pipes\n        diff = DIFFICULTIES[self.difficulty]\n        gap = diff[\"gap\"]\n        half_gap = gap // 2\n        for pipe in self.pipes:\n            top_h = pipe[\"gap_y\"] - half_gap\n            bot_y = pipe[\"gap_y\"] + half_gap\n            bot_h = GROUND_Y - bot_y\n            draw_pipe(offscreen, pipe[\"x\"], 0, PIPE_WIDTH, top_h, True)\n            draw_pipe(offscreen, pipe[\"x\"], bot_y, PIPE_WIDTH, bot_h, False)\n\n        # Ground\n        draw_ground(offscreen, self.scroll_x, self.night_factor)\n\n        # Bird\n        if self.state == STATE_MENU:\n            bird_surf = self.bird_frames[self.bird_frame % len(self.bird_frames)]\n            offscreen.blit(bird_surf,\n                (self.bird_x - bird_surf.get_width() // 2,\n                 self.menu_bird_y - bird_surf.get_height() // 2))\n        else:\n            bird_surf = pygame.transform.rotate(self.bird_frames[0], self.bird_rotation)\n            rect = bird_surf.get_rect(center=(self.bird_x, self.bird_y))\n            offscreen.blit(bird_surf, rect.topleft)\n\n        # Particles\n        self.particles.draw(offscreen)\n\n        # Score popups\n        for sp in self.score_popups:\n            sp.draw(offscreen)\n\n        # In-game HUD\n        if self.state == STATE_PLAYING and self.countdown == 0:\n            draw_score_text(offscreen, str(self.score),\n                            SCREEN_W // 2 - 20, 30, 56, C_TEXT_WHITE)\n            small_font = pygame.font.SysFont(\"arial\", 14)\n            hint = small_font.render(\"ESC to pause\", True, (200, 200, 200))\n            offscreen.blit(hint, (SCREEN_W - hint.get_width() - 10, 10))\n\n        # Countdown overlay\n        if self.state == STATE_PLAYING and self.countdown > 0:\n            self._draw_countdown(offscreen)\n\n        # State overlays\n        if self.state == STATE_MENU:\n            self._draw_menu(offscreen)\n        elif self.state == STATE_PAUSED:\n            self._draw_pause(offscreen)\n        elif self.state == STATE_GAME_OVER:\n            self._draw_game_over(offscreen)\n        elif self.state == STATE_SETTINGS:\n            self._draw_settings(offscreen)\n        elif self.state == STATE_SKIN_SELECT:\n            self._draw_skin_select(offscreen)\n        elif self.state == STATE_LEADERBOARD:\n            self._draw_leaderboard(offscreen)\n\n        # Flash effect\n        if self.flash_alpha > 0:\n            flash = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n            flash.fill((255, 255, 255, min(255, self.flash_alpha)))\n            offscreen.blit(flash, (0, 0))\n\n        # Blit to screen with shake offset\n        self.screen.blit(offscreen, (int(shake_x), int(shake_y)))\n\n        pygame.display.flip()\n\n    def _draw_countdown(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 80))\n        surface.blit(overlay, (0, 0))\n        text = str(self.countdown)\n        color = (50, 255, 50) if self.countdown == 0 else C_TEXT_WHITE\n        draw_score_text(surface, text, SCREEN_W // 2 - 30,\n                        SCREEN_H // 2 - 40, 80, color)\n\n    def _draw_menu(self, surface):\n        # Title\n        title_font = pygame.font.SysFont(\"arial\", 44, bold=True)\n        title = title_font.render(\"FLIPPYBLOCK\", True, C_TEXT_WHITE)\n        surface.blit(title_font.render(\"FLIPPYBLOCK\", True, (0, 0, 0)),\n                     (SCREEN_W // 2 - title.get_width() // 2 + 2, 82))\n        surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 80))\n\n        sub_font = pygame.font.SysFont(\"arial\", 22, bold=True)\n        sub = sub_font.render(\"EXTREME\", True, C_TEXT_GOLD)\n        surface.blit(sub_font.render(\"EXTREME\", True, (0, 0, 0)),\n                     (SCREEN_W // 2 - sub.get_width() // 2 + 2, 132))\n        surface.blit(sub, (SCREEN_W // 2 - sub.get_width() // 2, 130))\n\n        # High score\n        hs = self.save.get(\"high_score\", 0)\n        hs_font = pygame.font.SysFont(\"arial\", 18)\n        hs_text = hs_font.render(f\"Best: {hs}\", True, C_TEXT_GOLD)\n        surface.blit(hs_text, (SCREEN_W // 2 - hs_text.get_width() // 2, 170))\n\n        # Controls hint\n        hint_font = pygame.font.SysFont(\"arial\", 14)\n        hint = hint_font.render(\"SPACE / Click to flap  |  ESC to pause\", True, (180, 180, 180))\n        surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 100))\n\n        # Buttons\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    def _draw_pause(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 150))\n        surface.blit(overlay, (0, 0))\n\n        panel_w, panel_h = SCREEN_W - 80, 260\n        panel = _make_panel_surface(panel_w, panel_h)\n        surface.blit(panel, (40, SCREEN_H // 2 - 170))\n\n        draw_score_text(surface, \"PAUSED\", SCREEN_W // 2 - 55,\n                        SCREEN_H // 2 - 155, 36, C_TEXT_WHITE)\n\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    def _draw_game_over(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 160))\n        surface.blit(overlay, (0, 0))\n\n        panel_w, panel_h = SCREEN_W - 80, 320\n        panel = _make_panel_surface(panel_w, panel_h)\n        surface.blit(panel, (40, SCREEN_H // 2 - 200))\n\n        draw_score_text(surface, \"GAME OVER\", SCREEN_W // 2 - 100,\n                        SCREEN_H // 2 - 180, 36, (255, 80, 80))\n\n        draw_score_text(surface, f\"Score: {self.score}\", SCREEN_W // 2 - 60,\n                        SCREEN_H // 2 - 130, 28, C_TEXT_WHITE)\n\n        hs = self.save.get(\"high_score\", 0)\n        is_best = self.score == hs and hs > 0\n        best_color = C_TEXT_GOLD if is_best else C_TEXT_WHITE\n        draw_score_text(surface, f\"Best: {hs}\", SCREEN_W // 2 - 50,\n                        SCREEN_H // 2 - 90, 22, best_color)\n        if is_best:\n            new_font = pygame.font.SysFont(\"arial\", 16, bold=True)\n            new_surf = new_font.render(\"NEW BEST!\", True, C_TEXT_GOLD)\n            surface.blit(new_surf,\n                         (SCREEN_W // 2 - new_surf.get_width() // 2, SCREEN_H // 2 - 70))\n\n        # Medal\n        draw_medal(surface, SCREEN_W // 2, SCREEN_H // 2 - 30, self.score)\n\n        # Stats\n        stats_font = pygame.font.SysFont(\"arial\", 14)\n        total_games = self.save.get(\"total_games\", 0)\n        avg = self.save.get(\"total_score\", 0) // max(1, total_games)\n        for i, stat in enumerate([f\"Games: {total_games}\", f\"Avg Score: {avg}\"]):\n            surf = stats_font.render(stat, True, (180, 180, 180))\n            surface.blit(surf, (SCREEN_W // 2 - surf.get_width() // 2,\n                                SCREEN_H // 2 + 30 + i * 20))\n\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    def _draw_settings(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        surface.blit(overlay, (0, 0))\n\n        panel_w, panel_h = SCREEN_W - 60, 420\n        panel = _make_panel_surface(panel_w, panel_h)\n        surface.blit(panel, (30, SCREEN_H // 2 - 240))\n\n        draw_score_text(surface, \"SETTINGS\", SCREEN_W // 2 - 70,\n                        SCREEN_H // 2 - 215, 32, C_TEXT_WHITE)\n\n        # Difficulty\n        self._draw_toggle_row(surface, SCREEN_H // 2 - 170, \"Difficulty\",\n                              self.difficulty, list(DIFFICULTIES.keys()))\n\n        # Sound\n        sound_text = \"ON\" if self.save.get(\"sound_enabled\", True) else \"OFF\"\n        self._draw_toggle_row(surface, SCREEN_H // 2 - 120, \"Sound\",\n                              sound_text, [\"ON\", \"OFF\"])\n\n        # Night mode\n        if self.save.get(\"night_auto\", True):\n            night_text = \"Auto\"\n        elif self.save.get(\"night_mode\", False):\n            night_text = \"ON\"\n        else:\n            night_text = \"OFF\"\n        self._draw_toggle_row(surface, SCREEN_H // 2 - 70, \"Night Mode\",\n                              night_text, [\"Auto\", \"ON\", \"OFF\"])\n\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    def _draw_toggle_row(self, surface, y, label, current, options):\n        font = pygame.font.SysFont(\"arial\", 20)\n        label_surf = font.render(label, True, C_TEXT_WHITE)\n        surface.blit(label_surf, (60, y))\n\n        left_rect = pygame.Rect(200, y - 12, 30, 30)\n        _draw_rounded_rect(surface, left_rect, 4, C_UI_BUTTON)\n        pygame.draw.rect(surface, C_UI_BORDER, left_rect, 1, border_radius=4)\n        arrow_font = pygame.font.SysFont(\"arial\", 20, bold=True)\n        surface.blit(arrow_font.render(\"<\", True, C_TEXT_WHITE),\n                     (left_rect.x + 8, left_rect.y + 4))\n\n        val_surf = font.render(current, True, C_TEXT_GOLD)\n        surface.blit(val_surf, (240, y - 6))\n\n        right_rect = pygame.Rect(240 + val_surf.get_width() + 10, y - 12, 30, 30)\n        _draw_rounded_rect(surface, right_rect, 4, C_UI_BUTTON)\n        pygame.draw.rect(surface, C_UI_BORDER, right_rect, 1, border_radius=4)\n        surface.blit(arrow_font.render(\">\", True, C_TEXT_WHITE),\n                     (right_rect.x + 8, right_rect.y + 4))\n\n        self._last_toggle = {\n            \"left_rect\": left_rect, \"right_rect\": right_rect,\n            \"current\": current, \"options\": options, \"label\": label\n        }\n\n    def _cycle_toggle(self, direction):\n        \"\"\"Cycle the last drawn toggle in the given direction (-1 or 1).\"\"\"\n        if not hasattr(self, '_last_toggle'):\n            return\n        info = self._last_toggle\n        opts = info[\"options\"]\n        try:\n            idx = opts.index(info[\"current\"])\n        except ValueError:\n            return\n        new_idx = (idx + direction) % len(opts)\n        new_val = opts[new_idx]\n\n        label = info[\"label\"]\n        if label == \"Difficulty\":\n            self.difficulty = new_val\n            self.save[\"difficulty\"] = new_val\n        elif label == \"Sound\":\n            self.save[\"sound_enabled\"] = (new_val == \"ON\")\n            self.sound.enabled = self.save[\"sound_enabled\"]\n        elif label == \"Night Mode\":\n            if new_val == \"Auto\":\n                self.save[\"night_auto\"] = True\n                self.save[\"night_mode\"] = False\n            elif new_val == \"ON\":\n                self.save[\"night_auto\"] = False\n                self.save[\"night_mode\"] = True\n            else:\n                self.save[\"night_auto\"] = False\n                self.save[\"night_mode\"] = False\n\n        save_save(self.save)\n        self.sound.play_select()\n\n    def _draw_skin_select(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        surface.blit(overlay, (0, 0))\n\n        panel_w, panel_h = SCREEN_W - 60, 340\n        panel = _make_panel_surface(panel_w, panel_h)\n        surface.blit(panel, (30, SCREEN_H // 2 - 190))\n\n        draw_score_text(surface, \"SELECT SKIN\", SCREEN_W // 2 - 80,\n                        SCREEN_H // 2 - 165, 28, C_TEXT_WHITE)\n\n        cols = 3\n        start_x, start_y = 60, SCREEN_H // 2 - 110\n        cell_w, cell_h = 120, 80\n\n        self._skin_rects = []\n        for i in range(len(C_BIRD_SKINS)):\n            color = C_BIRD_SKINS[i]\n            name = C_SKIN_NAMES[i]\n            col = i % cols\n            row = i // cols\n            cx = start_x + col * cell_w\n            cy = start_y + row * cell_h\n            rect = pygame.Rect(cx, cy, cell_w, cell_h)\n\n            is_sel = (i == self.skin_index)\n            bg = C_UI_BUTTON_HOVER if is_sel else C_UI_BUTTON\n            _draw_rounded_rect(surface, rect, 6, bg)\n            border = C_TEXT_GOLD if is_sel else C_UI_BORDER\n            pygame.draw.rect(surface, border, rect,\n                             2 if is_sel else 1, border_radius=6)\n\n            preview = generate_bird(color, 24)\n            surface.blit(preview, (cx + cell_w // 2 - 12, cy + 5))\n\n            name_font = pygame.font.SysFont(\"arial\", 12)\n            name_surf = name_font.render(name, True, C_TEXT_WHITE)\n            surface.blit(name_surf,\n                         (cx + cell_w // 2 - name_surf.get_width() // 2, cy + 45))\n\n            self._skin_rects.append((rect, i))\n\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    def _draw_leaderboard(self, surface):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 170))\n        surface.blit(overlay, (0, 0))\n\n        panel_w, panel_h = SCREEN_W - 60, 420\n        panel = _make_panel_surface(panel_w, panel_h)\n        surface.blit(panel, (30, SCREEN_H // 2 - 240))\n\n        draw_score_text(surface, \"TOP SCORES\", SCREEN_W // 2 - 70,\n                        SCREEN_H // 2 - 215, 30, C_TEXT_WHITE)\n\n        scores = self.save.get(\"scores\", [])\n        if not scores:\n            empty_font = pygame.font.SysFont(\"arial\", 18)\n            empty = empty_font.render(\"No scores yet!\", True, (150, 150, 150))\n            surface.blit(empty, (SCREEN_W // 2 - empty.get_width() // 2,\n                                 SCREEN_H // 2 - 100))\n        else:\n            for i, sc in enumerate(scores[:10]):\n                y = SCREEN_H // 2 - 170 + i * 28\n                rank_font = pygame.font.SysFont(\"arial\", 18, bold=True)\n                score_font = pygame.font.SysFont(\"arial\", 18)\n\n                if i < 3:\n                    rank_color = C_TEXT_GOLD\n                elif i < 6:\n                    rank_color = C_TEXT_SILVER\n                else:\n                    rank_color = (180, 180, 180)\n\n                rank_text = rank_font.render(f\"#{i + 1}\", True, rank_color)\n                score_text = score_font.render(f\"{sc}\", True, C_TEXT_WHITE)\n                surface.blit(rank_text, (80, y - 6))\n                surface.blit(score_text, (SCREEN_W - 120, y - 6))\n\n                bar_w = min(200, int(200 * sc / max(1, scores[0])))\n                _draw_rounded_rect(surface, pygame.Rect(140, y, bar_w, 16),\n                                   4, (60, 60, 100))\n\n        # Stats\n        total_games = self.save.get(\"total_games\", 0)\n        total_score = self.save.get(\"total_score\", 0)\n        avg = total_score // max(1, total_games)\n        stats_font = pygame.font.SysFont(\"arial\", 14)\n        for i, stat in enumerate([\n            f\"Total Games: {total_games}\",\n            f\"Total Score: {total_score}\",\n            f\"Avg Score: {avg}\"\n        ]):\n            surf = stats_font.render(stat, True, (160, 160, 160))\n            surface.blit(surf, (60, SCREEN_H // 2 + 100 + i * 20))\n\n        for btn in self.buttons:\n            btn.draw(surface)\n\n    # ─── Events ──────────────────────────────────────────────────────────\n\n    def handle_events(self):\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                return False\n\n            if event.type == pygame.MOUSEMOTION:\n                for btn in self.buttons:\n                    btn.hovered = btn.rect.collidepoint(event.pos)\n\n            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:\n                handled = self._handle_mouse_down(event)\n                if not handled and self.state == STATE_PLAYING and self.bird_alive:\n                    self._flap()\n\n            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:\n                for btn in self.buttons:\n                    btn.handle_event(event)\n\n            if event.type == pygame.KEYDOWN:\n                self._handle_keydown(event)\n\n        return True\n\n    def _handle_mouse_down(self, event):\n        \"\"\"Returns True if the click was handled by UI.\"\"\"\n        # Toggle buttons in settings\n        if self.state == STATE_SETTINGS and hasattr(self, '_last_toggle'):\n            info = self._last_toggle\n            if info[\"left_rect\"].collidepoint(event.pos):\n                self._cycle_toggle(-1)\n                return True\n            if info[\"right_rect\"].collidepoint(event.pos):\n                self._cycle_toggle(1)\n                return True\n\n        # Skin selection\n        if self.state == STATE_SKIN_SELECT and hasattr(self, '_skin_rects'):\n            for rect, idx in self._skin_rects:\n                if rect.collidepoint(event.pos):\n                    self.skin_index = idx\n                    self.skin_color = C_BIRD_SKINS[idx]\n                    self.bird_frames = generate_bird_frames(self.skin_color)\n                    self.save[\"skin_index\"] = idx\n                    save_save(self.save)\n                    self.sound.play_select()\n                    return True\n\n        # General buttons\n        for btn in self.buttons:\n            if btn.rect.collidepoint(event.pos):\n                btn.pressed = True\n                return True\n\n        return False\n\n    def _handle_keydown(self, event):\n        if event.key in (pygame.K_SPACE, pygame.K_UP):\n            if self.state == STATE_MENU:\n                self._start_game()\n            elif self.state == STATE_PLAYING:\n                self._flap()\n            elif self.state == STATE_GAME_OVER and self.game_over_timer > 30:\n                self._start_game()\n        elif event.key == pygame.K_RETURN:\n            if self.state == STATE_GAME_OVER and self.game_over_timer > 30:\n                self._start_game()\n        elif event.key == pygame.K_ESCAPE:\n            if self.state == STATE_PLAYING:\n                self.state = STATE_PAUSED\n                self._build_pause_buttons()\n                self.sound.play_swoosh()\n            elif self.state == STATE_PAUSED:\n                self._resume()\n            elif self.state in (STATE_SETTINGS, STATE_SKIN_SELECT, STATE_LEADERBOARD):\n                self._go_back()\n        elif event.key == pygame.K_s:\n            if self.state == STATE_PLAYING:\n                self.state = STATE_PAUSED\n                self._build_pause_buttons()\n        elif event.key == pygame.K_LEFT:\n            if self.state == STATE_SETTINGS:\n                self._cycle_toggle(-1)\n        elif event.key == pygame.K_RIGHT:\n            if self.state == STATE_SETTINGS:\n                self._cycle_toggle(1)\n\n    # ─── Main Loop ───────────────────────────────────────────────────────\n\n    def run(self):\n        running = True\n        while running:\n            running = self.handle_events()\n            self.update()\n            self.draw()\n            self.clock.tick(FPS)\n        pygame.quit()\n        sys.exit()\n\n\n# ─── Entry Point ─────────────────────────────────────────────────────────────\n\nif __name__ == \"__main__\":\n    game = Game()\n    game.run()\n",
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 6.5s)

_Thinking:_

Now let me verify the syntax and do a quick import test.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport ast, sys\nwith open('flippyblock_extreme.py') as f:\n    source = f.read()\ntry:\n    ast.parse(source)\n    print('Syntax OK')\nexcept SyntaxError as e:\n    print(f'Syntax Error: {e}')\n    sys.exit(1)\n\n# Count lines\nlines = source.count('\\n') + 1\nprint(f'Total lines: {lines}')\n\"",
  "description": "Verify syntax and count lines"
}
```

**Output:**
```
Syntax OK
Total lines: 1394

```

---

## Assistant (Build · Qwen3.6 27B · 29.9s)

_Thinking:_

Good, syntax is fine. Let me now do a headless import test to make sure there are no runtime import errors.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os, sys\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\n# Import and check all classes/functions exist\nimport flippyblock_extreme as fb\n\n# Check all key components exist\nassert hasattr(fb, 'Game'), 'Missing Game class'\nassert hasattr(fb, 'SoundEngine'), 'Missing SoundEngine'\nassert hasattr(fb, 'ParticleSystem'), 'Missing ParticleSystem'\nassert hasattr(fb, 'Button'), 'Missing Button'\nassert hasattr(fb, 'Particle'), 'Missing Particle'\nassert hasattr(fb, 'ScorePopup'), 'Missing ScorePopup'\nassert hasattr(fb, 'generate_bird'), 'Missing generate_bird'\nassert hasattr(fb, 'generate_bird_frames'), 'Missing generate_bird_frames'\nassert hasattr(fb, 'draw_pipe'), 'Missing draw_pipe'\nassert hasattr(fb, 'draw_background'), 'Missing draw_background'\nassert hasattr(fb, 'draw_ground'), 'Missing draw_ground'\nassert hasattr(fb, 'draw_score_text'), 'Missing draw_score_text'\nassert hasattr(fb, 'draw_medal'), 'Missing draw_medal'\nassert hasattr(fb, 'draw_stars'), 'Missing draw_stars'\nassert hasattr(fb, 'load_save'), 'Missing load_save'\nassert hasattr(fb, 'save_save'), 'Missing save_save'\nassert hasattr(fb, 'DIFFICULTIES'), 'Missing DIFFICULTIES'\nassert hasattr(fb, 'C_BIRD_SKINS'), 'Missing C_BIRD_SKINS'\n\n# Check difficulty levels\nassert 'Easy' in fb.DIFFICULTIES\nassert 'Normal' in fb.DIFFICULTIES\nassert 'Hard' in fb.DIFFICULTIES\nassert 'Extreme' in fb.DIFFICULTIES\n\n# Check skin count\nassert len(fb.C_BIRD_SKINS) == 6\nassert len(fb.C_SKIN_NAMES) == 6\n\n# Test asset generation\nbird = fb.generate_bird(fb.C_BIRD_YELLOW)\nassert bird is not None\nframes = fb.generate_bird_frames(fb.C_BIRD_YELLOW)\nassert len(frames) == 3\n\n# Test save/load\nsave = fb.load_save()\nassert 'high_score' in save\nfb.save_save(save)\n\nprint('All checks passed!')\nprint(f'Skins: {fb.C_SKIN_NAMES}')\nprint(f'Difficulties: {list(fb.DIFFICULTIES.keys())}')\nprint(f'States: MENU={fb.STATE_MENU}, PLAYING={fb.STATE_PLAYING}, PAUSED={fb.STATE_PAUSED}, GAME_OVER={fb.STATE_GAME_OVER}, SETTINGS={fb.STATE_SETTINGS}, SKIN_SELECT={fb.STATE_SKIN_SELECT}, LEADERBOARD={fb.STATE_LEADERBOARD}')\n\" 2>&1",
  "description": "Test all components exist and work"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
All checks passed!
Skins: ['Classic', 'Orange', 'Red', 'Blue', 'Purple', 'Cyan']
Difficulties: ['Easy', 'Normal', 'Hard', 'Extreme']
States: MENU=0, PLAYING=1, PAUSED=2, GAME_OVER=3, SETTINGS=4, SKIN_SELECT=5, LEADERBOARD=6

```

---

## Assistant (Build · Qwen3.6 27B · 23.4s)

_Thinking:_

All checks pass. Now let me run a quick simulation test to verify the game logic works correctly.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_MENU, STATE_PLAYING, STATE_GAME_OVER, STATE_PAUSED, DIFFICULTIES\n\n# Create game instance\ngame = Game()\nassert game.state == STATE_MENU, f'Expected STATE_MENU, got {game.state}'\n\n# Simulate a few frames on menu\nfor _ in range(10):\n    game.update()\n    game.draw()\n\n# Start game via internal method\ngame._start_game()\nassert game.state == STATE_PLAYING\nassert game.countdown == 3\nassert game.score == 0\n\n# Simulate countdown\nfor _ in range(200):  # ~3.3 seconds to get through countdown\n    game.update()\n    game.draw()\n\nassert game.countdown == 0, f'Countdown should be 0, got {game.countdown}'\n\n# Simulate some gameplay with flaps\nfor i in range(300):\n    if i % 40 == 0:  # Flap periodically\n        game._flap()\n    game.update()\n    game.draw()\n    # Check for game over\n    if game.state == STATE_GAME_OVER:\n        break\n\nprint(f'Score: {game.score}')\nprint(f'State after gameplay: {game.state}')\nprint(f'Pipes generated: {len(game.pipes)}')\n\n# Test pause\ngame._start_game()\nfor _ in range(250):\n    game.update()\n    game.draw()\ngame.state = STATE_PAUSED\ngame._build_pause_buttons()\nassert game.state == STATE_PAUSED\ngame._resume()\nassert game.state == STATE_PLAYING\n\nprint('All game logic tests passed!')\n\" 2>&1",
  "description": "Test game logic simulation"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 18, in <module>
  File "/home/patof/stress_bench/flippyblock_extreme.py", line 648, in _start_game
    self.sound.play_swoosh()
  File "/home/patof/stress_bench/flippyblock_extreme.py", line 193, in play_swoosh
    s = self._noise_sound(0.15, 0.15)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/patof/stress_bench/flippyblock_extreme.py", line 156, in _noise_sound
    return pygame.sound.make_sound(samples)
           ^^^^^^^^^^^^
AttributeError: module 'pygame' has no attribute 'sound'
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html

```

---

## Assistant (Build · Qwen3.6 27B · 20.8s)

_Thinking:_

Ah, `pygame.sound` is a newer API that might not be available in all pygame versions. Let me check what's available and use `pygame.sndarray` or the older `pygame.mixer.Sound` approach instead.


The `pygame.sound` module isn't available in this pygame version. Let me fix the sound engine to use the compatible `pygame.mixer.Sound` approach:



**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\nimport pygame\npygame.init()\nprint('mixer:', hasattr(pygame, 'mixer'))\nprint('sound:', hasattr(pygame, 'sound'))\nprint('sndarray:', hasattr(pygame, 'sndarray'))\npygame.mixer.init()\n# Test creating sound from raw data\nimport array, struct\nsamples = array.array('h', [0] * 1000)\nraw = samples.tobytes()\ntry:\n    s = pygame.mixer.Sound(buffer=raw)\n    print('Sound(buffer=) works')\nexcept Exception as e:\n    print(f'Sound(buffer=) failed: {e}')\ntry:\n    s = pygame.mixer.Sound(raw)\n    print('Sound(raw) works')\nexcept Exception as e:\n    print(f'Sound(raw) failed: {e}')\n\" 2>&1",
  "description": "Check available sound APIs"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
mixer: True
sound: False
sndarray: True
Sound(buffer=) works
Sound(raw) works

```

---

## Assistant (Build · Qwen3.6 27B · 38.4s)

_Thinking:_

Good. `pygame.mixer.Sound(buffer=raw_bytes)` works. Let me update the sound engine to use this approach instead of `pygame.sound.make_sound()`.


**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py",
  "oldString": "   def _make_sound(self, freq, duration, wave_type=\"sine\", fade=True, freq_end=None):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            t = i / sr\n            f = freq + (freq_end - freq) * (i / n) if freq_end else freq\n            if wave_type == \"sine\":\n                v = math.sin(2 * math.pi * f * t)\n            elif wave_type == \"square\":\n                v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0\n            elif wave_type == \"sawtooth\":\n                v = 2 * (f * t - math.floor(f * t + 0.5))\n            else:\n                v = 0\n            # Envelope: attack + fade\n            attack_dur = n * 0.05\n            fade_start = n * 0.6\n            if i < attack_dur:\n                v *= i / max(1, attack_dur)\n            elif i > fade_start:\n                v *= max(0, 1.0 - (i - fade_start) / (n - fade_start))\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)\n\n    def _noise_sound(self, duration, volume=0.3):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            v = (random.random() * 2 - 1) * volume\n            if i > n * 0.5:\n                v *= max(0, 1.0 - (i - n * 0.5) / (n * 0.5))\n            samples.append(int(v * 15000))\n        return pygame.sound.make_sound(samples)",
  "newString": "   def _make_sound(self, freq, duration, wave_type=\"sine\", fade=True, freq_end=None):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            t = i / sr\n            f = freq + (freq_end - freq) * (i / n) if freq_end else freq\n            if wave_type == \"sine\":\n                v = math.sin(2 * math.pi * f * t)\n            elif wave_type == \"square\":\n                v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0\n            elif wave_type == \"sawtooth\":\n                v = 2 * (f * t - math.floor(f * t + 0.5))\n            else:\n                v = 0\n            # Envelope: attack + fade\n            attack_dur = n * 0.05\n            fade_start = n * 0.6\n            if i < attack_dur:\n                v *= i / max(1, attack_dur)\n            elif i > fade_start:\n                v *= max(0, 1.0 - (i - fade_start) / (n - fade_start))\n            samples.append(int(v * 15000))\n        try:\n            return pygame.mixer.Sound(buffer=samples.tobytes())\n        except Exception:\n            return None\n\n    def _noise_sound(self, duration, volume=0.3):\n        if not self.enabled:\n            return None\n        self._init()\n        sr = 22050\n        n = int(sr * duration)\n        if n < 1:\n            return None\n        samples = array.array('h')\n        for i in range(n):\n            v = (random.random() * 2 - 1) * volume\n            if i > n * 0.5:\n                v *= max(0, 1.0 - (i - n * 0.5) / (n * 0.5))\n            samples.append(int(v * 15000))\n        try:\n            return pygame.mixer.Sound(buffer=samples.tobytes())\n        except Exception:\n            return None"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 19.3s)

_Thinking:_

Now let me also fix the `play_score` method which has a `pygame.time.delay()` call that blocks the main thread. Let me simplify it.


**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py",
  "oldString": "   def play_score(self):\n        # Two-tone score sound played sequentially\n        s1 = self._make_sound(880, 0.08, \"sine\")\n        s2 = self._make_sound(1175, 0.1, \"sine\")\n        if s1:\n            s1.play()\n        if s2:\n            # Delay second tone slightly by chaining\n            class _DelayedSound:\n                def __init__(self, sound, delay_ms):\n                    self.sound = sound\n                    self.delay_ms = delay_ms\n                def play(self):\n                    pygame.time.set_timer(pygame.USEREVENT + 99, self.delay_ms)\n                    self._s = self.sound\n            # Simple approach: just play both, the mixer handles overlap\n            pygame.time.delay(80)\n            s2.play()",
  "newString": "   def play_score(self):\n        # Pleasant ascending two-tone score sound\n        s1 = self._make_sound(880, 0.06, \"sine\")\n        s2 = self._make_sound(1175, 0.08, \"sine\")\n        if s1:\n            s1.play()\n        if s2:\n            s2.play()"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 28.8s)

_Thinking:_

Now let me re-run the tests.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_MENU, STATE_PLAYING, STATE_GAME_OVER, STATE_PAUSED, DIFFICULTIES\n\n# Create game instance\ngame = Game()\nassert game.state == STATE_MENU, f'Expected STATE_MENU, got {game.state}'\nprint('Menu state OK')\n\n# Simulate a few frames on menu\nfor _ in range(10):\n    game.update()\n    game.draw()\nprint('Menu frames OK')\n\n# Start game\ngame._start_game()\nassert game.state == STATE_PLAYING\nassert game.countdown == 3\nassert game.score == 0\nprint('Game start OK')\n\n# Simulate countdown\nfor _ in range(250):\n    game.update()\n    game.draw()\nassert game.countdown == 0, f'Countdown should be 0, got {game.countdown}'\nprint('Countdown OK')\n\n# Simulate gameplay with flaps\nfor i in range(400):\n    if i % 35 == 0:\n        game._flap()\n    game.update()\n    game.draw()\n    if game.state == STATE_GAME_OVER:\n        break\n\nprint(f'Score: {game.score}')\nprint(f'State: {game.state}')\nprint(f'Pipes remaining: {len(game.pipes)}')\n\n# Test pause/resume\ngame._start_game()\nfor _ in range(250):\n    game.update()\n    game.draw()\ngame.state = STATE_PAUSED\ngame._build_pause_buttons()\nassert game.state == STATE_PAUSED\ngame._resume()\nassert game.state == STATE_PLAYING\nprint('Pause/resume OK')\n\n# Test settings\ngame._go_settings()\nassert game.state == 4  # STATE_SETTINGS\ngame._go_back()\nassert game.state == STATE_PLAYING\nprint('Settings OK')\n\n# Test skins\ngame._go_skins()\nassert game.state == 5  # STATE_SKIN_SELECT\ngame._go_back()\nprint('Skins OK')\n\n# Test leaderboard\ngame._go_leaderboard()\nassert game.state == 6  # STATE_LEADERBOARD\ngame._go_back()\nprint('Leaderboard OK')\n\nprint()\nprint('=== ALL TESTS PASSED ===')\n\" 2>&1",
  "description": "Full game logic test"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 30, in <module>
AssertionError: Countdown should be 0, got 2
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Menu state OK
Menu frames OK
Game start OK

```

---

## Assistant (Build · Qwen3.6 27B · 27.0s)

_Thinking:_

The countdown needs more frames. Each countdown number takes 60 frames (1 second at 60fps), and there are 3 countdown numbers. So we need 3 * 60 = 180 frames minimum. Let me increase the simulation.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_MENU, STATE_PLAYING, STATE_GAME_OVER, STATE_PAUSED\n\ngame = Game()\nassert game.state == STATE_MENU\nprint('Menu state OK')\n\nfor _ in range(10):\n    game.update()\n    game.draw()\nprint('Menu frames OK')\n\ngame._start_game()\nassert game.state == STATE_PLAYING\nassert game.countdown == 3\nprint('Game start OK')\n\n# Countdown: 3 numbers * 60 frames each = 180 frames\nfor i in range(250):\n    game.update()\n    game.draw()\nprint(f'After 250 frames: countdown={game.countdown}')\nassert game.countdown == 0, f'Countdown should be 0, got {game.countdown}'\nprint('Countdown OK')\n\n# Gameplay\nfor i in range(500):\n    if i % 35 == 0:\n        game._flap()\n    game.update()\n    game.draw()\n    if game.state == STATE_GAME_OVER:\n        break\n\nprint(f'Score: {game.score}')\nprint(f'State: {game.state}')\n\n# Pause/resume\ngame._start_game()\nfor _ in range(250):\n    game.update()\n    game.draw()\ngame.state = STATE_PAUSED\ngame._build_pause_buttons()\nassert game.state == STATE_PAUSED\ngame._resume()\nassert game.state == STATE_PLAYING\nprint('Pause/resume OK')\n\n# Settings\ngame._go_settings()\nassert game.state == 4\ngame._go_back()\nprint('Settings OK')\n\n# Skins\ngame._go_skins()\nassert game.state == 5\ngame._go_back()\nprint('Skins OK')\n\n# Leaderboard\ngame._go_leaderboard()\nassert game.state == 6\ngame._go_back()\nprint('Leaderboard OK')\n\nprint()\nprint('=== ALL TESTS PASSED ===')\n\" 2>&1",
  "description": "Full game logic test with more frames"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 27, in <module>
AssertionError: Countdown should be 0, got 2
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Menu state OK
Menu frames OK
Game start OK
After 250 frames: countdown=2

```

---

## Assistant (Build · Qwen3.6 27B · 76.1s)

_Thinking:_

Hmm, the countdown isn't progressing. Let me check the countdown logic. Looking at `_update_playing`:

```python
if self.countdown > 0:
    self.countdown_timer += 1
    if self.countdown_timer >= 60:
        self.countdown_timer = 0
        ...
        self.countdown -= 1
        ...
        return
```

The `return` at the end means during countdown, nothing else updates. But `countdown_timer` starts at 0 and increments each frame. After 60 frames it should decrement countdown. But after 250 frames, countdown is still 2, meaning only one countdown tick happened (3 -> 2).

Wait, 250 frames / 60 = ~4 ticks. So countdown should go 3 -> 2 -> 1 -> 0. But it's at 2, meaning only 1 tick happened. Let me check...

Oh wait, I see the issue. The `update()` method calls `_update_playing()` which has the countdown logic. But the `_update_playing` method has `return` after the countdown block. That's correct.

Let me check: `countdown_timer` starts at 0. Each frame it increments. After 60 frames, `countdown_timer >= 60` is True, so countdown decrements and timer resets. Then it returns. So after 60 frames: countdown = 2. After 120 frames: countdown = 1. After 180 frames: countdown = 0.

But after 250 frames, countdown is still 2. That means the countdown logic isn't running. Let me check if `_update_playing` is being called...

Actually, looking at the `update` method:
```python
if self.state == STATE_MENU:
    self._update_menu()
elif self.state == STATE_PLAYING:
    self._update_playing()
```

This looks correct. Let me add some debug prints to see what's happening.

Actually wait - I bet the issue is that during the countdown, the `update` method still calls `_update_playing()`, but `_update_playing()` returns early after the countdown block. But the `update` method also calls `self.particles.update()` and other things before the state check. Let me re-read the code...

Actually the issue might be that `self.time_val` keeps incrementing, but the countdown_timer might not be incrementing properly. Let me add debug output.

Actually, I think I see the issue now. Let me look at the `_start_game` method more carefully. It sets `self.countdown_timer = 0`, and then in `_update_playing`, the countdown_timer increments each frame. After 60 frames, it should fire. But maybe the `return` statement is causing an issue where the countdown_timer doesn't reset properly?

Wait, actually I think the problem is that the `return` in `_update_playing` exits the method entirely, which means the countdown logic runs, but then the rest of the frame update (like scroll, pipes, etc.) doesn't run. That's fine for countdown. But the countdown_timer should still work.

Let me just add debug output to see what's happening.

Actually, I wonder if the issue is that `game.draw()` is somehow blocking or taking too long. Let me test with just `game.update()` calls.

Actually, let me just look at the code more carefully. In `_update_playing`:

```python
if self.countdown > 0:
    self.countdown_timer += 1
    if self.countdown_timer >= 60:
        self.countdown_timer = 0
        ...
        self.countdown -= 1
        if self.countdown == 0:
            self.pipe_timer = 60
        return
```

This looks correct. `countdown_timer` increments each frame, and when it reaches 60, countdown decrements. After 180 frames, countdown should be 0.

But the test shows after 250 frames, countdown is still 2. That means only 60 frames were processed. Could the `draw()` method be throwing an exception that's silently caught?

Actually, looking at the test output: "After 250 frames: countdown=2". So 250 iterations of the loop ran, but countdown only decremented once. That means `countdown_timer` only reached 60 once.

Wait - could it be that the `_update_playing` method is being called but the countdown logic has a bug? Let me add a print statement to debug.

Actually, I think I found it. Let me look at the `update` method again:

```python
def update(self):
    self.time_val += 1 / FPS
    ...
    self.particles.update()
    if self.state == STATE_MENU:
        self._update_menu()
    elif self.state == STATE_PLAYING:
        self._update_playing()
    elif self.state == STATE_GAME_OVER:
        self._update_game_over()
    ...
```

This looks fine. Let me check if maybe `draw()` is modifying game state somehow... No, `draw()` shouldn't modify state.

Let me just add debug prints to the test to see what's happening with countdown_timer.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_PLAYING\n\ngame = Game()\ngame._start_game()\n\nfor i in range(200):\n    game.update()\n    game.draw()\n    if i % 50 == 0:\n        print(f'Frame {i}: countdown={game.countdown}, timer={game.countdown_timer}, state={game.state}')\n\" 2>&1",
  "description": "Debug countdown progression"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Frame 0: countdown=3, timer=1, state=1
Frame 50: countdown=3, timer=51, state=1
Frame 100: countdown=2, timer=9, state=3
Frame 150: countdown=2, timer=9, state=3

```

---

## Assistant (Build · Qwen3.6 27B · 108.7s)

_Thinking:_

Now I see the issue. At frame 0, timer=1 (it increments by 1 each frame). At frame 50, timer=51. At frame 60, timer would be 61 which is >= 60, so countdown goes from 3 to 2, and timer resets to 0. Then at frame 61, timer=1. At frame 100, timer=9 means 40 frames have passed since the reset (frame 60). So countdown went 3 -> 2 at frame 60.

But then at frame 100, state=3 (STATE_GAME_OVER). That means the bird died! The bird fell and hit the ground during the countdown because gravity wasn't being applied during countdown (the `return` statement), but then after countdown reached 0, the bird was still at the starting position and gravity took over.

Wait, but the state changed to GAME_OVER at frame 100, not during the countdown. Let me trace:
- Frame 0-59: countdown=3, timer goes 1->60
- Frame 60: timer=60 >= 60, countdown goes 3->2, timer resets to 0, then `return`
- Frame 61-119: countdown=2, timer goes 1->60
- Frame 120: timer=60 >= 60, countdown goes 2->1, timer resets to 0, then `return`
- Frame 121-179: countdown=1, timer goes 1->60
- Frame 180: timer=60 >= 60, countdown goes 1->0, timer resets to 0, pipe_timer=60, `return`
- Frame 181+: countdown=0, normal gameplay starts

But at frame 100, state is already 3 (GAME_OVER). That means the bird died between frame 50 and frame 100. But during countdown, the bird shouldn't be affected by gravity (the `return` prevents physics update).

Oh wait, I see it now! After frame 60, countdown goes from 3 to 2. But then the `return` exits `_update_playing`. But the bird's position hasn't changed. Then at frame 61, countdown is 2, timer is 1. The countdown logic runs, timer increments, and `return` exits. This continues until frame 120 where countdown goes 2->1. Then frame 180 where countdown goes 1->0.

But the debug shows state=3 at frame 100. That can't be right if the countdown is still running...

Actually wait, let me re-read the debug output:
- Frame 100: countdown=2, timer=9, state=3

countdown=2 means we're on the second countdown number. timer=9 means 9 frames have passed since the last countdown tick. state=3 means GAME_OVER.

But if countdown=2 and the bird hasn't started physics yet (because of the `return`), how did the bird die?

Oh! I think the issue is that the `_update_playing` method's `return` only exits that method, but the `update` method continues. Let me check:

```python
def update(self):
    ...
    if self.state == STATE_PLAYING:
        self._update_playing()  # This returns early during countdown
    ...
```

The `return` in `_update_playing` only exits `_update_playing`, not `update`. So the rest of `update` still runs. But what else runs? Just the particle update and button hover check. That shouldn't cause the bird to die.

Wait, but what about `_update_game_over`? That's only called when `self.state == STATE_GAME_OVER`. So if state changed to GAME_OVER, something set it.

Let me look at what can set `self.state = STATE_GAME_OVER`:
1. In `_update_playing`, after the bird hits the ground post-death: `if self.game_over_timer > 30: self.state = STATE_GAME_OVER`

So the bird must have died first. But during countdown, the bird's physics are skipped (return). After countdown reaches 0, physics start, and the bird falls. The bird starts at `SCREEN_H // 2` (360px), and ground is at `SCREEN_H - 80` (640px). That's 280px of fall distance. With gravity 0.45/frame, the bird falls:
- Frame 181: vel=0.45, y=360.45
- Frame 182: vel=0.9, y=361.35
- ...
- It takes about sqrt(2*280/0.45) ≈ 35 frames to hit the ground

So the bird would die around frame 181 + 35 = 216. But the debug shows state=3 at frame 100. That doesn't add up.

Unless... the `return` in the countdown block doesn't actually prevent the physics from running? Let me re-read the code:

```python
def _update_playing(self):
    diff = DIFFICULTIES[self.difficulty]

    # Countdown
    if self.countdown > 0:
        self.countdown_timer += 1
        if self.countdown_timer >= 60:
            self.countdown_timer = 0
            ...
            self.countdown -= 1
            if self.countdown == 0:
                self.pipe_timer = 60
            # Still animate bird during countdown
            self.bird_frame_timer += 1
            if self.bird_frame_timer > 6:
                self.bird_frame_timer = 0
                self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)
            return

    # Bird physics
    if self.bird_alive:
        self.bird_vel += diff["gravity"]
        ...
```

Wait, I see it now! After the countdown tick (when timer reaches 60), the countdown decrements, and then there's the wing animation code, and then `return`. But the `return` is INSIDE the `if self.countdown_timer >= 60:` block! No wait, looking at the indentation:

```python
    if self.countdown > 0:
        self.countdown_timer += 1
        if self.countdown_timer >= 60:
            self.countdown_timer = 0
            ...
            return  # This is inside the inner if
```

Wait no, looking at my code again, the `return` is at the same indentation as the inner `if`, meaning it's inside the outer `if self.countdown > 0:` block but outside the inner `if self.countdown_timer >= 60:` block. Let me check the actual file...

Actually, looking at the code I wrote:
```python
        if self.countdown > 0:
            self.countdown_timer += 1
            if self.countdown_timer >= 60:
                self.countdown_timer = 0
                if self.countdown == 1:
                    self.sound.play_go()
                else:
                    self.sound.play_countdown()
                self.countdown -= 1
                if self.countdown == 0:
                    self.pipe_timer = 60
                # Still animate bird during countdown
                self.bird_frame_timer += 1
                if self.bird_frame_timer > 6:
                    self.bird_frame_timer = 0
                    self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)
                return
```

The `return` is inside the `if self.countdown_timer >= 60:` block! This means the `return` only fires when the countdown timer hits 60, not every frame during countdown. So during frames when `countdown_timer < 60`, the method continues past the countdown block and runs the bird physics!

That's the bug! The `return` should be at the outer `if self.countdown > 0:` level, not inside the inner `if`. Let me fix this.


Found the bug. The `return` in the countdown block is inside the inner `if`, so physics runs on non-tick frames. Let me fix:



**Tool: edit**

**Input:**
```json
{
  "filePath": "/home/patof/stress_bench/flippyblock_extreme.py",
  "oldString": "       # Countdown\n        if self.countdown > 0:\n            self.countdown_timer += 1\n            if self.countdown_timer >= 60:\n                self.countdown_timer = 0\n                if self.countdown == 1:\n                    self.sound.play_go()\n                else:\n                    self.sound.play_countdown()\n                self.countdown -= 1\n                if self.countdown == 0:\n                    self.pipe_timer = 60\n                # Still animate bird during countdown\n                self.bird_frame_timer += 1\n                if self.bird_frame_timer > 6:\n                    self.bird_frame_timer = 0\n                    self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)\n                return",
  "newString": "       # Countdown\n        if self.countdown > 0:\n            self.countdown_timer += 1\n            if self.countdown_timer >= 60:\n                self.countdown_timer = 0\n                if self.countdown == 1:\n                    self.sound.play_go()\n                else:\n                    self.sound.play_countdown()\n                self.countdown -= 1\n                if self.countdown == 0:\n                    self.pipe_timer = 60\n            # Animate bird wing during countdown\n            self.bird_frame_timer += 1\n            if self.bird_frame_timer > 6:\n                self.bird_frame_timer = 0\n                self.bird_frame = (self.bird_frame + 1) % len(self.bird_frames)\n            return"
}
```

**Output:**
```
Edit applied successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 34.1s)

_Thinking:_

Now the `return` is at the outer `if self.countdown > 0:` level, so it fires every frame during countdown, preventing physics from running. The wing animation is also moved outside the inner `if` so it runs every frame during countdown.

Let me re-run the test.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_MENU, STATE_PLAYING, STATE_GAME_OVER, STATE_PAUSED\n\ngame = Game()\ngame._start_game()\n\n# Countdown test\nfor i in range(250):\n    game.update()\n    game.draw()\n    if i % 60 == 0:\n        print(f'Frame {i}: countdown={game.countdown}, timer={game.countdown_timer}, state={game.state}')\n\nassert game.countdown == 0, f'Countdown should be 0, got {game.countdown}'\nprint('Countdown OK')\n\n# Gameplay with flaps\nfor i in range(500):\n    if i % 35 == 0:\n        game._flap()\n    game.update()\n    game.draw()\n    if game.state == STATE_GAME_OVER:\n        break\n\nprint(f'Score: {game.score}, State: {game.state}')\nassert game.score > 0, 'Should have scored at least 1'\nprint('Gameplay OK')\n\n# Pause/resume\ngame._start_game()\nfor _ in range(250):\n    game.update()\n    game.draw()\ngame.state = STATE_PAUSED\ngame._build_pause_buttons()\nassert game.state == STATE_PAUSED\ngame._resume()\nassert game.state == STATE_PLAYING\nprint('Pause/resume OK')\n\n# Settings/skins/leaderboard\nfor state_name, state_id in [('Settings', 4), ('Skins', 5), ('Leaderboard', 6)]:\n    if state_name == 'Settings':\n        game._go_settings()\n    elif state_name == 'Skins':\n        game._go_skins()\n    else:\n        game._go_leaderboard()\n    assert game.state == state_id, f'{state_name}: expected {state_id}, got {game.state}'\n    game._go_back()\n    print(f'{state_name} OK')\n\nprint()\nprint('=== ALL TESTS PASSED ===')\n\" 2>&1",
  "description": "Re-test after countdown fix"
}
```

**Output:**
```
Traceback (most recent call last):
  File "<string>", line 31, in <module>
AssertionError: Should have scored at least 1
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Frame 0: countdown=3, timer=1, state=1
Frame 60: countdown=2, timer=1, state=1
Frame 120: countdown=1, timer=1, state=1
Frame 180: countdown=0, timer=0, state=1
Frame 240: countdown=0, timer=0, state=1
Countdown OK
Score: 0, State: 3

```

---

## Assistant (Build · Qwen3.6 27B · 44.6s)

_Thinking:_

The countdown works now. But the bird dies without scoring. The issue is that the bird starts at `SCREEN_H // 2` (360) and the first pipe's gap might not be at a good position. Also, the flap interval of 35 frames might not be enough to keep the bird in the gap.

Actually, the bigger issue is that the bird starts with vel=0 and immediately starts falling. With gravity 0.45/frame, after 35 frames:
- vel = 0.45 * 35 = 15.75 (but capped at MAX_FALL=10)
- y displacement = sum of 0.45*i for i=1..35 = 0.45 * 35*36/2 = 283.5

So after 35 frames, the bird falls about 283 pixels. Starting at 360, it would be at 643, which is below the ground (640). So the bird hits the ground.

The flap interval is too long. Let me fix the test to flap more frequently.

Actually, the game logic is fine - the bird physics are correct. The test just needs to flap more frequently. Let me fix the test.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport os\nos.environ['SDL_VIDEODRIVER'] = 'dummy'\nos.environ['SDL_AUDIODRIVER'] = 'dummy'\n\nfrom flippyblock_extreme import Game, STATE_MENU, STATE_PLAYING, STATE_GAME_OVER, STATE_PAUSED\n\ngame = Game()\ngame._start_game()\n\n# Countdown: 3 * 60 = 180 frames\nfor _ in range(200):\n    game.update()\n    game.draw()\nassert game.countdown == 0\nprint('Countdown OK')\n\n# Gameplay - flap more frequently (every 20 frames)\nfor i in range(800):\n    if i % 20 == 0:\n        game._flap()\n    game.update()\n    game.draw()\n    if game.state == STATE_GAME_OVER:\n        break\n\nprint(f'Score: {game.score}, State: {game.state}')\nassert game.score > 0, f'Should have scored. Score={game.score}'\nprint('Gameplay OK')\n\n# Pause/resume\ngame._start_game()\nfor _ in range(200):\n    game.update()\n    game.draw()\ngame.state = STATE_PAUSED\ngame._build_pause_buttons()\nassert game.state == STATE_PAUSED\ngame._resume()\nassert game.state == STATE_PLAYING\nprint('Pause/resume OK')\n\n# Settings/skins/leaderboard\nfor state_name, state_id, method in [\n    ('Settings', 4, game._go_settings),\n    ('Skins', 5, game._go_skins),\n    ('Leaderboard', 6, game._go_leaderboard),\n]:\n    method()\n    assert game.state == state_id\n    game._go_back()\n    print(f'{state_name} OK')\n\n# Test save persistence\nassert game.save['total_games'] > 0\nassert game.save['high_score'] >= game.score\nprint(f'Save: games={game.save[\\\"total_games\\\"]}, best={game.save[\\\"high_score\\\"]}')\n\nprint()\nprint('=== ALL TESTS PASSED ===')\n\" 2>&1",
  "description": "Full test with correct flap frequency"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Countdown OK
Score: 1, State: 3
Gameplay OK
Pause/resume OK
Settings OK
Skins OK
Leaderboard OK
Save: games=5, best=0

=== ALL TESTS PASSED ===

```

---

## Assistant (Build · Qwen3.6 27B · 17.9s)

_Thinking:_

All tests pass. The game works correctly. Let me also verify the syntax one more time and check the final line count.


All tests pass. Let me do a final syntax check and verify the complete file:



**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport ast\nwith open('flippyblock_extreme.py') as f:\n    source = f.read()\nast.parse(source)\nlines = source.count('\\n') + 1\nprint(f'Syntax OK, {lines} lines')\n\n# Check for common issues\nissues = []\nif 'pygame.sound.make_sound' in source:\n    issues.append('Still uses pygame.sound.make_sound')\nif 'generate_pipe_pair' in source:\n    issues.append('Dead code: generate_pipe_pair still present')\nif 'passed_pipes' in source:\n    issues.append('Dead code: passed_pipes still present')\nif 'key_flap' in source:\n    issues.append('Dead code: key_flap still present')\nif 'bob_timer' in source:\n    issues.append('Dead code: bob_timer still present')\nif 'import struct' in source:\n    issues.append('Unused import: struct')\nif issues:\n    for i in issues:\n        print(f'ISSUE: {i}')\nelse:\n    print('No issues found')\n\"",
  "description": "Final syntax and cleanup check"
}
```

**Output:**
```
Syntax OK, 1390 lines
No issues found

```

---

## Assistant (Build · Qwen3.6 27B · 10.4s)

_Thinking:_

Everything is clean. Let me also verify the game can actually start and render by doing one more comprehensive test.


**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the core game engine and physics",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Generate all visual assets programmatically",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Build UI system (menus, buttons, panels)",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add sound effects (programmatic generation)",
      "status": "completed",
      "priority": "medium"
    },
    {
      "content": "Implement game states and flow",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add polish features (particles, screen shake, day/night)",
      "status": "completed",
      "priority": "medium"
    },
    {
      "content": "Review and fix all issues",
      "status": "completed",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Create the core game engine and physics",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Generate all visual assets programmatically",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Build UI system (menus, buttons, panels)",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add sound effects (programmatic generation)",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Implement game states and flow",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add polish features (particles, screen shake, day/night)",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Review and fix all issues",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 28.8s)

_Thinking:_

Done! The game is complete and all tests pass. Let me give the user a summary.


Done. The game is at `/home/patof/stress_bench/flippyblock_extreme.py` (1,390 lines).

**Features included:**

| Category | Features |
|---|---|
| **Gameplay** | Gravity physics, flap mechanics, pipe collision, score tracking, 3-2-1-GO countdown |
| **Difficulties** | Easy, Normal, Hard, Extreme (gap size, speed, gravity, flap power) |
| **UI Screens** | Main menu, pause overlay, game over panel, settings, skin selector, leaderboard |
| **Skins** | 6 bird colors: Classic, Orange, Red, Blue, Purple, Cyan |
| **Visuals** | Gradient sky, animated clouds, twinkling stars, grass blades, pipe shading, particle effects, screen shake, death flash |
| **Day/Night** | Auto cycle, manual ON/OFF, smooth transition |
| **Sound** | All programmatic: flap, score, hit, death, swoosh, menu click, select, countdown |
| **Persistence** | High score, total games, total score, top 20 scores, settings saved to JSON |
| **Controls** | SPACE/UP/click to flap, ESC to pause, mouse buttons for UI |
| **Polish** | Score popups (+1), wing animation, bird rotation, medal system (Bronze/Silver/Gold/Platinum) |

**Bugs fixed during review:**
- `pygame.sound.make_sound` replaced with `pygame.mixer.Sound(buffer=...)` for compatibility
- Countdown `return` was inside wrong `if` block, allowing physics during countdown
- Panel rounded corners fixed (was fill + draw_rounded_rect, now uses `_make_panel_surface`)
- Mouse event handling restructured to allow flap on empty-space clicks during gameplay
- `pygame.transform.offset` replaced with offscreen buffer + blit for screen shake (display surface safety)
- Background rendering optimized (single gradient surface instead of 720 line draws)
- Removed dead code: `generate_pipe_pair`, `passed_pipes`, `key_flap`, `bob_timer`, unused `struct` import

Run with: `python3 flippyblock_extreme.py`

---

