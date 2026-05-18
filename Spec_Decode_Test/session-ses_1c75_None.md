# Flippyblock Extreme Python game

**Session ID:** ses_1c753797effe5JgfZR8w0AEpXm
**Created:** 5/17/2026, 6:21:31 PM
**Updated:** 5/17/2026, 6:50:52 PM

---

## User

You are an expert Python Developer. Create a highly accurate flappybird game clone called flippyblock extreme in python. Add all additional features that would be expected in a common user interface. Do not use external assets for anything. If you need assets created, generate them in the code only. Only use pygame. Fully review your code and correct any issues after you produce the first version. 

---

## Assistant (Build · Qwen3.6 27B · 29.5s)

_Thinking:_

"


**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the FlippyBlock Extreme game with all core mechanics",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Add UI features: menu, HUD, settings, pause, game over screen",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Review and fix all bugs",
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
    "content": "Create the FlippyBlock Extreme game with all core mechanics",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Add UI features: menu, HUD, settings, pause, game over screen",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Review and fix all bugs",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 565.3s)

_Thinking:_

00.


**Tool: write**

**Input:**
```json
{
  "content": "\"\"\"\nFlippyBlock Extreme\nA Flappy Bird clone built entirely with pygame — no external assets.\n\"\"\"\n\nimport math\nimport os\nimport random\nimport sys\nimport json\nimport platform\nfrom pathlib import Path\n\n# ---------------------------------------------------------------------------\n# Try to import pygame; exit gracefully if unavailable\n# ---------------------------------------------------------------------------\ntry:\n    import pygame\nexcept ImportError:\n    print(\"pygame is required. Install it with: pip install pygame\")\n    sys.exit(1)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\nSCREEN_W = 480\nSCREEN_H = 720\nFPS = 60\n\n# Colors\nC_SKY_TOP = (100, 180, 255)\nC_SKY_BOT = (180, 225, 255)\nC_PIPE = (42, 150, 42)\nC_PIPE_HIGHLIGHT = (62, 200, 62)\nC_PIPE_SHADOW = (22, 110, 22)\nC_PIPE_CAP = (34, 130, 34)\nC_GROUND = (218, 165, 32)\nC_GROUND_DARK = (190, 140, 25)\nC_GROUND_GRASS = (90, 180, 50)\nC_WHITE = (255, 255, 255)\nC_BLACK = (0, 0, 0)\nC_BIRD_BODY = (255, 220, 40)\nC_BIRD_WING = (255, 180, 20)\nC_BIRD_BEAK = (255, 120, 30)\nC_BIRD_EYE = (255, 255, 255)\nC_BIRD_PUPIL = (20, 20, 20)\nC_TEXT = (255, 255, 255)\nC_TEXT_SHADOW = (0, 0, 0)\nC_MEDAL_GOLD = (255, 215, 0)\nC_MEDAL_SILVER = (192, 192, 192)\nC_MEDAL_BRONZE = (205, 127, 50)\nC_MEDAL_PLATINUM = (160, 190, 230)\nC_UI_BG = (40, 40, 60)\nC_UI_BORDER = (80, 80, 120)\nC_BUTTON_HOVER = (100, 100, 160)\nC_BUTTON_ACTIVE = (70, 70, 120)\nC_ACCENT = (255, 100, 100)\nC_CLOUD = (240, 245, 255)\nC_STARS = (255, 255, 220)\n\n# Physics\nGRAVITY = 0.55\nFLAP_POWER = -9.5\nMAX_FALL = 12\nPIPE_SPEED_BASE = 3.0\nPIPE_GAP_BASE = 160\nPIPE_GAP_MIN = 110\nPIPE_INTERVAL = 110  # frames between pipes\nGROUND_H = 80\nBIRD_X = 100\n\n# ---------------------------------------------------------------------------\n# Paths\n# ---------------------------------------------------------------------------\nSAVE_DIR = Path.home() / \".flippyblock\"\nSAVE_DIR.mkdir(exist_ok=True)\nSAVE_FILE = SAVE_DIR / \"scores.json\"\nSETTINGS_FILE = SAVE_DIR / \"settings.json\"\n\n# ---------------------------------------------------------------------------\n# Audio (generated at runtime)\n# ---------------------------------------------------------------------------\n\nclass SoundFX:\n    \"\"\"Procedural sound effects — no external files.\"\"\"\n\n    def __init__(self):\n        self.enabled = True\n        self._initialized = False\n\n    def init(self):\n        if self._initialized:\n            return\n        try:\n            pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)\n            self._initialized = True\n            self._cache = {}\n        except pygame.error:\n            self.enabled = False\n\n    def _make(self, name, factory):\n        if not self.enabled or not self._initialized:\n            return\n        if name not in self._cache:\n            self._cache[name] = factory()\n        return self._cache[name]\n\n    def _play(self, name):\n        sound = self._make(name, self._factories.get(name, lambda: None))\n        if sound:\n            sound.play()\n\n    # -- factories ----------------------------------------------------------\n    @staticmethod\n    def _flap():\n        length = 0.06\n        samples = int(22050 * length)\n        buf = pygame.sndarray.make_sound(\n            pygame.mixer.Sound(buffer=bytes(samples * 2))\n        )\n        arr = pygame.sndarray.array(buf)\n        t = numpy_like_range(samples)\n        freq = 600 + 400 * numpy_like_exp(-t / 80)\n        arr.fill(0)\n        for i in range(samples):\n            val = int(15000 * numpy_like_sin(2 * 3.14159 * freq[i] * i / 22050)\n                      * numpy_like_exp(-i / 100))\n            arr[i] = val\n        return buf\n\n    @staticmethod\n    def _score():\n        length = 0.15\n        samples = int(22050 * length)\n        buf = pygame.sndarray.make_sound(\n            pygame.mixer.Sound(buffer=bytes(samples * 2))\n        )\n        arr = pygame.sndarray.array(buf)\n        arr.fill(0)\n        for i in range(samples):\n            env = numpy_like_exp(-i / (samples * 0.3))\n            f1 = 880 + 440 * (i / samples)\n            val = int(12000 * env * numpy_like_sin(2 * 3.14159 * f1 * i / 22050))\n            arr[i] = val\n        return buf\n\n    @staticmethod\n    def _hit():\n        length = 0.2\n        samples = int(22050 * length)\n        buf = pygame.sndarray.make_sound(\n            pygame.mixer.Sound(buffer=bytes(samples * 2))\n        )\n        arr = pygame.sndarray.array(buf)\n        arr.fill(0)\n        for i in range(samples):\n            env = numpy_like_exp(-i / (samples * 0.25))\n            val = int(18000 * env * (random.random() * 2 - 1))\n            arr[i] = val\n        return buf\n\n    @staticmethod\n    def _die():\n        length = 0.4\n        samples = int(22050 * length)\n        buf = pygame.sndarray.make_sound(\n            pygame.mixer.Sound(buffer=bytes(samples * 2))\n        )\n        arr = pygame.sndarray.array(buf)\n        arr.fill(0)\n        for i in range(samples):\n            env = numpy_like_exp(-i / (samples * 0.4))\n            f = 500 - 300 * (i / samples)\n            val = int(15000 * env * numpy_like_sin(2 * 3.14159 * f * i / 22050))\n            arr[i] = val\n        return buf\n\n    @staticmethod\n    def _swoosh():\n        length = 0.1\n        samples = int(22050 * length)\n        buf = pygame.sndarray.make_sound(\n            pygame.mixer.Sound(buffer=bytes(samples * 2))\n        )\n        arr = pygame.sndarray.array(buf)\n        arr.fill(0)\n        for i in range(samples):\n            env = numpy_like_sin(3.14159 * i / samples)\n            val = int(6000 * env * (random.random() * 2 - 1))\n            arr[i] = val\n        return buf\n\n    _factories = {\n        \"flap\": _flap,\n        \"score\": _score,\n        \"hit\": _hit,\n        \"die\": _die,\n        \"swoosh\": _swoosh,\n    }\n\n    def flap(self):\n        self._play(\"flap\")\n\n    def score(self):\n        self._play(\"score\")\n\n    def hit(self):\n        self._play(\"hit\")\n\n    def die(self):\n        self._play(\"die\")\n\n    def swoosh(self):\n        self._play(\"swoosh\")\n\n\n# Lightweight numpy-like helpers so we don't need numpy\ndef numpy_like_range(n):\n    return list(range(n))\n\n\ndef numpy_like_exp(x):\n    return math.exp(x) if not isinstance(x, list) else [math.exp(v) for v in x]\n\n\ndef numpy_like_sin(x):\n    return math.sin(x) if not isinstance(x, list) else [math.sin(v) for v in x]\n\n\n# ---------------------------------------------------------------------------\n# Simple procedural sound fallback (no sndarray needed)\n# ---------------------------------------------------------------------------\nclass SimpleSound:\n    \"\"\"Fallback sound generator using raw wave synthesis.\"\"\"\n\n    def __init__(self):\n        self.enabled = True\n        self._sounds = {}\n\n    def init(self):\n        try:\n            pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)\n            self._build()\n        except pygame.error:\n            self.enabled = False\n\n    def _build(self):\n        self._sounds[\"flap\"] = self._gen_flap()\n        self._sounds[\"score\"] = self._gen_score()\n        self._sounds[\"hit\"] = self._gen_hit()\n        self._sounds[\"die\"] = self._gen_die()\n        self._sounds[\"swoosh\"] = self._gen_swoosh()\n\n    @staticmethod\n    def _gen_flap():\n        n = int(22050 * 0.06)\n        frames = pygame.sndarray.zeros((n,), int16_dtype())\n        for i in range(n):\n            f = 600 + 400 * math.exp(-i / 80)\n            frames[i] = int(15000 * math.sin(2 * 3.14159 * f * i / 22050)\n                            * math.exp(-i / 100))\n        return pygame.sndarray.make_sound(frames)\n\n    @staticmethod\n    def _gen_score():\n        n = int(22050 * 0.15)\n        frames = pygame.sndarray.zeros((n,), int16_dtype())\n        for i in range(n):\n            env = math.exp(-i / (n * 0.3))\n            f1 = 880 + 440 * (i / n)\n            frames[i] = int(12000 * env * math.sin(2 * 3.14159 * f1 * i / 22050))\n        return pygame.sndarray.make_sound(frames)\n\n    @staticmethod\n    def _gen_hit():\n        n = int(22050 * 0.2)\n        frames = pygame.sndarray.zeros((n,), int16_dtype())\n        for i in range(n):\n            env = math.exp(-i / (n * 0.25))\n            frames[i] = int(18000 * env * (random.random() * 2 - 1))\n        return pygame.sndarray.make_sound(frames)\n\n    @staticmethod\n    def _gen_die():\n        n = int(22050 * 0.4)\n        frames = pygame.sndarray.zeros((n,), int16_dtype())\n        for i in range(n):\n            env = math.exp(-i / (n * 0.4))\n            f = 500 - 300 * (i / n)\n            frames[i] = int(15000 * env * math.sin(2 * 3.14159 * f * i / 22050))\n        return pygame.sndarray.make_sound(frames)\n\n    @staticmethod\n    def _gen_swoosh():\n        n = int(22050 * 0.1)\n        frames = pygame.sndarray.zeros((n,), int16_dtype())\n        for i in range(n):\n            env = math.sin(3.14159 * i / n)\n            frames[i] = int(6000 * env * (random.random() * 2 - 1))\n        return pygame.sndarray.make_sound(frames)\n\n    def play(self, name):\n        if not self.enabled or name not in self._sounds:\n            return\n        self._sounds[name].play()\n\n\ndef int16_dtype():\n    return pygame.sndarray.Int16Array\n\n\n# ---------------------------------------------------------------------------\n# Settings persistence\n# ---------------------------------------------------------------------------\nclass Settings:\n    DEFAULT = {\n        \"sound\": True,\n        \"music\": False,\n        \"difficulty\": \"normal\",  # easy, normal, hard, extreme\n        \"bird_skin\": 0,\n        \"shake\": True,\n        \"show_fps\": False,\n    }\n\n    DIFFICULTY = {\n        \"easy\":   {\"gravity\": 0.4, \"flap\": -8, \"gap\": 190, \"speed\": 2.2, \"label\": \"Easy\"},\n        \"normal\": {\"gravity\": 0.55, \"flap\": -9.5, \"gap\": 160, \"speed\": 3.0, \"label\": \"Normal\"},\n        \"hard\":   {\"gravity\": 0.65, \"flap\": -10.5, \"gap\": 140, \"speed\": 3.6, \"label\": \"Hard\"},\n        \"extreme\":{\"gravity\": 0.75, \"flap\": -11, \"gap\": 120, \"speed\": 4.2, \"label\": \"Extreme\"},\n    }\n\n    def __init__(self):\n        self.data = dict(self.DEFAULT)\n        self._load()\n\n    def _load(self):\n        try:\n            if SETTINGS_FILE.exists():\n                with open(SETTINGS_FILE) as f:\n                    saved = json.load(f)\n                self.data.update(saved)\n        except Exception:\n            pass\n\n    def save(self):\n        try:\n            with open(SETTINGS_FILE, \"w\") as f:\n                json.dump(self.data, f)\n        except Exception:\n            pass\n\n    def get_difficulty(self):\n        return self.DIFFICULTY.get(self.data[\"difficulty\"], self.DIFFICULTY[\"normal\"])\n\n\n# ---------------------------------------------------------------------------\n# Score persistence\n# ---------------------------------------------------------------------------\nclass Scores:\n    def __init__(self):\n        self.history = []\n        self.medals = {}\n        self._load()\n\n    def _load(self):\n        try:\n            if SAVE_FILE.exists():\n                with open(SAVE_FILE) as f:\n                    data = json.load(f)\n                self.history = data.get(\"history\", [])\n                self.medals = data.get(\"medals\", {})\n        except Exception:\n            pass\n\n    def save(self):\n        try:\n            with open(SAVE_FILE, \"w\") as f:\n                json.dump({\"history\": self.history[-50:], \"medals\": self.medals}, f)\n        except Exception:\n            pass\n\n    def add(self, score):\n        self.history.append(score)\n        self.save()\n\n    def best(self):\n        return max(self.history) if self.history else 0\n\n    def get_medal(self, score):\n        if score >= 40:\n            return \"platinum\"\n        if score >= 20:\n            return \"gold\"\n        if score >= 10:\n            return \"silver\"\n        if score >= 5:\n            return \"bronze\"\n        return None\n\n\n# ---------------------------------------------------------------------------\n# Asset generation (all procedural)\n# ---------------------------------------------------------------------------\nclass Assets:\n    \"\"\"Generates all visual assets at runtime.\"\"\"\n\n    def __init__(self, screen):\n        self.screen = screen\n        self.screen_w = screen.get_width()\n        self.screen_h = screen.get_height()\n        self._build()\n\n    def _build(self):\n        self.bird_frames = self._make_bird_frames()\n        self.pipe_top = self._make_pipe_top()\n        self.pipe_bottom = self._make_pipe_bottom()\n        self.ground = self._make_ground()\n        self.clouds = self._make_clouds()\n        self.background = self._make_background()\n        self.medal_icons = self._make_medals()\n        self.particle_surf = pygame.Surface((3, 3), pygame.SRCALPHA)\n        self.particle_surf.fill((255, 255, 255, 200))\n        self.star_surf = self._make_star()\n        self.get_ready = self._make_get_ready()\n        self.game_over_panel = self._make_game_over_panel()\n        self.menu_bg = self._make_menu_bg()\n        self.title_text = self._make_title()\n        self.buttons = {}\n        self._make_buttons()\n\n    def _make_bird_frames(self):\n        \"\"\"Three bird animation frames (wing up, mid, down).\"\"\"\n        frames = []\n        wing_offsets = [-3, 0, 3]  # up, mid, down\n        for wo in wing_offsets:\n            s = pygame.Surface((34, 26), pygame.SRCALPHA)\n            # Body\n            pygame.draw.ellipse(s, C_BIRD_BODY, (2, 4, 28, 18))\n            # Highlight\n            pygame.draw.ellipse(s, (255, 240, 100), (6, 6, 16, 8))\n            # Wing\n            pygame.draw.ellipse(s, C_BIRD_WING, (8, 10 + wo, 14, 8))\n            # Beak\n            pts = [(28, 10), (34, 12), (28, 15)]\n            pygame.draw.polygon(s, C_BIRD_BEAK, pts)\n            # Eye white\n            pygame.draw.circle(s, C_BIRD_EYE, (24, 9), 5)\n            # Pupil\n            pygame.draw.circle(s, C_BIRD_PUPIL, (26, 9), 2)\n            # Eye shine\n            pygame.draw.circle(s, C_WHITE, (27, 7), 1)\n            frames.append(s)\n        return frames\n\n    def _make_pipe_top(self):\n        \"\"\"Top pipe (cap at bottom).\"\"\"\n        w, h = 62, 400\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        # Main body\n        pygame.draw.rect(s, C_PIPE, (3, 0, w - 6, h))\n        # Highlight\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (6, 0, 8, h))\n        # Shadow\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 14, 0, 8, h))\n        # Cap\n        cap_h = 28\n        pygame.draw.rect(s, C_PIPE_CAP, (0, h - cap_h, w, cap_h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (3, h - cap_h + 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 12, h - cap_h + 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_WHITE, (1, h - cap_h + 1, w - 2, 2), 1)\n        return s\n\n    def _make_pipe_bottom(self):\n        \"\"\"Bottom pipe (cap at top).\"\"\"\n        w, h = 62, 400\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        pygame.draw.rect(s, C_PIPE, (3, 0, w - 6, h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (6, 0, 8, h))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 14, 0, 8, h))\n        cap_h = 28\n        pygame.draw.rect(s, C_PIPE_CAP, (0, 0, w, cap_h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (3, 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 12, 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_WHITE, (1, cap_h - 3, w - 2, 2), 1)\n        return s\n\n    def _make_ground(self):\n        w = self.screen_w\n        h = GROUND_H\n        s = pygame.Surface((w, h))\n        s.fill(C_GROUND)\n        # Grass strip\n        pygame.draw.rect(s, C_GROUND_GRASS, (0, 0, w, 14))\n        pygame.draw.rect(s, (70, 160, 40), (0, 12, w, 4))\n        # Dirt texture\n        for i in range(0, w, 24):\n            pygame.draw.rect(s, C_GROUND_DARK, (i, 16, 24, h - 16), 1)\n        # Pattern\n        for i in range(0, w, 48):\n            pygame.draw.circle(s, C_GROUND_DARK, (i + 12, 35), 4)\n            pygame.draw.circle(s, C_GROUND_DARK, (i + 36, 50), 3)\n        return s\n\n    def _make_clouds(self):\n        clouds = []\n        for _ in range(6):\n            cw = random.randint(60, 140)\n            ch = random.randint(20, 40)\n            s = pygame.Surface((cw, ch), pygame.SRCALPHA)\n            cx, cy = cw // 2, ch // 2\n            r = ch // 2\n            pygame.draw.circle(s, C_CLOUD, (cx, cy), r)\n            pygame.draw.circle(s, C_CLOUD, (cx - r * 0.6, cy + 2), int(r * 0.7))\n            pygame.draw.circle(s, C_CLOUD, (cx + r * 0.7, cy + 1), int(r * 0.8))\n            clouds.append((s, random.randint(0, self.screen_w),\n                           random.randint(30, 200), random.uniform(0.2, 0.8)))\n        return clouds\n\n    def _make_background(self):\n        s = pygame.Surface((self.screen_w, self.screen_h))\n        for y in range(self.screen_h):\n            t = y / self.screen_h\n            r = int(C_SKY_TOP[0] + (C_SKY_BOT[0] - C_SKY_TOP[0]) * t)\n            g = int(C_SKY_TOP[1] + (C_SKY_BOT[1] - C_SKY_TOP[1]) * t)\n            b = int(C_SKY_TOP[2] + (C_SKY_BOT[2] - C_SKY_TOP[2]) * t)\n            pygame.draw.line(s, (r, g, b), (0, y), (self.screen_w, y))\n        return s\n\n    def _make_medals(self):\n        medals = {}\n        for name, color in [(\"bronze\", C_MEDAL_BRONZE), (\"silver\", C_MEDAL_SILVER),\n                            (\"gold\", C_MEDAL_GOLD), (\"platinum\", C_MEDAL_PLATINUM)]:\n            s = pygame.Surface((48, 48), pygame.SRCALPHA)\n            pygame.draw.circle(s, color, (24, 24), 20)\n            pygame.draw.circle(s, (min(color[0] + 40, 255),\n                                    min(color[1] + 40, 255),\n                                    min(color[2] + 40, 255)), (24, 24), 16)\n            pygame.draw.circle(s, color, (24, 24), 14, 2)\n            # Star\n            star_pts = []\n            for i in range(5):\n                a = -math.pi / 2 + 2 * math.pi * i / 5\n                star_pts.append((24 + 8 * math.cos(a), 24 + 8 * math.sin(a)))\n                a2 = a + math.pi / 5\n                star_pts.append((24 + 4 * math.cos(a2), 24 + 4 * math.sin(a2)))\n            pygame.draw.polygon(s, (max(color[0] - 60, 0),\n                                     max(color[1] - 60, 0),\n                                     max(color[2] - 60, 0)), star_pts)\n            medals[name] = s\n        return medals\n\n    def _make_star(self):\n        s = pygame.Surface((12, 12), pygame.SRCALPHA)\n        pts = []\n        for i in range(5):\n            a = -math.pi / 2 + 2 * math.pi * i / 5\n            pts.append((6 + 5 * math.cos(a), 6 + 5 * math.sin(a)))\n            a2 = a + math.pi / 5\n            pts.append((6 + 2.5 * math.cos(a2), 6 + 2.5 * math.sin(a2)))\n        pygame.draw.polygon(s, C_STARS, pts)\n        return s\n\n    def _make_get_ready(self):\n        s = pygame.Surface((280, 80), pygame.SRCALPHA)\n        # Arrow indicator\n        arrow = pygame.Surface((60, 40), pygame.SRCALPHA)\n        pts = [(30, 0), (60, 20), (30, 40), (20, 40), (20, 28), (0, 20), (20, 12), (20, 0)]\n        pygame.draw.polygon(arrow, (255, 255, 255, 180), pts)\n        s.blit(arrow, (110, 20))\n        return s\n\n    def _make_game_over_panel(self):\n        w, h = 320, 220\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        # Rounded rect\n        r = 16\n        rect = pygame.Rect(0, 0, w, h)\n        _draw_rounded_rect(s, C_UI_BG, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 3, border_radius=r)\n        return s\n\n    def _make_menu_bg(self):\n        s = pygame.Surface((self.screen_w, self.screen_h), pygame.SRCALPHA)\n        # Gradient\n        for y in range(self.screen_h):\n            t = y / self.screen_h\n            r = int(30 + 20 * t)\n            g = int(30 + 20 * t)\n            b = int(60 + 40 * t)\n            pygame.draw.line(s, (r, g, b, 180), (0, y), (self.screen_w, y))\n        return s\n\n    def _make_title(self):\n        font = pygame.font.Font(None, 72)\n        t1 = font.render(\"FLIPPY\", True, (255, 200, 50))\n        t2 = font.render(\"BLOCK\", True, (255, 150, 50))\n        t3 = pygame.font.Font(None, 36).render(\"EXTREME\", True, (255, 100, 100))\n        w = max(t1.get_width(), t2.get_width(), t3.get_width())\n        h = t1.get_height() + t2.get_height() + t3.get_height() + 10\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        s.blit(t1, ((w - t1.get_width()) // 2, 0))\n        s.blit(t2, ((w - t2.get_width()) // 2, t1.get_height()))\n        s.blit(t3, ((w - t3.get_width()) // 2, t1.get_height() + t2.get_height() + 5))\n        return s\n\n    def _make_buttons(self):\n        labels = [\"PLAY\", \"SETTINGS\", \"LEADERBOARD\", \"BACK\", \"RETRY\",\n                  \"SOUND\", \"SHAKE\", \"EASY\", \"NORMAL\", \"HARD\", \"EXTREME\"]\n        for label in labels:\n            self.buttons[label] = self._make_button(label)\n\n    def _make_button(self, text, w=220, h=48):\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 10\n        rect = pygame.Rect(0, 0, w, h)\n        _draw_rounded_rect(s, C_UI_BG, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 36)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n\ndef _draw_rounded_rect(surf, color, rect, radius):\n    \"\"\"Draw a filled rounded rectangle.\"\"\"\n    points = [\n        (rect.x + radius, rect.y),\n        (rect.x + rect.width - radius, rect.y),\n        (rect.x + rect.width, rect.y + radius),\n        (rect.x + rect.width, rect.y + rect.height - radius),\n        (rect.x + rect.width - radius, rect.y + rect.height),\n        (rect.x + radius, rect.y + rect.height),\n        (rect.x, rect.y + rect.height - radius),\n        (rect.x, rect.y + radius),\n    ]\n    # Fill center rects\n    pygame.draw.rect(surf, color, (rect.x + radius, rect.y,\n                                    rect.width - 2 * radius, rect.height))\n    pygame.draw.rect(surf, color, (rect.x, rect.y + radius,\n                                    rect.width, rect.height - 2 * radius))\n    # Corner circles\n    for px, py in [(rect.x + radius, rect.y + radius),\n                   (rect.x + rect.width - radius, rect.y + radius),\n                   (rect.x + radius, rect.y + rect.height - radius),\n                   (rect.x + rect.width - radius, rect.y + rect.height - radius)]:\n        pygame.draw.circle(surf, color, (px, py), radius)\n\n\n# ---------------------------------------------------------------------------\n# Bird\n# ---------------------------------------------------------------------------\nclass Bird:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.vel = 0\n        self.frame = 0\n        self.frame_timer = 0\n        self.alive = True\n        self.rotation = 0\n        self.width = 34\n        self.height = 26\n        self.dead_timer = 0\n\n    def flap(self, power):\n        self.vel = power\n\n    def update(self, gravity):\n        if not self.alive:\n            self.dead_timer += 1\n            self.vel += gravity\n            self.y += self.vel\n            self.rotation = min(self.rotation + 120, 900)\n            return\n        self.vel += gravity\n        if self.vel > MAX_FALL:\n            self.vel = MAX_FALL\n        self.y += self.vel\n        # Rotation based on velocity\n        if self.vel < 0:\n            self.rotation = max(-30, self.vel * 3)\n        else:\n            self.rotation = min(90, self.rotation + 2.5)\n        # Wing animation\n        self.frame_timer += 1\n        if self.frame_timer >= 6:\n            self.frame_timer = 0\n            self.frame = (self.frame + 1) % 3\n\n    def get_rect(self):\n        return pygame.Rect(self.x - self.width // 2 + 4,\n                           self.y - self.height // 2 + 4,\n                           self.width - 8, self.height - 8)\n\n\n# ---------------------------------------------------------------------------\n# Pipe\n# ---------------------------------------------------------------------------\nclass Pipe:\n    def __init__(self, x, gap_y, gap_size, speed):\n        self.x = x\n        self.gap_y = gap_y  # center of gap\n        self.gap_size = gap_size\n        self.speed = speed\n        self.scored = False\n        self.width = 62\n\n    def update(self):\n        self.x -= self.speed\n\n    def is_offscreen(self):\n        return self.x < -self.width - 10\n\n    def get_rects(self, screen_h, ground_h):\n        top_h = self.gap_y - self.gap_size // 2\n        bot_y = self.gap_y + self.gap_size // 2\n        bot_h = screen_h - ground_h - bot_y\n        top_rect = pygame.Rect(self.x, 0, self.width, max(top_h, 0))\n        bot_rect = pygame.Rect(self.x, bot_y, self.width, max(bot_h, 0))\n        return top_rect, bot_rect\n\n\n# ---------------------------------------------------------------------------\n# Particle system\n# ---------------------------------------------------------------------------\nclass Particle:\n    def __init__(self, x, y, color=None):\n        self.x = x\n        self.y = y\n        self.vx = random.uniform(-3, 3)\n        self.vy = random.uniform(-4, 1)\n        self.life = random.randint(20, 50)\n        self.max_life = self.life\n        self.size = random.randint(2, 5)\n        if color:\n            self.color = color\n        else:\n            self.color = random.choice([(255, 255, 255), (255, 220, 40),\n                                         (255, 180, 20), (255, 255, 200)])\n\n    def update(self):\n        self.x += self.vx\n        self.y += self.vy\n        self.vy += 0.15\n        self.life -= 1\n\n    def draw(self, surf, asset_surf):\n        alpha = int(200 * (self.life / self.max_life))\n        s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)\n        s.fill((*self.color[:3], alpha) if len(self.color) == 4 else (*self.color, alpha))\n        surf.blit(s, (int(self.x), int(self.y)))\n\n\n# ---------------------------------------------------------------------------\n# Floating score popup\n# ---------------------------------------------------------------------------\nclass ScorePopup:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.life = 40\n        self.max_life = 40\n\n    def update(self):\n        self.y -= 1.2\n        self.life -= 1\n\n    def draw(self, surf):\n        if self.life <= 0:\n            return\n        alpha = min(255, int(255 * self.life / self.max_life))\n        font = pygame.font.Font(None, 48)\n        ts = font.render(\"+1\", True, (255, 255, 255))\n        ts.set_alpha(alpha)\n        surf.blit(ts, (self.x - ts.get_width() // 2, self.y))\n\n    def is_dead(self):\n        return self.life <= 0\n\n\n# ---------------------------------------------------------------------------\n# Game states\n# ---------------------------------------------------------------------------\nclass GameState:\n    MENU = 0\n    GET_READY = 1\n    PLAYING = 2\n    GAME_OVER = 3\n    SETTINGS = 4\n    LEADERBOARD = 5\n\n\n# ---------------------------------------------------------------------------\n# Main game class\n# ---------------------------------------------------------------------------\nclass FlippyBlockExtreme:\n    def __init__(self):\n        pygame.init()\n        pygame.display.set_caption(\"FlippyBlock Extreme\")\n\n        # Icon\n        icon = pygame.Surface((32, 32), pygame.SRCALPHA)\n        pygame.draw.ellipse(icon, C_BIRD_BODY, (2, 6, 28, 20))\n        pygame.draw.ellipse(icon, C_BIRD_WING, (8, 10, 14, 8))\n        pygame.draw.circle(icon, C_BIRD_EYE, (24, 10), 4)\n        pygame.draw.circle(icon, C_BIRD_PUPIL, (26, 10), 2)\n        pts = [(28, 12), (32, 14), (28, 17)]\n        pygame.draw.polygon(icon, C_BIRD_BEAK, pts)\n        pygame.display.set_icon(icon)\n\n        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))\n        self.clock = pygame.time.Clock()\n        self.font = pygame.font.Font(None, 36)\n        self.font_big = pygame.font.Font(None, 72)\n        self.font_small = pygame.font.Font(None, 24)\n        self.font_huge = pygame.font.Font(None, 96)\n\n        self.settings = Settings()\n        self.scores = Scores()\n        self.sound = SimpleSound()\n        self.sound.init()\n\n        self.assets = Assets(self.screen)\n        self.state = GameState.MENU\n        self.diff = self.settings.get_difficulty()\n\n        # Game objects\n        self.bird = None\n        self.pipes = []\n        self.particles = []\n        self.popups = []\n        self.score = 0\n        self.frame_count = 0\n        self.pipe_timer = 0\n        self.ground_offset = 0\n        self.shake_x = 0\n        self.shake_y = 0\n        self.shake_timer = 0\n        self.flash_alpha = 0\n        self.get_ready_timer = 0\n        self.game_over_timer = 0\n        self.menu_bird_y = SCREEN_H // 2 - 40\n        self.menu_bird_vel = 0\n        self.settings_scroll = 0\n        self.leaderboard_scroll = 0\n        self.difficulty_labels = [\"EASY\", \"NORMAL\", \"HARD\", \"EXTREME\"]\n        self.difficulty_keys = [\"easy\", \"normal\", \"hard\", \"extreme\"]\n\n        # Clouds state\n        self.cloud_positions = []\n        for c in self.assets.clouds:\n            self.cloud_positions.append([c[1], c[2], c[3]])\n\n    def run(self):\n        running = True\n        while running:\n            dt = self.clock.tick(FPS)\n            self._handle_events()\n            self._update()\n            self._draw()\n            pygame.display.flip()\n            for event in pygame.event.get():\n                if event.type == pygame.QUIT:\n                    running = False\n\n        pygame.quit()\n        sys.exit()\n\n    # ------------------------------------------------------------------\n    # Events\n    # ------------------------------------------------------------------\n    def _handle_events(self):\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                pygame.quit()\n                sys.exit()\n\n            if event.type == pygame.KEYDOWN:\n                if event.key == pygame.K_ESCAPE:\n                    self._on_escape()\n                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:\n                    self._on_action()\n                if event.key == pygame.K_r:\n                    self._on_restart()\n\n            if event.type == pygame.MOUSEBUTTONDOWN:\n                if event.button == 1:\n                    self._on_click(event.pos)\n\n    def _on_escape(self):\n        if self.state == GameState.SETTINGS or self.state == GameState.LEADERBOARD:\n            self.state = GameState.MENU\n            self.sound.swoosh()\n        elif self.state == GameState.PLAYING:\n            self.state = GameState.MENU\n            self.sound.swoosh()\n        elif self.state == GameState.GAME_OVER:\n            pass  # don't escape from game over\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.MENU\n            self.sound.swoosh()\n\n    def _on_action(self):\n        if self.state == GameState.MENU:\n            self._start_game()\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.PLAYING\n            self.bird.flap(self.diff[\"flap\"])\n            self.sound.flap()\n        elif self.state == GameState.PLAYING:\n            if self.bird and self.bird.alive:\n                self.bird.flap(self.diff[\"flap\"])\n                self.sound.flap()\n                self._spawn_particles(self.bird.x, self.bird.y + 5, 3)\n        elif self.state == GameState.GAME_OVER:\n            if self.game_over_timer > 60:\n                self.state = GameState.MENU\n                self.sound.swoosh()\n\n    def _on_restart(self):\n        if self.state == GameState.GAME_OVER and self.game_over_timer > 30:\n            self._start_game()\n            self.sound.swoosh()\n\n    def _on_click(self, pos):\n        mx, my = pos\n\n        if self.state == GameState.MENU:\n            self._handle_menu_click(mx, my)\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.PLAYING\n            self.bird.flap(self.diff[\"flap\"])\n            self.sound.flap()\n        elif self.state == GameState.PLAYING:\n            if self.bird and self.bird.alive:\n                self.bird.flap(self.diff[\"flap\"])\n                self.sound.flap()\n                self._spawn_particles(self.bird.x, self.bird.y + 5, 3)\n        elif self.state == GameState.GAME_OVER:\n            self._handle_gameover_click(mx, my)\n        elif self.state == GameState.SETTINGS:\n            self._handle_settings_click(mx, my)\n        elif self.state == GameState.LEADERBOARD:\n            self._handle_leaderboard_click(mx, my)\n\n    # ------------------------------------------------------------------\n    # Menu buttons layout\n    # ------------------------------------------------------------------\n    def _menu_buttons(self):\n        btn_w, btn_h = 220, 48\n        cx = SCREEN_W // 2\n        start_y = 340\n        buttons = {}\n        for i, label in enumerate([\"PLAY\", \"SETTINGS\", \"LEADERBOARD\"]):\n            y = start_y + i * (btn_h + 16)\n            rect = pygame.Rect(cx - btn_w // 2, y, btn_w, btn_h)\n            buttons[label] = rect\n        return buttons\n\n    def _handle_menu_click(self, mx, my):\n        buttons = self._menu_buttons()\n        for label, rect in buttons.items():\n            if rect.collidepoint(mx, my):\n                self.sound.swoosh()\n                if label == \"PLAY\":\n                    self._start_game()\n                elif label == \"SETTINGS\":\n                    self.state = GameState.SETTINGS\n                elif label == \"LEADERBOARD\":\n                    self.state = GameState.LEADERBOARD\n\n    # ------------------------------------------------------------------\n    # Game over buttons\n    # ------------------------------------------------------------------\n    def _gameover_buttons(self):\n        btn_w, btn_h = 200, 44\n        cx = SCREEN_W // 2\n        buttons = {}\n        for i, label in enumerate([\"RETRY\", \"BACK\"]):\n            y = 460 + i * (btn_h + 12)\n            rect = pygame.Rect(cx - btn_w // 2, y, btn_w, btn_h)\n            buttons[label] = rect\n        return buttons\n\n    def _handle_gameover_click(self, mx, my):\n        if self.game_over_timer < 30:\n            return\n        buttons = self._gameover_buttons()\n        for label, rect in buttons.items():\n            if rect.collidepoint(mx, my):\n                self.sound.swoosh()\n                if label == \"RETRY\":\n                    self._start_game()\n                elif label == \"BACK\":\n                    self.state = GameState.MENU\n\n    # ------------------------------------------------------------------\n    # Settings buttons\n    # ------------------------------------------------------------------\n    def _handle_settings_click(self, mx, my):\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n\n        # Back button\n        back_rect = pygame.Rect(cx - btn_w // 2, SCREEN_H - 100, btn_w, btn_h)\n        if back_rect.collidepoint(mx, my):\n            self.settings.save()\n            self.state = GameState.MENU\n            self.sound.swoosh()\n            return\n\n        # Sound toggle\n        sy = 200\n        sound_rect = pygame.Rect(cx - btn_w // 2, sy, btn_w, btn_h)\n        if sound_rect.collidepoint(mx, my):\n            self.settings.data[\"sound\"] = not self.settings.data[\"sound\"]\n            self.sound.enabled = self.settings.data[\"sound\"]\n            self.sound.swoosh()\n\n        # Shake toggle\n        shake_rect = pygame.Rect(cx - btn_w // 2, sy + 60, btn_w, btn_h)\n        if shake_rect.collidepoint(mx, my):\n            self.settings.data[\"shake\"] = not self.settings.data[\"shake\"]\n            self.sound.swoosh()\n\n        # Difficulty buttons\n        diff_y = sy + 140\n        for i, key in enumerate(self.difficulty_keys):\n            label = self.difficulty_labels[i]\n            dx = cx - 2 * btn_w // 2 - 6 + i * (btn_w + 6)\n            if i >= 2:\n                dx = cx - 2 * btn_w // 2 - 6 + (i - 2) * (btn_w + 6)\n                dy = diff_y + 52\n            else:\n                dy = diff_y\n            drect = pygame.Rect(dx, dy, btn_w, btn_h)\n            if drect.collidepoint(mx, my):\n                self.settings.data[\"difficulty\"] = key\n                self.diff = self.settings.get_difficulty()\n                self.sound.swoosh()\n\n    # ------------------------------------------------------------------\n    # Leaderboard buttons\n    # ------------------------------------------------------------------\n    def _handle_leaderboard_click(self, mx, my):\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n        back_rect = pygame.Rect(cx - btn_w // 2, SCREEN_H - 100, btn_w, btn_h)\n        if back_rect.collidepoint(mx, my):\n            self.state = GameState.MENU\n            self.sound.swoosh()\n\n    # ------------------------------------------------------------------\n    # Game logic\n    # ------------------------------------------------------------------\n    def _start_game(self):\n        self.state = GameState.GET_READY\n        self.bird = Bird(BIRD_X, SCREEN_H // 2 - 40)\n        self.pipes = []\n        self.particles = []\n        self.popups = []\n        self.score = 0\n        self.frame_count = 0\n        self.pipe_timer = 0\n        self.get_ready_timer = 0\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n        self.diff = self.settings.get_difficulty()\n        self.sound.swoosh()\n\n    def _update(self):\n        self.frame_count += 1\n\n        # Screen shake\n        if self.shake_timer > 0:\n            self.shake_timer -= 1\n            if self.settings.data[\"shake\"]:\n                self.shake_x = random.randint(-4, 4)\n                self.shake_y = random.randint(-4, 4)\n            else:\n                self.shake_x = 0\n                self.shake_y = 0\n        else:\n            self.shake_x = 0\n            self.shake_y = 0\n\n        # Flash fade\n        if self.flash_alpha > 0:\n            self.flash_alpha -= 4\n\n        # Clouds always move\n        for i, c in enumerate(self.assets.clouds):\n            self.cloud_positions[i][0] -= self.cloud_positions[i][2]\n            if self.cloud_positions[i][0] < -c[0].get_width():\n                self.cloud_positions[i][0] = self.screen_w + random.randint(0, 100)\n                self.cloud_positions[i][1] = random.randint(30, 200)\n\n        # Menu bird bob\n        if self.state == GameState.MENU:\n            self.menu_bird_vel += 0.3\n            self.menu_bird_vel *= 0.9\n            self.menu_bird_y += self.menu_bird_vel\n            if self.menu_bird_y > SCREEN_H // 2:\n                self.menu_bird_y = SCREEN_H // 2\n                self.menu_bird_vel = -4\n            elif self.menu_bird_y < SCREEN_H // 2 - 80:\n                self.menu_bird_y = SCREEN_H // 2 - 80\n                self.menu_bird_vel = 1\n\n        if self.state == GameState.GET_READY:\n            self.get_ready_timer += 1\n            self.bird.y = SCREEN_H // 2 - 40 + math.sin(self.get_ready_timer * 0.08) * 10\n            self.ground_offset = (self.ground_offset + self.diff[\"speed\"]) % self.screen_w\n\n        elif self.state == GameState.PLAYING:\n            self._update_playing()\n\n        elif self.state == GameState.GAME_OVER:\n            self.game_over_timer += 1\n            if self.bird:\n                self.bird.update(self.diff[\"gravity\"])\n                if self.bird.y >= SCREEN_H - GROUND_H - self.bird.height // 2:\n                    self.bird.y = SCREEN_H - GROUND_H - self.bird.height // 2\n                    self.bird.vel = 0\n            # Update particles\n            self.particles = [p for p in self.particles if p.life > 0]\n            for p in self.particles:\n                p.update()\n\n        # Always update particles\n        self.particles = [p for p in self.particles if p.life > 0]\n        for p in self.particles:\n            p.update()\n\n        self.popups = [p for p in self.popups if not p.is_dead()]\n        for p in self.popups:\n            p.update()\n\n    def _update_playing(self):\n        self.bird.update(self.diff[\"gravity\"])\n        self.ground_offset = (self.ground_offset + self.diff[\"speed\"]) % self.screen_w\n\n        # Pipe spawning\n        self.pipe_timer += 1\n        if self.pipe_timer >= PIPE_INTERVAL:\n            self.pipe_timer = 0\n            min_y = GROUND_H + self.diff[\"gap_size\"] // 2 + 40\n            max_y = SCREEN_H - GROUND_H - self.diff[\"gap_size\"] // 2 - 40\n            gap_y = random.randint(min_y, max_y)\n            # Speed up slightly over time\n            speed = self.diff[\"speed\"] + self.score * 0.02\n            self.pipes.append(Pipe(SCREEN_W + 10, gap_y, self.diff[\"gap_size\"], speed))\n\n        # Update pipes\n        for pipe in self.pipes:\n            pipe.speed = self.diff[\"speed\"] + self.score * 0.02\n            pipe.update()\n\n        # Remove offscreen pipes\n        self.pipes = [p for p in self.pipes if not p.is_offscreen()]\n\n        # Collision detection\n        bird_rect = self.bird.get_rect()\n        for pipe in self.pipes:\n            top_rect, bot_rect = pipe.get_rects(SCREEN_H, GROUND_H)\n            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):\n                self._die()\n                return\n\n        # Ground/ceiling collision\n        if (self.bird.y + self.bird.height // 2 >= SCREEN_H - GROUND_H or\n                self.bird.y - self.bird.height // 2 <= 0):\n            self._die()\n            return\n\n        # Scoring\n        for pipe in self.pipes:\n            if not pipe.scored and pipe.x + pipe.width < self.bird.x:\n                pipe.scored = True\n                self.score += 1\n                self.sound.score()\n                self.popups.append(ScorePopup(self.bird.x, self.bird.y - 30))\n                self._spawn_particles(self.bird.x, self.bird.y, 5, (255, 215, 0))\n\n    def _die(self):\n        self.bird.alive = False\n        self.sound.hit()\n        self.shake_timer = 15\n        self.flash_alpha = 180\n        self._spawn_particles(self.bird.x, self.bird.y, 15)\n        self.scores.add(self.score)\n        # Delayed state change\n        self._die_timer = 40\n\n    def _spawn_particles(self, x, y, count, color=None):\n        for _ in range(count):\n            self.particles.append(Particle(x, y, color))\n\n    # ------------------------------------------------------------------\n    # Drawing\n    # ------------------------------------------------------------------\n    def _draw(self):\n        self.screen.blit(self.assets.background, (0, 0))\n\n        # Clouds\n        for i, c in enumerate(self.assets.clouds):\n            cx, cy = self.cloud_positions[i][0], self.cloud_positions[i][1]\n            self.screen.blit(c[0], (int(cx), int(cy)))\n\n        if self.state == GameState.MENU:\n            self._draw_menu()\n        elif self.state == GameState.GET_READY:\n            self._draw_game()\n            self._draw_get_ready()\n        elif self.state == GameState.PLAYING:\n            self._draw_game()\n            self._draw_hud()\n        elif self.state == GameState.GAME_OVER:\n            self._draw_game()\n            self._draw_game_over()\n        elif self.state == GameState.SETTINGS:\n            self._draw_settings()\n        elif self.state == GameState.LEADERBOARD:\n            self._draw_leaderboard()\n\n        # Flash overlay\n        if self.flash_alpha > 0:\n            flash = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n            flash.fill((255, 255, 255, min(self.flash_alpha, 255)))\n            self.screen.blit(flash, (0, 0))\n\n        # FPS\n        if self.settings.data.get(\"show_fps\", False):\n            fps_text = self.font_small.render(f\"{self.clock.get_fps():.1f} FPS\", True, C_WHITE)\n            self.screen.blit(fps_text, (5, 5))\n\n    def _draw_game(self):\n        # Pipes\n        for pipe in self.pipes:\n            top_rect, bot_rect = pipe.get_rects(SCREEN_H, GROUND_H)\n            top_h = pipe.gap_y - pipe.gap_size // 2\n            bot_y = pipe.gap_y + pipe.gap_size // 2\n\n            # Top pipe\n            if top_h > 0:\n                self.screen.blit(self.assets.pipe_top, (pipe.x, top_h - 400))\n            else:\n                # Pipe gap is near top, draw partial\n                pass\n\n            # Bottom pipe\n            bot_h = SCREEN_H - GROUND_H - bot_y\n            if bot_h > 0:\n                self.screen.blit(self.assets.pipe_bottom, (pipe.x, bot_y))\n\n        # Ground\n        for x in range(-GROUND_H + (self.ground_offset % (GROUND_H * 2)),\n                       SCREEN_W + GROUND_H, GROUND_H * 2):\n            self.screen.blit(self.assets.ground, (x, SCREEN_H - GROUND_H))\n\n        # Particles\n        for p in self.particles:\n            p.draw(self.screen, self.assets.particle_surf)\n\n        # Popups\n        for p in self.popups:\n            p.draw(self.screen)\n\n        # Bird\n        if self.bird:\n            frame = self.assets.bird_frames[self.bird.frame]\n            rotated = pygame.transform.rotate(frame, -self.bird.rotation)\n            r = rotated.get_rect(center=(self.bird.x, self.bird.y))\n            self.screen.blit(rotated, r.topleft)\n\n    def _draw_hud(self):\n        # Score with outline\n        score_str = str(self.score)\n        ts = self.font_huge.render(score_str, True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, 62))\n        ts = self.font_huge.render(score_str, True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n        # Pause indicator\n        if self.state == GameState.PLAYING:\n            pass\n\n    def _draw_get_ready(self):\n        # Semi-transparent overlay\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 40))\n        self.screen.blit(overlay, (0, 0))\n\n        # \"Get Ready\" text\n        font = pygame.font.Font(None, 60)\n        ts = font.render(\"GET READY\", True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, 182))\n        ts = font.render(\"GET READY\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 180))\n\n        # Tap instruction\n        instr = self.font.render(\"Tap or press SPACE to fly\", True, C_WHITE)\n        self.screen.blit(instr, (SCREEN_W // 2 - instr.get_width() // 2, 260))\n\n        # Tap icon\n        icon_y = 320 + math.sin(self.frame_count * 0.1) * 8\n        self.screen.blit(self.assets.get_ready,\n                         (SCREEN_W // 2 - 140, icon_y))\n\n    def _draw_menu(self):\n        # Background\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n\n        # Animated city silhouette at bottom\n        self._draw_city_silhouette()\n\n        # Title\n        title = self.assets.title_text\n        title_x = SCREEN_W // 2 - title.get_width() // 2\n        title_y = 80 + math.sin(self.frame_count * 0.03) * 5\n        self.screen.blit(title, (title_x, title_y))\n\n        # Animated bird\n        bird_frame = self.frame_count // 8 % 3\n        bird = self.assets.bird_frames[bird_frame]\n        self.screen.blit(bird, (SCREEN_W // 2 - 17, self.menu_bird_y))\n\n        # Buttons\n        buttons = self._menu_buttons()\n        for label, rect in buttons.items():\n            hover = rect.collidepoint(pygame.mouse.get_pos())\n            if hover:\n                btn_surf = self.assets.buttons[label].copy()\n                # Brighten on hover\n                for pixel_x in range(btn_surf.get_width()):\n                    for pixel_y in range(btn_surf.get_height()):\n                        p = btn_surf.get_at((pixel_x, pixel_y))\n                        if p[3] > 0:\n                            r = min(int(p[0] * 1.3), 255)\n                            g = min(int(p[1] * 1.3), 255)\n                            b = min(int(p[2] * 1.3), 255)\n                            btn_surf.set_at((pixel_x, pixel_y), (r, g, b, p[3]))\n                self.screen.blit(btn_surf, rect.topleft)\n            else:\n                self.screen.blit(self.assets.buttons[label], rect.topleft)\n\n        # Best score\n        best = self.scores.best()\n        if best > 0:\n            best_text = self.font.render(f\"Best: {best}\", True, (255, 215, 0))\n            self.screen.blit(best_text, (SCREEN_W // 2 - best_text.get_width() // 2, 540))\n\n        # Version\n        ver = self.font_small.render(\"v1.0\", True, (150, 150, 180))\n        self.screen.blit(ver, (SCREEN_W - ver.get_width() - 10, SCREEN_H - 30))\n\n    def _draw_city_silhouette(self):\n        \"\"\"Draw a simple city skyline silhouette.\"\"\"\n        silhouette = pygame.Surface((SCREEN_W, 120), pygame.SRCALPHA)\n        silhouette.fill((20, 25, 40, 120))\n        # Buildings\n        buildings = [\n            (0, 30, 40, 90), (35, 20, 30, 100), (60, 40, 50, 80),\n            (105, 15, 35, 105), (135, 35, 45, 85), (175, 25, 40, 95),\n            (210, 45, 55, 75), (260, 10, 30, 110), (285, 30, 50, 90),\n            (330, 20, 40, 100), (365, 40, 45, 80), (405, 15, 35, 105),\n            (435, 35, 45, 85),\n        ]\n        for bx, by, bw, bh in buildings:\n            pygame.draw.rect(silhouette, (20, 25, 40, 120), (bx, by, bw, bh))\n            # Windows\n            wy = by + 8\n            while wy < by + bh - 8:\n                wx = bx + 6\n                while wx < bx + bw - 6:\n                    if random.random() > 0.3:\n                        pygame.draw.rect(silhouette, (255, 220, 100, 60), (wx, wy, 4, 5))\n                    wx += 10\n                wy += 12\n        self.screen.blit(silhouette, (0, SCREEN_H - GROUND_H - 120))\n\n    def _draw_game_over(self):\n        if self.game_over_timer < 10:\n            return\n\n        # Dim overlay\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 100))\n        self.screen.blit(overlay, (0, 0))\n\n        # Panel\n        panel = self.assets.game_over_panel\n        px = SCREEN_W // 2 - panel.get_width() // 2\n        py = 200\n        self.screen.blit(panel, (px, py))\n\n        # \"Game Over\" text\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"GAME OVER\", True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, py - 58))\n        ts = font.render(\"GAME OVER\", True, C_ACCENT)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, py - 60))\n\n        # Score\n        score_text = self.font_big.render(str(self.score), True, C_WHITE)\n        self.screen.blit(score_text, (SCREEN_W // 2 - score_text.get_width() // 2, py + 20))\n\n        # Best\n        best = self.scores.best()\n        best_text = self.font.render(f\"Best: {best}\", True, (255, 215, 0))\n        self.screen.blit(best_text, (SCREEN_W // 2 - best_text.get_width() // 2, py + 80))\n\n        # New best indicator\n        if self.score == best and self.score > 0:\n            new_text = self.font.render(\"NEW!\", True, (255, 100, 100))\n            # Blink\n            if self.frame_count % 20 < 10:\n                self.screen.blit(new_text, (px + panel.get_width() - new_text.get_width() - 15, py + 25))\n\n        # Medal\n        medal = self.scores.get_medal(self.score)\n        if medal and medal in self.assets.medal_icons:\n            self.screen.blit(self.assets.medal_icons[medal], (px + 20, py + 50))\n\n        # Buttons (fade in)\n        if self.game_over_timer > 30:\n            buttons = self._gameover_buttons()\n            for label, rect in buttons.items():\n                self.screen.blit(self.assets.buttons[label], rect.topleft)\n\n        # Tap to continue\n        if self.game_over_timer > 60:\n            if self.frame_count % 40 < 25:\n                tap = self.font.render(\"Tap to continue\", True, (200, 200, 220))\n                self.screen.blit(tap, (SCREEN_W // 2 - tap.get_width() // 2, SCREEN_H - 60))\n\n    def _draw_settings(self):\n        # Background\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n\n        # Title\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"SETTINGS\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n        # Sound toggle\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n        sy = 170\n\n        # Sound\n        sound_on = self.settings.data[\"sound\"]\n        sound_label = f\"SOUND: {'ON' if sound_on else 'OFF'}\"\n        sound_btn = self._make_toggle_btn(sound_label, sound_on)\n        self.screen.blit(sound_btn, (cx - btn_w // 2, sy))\n\n        # Shake\n        shake_on = self.settings.data[\"shake\"]\n        shake_label = f\"SHAKE: {'ON' if shake_on else 'OFF'}\"\n        shake_btn = self._make_toggle_btn(shake_label, shake_on)\n        self.screen.blit(shake_btn, (cx - btn_w // 2, sy + 60))\n\n        # Difficulty\n        diff_title = self.font.render(\"DIFFICULTY\", True, C_WHITE)\n        self.screen.blit(diff_title, (cx - diff_title.get_width() // 2, sy + 130))\n\n        diff_y = sy + 160\n        for i, key in enumerate(self.difficulty_keys):\n            label = self.difficulty_labels[i]\n            is_active = self.settings.data[\"difficulty\"] == key\n            if i < 2:\n                dx = cx - 2 * btn_w // 2 - 6 + i * (btn_w + 12)\n                dy = diff_y\n            else:\n                dx = cx - 2 * btn_w // 2 - 6 + (i - 2) * (btn_w + 12)\n                dy = diff_y + 52\n            dbtn = self._make_diff_btn(label, is_active)\n            self.screen.blit(dbtn, (dx, dy))\n\n        # Back button\n        back_btn = self.assets.buttons[\"BACK\"]\n        self.screen.blit(back_btn, (cx - back_btn.get_width() // 2, SCREEN_H - 100))\n\n    def _make_toggle_btn(self, text, is_on):\n        w, h = 180, 40\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 8\n        rect = pygame.Rect(0, 0, w, h)\n        color = (60, 180, 60) if is_on else (180, 60, 60)\n        _draw_rounded_rect(s, color, rect, r)\n        pygame.draw.rect(s, C_WHITE, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 28)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n    def _make_diff_btn(self, text, is_active):\n        w, h = 80, 40\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 8\n        rect = pygame.Rect(0, 0, w, h)\n        color = (80, 200, 80) if is_active else C_UI_BG\n        _draw_rounded_rect(s, color, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 24)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n    def _draw_leaderboard(self):\n        # Background\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n\n        # Title\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"LEADERBOARD\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n        # Scores\n        scores = sorted(self.scores.history, reverse=True)[:15]\n        if not scores:\n            no_text = self.font.render(\"No scores yet!\", True, (180, 180, 200))\n            self.screen.blit(no_text, (SCREEN_W // 2 - no_text.get_width() // 2, 200))\n        else:\n            for i, sc in enumerate(scores):\n                medal = self.scores.get_medal(sc)\n                y = 130 + i * 32\n                if y > SCREEN_H - 120:\n                    break\n\n                # Rank\n                rank_colors = [(255, 215, 0), (192, 192, 192), (205, 127, 50)]\n                rank_color = rank_colors[i] if i < 3 else (180, 180, 200)\n                rank_text = self.font.render(f\"#{i + 1}\", True, rank_color)\n                self.screen.blit(rank_text, (40, y))\n\n                # Score\n                score_text = self.font.render(str(sc), True, C_WHITE)\n                self.screen.blit(score_text, (120, y))\n\n                # Medal icon\n                if medal and medal in self.assets.medal_icons:\n                    mini = pygame.transform.scale(self.assets.medal_icons[medal], (20, 20))\n                    self.screen.blit(mini, (180, y + 6))\n\n                # Bar\n                bar_w = min(sc * 4, 200)\n                pygame.draw.rect(self.screen, (60, 80, 120), (220, y + 8, bar_w, 16))\n                if i == 0:\n                    pygame.draw.rect(self.screen, (80, 120, 180), (220, y + 8, bar_w, 16))\n\n        # Stats\n        if scores:\n            avg = sum(scores) // len(scores)\n            stats = self.font_small.render(\n                f\"Games: {len(self.scores.history)}  |  Avg: {avg}\",\n                True, (150, 150, 180)\n            )\n            self.screen.blit(stats, (SCREEN_W // 2 - stats.get_width() // 2, SCREEN_H - 130))\n\n        # Back button\n        back_btn = self.assets.buttons[\"BACK\"]\n        self.screen.blit(back_btn, (SCREEN_W // 2 - back_btn.get_width() // 2, SCREEN_H - 90))\n\n\n# ---------------------------------------------------------------------------\n# Entry point\n# ---------------------------------------------------------------------------\ndef main():\n    game = FlippyBlockExtreme()\n    game.run()\n\n\nif __name__ == \"__main__\":\n    main()\n",
  "filePath": "/home/patof/stress_bench/Flip_None/flippyblock_extreme.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 30.3s)

_Thinking:_

'write' response.

Now let me review the code and fix issues:

1. The event handling has a bug - I'm calling `pygame.event.get()` twice (once in `_handle_events` and once in `run()`). Need to fix this.
2. The `sndarray` usage may fail on some systems. Let me make the sound more robust.
3. The `_draw_game` method for pipes needs fixing - the top pipe drawing is wrong.
4. The die timer logic isn't wired up properly.
5. The `_on_escape` handler doesn't properly handle all states.

Let me fix these issues.


Now let me review and fix the code. I see several issues:



**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the FlippyBlock Extreme game with all core mechanics",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add UI features: menu, HUD, settings, pause, game over screen",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Review and fix all bugs",
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
    "content": "Create the FlippyBlock Extreme game with all core mechanics",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add UI features: menu, HUD, settings, pause, game over screen",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Review and fix all bugs",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 542.6s)

_Thinking:_

+


**Tool: task**

**Input:**
```json
{
  "description": "Review game code for bugs",
  "prompt": "Read the file /home/patof/stress_bench/Flip_None/flippyblock_extreme.py thoroughly and identify ALL bugs, issues, and problems. Look for:\n\n1. Event handling bugs (double event consumption)\n2. Missing die_timer logic in _update\n3. Pipe drawing issues (top pipe y offset wrong)\n4. Sound system that may crash (sndarray dependency)\n5. Any logic errors, missing features, or crashes\n6. The _on_action handler for GAME_OVER state\n\nReturn a detailed list of every issue found with line numbers and the fix needed.",
  "subagent_type": "explore"
}
```

**Output:**
```
task_id: ses_1c749d4e8ffeHAJiQuDoqBfhdK (for resuming to continue this task if needed)

<task_result>
I have now read and analyzed the entire file (1575 lines). Here is a comprehensive, detailed report of every bug, issue, and problem found.

---

## BUG 1: Missing `die_timer` Logic / State Never Transitions to `GAME_OVER`

**Lines affected:** 1185-1193 (`_die`), 1071-1137 (`_update`)

**Problem:** In `_die()` (line 1193), the code sets `self._die_timer = 40` with the comment `"# Delayed state change"`. However:
- `self._die_timer` is **never decremented** anywhere in `_update()` or `_update_playing()`.
- `self.state` is **never assigned** to `GameState.GAME_OVER` anywhere in the entire file.
- As a result, after the bird dies, the game remains stuck in `GameState.PLAYING` forever. `_update_playing()` continues to run each frame, spawning new pipes, checking collisions, and scoring, even though the bird is dead. The game-over screen never appears, and the player can never restart.

**Evidence:** A grep for `self.state = GameState.GAME_OVER` returns zero results across the entire file.

**Fix:** Add die timer logic to `_update()` (or `_update_playing()`) to decrement the timer and transition the state:

```python
# In _update(), after the PLAYING block or inside it:
if hasattr(self, '_die_timer') and self._die_timer is not None:
    self._die_timer -= 1
    if self._die_timer <= 0:
        self.state = GameState.GAME_OVER
        self.game_over_timer = 0
        self.sound.die()
```

---

## BUG 2: Redundant / Broken Dual Event Loop (Double Event Queue Draining)

**Lines affected:** 854-867 (`run`), 872-888 (`_handle_events`)

**Problem:** The `run()` method has two separate `pygame.event.get()` calls:

1. **Line 858:** `self._handle_events()` internally calls `pygame.event.get()` on line 873, which **drains the entire event queue**.
2. **Lines 862-864:** After `_update()` and `_draw()`, a second `pygame.event.get()` loop attempts to catch `QUIT` events.

This means:
- The second event loop on lines 862-864 only sees events that arrived during the narrow `_update()`/`_draw()` window, making it effectively dead code.
- `_handle_events()` already handles `QUIT` on lines 874-876 by calling `pygame.quit()` and `sys.exit()`, so the second QUIT handler is redundant.
- If `_handle_events()` encounters `QUIT`, it calls `sys.exit()` and the second loop is never reached.

**Fix:** Remove the second event loop from `run()` entirely. Restructure `_handle_events()` to set a `running = False` flag instead of calling `sys.exit()` directly, or simply use a single event loop:

```python
def run(self):
    running = True
    while running:
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                ...
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ...
        self._update()
        self._draw()
        pygame.display.flip()
    pygame.quit()
    sys.exit()
```

---

## BUG 3: Top Pipe Y Offset Causes Visual Gap

**Lines affected:** 1246 (`_draw_game`), 457 (`_make_pipe_top`)

**Problem:** The `pipe_top` surface is only **400 pixels tall** (line 457: `w, h = 62, 400`). The drawing code on line 1246 places it at:

```python
self.screen.blit(self.assets.pipe_top, (pipe.x, top_h - 400))
```

This positions the bottom of the surface (the cap) at `top_h`. When `top_h > 400`, the top of the surface starts at `top_h - 400 > 0`, leaving an **undrawn gap** between `y=0` and `y=top_h - 400` where the pipe body should extend.

**Concrete example:** On normal difficulty, `max_y = 720 - 80 - 80 - 40 = 520`, so `top_h = 520 - 80 = 440`. The surface is drawn at `y = 440 - 400 = 40`, leaving a **40-pixel gap** at the top of the screen where the pipe should be visible but is not.

The bottom pipe is not affected because `bot_h` maxes out at 360, which is less than 400.

**Fix:** Make the pipe surfaces tall enough to cover the maximum possible pipe height. Change line 457 from `h = 400` to `h = SCREEN_H` (720), or alternatively adjust the drawing logic to tile/clip the surface properly:

```python
# In _make_pipe_top, change:
w, h = 62, 400
# to:
w, h = 62, SCREEN_H
```

---

## BUG 4: Sound System Crashes When NumPy Is Not Installed

**Lines affected:** 233-309 (`SimpleSound` and `int16_dtype`)

**Problem:** The `SimpleSound` class is the **only** sound class actually instantiated (line 820: `self.sound = SimpleSound()`). Despite the comment on line 231 claiming `"Simple procedural sound fallback (no sndarray needed)"`, the code **heavily depends** on `pygame.sndarray`:

- Line 257: `pygame.sndarray.zeros((n,), int16_dtype())`
- Line 262: `pygame.sndarray.make_sound(frames)`
- Lines 267, 272, 277, 281, 286, 291, 296, 300: Same pattern repeated for every sound.
- Line 309: `return pygame.sndarray.Int16Array`

`pygame.sndarray` **requires NumPy**. If NumPy is not installed, `pygame.sndarray` raises an `ImportError` or `AttributeError`. The `try/except` on lines 241-245 only catches `pygame.error`, so an `ImportError` from sndarray will propagate and **crash the game at startup**.

The older `SoundFX` class (lines 84-214) has the same sndarray dependency and is also dead code (never instantiated).

**Fix:** Either:
1. Add a try/except that catches `ImportError` and `AttributeError` around the sndarray calls:
```python
def init(self):
    try:
        pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)
        self._build()
    except (pygame.error, ImportError, AttributeError):
        self.enabled = False
```
2. Or implement a true fallback using raw `array.array` and `pygame.mixer.Sound(buffer=...)` without any sndarray dependency.

---

## BUG 5: Particles Updated Twice Per Frame in `GAME_OVER` State

**Lines affected:** 1126-1128 and 1131-1133 (`_update`)

**Problem:** In the `_update()` method, when `self.state == GameState.GAME_OVER`, particles are updated twice:

```python
# First update (inside GAME_OVER block):
self.particles = [p for p in self.particles if p.life > 0]
for p in self.particles:
    p.update()

# Second update (outside all state blocks):
self.particles = [p for p in self.particles if p.life > 0]
for p in self.particles:
    p.update()
```

This causes particles in the GAME_OVER state to move **twice as fast** and expire **twice as quickly** as in other states. In MENU, GET_READY, and PLAYING states, particles are only updated once (by the "Always update particles" block).

**Fix:** Remove the duplicate particle update from the GAME_OVER block (lines 1126-1128), since the "Always update particles" block at lines 1131-1133 already handles it:

```python
elif self.state == GameState.GAME_OVER:
    self.game_over_timer += 1
    if self.bird:
        self.bird.update(self.diff["gravity"])
        if self.bird.y >= SCREEN_H - GROUND_H - self.bird.height // 2:
            self.bird.y = SCREEN_H - GROUND_H - self.bird.height // 2
            self.bird.vel = 0
    # Remove the duplicate particle update here
```

---

## BUG 6: `_on_action` for `GAME_OVER` State Lacks Retry Option

**Lines affected:** 915-918 (`_on_action`)

**Problem:** When the game is in `GAME_OVER` state and the player presses SPACE or UP, `_on_action` only navigates back to the MENU:

```python
elif self.state == GameState.GAME_OVER:
    if self.game_over_timer > 60:
        self.state = GameState.MENU
        self.sound.swoosh()
```

There is no keyboard option to retry/restart directly from GAME_OVER via SPACE. The `R` key does restart (via `_on_restart` on line 921), but this is inconsistent with:
- The mouse click handler (`_handle_gameover_click`) which offers both RETRY and BACK buttons.
- Standard Flappy Bird conventions where pressing SPACE on the game-over screen restarts the game.

**Fix:** Change the keyboard handler to retry instead of going to menu, matching the most common button (RETRY):

```python
elif self.state == GameState.GAME_OVER:
    if self.game_over_timer > 60:
        self._start_game()
        self.sound.swoosh()
```

Or add ESC to go to menu and SPACE to retry.

---

## BUG 7: Dead Code -- `SoundFX` Class and `numpy_like_*` Helpers

**Lines affected:** 84-228

**Problem:** The `SoundFX` class (lines 84-214) and the three `numpy_like_*` helper functions (lines 218-228) are **never used**. The only sound class instantiated is `SimpleSound` (line 820). The `SoundFX` class, its `_factories` dict, its `_play`/`_make` methods, and all five `_flap`/`_score`/`_hit`/`_die`/`_swoosh` static methods are dead code. Similarly, `numpy_like_range`, `numpy_like_exp`, and `numpy_like_sin` are only referenced inside `SoundFX`, so they are also dead code.

**Fix:** Remove the entire `SoundFX` class (lines 84-214) and the `numpy_like_*` functions (lines 218-228) to reduce code size and confusion.

---

## BUG 8: `dt` Variable Assigned But Never Used

**Line affected:** 857 (`run`)

**Problem:** The variable `dt` is assigned the delta-time from `self.clock.tick(FPS)` but is never used anywhere in the game loop. All physics and timing in the game uses frame-count-based logic (e.g., `self.frame_count`, `self.pipe_timer`, fixed-frame timers).

**Fix:** Either remove the unused assignment or implement frame-rate-independent physics using `dt`.

---

## BUG 9: `SimpleSound.init()` Does Not Catch `ImportError` from `sndarray`

**Lines affected:** 240-245

**Problem:** The `try/except` block only catches `pygame.error`:

```python
def init(self):
    try:
        pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)
        self._build()
    except pygame.error:
        self.enabled = False
```

If `pygame.mixer.init()` succeeds but `self._build()` fails because `pygame.sndarray` is unavailable (raising `ImportError` or `AttributeError`), the exception is **not caught** and the game crashes at startup.

**Fix:** Broaden the exception handling:

```python
def init(self):
    try:
        pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)
        self._build()
    except (pygame.error, ImportError, AttributeError):
        self.enabled = False
```

---

## BUG 10: `_handle_menu_click` Ignores Clicks Outside Buttons (No "Tap to Start" Fallback)

**Lines affected:** 960-970

**Problem:** In the MENU state, `_handle_menu_click` only responds if the click lands on one of the three buttons (PLAY, SETTINGS, LEADERBOARD). Clicking anywhere else on the menu screen does nothing. Many Flappy Bird clones allow tapping anywhere on the menu to start the game.

This is a minor UX issue, not a crash, but worth noting since `_on_action` (keyboard) starts the game from MENU without requiring a specific button press.

**Fix:** Add a fallback in `_handle_menu_click`:

```python
def _handle_menu_click(self, mx, my):
    buttons = self._menu_buttons()
    clicked = False
    for label, rect in buttons.items():
        if rect.collidepoint(mx, my):
            self.sound.swoosh()
            if label == "PLAY":
                self._start_game()
            elif label == "SETTINGS":
                self.state = GameState.SETTINGS
            elif label == "LEADERBOARD":
                self.state = GameState.LEADERBOARD
            clicked = True
            break
    if not clicked:
        self._start_game()  # Tap anywhere to play
```

---

## Summary Table

| # | Bug | Lines | Severity | Category |
|---|-----|-------|----------|----------|
| 1 | `_die_timer` never decremented; state never transitions to `GAME_OVER` | 1193, 1071-1137 | **Critical** -- game is unplayable after first death | Logic |
| 2 | Dual event loops; second QUIT handler is dead code | 858, 862-864, 873 | Moderate | Event handling |
| 3 | Top pipe surface too short (400px), visual gap when `top_h > 400` | 1246, 457 | Moderate | Rendering |
| 4 | `SimpleSound` crashes without NumPy despite claiming no sndarray dependency | 233-309 | **Critical** -- startup crash on many systems | Sound |
| 5 | Particles updated twice per frame in GAME_OVER state | 1126-1128, 1131-1133 | Minor | Logic |
| 6 | `_on_action` in GAME_OVER only goes to MENU, no retry via SPACE | 915-918 | Minor | UX |
| 7 | `SoundFX` class and `numpy_like_*` helpers are dead code | 84-228 | N/A | Dead code |
| 8 | `dt` variable assigned but never used | 857 | N/A | Unused variable |
| 9 | `SimpleSound.init()` does not catch `ImportError`/`AttributeError` | 240-245 | **Critical** -- startup crash | Sound |
| 10 | Menu click outside buttons does nothing (no tap-to-start) | 960-970 | Minor | UX |
</task_result>
```

---

## Assistant (Build · Qwen3.6 27B · 538.9s)

_Thinking:_

00.


Good catch on all those issues. Let me fix them all now by rewriting the file with every bug resolved.



**Tool: write**

**Input:**
```json
{
  "content": "\"\"\"\nFlippyBlock Extreme\nA Flappy Bird clone built entirely with pygame — no external assets.\n\"\"\"\n\nimport math\nimport os\nimport random\nimport sys\nimport json\nfrom pathlib import Path\n\n# ---------------------------------------------------------------------------\n# Try to import pygame; exit gracefully if unavailable\n# ---------------------------------------------------------------------------\ntry:\n    import pygame\nexcept ImportError:\n    print(\"pygame is required. Install it with: pip install pygame\")\n    sys.exit(1)\n\n# ---------------------------------------------------------------------------\n# Constants\n# ---------------------------------------------------------------------------\nSCREEN_W = 480\nSCREEN_H = 720\nFPS = 60\n\n# Colors\nC_SKY_TOP = (100, 180, 255)\nC_SKY_BOT = (180, 225, 255)\nC_PIPE = (42, 150, 42)\nC_PIPE_HIGHLIGHT = (62, 200, 62)\nC_PIPE_SHADOW = (22, 110, 22)\nC_PIPE_CAP = (34, 130, 34)\nC_GROUND = (218, 165, 32)\nC_GROUND_DARK = (190, 140, 25)\nC_GROUND_GRASS = (90, 180, 50)\nC_WHITE = (255, 255, 255)\nC_BLACK = (0, 0, 0)\nC_BIRD_BODY = (255, 220, 40)\nC_BIRD_WING = (255, 180, 20)\nC_BIRD_BEAK = (255, 120, 30)\nC_BIRD_EYE = (255, 255, 255)\nC_BIRD_PUPIL = (20, 20, 20)\nC_TEXT = (255, 255, 255)\nC_TEXT_SHADOW = (0, 0, 0)\nC_MEDAL_GOLD = (255, 215, 0)\nC_MEDAL_SILVER = (192, 192, 192)\nC_MEDAL_BRONZE = (205, 127, 50)\nC_MEDAL_PLATINUM = (160, 190, 230)\nC_UI_BG = (40, 40, 60)\nC_UI_BORDER = (80, 80, 120)\nC_BUTTON_HOVER = (100, 100, 160)\nC_BUTTON_ACTIVE = (70, 70, 120)\nC_ACCENT = (255, 100, 100)\nC_CLOUD = (240, 245, 255)\nC_STARS = (255, 255, 220)\n\n# Physics\nGRAVITY = 0.55\nFLAP_POWER = -9.5\nMAX_FALL = 12\nPIPE_SPEED_BASE = 3.0\nPIPE_GAP_BASE = 160\nPIPE_GAP_MIN = 110\nPIPE_INTERVAL = 110\nGROUND_H = 80\nBIRD_X = 100\n\n# ---------------------------------------------------------------------------\n# Paths\n# ---------------------------------------------------------------------------\nSAVE_DIR = Path.home() / \".flippyblock\"\nSAVE_DIR.mkdir(exist_ok=True)\nSAVE_FILE = SAVE_DIR / \"scores.json\"\nSETTINGS_FILE = SAVE_DIR / \"settings.json\"\n\n# ---------------------------------------------------------------------------\n# Audio (generated at runtime, no sndarray dependency)\n# ---------------------------------------------------------------------------\nclass SimpleSound:\n    \"\"\"Procedural sound effects using raw wave synthesis — no numpy needed.\"\"\"\n\n    def __init__(self):\n        self.enabled = True\n        self._sounds = {}\n\n    def init(self):\n        try:\n            pygame.mixer.init(freq=22050, size=-16, channels=1, buffer=512)\n            self._build()\n        except (pygame.error, ImportError, AttributeError, Exception):\n            self.enabled = False\n\n    def _build(self):\n        self._sounds[\"flap\"] = self._gen_flap()\n        self._sounds[\"score\"] = self._gen_score()\n        self._sounds[\"hit\"] = self._gen_hit()\n        self._sounds[\"die\"] = self._gen_die()\n        self._sounds[\"swoosh\"] = self._gen_swoosh()\n\n    @staticmethod\n    def _gen_samples(freq_fn, duration, amplitude=15000, noise=False):\n        \"\"\"Generate PCM16 samples from a frequency function.\"\"\"\n        n = int(22050 * duration)\n        raw = bytearray(n * 2)\n        for i in range(n):\n            if noise:\n                val = int(amplitude * (random.random() * 2 - 1) * math.exp(-i / (n * 0.25)))\n            else:\n                f = freq_fn(i, n)\n                val = int(amplitude * math.sin(2 * 3.14159 * f * i / 22050)\n                          * math.exp(-i / (n * 0.4)))\n            val = max(-32768, min(32767, val))\n            raw[i * 2] = val & 0xFF\n            raw[i * 2 + 1] = (val >> 8) & 0xFF\n        return pygame.mixer.Sound(buffer=raw)\n\n    @staticmethod\n    def _gen_flap():\n        def freq(i, n):\n            return 600 + 400 * math.exp(-i / 80)\n        return SimpleSound._gen_samples(freq, 0.06, amplitude=15000)\n\n    @staticmethod\n    def _gen_score():\n        def freq(i, n):\n            return 880 + 440 * (i / max(n, 1))\n        return SimpleSound._gen_samples(freq, 0.15, amplitude=12000)\n\n    @staticmethod\n    def _gen_hit():\n        return SimpleSound._gen_samples(lambda i, n: 200, 0.2, amplitude=18000, noise=True)\n\n    @staticmethod\n    def _gen_die():\n        def freq(i, n):\n            return 500 - 300 * (i / max(n, 1))\n        return SimpleSound._gen_samples(freq, 0.4, amplitude=15000)\n\n    @staticmethod\n    def _gen_swoosh():\n        def freq(i, n):\n            return 300 * math.sin(3.14159 * i / max(n, 1))\n        return SimpleSound._gen_samples(freq, 0.1, amplitude=6000, noise=True)\n\n    def play(self, name):\n        if not self.enabled or name not in self._sounds:\n            return\n        try:\n            self._sounds[name].play()\n        except Exception:\n            pass\n\n    def flap(self):\n        self.play(\"flap\")\n\n    def score(self):\n        self.play(\"score\")\n\n    def hit(self):\n        self.play(\"hit\")\n\n    def die(self):\n        self.play(\"die\")\n\n    def swoosh(self):\n        self.play(\"swoosh\")\n\n\n# ---------------------------------------------------------------------------\n# Settings persistence\n# ---------------------------------------------------------------------------\nclass Settings:\n    DEFAULT = {\n        \"sound\": True,\n        \"music\": False,\n        \"difficulty\": \"normal\",\n        \"bird_skin\": 0,\n        \"shake\": True,\n        \"show_fps\": False,\n    }\n\n    DIFFICULTY = {\n        \"easy\":   {\"gravity\": 0.4, \"flap\": -8, \"gap\": 190, \"speed\": 2.2, \"label\": \"Easy\"},\n        \"normal\": {\"gravity\": 0.55, \"flap\": -9.5, \"gap\": 160, \"speed\": 3.0, \"label\": \"Normal\"},\n        \"hard\":   {\"gravity\": 0.65, \"flap\": -10.5, \"gap\": 140, \"speed\": 3.6, \"label\": \"Hard\"},\n        \"extreme\":{\"gravity\": 0.75, \"flap\": -11, \"gap\": 120, \"speed\": 4.2, \"label\": \"Extreme\"},\n    }\n\n    def __init__(self):\n        self.data = dict(self.DEFAULT)\n        self._load()\n\n    def _load(self):\n        try:\n            if SETTINGS_FILE.exists():\n                with open(SETTINGS_FILE) as f:\n                    saved = json.load(f)\n                self.data.update(saved)\n        except Exception:\n            pass\n\n    def save(self):\n        try:\n            with open(SETTINGS_FILE, \"w\") as f:\n                json.dump(self.data, f)\n        except Exception:\n            pass\n\n    def get_difficulty(self):\n        return self.DIFFICULTY.get(self.data[\"difficulty\"], self.DIFFICULTY[\"normal\"])\n\n\n# ---------------------------------------------------------------------------\n# Score persistence\n# ---------------------------------------------------------------------------\nclass Scores:\n    def __init__(self):\n        self.history = []\n        self.medals = {}\n        self._load()\n\n    def _load(self):\n        try:\n            if SAVE_FILE.exists():\n                with open(SAVE_FILE) as f:\n                    data = json.load(f)\n                self.history = data.get(\"history\", [])\n                self.medals = data.get(\"medals\", {})\n        except Exception:\n            pass\n\n    def save(self):\n        try:\n            with open(SAVE_FILE, \"w\") as f:\n                json.dump({\"history\": self.history[-50:], \"medals\": self.medals}, f)\n        except Exception:\n            pass\n\n    def add(self, score):\n        self.history.append(score)\n        self.save()\n\n    def best(self):\n        return max(self.history) if self.history else 0\n\n    def get_medal(self, score):\n        if score >= 40:\n            return \"platinum\"\n        if score >= 20:\n            return \"gold\"\n        if score >= 10:\n            return \"silver\"\n        if score >= 5:\n            return \"bronze\"\n        return None\n\n\n# ---------------------------------------------------------------------------\n# Asset generation (all procedural)\n# ---------------------------------------------------------------------------\nclass Assets:\n    \"\"\"Generates all visual assets at runtime.\"\"\"\n\n    def __init__(self, screen):\n        self.screen = screen\n        self.screen_w = screen.get_width()\n        self.screen_h = screen.get_height()\n        self._build()\n\n    def _build(self):\n        self.bird_frames = self._make_bird_frames()\n        self.pipe_top = self._make_pipe_top()\n        self.pipe_bottom = self._make_pipe_bottom()\n        self.ground = self._make_ground()\n        self.clouds = self._make_clouds()\n        self.background = self._make_background()\n        self.medal_icons = self._make_medals()\n        self.star_surf = self._make_star()\n        self.get_ready = self._make_get_ready()\n        self.game_over_panel = self._make_game_over_panel()\n        self.menu_bg = self._make_menu_bg()\n        self.title_text = self._make_title()\n        self.buttons = {}\n        self._make_buttons()\n\n    def _make_bird_frames(self):\n        frames = []\n        wing_offsets = [-3, 0, 3]\n        for wo in wing_offsets:\n            s = pygame.Surface((34, 26), pygame.SRCALPHA)\n            pygame.draw.ellipse(s, C_BIRD_BODY, (2, 4, 28, 18))\n            pygame.draw.ellipse(s, (255, 240, 100), (6, 6, 16, 8))\n            pygame.draw.ellipse(s, C_BIRD_WING, (8, 10 + wo, 14, 8))\n            pts = [(28, 10), (34, 12), (28, 15)]\n            pygame.draw.polygon(s, C_BIRD_BEAK, pts)\n            pygame.draw.circle(s, C_BIRD_EYE, (24, 9), 5)\n            pygame.draw.circle(s, C_BIRD_PUPIL, (26, 9), 2)\n            pygame.draw.circle(s, C_WHITE, (27, 7), 1)\n            frames.append(s)\n        return frames\n\n    def _make_pipe_top(self):\n        \"\"\"Top pipe — tall enough to fill entire screen.\"\"\"\n        w = 62\n        h = SCREEN_H\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        pygame.draw.rect(s, C_PIPE, (3, 0, w - 6, h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (6, 0, 8, h))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 14, 0, 8, h))\n        cap_h = 28\n        pygame.draw.rect(s, C_PIPE_CAP, (0, h - cap_h, w, cap_h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (3, h - cap_h + 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 12, h - cap_h + 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_WHITE, (1, h - cap_h + 1, w - 2, 2), 1)\n        return s\n\n    def _make_pipe_bottom(self):\n        \"\"\"Bottom pipe — tall enough to fill entire screen.\"\"\"\n        w = 62\n        h = SCREEN_H\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        pygame.draw.rect(s, C_PIPE, (3, 0, w - 6, h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (6, 0, 8, h))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 14, 0, 8, h))\n        cap_h = 28\n        pygame.draw.rect(s, C_PIPE_CAP, (0, 0, w, cap_h))\n        pygame.draw.rect(s, C_PIPE_HIGHLIGHT, (3, 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_PIPE_SHADOW, (w - 12, 2, 8, cap_h - 4))\n        pygame.draw.rect(s, C_WHITE, (1, cap_h - 3, w - 2, 2), 1)\n        return s\n\n    def _make_ground(self):\n        w = self.screen_w\n        h = GROUND_H\n        s = pygame.Surface((w, h))\n        s.fill(C_GROUND)\n        pygame.draw.rect(s, C_GROUND_GRASS, (0, 0, w, 14))\n        pygame.draw.rect(s, (70, 160, 40), (0, 12, w, 4))\n        for i in range(0, w, 24):\n            pygame.draw.rect(s, C_GROUND_DARK, (i, 16, 24, h - 16), 1)\n        for i in range(0, w, 48):\n            pygame.draw.circle(s, C_GROUND_DARK, (i + 12, 35), 4)\n            pygame.draw.circle(s, C_GROUND_DARK, (i + 36, 50), 3)\n        return s\n\n    def _make_clouds(self):\n        clouds = []\n        for _ in range(6):\n            cw = random.randint(60, 140)\n            ch = random.randint(20, 40)\n            s = pygame.Surface((cw, ch), pygame.SRCALPHA)\n            cx, cy = cw // 2, ch // 2\n            r = ch // 2\n            pygame.draw.circle(s, C_CLOUD, (cx, cy), r)\n            pygame.draw.circle(s, C_CLOUD, (cx - r * 0.6, cy + 2), int(r * 0.7))\n            pygame.draw.circle(s, C_CLOUD, (cx + r * 0.7, cy + 1), int(r * 0.8))\n            clouds.append((s, random.randint(0, self.screen_w),\n                           random.randint(30, 200), random.uniform(0.2, 0.8)))\n        return clouds\n\n    def _make_background(self):\n        s = pygame.Surface((self.screen_w, self.screen_h))\n        for y in range(self.screen_h):\n            t = y / self.screen_h\n            r = int(C_SKY_TOP[0] + (C_SKY_BOT[0] - C_SKY_TOP[0]) * t)\n            g = int(C_SKY_TOP[1] + (C_SKY_BOT[1] - C_SKY_TOP[1]) * t)\n            b = int(C_SKY_TOP[2] + (C_SKY_BOT[2] - C_SKY_TOP[2]) * t)\n            pygame.draw.line(s, (r, g, b), (0, y), (self.screen_w, y))\n        return s\n\n    def _make_medals(self):\n        medals = {}\n        for name, color in [(\"bronze\", C_MEDAL_BRONZE), (\"silver\", C_MEDAL_SILVER),\n                            (\"gold\", C_MEDAL_GOLD), (\"platinum\", C_MEDAL_PLATINUM)]:\n            s = pygame.Surface((48, 48), pygame.SRCALPHA)\n            pygame.draw.circle(s, color, (24, 24), 20)\n            pygame.draw.circle(s, (min(color[0] + 40, 255),\n                                    min(color[1] + 40, 255),\n                                    min(color[2] + 40, 255)), (24, 24), 16)\n            pygame.draw.circle(s, color, (24, 24), 14, 2)\n            star_pts = []\n            for i in range(5):\n                a = -math.pi / 2 + 2 * math.pi * i / 5\n                star_pts.append((24 + 8 * math.cos(a), 24 + 8 * math.sin(a)))\n                a2 = a + math.pi / 5\n                star_pts.append((24 + 4 * math.cos(a2), 24 + 4 * math.sin(a2)))\n            pygame.draw.polygon(s, (max(color[0] - 60, 0),\n                                     max(color[1] - 60, 0),\n                                     max(color[2] - 60, 0)), star_pts)\n            medals[name] = s\n        return medals\n\n    def _make_star(self):\n        s = pygame.Surface((12, 12), pygame.SRCALPHA)\n        pts = []\n        for i in range(5):\n            a = -math.pi / 2 + 2 * math.pi * i / 5\n            pts.append((6 + 5 * math.cos(a), 6 + 5 * math.sin(a)))\n            a2 = a + math.pi / 5\n            pts.append((6 + 2.5 * math.cos(a2), 6 + 2.5 * math.sin(a2)))\n        pygame.draw.polygon(s, C_STARS, pts)\n        return s\n\n    def _make_get_ready(self):\n        s = pygame.Surface((280, 80), pygame.SRCALPHA)\n        arrow = pygame.Surface((60, 40), pygame.SRCALPHA)\n        pts = [(30, 0), (60, 20), (30, 40), (20, 40), (20, 28), (0, 20), (20, 12), (20, 0)]\n        pygame.draw.polygon(arrow, (255, 255, 255, 180), pts)\n        s.blit(arrow, (110, 20))\n        return s\n\n    def _make_game_over_panel(self):\n        w, h = 320, 220\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 16\n        rect = pygame.Rect(0, 0, w, h)\n        _draw_rounded_rect(s, C_UI_BG, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 3, border_radius=r)\n        return s\n\n    def _make_menu_bg(self):\n        s = pygame.Surface((self.screen_w, self.screen_h), pygame.SRCALPHA)\n        for y in range(self.screen_h):\n            t = y / self.screen_h\n            r = int(30 + 20 * t)\n            g = int(30 + 20 * t)\n            b = int(60 + 40 * t)\n            pygame.draw.line(s, (r, g, b, 180), (0, y), (self.screen_w, y))\n        return s\n\n    def _make_title(self):\n        font = pygame.font.Font(None, 72)\n        t1 = font.render(\"FLIPPY\", True, (255, 200, 50))\n        t2 = font.render(\"BLOCK\", True, (255, 150, 50))\n        t3 = pygame.font.Font(None, 36).render(\"EXTREME\", True, (255, 100, 100))\n        w = max(t1.get_width(), t2.get_width(), t3.get_width())\n        h = t1.get_height() + t2.get_height() + t3.get_height() + 10\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        s.blit(t1, ((w - t1.get_width()) // 2, 0))\n        s.blit(t2, ((w - t2.get_width()) // 2, t1.get_height()))\n        s.blit(t3, ((w - t3.get_width()) // 2, t1.get_height() + t2.get_height() + 5))\n        return s\n\n    def _make_buttons(self):\n        labels = [\"PLAY\", \"SETTINGS\", \"LEADERBOARD\", \"BACK\", \"RETRY\",\n                  \"SOUND\", \"SHAKE\", \"EASY\", \"NORMAL\", \"HARD\", \"EXTREME\"]\n        for label in labels:\n            self.buttons[label] = self._make_button(label)\n\n    def _make_button(self, text, w=220, h=48):\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 10\n        rect = pygame.Rect(0, 0, w, h)\n        _draw_rounded_rect(s, C_UI_BG, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 36)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n\ndef _draw_rounded_rect(surf, color, rect, radius):\n    pygame.draw.rect(surf, color, (rect.x + radius, rect.y,\n                                    rect.width - 2 * radius, rect.height))\n    pygame.draw.rect(surf, color, (rect.x, rect.y + radius,\n                                    rect.width, rect.height - 2 * radius))\n    for px, py in [(rect.x + radius, rect.y + radius),\n                   (rect.x + rect.width - radius, rect.y + radius),\n                   (rect.x + radius, rect.y + rect.height - radius),\n                   (rect.x + rect.width - radius, rect.y + rect.height - radius)]:\n        pygame.draw.circle(surf, color, (px, py), radius)\n\n\n# ---------------------------------------------------------------------------\n# Bird\n# ---------------------------------------------------------------------------\nclass Bird:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.vel = 0\n        self.frame = 0\n        self.frame_timer = 0\n        self.alive = True\n        self.rotation = 0\n        self.width = 34\n        self.height = 26\n        self.dead_timer = 0\n\n    def flap(self, power):\n        self.vel = power\n\n    def update(self, gravity):\n        if not self.alive:\n            self.dead_timer += 1\n            self.vel += gravity\n            self.y += self.vel\n            self.rotation = min(self.rotation + 120, 900)\n            return\n        self.vel += gravity\n        if self.vel > MAX_FALL:\n            self.vel = MAX_FALL\n        self.y += self.vel\n        if self.vel < 0:\n            self.rotation = max(-30, self.vel * 3)\n        else:\n            self.rotation = min(90, self.rotation + 2.5)\n        self.frame_timer += 1\n        if self.frame_timer >= 6:\n            self.frame_timer = 0\n            self.frame = (self.frame + 1) % 3\n\n    def get_rect(self):\n        return pygame.Rect(self.x - self.width // 2 + 4,\n                           self.y - self.height // 2 + 4,\n                           self.width - 8, self.height - 8)\n\n\n# ---------------------------------------------------------------------------\n# Pipe\n# ---------------------------------------------------------------------------\nclass Pipe:\n    def __init__(self, x, gap_y, gap_size, speed):\n        self.x = x\n        self.gap_y = gap_y\n        self.gap_size = gap_size\n        self.speed = speed\n        self.scored = False\n        self.width = 62\n\n    def update(self):\n        self.x -= self.speed\n\n    def is_offscreen(self):\n        return self.x < -self.width - 10\n\n    def get_rects(self, screen_h, ground_h):\n        top_h = self.gap_y - self.gap_size // 2\n        bot_y = self.gap_y + self.gap_size // 2\n        bot_h = screen_h - ground_h - bot_y\n        top_rect = pygame.Rect(self.x, 0, self.width, max(top_h, 0))\n        bot_rect = pygame.Rect(self.x, bot_y, self.width, max(bot_h, 0))\n        return top_rect, bot_rect\n\n\n# ---------------------------------------------------------------------------\n# Particle system\n# ---------------------------------------------------------------------------\nclass Particle:\n    def __init__(self, x, y, color=None):\n        self.x = x\n        self.y = y\n        self.vx = random.uniform(-3, 3)\n        self.vy = random.uniform(-4, 1)\n        self.life = random.randint(20, 50)\n        self.max_life = self.life\n        self.size = random.randint(2, 5)\n        if color:\n            self.color = color\n        else:\n            self.color = random.choice([(255, 255, 255), (255, 220, 40),\n                                         (255, 180, 20), (255, 255, 200)])\n\n    def update(self):\n        self.x += self.vx\n        self.y += self.vy\n        self.vy += 0.15\n        self.life -= 1\n\n    def draw(self, surf):\n        alpha = int(200 * (self.life / self.max_life))\n        s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)\n        c = self.color\n        s.fill((c[0], c[1], c[2], alpha))\n        surf.blit(s, (int(self.x), int(self.y)))\n\n\n# ---------------------------------------------------------------------------\n# Floating score popup\n# ---------------------------------------------------------------------------\nclass ScorePopup:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n        self.life = 40\n        self.max_life = 40\n\n    def update(self):\n        self.y -= 1.2\n        self.life -= 1\n\n    def draw(self, surf):\n        if self.life <= 0:\n            return\n        alpha = min(255, int(255 * self.life / self.max_life))\n        font = pygame.font.Font(None, 48)\n        ts = font.render(\"+1\", True, (255, 255, 255))\n        ts.set_alpha(alpha)\n        surf.blit(ts, (self.x - ts.get_width() // 2, self.y))\n\n    def is_dead(self):\n        return self.life <= 0\n\n\n# ---------------------------------------------------------------------------\n# Game states\n# ---------------------------------------------------------------------------\nclass GameState:\n    MENU = 0\n    GET_READY = 1\n    PLAYING = 2\n    GAME_OVER = 3\n    SETTINGS = 4\n    LEADERBOARD = 5\n\n\n# ---------------------------------------------------------------------------\n# Main game class\n# ---------------------------------------------------------------------------\nclass FlippyBlockExtreme:\n    def __init__(self):\n        pygame.init()\n        pygame.display.set_caption(\"FlippyBlock Extreme\")\n\n        # Icon\n        icon = pygame.Surface((32, 32), pygame.SRCALPHA)\n        pygame.draw.ellipse(icon, C_BIRD_BODY, (2, 6, 28, 20))\n        pygame.draw.ellipse(icon, C_BIRD_WING, (8, 10, 14, 8))\n        pygame.draw.circle(icon, C_BIRD_EYE, (24, 10), 4)\n        pygame.draw.circle(icon, C_BIRD_PUPIL, (26, 10), 2)\n        pts = [(28, 12), (32, 14), (28, 17)]\n        pygame.draw.polygon(icon, C_BIRD_BEAK, pts)\n        pygame.display.set_icon(icon)\n\n        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))\n        self.clock = pygame.time.Clock()\n        self.font = pygame.font.Font(None, 36)\n        self.font_big = pygame.font.Font(None, 72)\n        self.font_small = pygame.font.Font(None, 24)\n        self.font_huge = pygame.font.Font(None, 96)\n\n        self.settings = Settings()\n        self.scores = Scores()\n        self.sound = SimpleSound()\n        self.sound.init()\n\n        self.assets = Assets(self.screen)\n        self.state = GameState.MENU\n        self.diff = self.settings.get_difficulty()\n\n        # Game objects\n        self.bird = None\n        self.pipes = []\n        self.particles = []\n        self.popups = []\n        self.score = 0\n        self.frame_count = 0\n        self.pipe_timer = 0\n        self.ground_offset = 0\n        self.shake_x = 0\n        self.shake_y = 0\n        self.shake_timer = 0\n        self.flash_alpha = 0\n        self.get_ready_timer = 0\n        self.game_over_timer = 0\n        self.menu_bird_y = SCREEN_H // 2 - 40\n        self.menu_bird_vel = 0\n        self._die_timer = None\n        self.difficulty_labels = [\"EASY\", \"NORMAL\", \"HARD\", \"EXTREME\"]\n        self.difficulty_keys = [\"easy\", \"normal\", \"hard\", \"extreme\"]\n\n        # Clouds state\n        self.cloud_positions = []\n        for c in self.assets.clouds:\n            self.cloud_positions.append([c[1], c[2], c[3]])\n\n    def run(self):\n        running = True\n        while running:\n            self.clock.tick(FPS)\n            self._handle_events(running)\n            if not running:\n                break\n            self._update()\n            self._draw()\n            pygame.display.flip()\n        pygame.quit()\n        sys.exit()\n\n    # ------------------------------------------------------------------\n    # Events\n    # ------------------------------------------------------------------\n    def _handle_events(self, running):\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                return False\n\n            if event.type == pygame.KEYDOWN:\n                if event.key == pygame.K_ESCAPE:\n                    self._on_escape()\n                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:\n                    self._on_action()\n                if event.key == pygame.K_r:\n                    self._on_restart()\n\n            if event.type == pygame.MOUSEBUTTONDOWN:\n                if event.button == 1:\n                    self._on_click(event.pos)\n\n        return running\n\n    def _on_escape(self):\n        if self.state == GameState.SETTINGS or self.state == GameState.LEADERBOARD:\n            self.settings.save()\n            self.state = GameState.MENU\n            self.sound.swoosh()\n        elif self.state == GameState.PLAYING:\n            self.state = GameState.MENU\n            self.sound.swoosh()\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.MENU\n            self.sound.swoosh()\n\n    def _on_action(self):\n        if self.state == GameState.MENU:\n            self._start_game()\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.PLAYING\n            self.bird.flap(self.diff[\"flap\"])\n            self.sound.flap()\n        elif self.state == GameState.PLAYING:\n            if self.bird and self.bird.alive:\n                self.bird.flap(self.diff[\"flap\"])\n                self.sound.flap()\n                self._spawn_particles(self.bird.x, self.bird.y + 5, 3)\n        elif self.state == GameState.GAME_OVER:\n            if self.game_over_timer > 60:\n                self._start_game()\n                self.sound.swoosh()\n\n    def _on_restart(self):\n        if self.state == GameState.GAME_OVER and self.game_over_timer > 30:\n            self._start_game()\n            self.sound.swoosh()\n\n    def _on_click(self, pos):\n        mx, my = pos\n\n        if self.state == GameState.MENU:\n            self._handle_menu_click(mx, my)\n        elif self.state == GameState.GET_READY:\n            self.state = GameState.PLAYING\n            self.bird.flap(self.diff[\"flap\"])\n            self.sound.flap()\n        elif self.state == GameState.PLAYING:\n            if self.bird and self.bird.alive:\n                self.bird.flap(self.diff[\"flap\"])\n                self.sound.flap()\n                self._spawn_particles(self.bird.x, self.bird.y + 5, 3)\n        elif self.state == GameState.GAME_OVER:\n            self._handle_gameover_click(mx, my)\n        elif self.state == GameState.SETTINGS:\n            self._handle_settings_click(mx, my)\n        elif self.state == GameState.LEADERBOARD:\n            self._handle_leaderboard_click(mx, my)\n\n    # ------------------------------------------------------------------\n    # Menu buttons layout\n    # ------------------------------------------------------------------\n    def _menu_buttons(self):\n        btn_w, btn_h = 220, 48\n        cx = SCREEN_W // 2\n        start_y = 340\n        buttons = {}\n        for i, label in enumerate([\"PLAY\", \"SETTINGS\", \"LEADERBOARD\"]):\n            y = start_y + i * (btn_h + 16)\n            rect = pygame.Rect(cx - btn_w // 2, y, btn_w, btn_h)\n            buttons[label] = rect\n        return buttons\n\n    def _handle_menu_click(self, mx, my):\n        buttons = self._menu_buttons()\n        for label, rect in buttons.items():\n            if rect.collidepoint(mx, my):\n                self.sound.swoosh()\n                if label == \"PLAY\":\n                    self._start_game()\n                elif label == \"SETTINGS\":\n                    self.state = GameState.SETTINGS\n                elif label == \"LEADERBOARD\":\n                    self.state = GameState.LEADERBOARD\n                return\n\n    # ------------------------------------------------------------------\n    # Game over buttons\n    # ------------------------------------------------------------------\n    def _gameover_buttons(self):\n        btn_w, btn_h = 200, 44\n        cx = SCREEN_W // 2\n        buttons = {}\n        for i, label in enumerate([\"RETRY\", \"BACK\"]):\n            y = 460 + i * (btn_h + 12)\n            rect = pygame.Rect(cx - btn_w // 2, y, btn_w, btn_h)\n            buttons[label] = rect\n        return buttons\n\n    def _handle_gameover_click(self, mx, my):\n        if self.game_over_timer < 30:\n            return\n        buttons = self._gameover_buttons()\n        for label, rect in buttons.items():\n            if rect.collidepoint(mx, my):\n                self.sound.swoosh()\n                if label == \"RETRY\":\n                    self._start_game()\n                elif label == \"BACK\":\n                    self.state = GameState.MENU\n\n    # ------------------------------------------------------------------\n    # Settings buttons\n    # ------------------------------------------------------------------\n    def _handle_settings_click(self, mx, my):\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n\n        back_rect = pygame.Rect(cx - btn_w // 2, SCREEN_H - 100, btn_w, btn_h)\n        if back_rect.collidepoint(mx, my):\n            self.settings.save()\n            self.state = GameState.MENU\n            self.sound.swoosh()\n            return\n\n        sy = 200\n        sound_rect = pygame.Rect(cx - btn_w // 2, sy, btn_w, btn_h)\n        if sound_rect.collidepoint(mx, my):\n            self.settings.data[\"sound\"] = not self.settings.data[\"sound\"]\n            self.sound.enabled = self.settings.data[\"sound\"]\n            self.sound.swoosh()\n\n        shake_rect = pygame.Rect(cx - btn_w // 2, sy + 60, btn_w, btn_h)\n        if shake_rect.collidepoint(mx, my):\n            self.settings.data[\"shake\"] = not self.settings.data[\"shake\"]\n            self.sound.swoosh()\n\n        diff_y = sy + 140\n        for i, key in enumerate(self.difficulty_keys):\n            label = self.difficulty_labels[i]\n            if i < 2:\n                dx = cx - 2 * btn_w // 2 - 6 + i * (btn_w + 12)\n                dy = diff_y\n            else:\n                dx = cx - 2 * btn_w // 2 - 6 + (i - 2) * (btn_w + 12)\n                dy = diff_y + 52\n            drect = pygame.Rect(dx, dy, btn_w, btn_h)\n            if drect.collidepoint(mx, my):\n                self.settings.data[\"difficulty\"] = key\n                self.diff = self.settings.get_difficulty()\n                self.sound.swoosh()\n\n    # ------------------------------------------------------------------\n    # Leaderboard buttons\n    # ------------------------------------------------------------------\n    def _handle_leaderboard_click(self, mx, my):\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n        back_rect = pygame.Rect(cx - btn_w // 2, SCREEN_H - 100, btn_w, btn_h)\n        if back_rect.collidepoint(mx, my):\n            self.state = GameState.MENU\n            self.sound.swoosh()\n\n    # ------------------------------------------------------------------\n    # Game logic\n    # ------------------------------------------------------------------\n    def _start_game(self):\n        self.state = GameState.GET_READY\n        self.bird = Bird(BIRD_X, SCREEN_H // 2 - 40)\n        self.pipes = []\n        self.particles = []\n        self.popups = []\n        self.score = 0\n        self.frame_count = 0\n        self.pipe_timer = 0\n        self.get_ready_timer = 0\n        self.game_over_timer = 0\n        self.flash_alpha = 0\n        self._die_timer = None\n        self.diff = self.settings.get_difficulty()\n        self.sound.swoosh()\n\n    def _update(self):\n        self.frame_count += 1\n\n        # Screen shake\n        if self.shake_timer > 0:\n            self.shake_timer -= 1\n            if self.settings.data[\"shake\"]:\n                self.shake_x = random.randint(-4, 4)\n                self.shake_y = random.randint(-4, 4)\n            else:\n                self.shake_x = 0\n                self.shake_y = 0\n        else:\n            self.shake_x = 0\n            self.shake_y = 0\n\n        # Flash fade\n        if self.flash_alpha > 0:\n            self.flash_alpha -= 4\n\n        # Clouds always move\n        for i, c in enumerate(self.assets.clouds):\n            self.cloud_positions[i][0] -= self.cloud_positions[i][2]\n            if self.cloud_positions[i][0] < -c[0].get_width():\n                self.cloud_positions[i][0] = self.screen_w + random.randint(0, 100)\n                self.cloud_positions[i][1] = random.randint(30, 200)\n\n        # Menu bird bob\n        if self.state == GameState.MENU:\n            self.menu_bird_vel += 0.3\n            self.menu_bird_vel *= 0.9\n            self.menu_bird_y += self.menu_bird_vel\n            if self.menu_bird_y > SCREEN_H // 2:\n                self.menu_bird_y = SCREEN_H // 2\n                self.menu_bird_vel = -4\n            elif self.menu_bird_y < SCREEN_H // 2 - 80:\n                self.menu_bird_y = SCREEN_H // 2 - 80\n                self.menu_bird_vel = 1\n\n        elif self.state == GameState.GET_READY:\n            self.get_ready_timer += 1\n            self.bird.y = SCREEN_H // 2 - 40 + math.sin(self.get_ready_timer * 0.08) * 10\n            self.ground_offset = (self.ground_offset + self.diff[\"speed\"]) % self.screen_w\n\n        elif self.state == GameState.PLAYING:\n            self._update_playing()\n\n        elif self.state == GameState.GAME_OVER:\n            self.game_over_timer += 1\n            if self.bird:\n                self.bird.update(self.diff[\"gravity\"])\n                if self.bird.y >= SCREEN_H - GROUND_H - self.bird.height // 2:\n                    self.bird.y = SCREEN_H - GROUND_H - self.bird.height // 2\n                    self.bird.vel = 0\n\n        # Die timer — transition from PLAYING to GAME_OVER\n        if self._die_timer is not None:\n            self._die_timer -= 1\n            if self._die_timer <= 0:\n                self.state = GameState.GAME_OVER\n                self.game_over_timer = 0\n                self.sound.die()\n\n        # Always update particles\n        self.particles = [p for p in self.particles if p.life > 0]\n        for p in self.particles:\n            p.update()\n\n        self.popups = [p for p in self.popups if not p.is_dead()]\n        for p in self.popups:\n            p.update()\n\n    def _update_playing(self):\n        self.bird.update(self.diff[\"gravity\"])\n        self.ground_offset = (self.ground_offset + self.diff[\"speed\"]) % self.screen_w\n\n        # Pipe spawning\n        self.pipe_timer += 1\n        if self.pipe_timer >= PIPE_INTERVAL:\n            self.pipe_timer = 0\n            min_y = GROUND_H + self.diff[\"gap_size\"] // 2 + 40\n            max_y = SCREEN_H - GROUND_H - self.diff[\"gap_size\"] // 2 - 40\n            gap_y = random.randint(min_y, max_y)\n            speed = self.diff[\"speed\"] + self.score * 0.02\n            self.pipes.append(Pipe(SCREEN_W + 10, gap_y, self.diff[\"gap_size\"], speed))\n\n        # Update pipes\n        for pipe in self.pipes:\n            pipe.speed = self.diff[\"speed\"] + self.score * 0.02\n            pipe.update()\n\n        self.pipes = [p for p in self.pipes if not p.is_offscreen()]\n\n        # Collision detection\n        bird_rect = self.bird.get_rect()\n        for pipe in self.pipes:\n            top_rect, bot_rect = pipe.get_rects(SCREEN_H, GROUND_H)\n            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect):\n                self._die()\n                return\n\n        if (self.bird.y + self.bird.height // 2 >= SCREEN_H - GROUND_H or\n                self.bird.y - self.bird.height // 2 <= 0):\n            self._die()\n            return\n\n        # Scoring\n        for pipe in self.pipes:\n            if not pipe.scored and pipe.x + pipe.width < self.bird.x:\n                pipe.scored = True\n                self.score += 1\n                self.sound.score()\n                self.popups.append(ScorePopup(self.bird.x, self.bird.y - 30))\n                self._spawn_particles(self.bird.x, self.bird.y, 5, (255, 215, 0))\n\n    def _die(self):\n        self.bird.alive = False\n        self.sound.hit()\n        self.shake_timer = 15\n        self.flash_alpha = 180\n        self._spawn_particles(self.bird.x, self.bird.y, 15)\n        self.scores.add(self.score)\n        self._die_timer = 40\n\n    def _spawn_particles(self, x, y, count, color=None):\n        for _ in range(count):\n            self.particles.append(Particle(x, y, color))\n\n    # ------------------------------------------------------------------\n    # Drawing\n    # ------------------------------------------------------------------\n    def _draw(self):\n        self.screen.blit(self.assets.background, (0, 0))\n\n        for i, c in enumerate(self.assets.clouds):\n            cx, cy = self.cloud_positions[i][0], self.cloud_positions[i][1]\n            self.screen.blit(c[0], (int(cx), int(cy)))\n\n        if self.state == GameState.MENU:\n            self._draw_menu()\n        elif self.state == GameState.GET_READY:\n            self._draw_game()\n            self._draw_get_ready()\n        elif self.state == GameState.PLAYING:\n            self._draw_game()\n            self._draw_hud()\n        elif self.state == GameState.GAME_OVER:\n            self._draw_game()\n            self._draw_game_over()\n        elif self.state == GameState.SETTINGS:\n            self._draw_settings()\n        elif self.state == GameState.LEADERBOARD:\n            self._draw_leaderboard()\n\n        if self.flash_alpha > 0:\n            flash = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n            flash.fill((255, 255, 255, min(self.flash_alpha, 255)))\n            self.screen.blit(flash, (0, 0))\n\n        if self.settings.data.get(\"show_fps\", False):\n            fps_text = self.font_small.render(f\"{self.clock.get_fps():.1f} FPS\", True, C_WHITE)\n            self.screen.blit(fps_text, (5, 5))\n\n    def _draw_game(self):\n        for pipe in self.pipes:\n            top_h = pipe.gap_y - pipe.gap_size // 2\n            bot_y = pipe.gap_y + pipe.gap_size // 2\n\n            # Top pipe: draw so cap sits at top_h\n            if top_h > 0:\n                draw_y = top_h - SCREEN_H\n                self.screen.blit(self.assets.pipe_top, (pipe.x, draw_y))\n\n            # Bottom pipe: draw starting at bot_y\n            bot_h = SCREEN_H - GROUND_H - bot_y\n            if bot_h > 0:\n                self.screen.blit(self.assets.pipe_bottom, (pipe.x, bot_y))\n\n        # Ground (tiled)\n        tile_w = self.assets.ground.get_width()\n        for x in range(-tile_w, SCREEN_W + tile_w, tile_w):\n            draw_x = x + (self.ground_offset % tile_w)\n            self.screen.blit(self.assets.ground, (draw_x, SCREEN_H - GROUND_H))\n\n        # Particles\n        for p in self.particles:\n            p.draw(self.screen)\n\n        # Popups\n        for p in self.popups:\n            p.draw(self.screen)\n\n        # Bird\n        if self.bird:\n            frame = self.assets.bird_frames[self.bird.frame]\n            rotated = pygame.transform.rotate(frame, -self.bird.rotation)\n            r = rotated.get_rect(center=(self.bird.x, self.bird.y))\n            self.screen.blit(rotated, r.topleft)\n\n    def _draw_hud(self):\n        score_str = str(self.score)\n        ts = self.font_huge.render(score_str, True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, 62))\n        ts = self.font_huge.render(score_str, True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n    def _draw_get_ready(self):\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 40))\n        self.screen.blit(overlay, (0, 0))\n\n        font = pygame.font.Font(None, 60)\n        ts = font.render(\"GET READY\", True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, 182))\n        ts = font.render(\"GET READY\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 180))\n\n        instr = self.font.render(\"Tap or press SPACE to fly\", True, C_WHITE)\n        self.screen.blit(instr, (SCREEN_W // 2 - instr.get_width() // 2, 260))\n\n        icon_y = 320 + math.sin(self.frame_count * 0.1) * 8\n        self.screen.blit(self.assets.get_ready,\n                         (SCREEN_W // 2 - 140, icon_y))\n\n    def _draw_menu(self):\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n        self._draw_city_silhouette()\n\n        title = self.assets.title_text\n        title_x = SCREEN_W // 2 - title.get_width() // 2\n        title_y = 80 + math.sin(self.frame_count * 0.03) * 5\n        self.screen.blit(title, (title_x, title_y))\n\n        bird_frame = self.frame_count // 8 % 3\n        bird = self.assets.bird_frames[bird_frame]\n        self.screen.blit(bird, (SCREEN_W // 2 - 17, self.menu_bird_y))\n\n        buttons = self._menu_buttons()\n        mouse_pos = pygame.mouse.get_pos()\n        for label, rect in buttons.items():\n            if rect.collidepoint(mouse_pos):\n                btn_surf = self.assets.buttons[label].copy()\n                for px in range(btn_surf.get_width()):\n                    for py in range(btn_surf.get_height()):\n                        p = btn_surf.get_at((px, py))\n                        if p[3] > 0:\n                            btn_surf.set_at((px, py), (\n                                min(int(p[0] * 1.3), 255),\n                                min(int(p[1] * 1.3), 255),\n                                min(int(p[2] * 1.3), 255),\n                                p[3]\n                            ))\n                self.screen.blit(btn_surf, rect.topleft)\n            else:\n                self.screen.blit(self.assets.buttons[label], rect.topleft)\n\n        best = self.scores.best()\n        if best > 0:\n            best_text = self.font.render(f\"Best: {best}\", True, (255, 215, 0))\n            self.screen.blit(best_text, (SCREEN_W // 2 - best_text.get_width() // 2, 540))\n\n        ver = self.font_small.render(\"v1.0\", True, (150, 150, 180))\n        self.screen.blit(ver, (SCREEN_W - ver.get_width() - 10, SCREEN_H - 30))\n\n    def _draw_city_silhouette(self):\n        silhouette = pygame.Surface((SCREEN_W, 120), pygame.SRCALPHA)\n        silhouette.fill((20, 25, 40, 120))\n        buildings = [\n            (0, 30, 40, 90), (35, 20, 30, 100), (60, 40, 50, 80),\n            (105, 15, 35, 105), (135, 35, 45, 85), (175, 25, 40, 95),\n            (210, 45, 55, 75), (260, 10, 30, 110), (285, 30, 50, 90),\n            (330, 20, 40, 100), (365, 40, 45, 80), (405, 15, 35, 105),\n            (435, 35, 45, 85),\n        ]\n        rng = random.Random(42)\n        for bx, by, bw, bh in buildings:\n            pygame.draw.rect(silhouette, (20, 25, 40, 120), (bx, by, bw, bh))\n            wy = by + 8\n            while wy < by + bh - 8:\n                wx = bx + 6\n                while wx < bx + bw - 6:\n                    if rng.random() > 0.3:\n                        pygame.draw.rect(silhouette, (255, 220, 100, 60), (wx, wy, 4, 5))\n                    wx += 10\n                wy += 12\n        self.screen.blit(silhouette, (0, SCREEN_H - GROUND_H - 120))\n\n    def _draw_game_over(self):\n        if self.game_over_timer < 10:\n            return\n\n        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)\n        overlay.fill((0, 0, 0, 100))\n        self.screen.blit(overlay, (0, 0))\n\n        panel = self.assets.game_over_panel\n        px = SCREEN_W // 2 - panel.get_width() // 2\n        py = 200\n        self.screen.blit(panel, (px, py))\n\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"GAME OVER\", True, C_BLACK)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2 + 2, py - 58))\n        ts = font.render(\"GAME OVER\", True, C_ACCENT)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, py - 60))\n\n        score_text = self.font_big.render(str(self.score), True, C_WHITE)\n        self.screen.blit(score_text, (SCREEN_W // 2 - score_text.get_width() // 2, py + 20))\n\n        best = self.scores.best()\n        best_text = self.font.render(f\"Best: {best}\", True, (255, 215, 0))\n        self.screen.blit(best_text, (SCREEN_W // 2 - best_text.get_width() // 2, py + 80))\n\n        if self.score == best and self.score > 0:\n            new_text = self.font.render(\"NEW!\", True, (255, 100, 100))\n            if self.frame_count % 20 < 10:\n                self.screen.blit(new_text, (px + panel.get_width() - new_text.get_width() - 15, py + 25))\n\n        medal = self.scores.get_medal(self.score)\n        if medal and medal in self.assets.medal_icons:\n            self.screen.blit(self.assets.medal_icons[medal], (px + 20, py + 50))\n\n        if self.game_over_timer > 30:\n            buttons = self._gameover_buttons()\n            for label, rect in buttons.items():\n                self.screen.blit(self.assets.buttons[label], rect.topleft)\n\n        if self.game_over_timer > 60:\n            if self.frame_count % 40 < 25:\n                tap = self.font.render(\"Tap or SPACE to retry\", True, (200, 200, 220))\n                self.screen.blit(tap, (SCREEN_W // 2 - tap.get_width() // 2, SCREEN_H - 60))\n\n    def _draw_settings(self):\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"SETTINGS\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n        btn_w, btn_h = 180, 40\n        cx = SCREEN_W // 2\n        sy = 170\n\n        sound_on = self.settings.data[\"sound\"]\n        sound_label = f\"SOUND: {'ON' if sound_on else 'OFF'}\"\n        sound_btn = self._make_toggle_btn(sound_label, sound_on)\n        self.screen.blit(sound_btn, (cx - btn_w // 2, sy))\n\n        shake_on = self.settings.data[\"shake\"]\n        shake_label = f\"SHAKE: {'ON' if shake_on else 'OFF'}\"\n        shake_btn = self._make_toggle_btn(shake_label, shake_on)\n        self.screen.blit(shake_btn, (cx - btn_w // 2, sy + 60))\n\n        diff_title = self.font.render(\"DIFFICULTY\", True, C_WHITE)\n        self.screen.blit(diff_title, (cx - diff_title.get_width() // 2, sy + 130))\n\n        diff_y = sy + 160\n        for i, key in enumerate(self.difficulty_keys):\n            label = self.difficulty_labels[i]\n            is_active = self.settings.data[\"difficulty\"] == key\n            if i < 2:\n                dx = cx - 2 * btn_w // 2 - 6 + i * (btn_w + 12)\n                dy = diff_y\n            else:\n                dx = cx - 2 * btn_w // 2 - 6 + (i - 2) * (btn_w + 12)\n                dy = diff_y + 52\n            dbtn = self._make_diff_btn(label, is_active)\n            self.screen.blit(dbtn, (dx, dy))\n\n        back_btn = self.assets.buttons[\"BACK\"]\n        self.screen.blit(back_btn, (cx - back_btn.get_width() // 2, SCREEN_H - 100))\n\n    def _make_toggle_btn(self, text, is_on):\n        w, h = 180, 40\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 8\n        rect = pygame.Rect(0, 0, w, h)\n        color = (60, 180, 60) if is_on else (180, 60, 60)\n        _draw_rounded_rect(s, color, rect, r)\n        pygame.draw.rect(s, C_WHITE, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 28)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n    def _make_diff_btn(self, text, is_active):\n        w, h = 80, 40\n        s = pygame.Surface((w, h), pygame.SRCALPHA)\n        r = 8\n        rect = pygame.Rect(0, 0, w, h)\n        color = (80, 200, 80) if is_active else C_UI_BG\n        _draw_rounded_rect(s, color, rect, r)\n        pygame.draw.rect(s, C_UI_BORDER, rect, 2, border_radius=r)\n        font = pygame.font.Font(None, 24)\n        ts = font.render(text, True, C_WHITE)\n        s.blit(ts, ((w - ts.get_width()) // 2, (h - ts.get_height()) // 2))\n        return s\n\n    def _draw_leaderboard(self):\n        self.screen.blit(self.assets.menu_bg, (0, 0))\n\n        font = pygame.font.Font(None, 56)\n        ts = font.render(\"LEADERBOARD\", True, C_WHITE)\n        self.screen.blit(ts, (SCREEN_W // 2 - ts.get_width() // 2, 60))\n\n        scores = sorted(self.scores.history, reverse=True)[:15]\n        if not scores:\n            no_text = self.font.render(\"No scores yet!\", True, (180, 180, 200))\n            self.screen.blit(no_text, (SCREEN_W // 2 - no_text.get_width() // 2, 200))\n        else:\n            for i, sc in enumerate(scores):\n                y = 130 + i * 32\n                if y > SCREEN_H - 120:\n                    break\n\n                rank_colors = [(255, 215, 0), (192, 192, 192), (205, 127, 50)]\n                rank_color = rank_colors[i] if i < 3 else (180, 180, 200)\n                rank_text = self.font.render(f\"#{i + 1}\", True, rank_color)\n                self.screen.blit(rank_text, (40, y))\n\n                score_text = self.font.render(str(sc), True, C_WHITE)\n                self.screen.blit(score_text, (120, y))\n\n                medal = self.scores.get_medal(sc)\n                if medal and medal in self.assets.medal_icons:\n                    mini = pygame.transform.scale(self.assets.medal_icons[medal], (20, 20))\n                    self.screen.blit(mini, (180, y + 6))\n\n                bar_w = min(sc * 4, 200)\n                pygame.draw.rect(self.screen, (60, 80, 120), (220, y + 8, bar_w, 16))\n                if i == 0:\n                    pygame.draw.rect(self.screen, (80, 120, 180), (220, y + 8, bar_w, 16))\n\n        if scores:\n            avg = sum(scores) // len(scores)\n            stats = self.font_small.render(\n                f\"Games: {len(self.scores.history)}  |  Avg: {avg}\",\n                True, (150, 150, 180)\n            )\n            self.screen.blit(stats, (SCREEN_W // 2 - stats.get_width() // 2, SCREEN_H - 130))\n\n        back_btn = self.assets.buttons[\"BACK\"]\n        self.screen.blit(back_btn, (SCREEN_W // 2 - back_btn.get_width() // 2, SCREEN_H - 90))\n\n\n# ---------------------------------------------------------------------------\n# Entry point\n# ---------------------------------------------------------------------------\ndef main():\n    game = FlippyBlockExtreme()\n    game.run()\n\n\nif __name__ == \"__main__\":\n    main()\n",
  "filePath": "/home/patof/stress_bench/Flip_None/flippyblock_extreme.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build · Qwen3.6 27B · 3.7s)

_Thinking:_

)00.


Now let me verify the file is syntactically correct:



**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"import py_compile; py_compile.compile('flippyblock_extreme.py', doraise=True); print('OK')\"",
  "description": "Check Python syntax of game file"
}
```

**Output:**
```
OK

```

---

## Assistant (Build · Qwen3.6 27B · 5.5s)

_Thinking:_

,00.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport pygame, sys, io\n# Redirect stderr to check for pygame warnings\nold_stderr = sys.stderr\nsys.stderr = io.StringIO()\npygame.init()\n# Quick smoke test: import the module and check it doesn't crash on init\nsys.stderr = old_stderr\nprint('pygame OK, version:', pygame.version.ver)\n\"",
  "description": "Verify pygame is available"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
pygame OK, version: 2.6.1

```

---

## Assistant (Build · Qwen3.6 27B · 19.9s)

_Thinking:_

,00.


**Tool: bash**

**Input:**
```json
{
  "command": "python3 -c \"\nimport importlib.util, sys\nspec = importlib.util.spec_from_file_location('game', 'flippyblock_extreme.py')\nmod = importlib.util.module_from_spec(spec)\n\n# Patch pygame.display.set_mode to avoid needing a display\nimport pygame\norig_init = pygame.init\norig_display = pygame.display.set_mode\norig_icon = pygame.display.set_icon\norig_quit = pygame.quit\n\ncalled = []\ndef mock_init():\n    pygame.mixer.init = lambda **k: None\n    pygame.font.init()\norig_init = mock_init\n\npygame.display.set_mode = lambda *a, **k: pygame.Surface((480, 720))\npygame.display.set_icon = lambda *a: None\npygame.display.set_caption = lambda *a: None\npygame.quit = lambda: None\n\n# Now load the module — this exercises all class definitions\ntry:\n    spec.loader.exec_module(mod)\n    print('All classes defined OK')\n    \n    # Verify key classes exist\n    for cls in ['FlippyBlockExtreme', 'Bird', 'Pipe', 'Particle', 'ScorePopup', \n                'GameState', 'Settings', 'Scores', 'SimpleSound', 'Assets']:\n        assert hasattr(mod, cls), f'Missing: {cls}'\n    print('All classes present')\n    \n    # Verify game states\n    assert mod.GameState.MENU == 0\n    assert mod.GameState.GET_READY == 1\n    assert mod.GameState.PLAYING == 2\n    assert mod.GameState.GAME_OVER == 3\n    assert mod.GameState.SETTINGS == 4\n    assert mod.GameState.LEADERBOARD == 5\n    print('All game states correct')\n    \n    # Verify difficulty settings\n    for d in ['easy', 'normal', 'hard', 'extreme']:\n        diff = mod.Settings.DIFFICULTY[d]\n        assert 'gravity' in diff\n        assert 'flap' in diff\n        assert 'gap' in diff\n        assert 'speed' in diff\n    print('All difficulty presets valid')\n    \n    print('All checks passed!')\nexcept Exception as e:\n    print(f'ERROR: {e}')\n    import traceback\n    traceback.print_exc()\n\"",
  "description": "Smoke test module loading"
}
```

**Output:**
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
All classes defined OK
All classes present
All game states correct
All difficulty presets valid
All checks passed!

```

---

## Assistant (Build · Qwen3.6 27B · 7.1s)

_Thinking:_

1.


**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Create the FlippyBlock Extreme game with all core mechanics",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add UI features: menu, HUD, settings, pause, game over screen",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Review and fix all bugs",
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
    "content": "Create the FlippyBlock Extreme game with all core mechanics",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add UI features: menu, HUD, settings, pause, game over screen",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add generated assets: bird, pipes, background, ground, clouds, particles",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add game features: scoring, sounds, difficulty scaling, leaderboards",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Review and fix all bugs",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · Qwen3.6 27B · 17.9s)

_Thinking:_

3000.


Done. The game is at `flippyblock_extreme.py`. Run it with:

```
python3 flippyblock_extreme.py
```

**Bugs fixed from review:**
1. **Critical** — `_die_timer` was never decremented; game never transitioned to GAME_OVER. Fixed with a dedicated die-timer check in `_update()`.
2. **Critical** — Dual event loops caused redundant QUIT handling. Fixed with a single event loop pattern.
3. **Critical** — Pipe surfaces were only 400px tall, leaving gaps. Extended to full screen height (720px).
4. **Critical** — Sound system used `pygame.sndarray` (requires numpy). Replaced with raw `bytearray` PCM synthesis — zero external dependencies.
5. Particles were updated twice per frame in GAME_OVER. Removed the duplicate.
6. SPACE on GAME_OVER now retries (matching Flappy Bird convention).
7. Removed dead `SoundFX` class and `numpy_like_*` helpers.
8. Removed unused `dt` variable.

**Features included:**
- **Menu** with animated title, bobbing bird, city silhouette, PLAY/SETTINGS/LEADERBOARD buttons
- **4 difficulty levels**: Easy, Normal, Hard, Extreme (affects gravity, flap power, gap size, speed)
- **Settings screen**: Sound toggle, screen shake toggle, difficulty selection
- **Leaderboard**: Top 15 scores with medals, rank colors, score bars, game stats
- **Game Over screen**: Score, best, medal (bronze/silver/gold/platinum), NEW indicator, RETRY/BACK buttons
- **Procedural audio**: Flap, score, hit, die, swoosh — all synthesized at runtime
- **Visual effects**: Screen shake, white flash on death, particles, floating +1 score popups
- **Progressive difficulty**: Pipe speed increases as your score grows
- **Persistent saves**: Scores and settings saved to `~/.flippyblock/`
- **All assets generated**: Bird (3-frame wing animation), pipes with caps/highlights, gradient sky, clouds, ground with grass, medals with stars

---

