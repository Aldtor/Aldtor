import os

out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

with open(os.path.join(out_dir, "char_b64.txt"), "r") as f:
    char_b64 = f.read().strip()

with open(os.path.join(out_dir, "face_b64.txt"), "r") as f:
    face_b64 = f.read().strip()

print(f"Loaded char_b64 len={len(char_b64)}, face_b64 len={len(face_b64)}")

username = "Aldtor"
display_name = "ALDTOR"
raw_base = "https://raw.githubusercontent.com/Aldtor/Aldtor/main"

# 1. banner.svg (Dark Mode - Strict Valid XML, replacing &nbsp; with &#160;)
banner_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0518" />
      <stop offset="50%" stop-color="#140b29" />
      <stop offset="100%" stop-color="#090314" />
    </linearGradient>

    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff4da6">
        <animate attributeName="stop-color" values="#ff4da6; #9b51e0; #00f2fe; #ff4da6" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#b55fe6">
        <animate attributeName="stop-color" values="#b55fe6; #ff4da6; #9b51e0; #b55fe6" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#38ef7d">
        <animate attributeName="stop-color" values="#38ef7d; #00f2fe; #ff4da6; #38ef7d" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff00a0" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ff00a0" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <clipPath id="banner-clip">
      <rect x="0" y="0" width="1280" height="740" rx="24" ry="24" />
    </clipPath>
  </defs>

  <style>
    .terminal-text {{ font-family: 'Fira Code', 'Courier New', monospace; font-size: 16px; fill: #00ffcc; }}
    .name-title {{ font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 58px; font-weight: 900; letter-spacing: 4px; fill: url(#text-grad); }}
    .role-title {{ font-family: 'Fira Code', monospace; font-size: 22px; fill: #e0b0ff; }}
    .code-text {{ font-family: 'Consolas', monospace; font-size: 14px; fill: #f8f8f2; }}
    .pill-bg {{ fill: rgba(255, 255, 255, 0.07); stroke: rgba(255, 105, 180, 0.4); stroke-width: 1.5; rx: 14; }}
    .pill-text {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; font-weight: 600; fill: #ffffff; }}

    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    .cursor {{ animation: blink 1s infinite; fill: #00ffcc; }}

    @keyframes neonPulse {{
      0%, 100% {{ opacity: 0.9; filter: drop-shadow(0 0 8px #ff007f); }}
      50% {{ opacity: 0.4; filter: drop-shadow(0 0 2px #ff007f); }}
    }}
    .neon-box {{ animation: neonPulse 2.5s infinite; }}
  </style>

  <g clip-path="url(#banner-clip)">
    <rect width="1280" height="740" fill="url(#bg-grad)" />

    <circle cx="150" cy="150" r="220" fill="#9b51e0" opacity="0.15" filter="url(#glow)"/>
    <circle cx="1100" cy="550" r="280" fill="#ff2a85" opacity="0.12" filter="url(#glow)"/>
    <circle cx="640" cy="370" r="300" fill="#00f2fe" opacity="0.08" filter="url(#glow)"/>

    <path d="M0 100 H1280 M0 200 H1280 M0 300 H1280 M0 400 H1280 M0 500 H1280 M0 600 H1280 M0 700 H1280" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1"/>
    <path d="M200 0 V740 M400 0 V740 M600 0 V740 M800 0 V740 M1000 0 V740 M1200 0 V740" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1"/>

    <!-- Terminal Prompt Card -->
    <rect x="50" y="45" width="680" height="52" rx="12" fill="#0d071b" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
    <circle cx="75" cy="71" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="71" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="71" r="6" fill="#27c93f"/>
    <text x="140" y="76" class="terminal-text">aldtor@github:~$ cat profile.md<tspan class="cursor">_</tspan></text>

    <!-- Name Header -->
    <text x="50" y="160" class="name-title">{display_name}</text>

    <!-- Animated Typing Role Titles -->
    <g transform="translate(50, 195)">
      <rect x="0" y="-22" width="460" height="32" rx="6" fill="rgba(155, 81, 224, 0.15)"/>
      <text x="12" y="0" class="role-title">⚡ Full Stack Developer &amp; Engineer</text>
    </g>

    <!-- Tagline Neon Box -->
    <g transform="translate(50, 245)" class="neon-box">
      <rect x="0" y="0" width="380" height="42" rx="8" fill="rgba(255, 0, 127, 0.08)" stroke="#ff007f" stroke-width="2"/>
      <text x="190" y="27" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="16" fill="#ff66cc" text-anchor="middle" letter-spacing="3">✦ KEEP CODING • KEEP GROWING ✦</text>
    </g>

    <!-- Tech Stack Pills -->
    <g transform="translate(50, 315)">
      <g transform="translate(0, 0)">
        <rect width="105" height="32" class="pill-bg"/>
        <text x="52" y="21" class="pill-text" text-anchor="middle">⚡ JavaScript</text>
      </g>
      <g transform="translate(115, 0)">
        <rect width="105" height="32" class="pill-bg"/>
        <text x="52" y="21" class="pill-text" text-anchor="middle">🔷 TypeScript</text>
      </g>
      <g transform="translate(230, 0)">
        <rect width="90" height="32" class="pill-bg"/>
        <text x="45" y="21" class="pill-text" text-anchor="middle">⚛️ React</text>
      </g>
      <g transform="translate(330, 0)">
        <rect width="95" height="32" class="pill-bg"/>
        <text x="47" y="21" class="pill-text" text-anchor="middle">🟢 Node.js</text>
      </g>
      <g transform="translate(435, 0)">
        <rect width="90" height="32" class="pill-bg"/>
        <text x="45" y="21" class="pill-text" text-anchor="middle">🐍 Python</text>
      </g>
      <g transform="translate(0, 44)">
        <rect width="95" height="32" class="pill-bg"/>
        <text x="47" y="21" class="pill-text" text-anchor="middle">🎨 HTML/CSS</text>
      </g>
      <g transform="translate(105, 44)">
        <rect width="80" height="32" class="pill-bg"/>
        <text x="40" y="21" class="pill-text" text-anchor="middle">🗄️ SQL</text>
      </g>
      <g transform="translate(195, 44)">
        <rect width="75" height="32" class="pill-bg"/>
        <text x="37" y="21" class="pill-text" text-anchor="middle">🔀 Git</text>
      </g>
      <g transform="translate(280, 44)">
        <rect width="115" height="32" class="pill-bg"/>
        <text x="57" y="21" class="pill-text" text-anchor="middle">🚀 REST APIs</text>
      </g>
      <g transform="translate(405, 44)">
        <rect width="120" height="32" class="pill-bg"/>
        <text x="60" y="21" class="pill-text" text-anchor="middle">✨ UI/UX Design</text>
      </g>
    </g>

    <!-- Code Editor Window -->
    <g transform="translate(50, 420)">
      <rect width="680" height="270" rx="14" fill="#0c0719" stroke="rgba(155, 81, 224, 0.4)" stroke-width="1.5"/>
      <path d="M0 14 Q0 0 14 0 H666 Q680 0 680 14 V38 H0 Z" fill="#160e29"/>
      <circle cx="25" cy="19" r="5.5" fill="#ff5f56"/>
      <circle cx="42" cy="19" r="5.5" fill="#ffbd2e"/>
      <circle cx="59" cy="19" r="5.5" fill="#27c93f"/>
      <text x="340" y="24" font-family="'Fira Code', monospace" font-size="13" fill="#a090c0" text-anchor="middle">buildDreams.jsx</text>

      <g transform="translate(25, 65)">
        <text y="0" class="code-text"><tspan fill="#ff79c6">const</tspan> <tspan fill="#50fa7b">developer</tspan> = &#123;</text>
        <text y="28" class="code-text">&#160;&#160;name: <tspan fill="#f1fa8c">"{username}"</tspan>,</text>
        <text y="56" class="code-text">&#160;&#160;passion: <tspan fill="#f1fa8c">"Building slick interactive web apps"</tspan>,</text>
        <text y="84" class="code-text">&#160;&#160;currentGoal: <tspan fill="#bd93f9">"Mastering SVG animations &amp; AI"</tspan>,</text>
        <text y="112" class="code-text">&#160;&#160;buildDreams: () =&gt; &#123; <tspan fill="#ff79c6">return</tspan> <tspan fill="#f1fa8c">"Code. Learn. Build. Repeat."</tspan>; &#125;</text>
        <text y="140" class="code-text">&#125;;</text>
        <text y="172" class="code-text"><tspan fill="#ff79c6">export default</tspan> <tspan fill="#50fa7b">developer</tspan>;</text>
      </g>
    </g>

    <!-- RIGHT COLUMN: Character Art & Scanner -->
    <g transform="translate(760, 30)">
      <rect x="10" y="10" width="470" height="670" rx="20" fill="none" stroke="url(#text-grad)" stroke-width="2" opacity="0.6"/>

      <g clip-path="url(#char-clip)">
        <clipPath id="char-clip">
          <rect x="15" y="15" width="460" height="660" rx="18"/>
        </clipPath>
        <image href="{char_b64}" xlink:href="{char_b64}" x="15" y="15" width="460" height="660" preserveAspectRatio="xMidYMid slice" />
        <rect x="15" y="15" width="460" height="660" rx="18" fill="rgba(10, 5, 24, 0.15)"/>

        <g>
          <line x1="0" y1="0" x2="490" y2="0" stroke="#00f2fe" stroke-width="4" filter="url(#glow)">
            <animateTransform attributeName="transform" type="translate" from="0, 15" to="0, 675" dur="3.5s" repeatCount="indefinite"/>
          </line>
          <rect x="15" y="0" width="460" height="40" fill="url(#scan-grad)">
            <animateTransform attributeName="transform" type="translate" from="0, -15" to="0, 645" dur="3.5s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>
    </g>

    <rect width="1280" height="740" rx="24" ry="24" fill="none" stroke="#ff2a85" stroke-width="3" opacity="0.8"/>
  </g>
</svg>'''

with open(os.path.join(out_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(banner_svg_content)

print("Created valid XML banner.svg")

# 2. banner-light.svg (Light Mode)
banner_light_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <linearGradient id="bg-grad-light" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdfbfb" />
      <stop offset="50%" stop-color="#f4effa" />
      <stop offset="100%" stop-color="#ebedee" />
    </linearGradient>

    <linearGradient id="text-grad-light" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d63384"/>
      <stop offset="50%" stop-color="#6f42c1"/>
      <stop offset="100%" stop-color="#0d6efd"/>
    </linearGradient>

    <linearGradient id="scan-grad-light" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#d63384" stop-opacity="0"/>
      <stop offset="50%" stop-color="#6f42c1" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#d63384" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow-light" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <clipPath id="banner-clip-light">
      <rect x="0" y="0" width="1280" height="740" rx="24" ry="24" />
    </clipPath>
  </defs>

  <style>
    .terminal-text-light {{ font-family: 'Fira Code', 'Courier New', monospace; font-size: 16px; fill: #6f42c1; font-weight: 600; }}
    .name-title-light {{ font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 58px; font-weight: 900; letter-spacing: 4px; fill: url(#text-grad-light); }}
    .role-title-light {{ font-family: 'Fira Code', monospace; font-size: 22px; fill: #495057; font-weight: 600; }}
    .code-text-light {{ font-family: 'Consolas', monospace; font-size: 14px; fill: #212529; }}
    .pill-bg-light {{ fill: #ffffff; stroke: #d63384; stroke-width: 1.5; rx: 14; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06)); }}
    .pill-text-light {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; font-weight: 700; fill: #333333; }}

    @keyframes blink-light {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    .cursor-light {{ animation: blink-light 1s infinite; fill: #d63384; }}

    @keyframes neonPulseLight {{
      0%, 100% {{ opacity: 1; filter: drop-shadow(0 0 6px #d63384); }}
      50% {{ opacity: 0.6; filter: drop-shadow(0 0 2px #d63384); }}
    }}
    .neon-box-light {{ animation: neonPulseLight 2.5s infinite; }}
  </style>

  <g clip-path="url(#banner-clip-light)">
    <rect width="1280" height="740" fill="url(#bg-grad-light)" />

    <circle cx="150" cy="150" r="220" fill="#e0c3fc" opacity="0.4" filter="url(#glow-light)"/>
    <circle cx="1100" cy="550" r="280" fill="#8ec5fc" opacity="0.3" filter="url(#glow-light)"/>

    <path d="M0 100 H1280 M0 200 H1280 M0 300 H1280 M0 400 H1280 M0 500 H1280 M0 600 H1280 M0 700 H1280" stroke="#000000" stroke-opacity="0.04" stroke-width="1"/>
    <path d="M200 0 V740 M400 0 V740 M600 0 V740 M800 0 V740 M1000 0 V740 M1200 0 V740" stroke="#000000" stroke-opacity="0.04" stroke-width="1"/>

    <!-- Terminal Prompt Card -->
    <rect x="50" y="45" width="680" height="52" rx="12" fill="#ffffff" stroke="rgba(111, 66, 193, 0.3)" stroke-width="1.5"/>
    <circle cx="75" cy="71" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="71" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="71" r="6" fill="#27c93f"/>
    <text x="140" y="76" class="terminal-text-light">aldtor@github:~$ cat profile.md<tspan class="cursor-light">_</tspan></text>

    <!-- Name Header -->
    <text x="50" y="160" class="name-title-light">{display_name}</text>

    <!-- Role Titles -->
    <g transform="translate(50, 195)">
      <rect x="0" y="-22" width="460" height="32" rx="6" fill="rgba(214, 51, 132, 0.1)"/>
      <text x="12" y="0" class="role-title-light">⚡ Full Stack Developer &amp; Engineer</text>
    </g>

    <!-- Tagline Neon Box -->
    <g transform="translate(50, 245)" class="neon-box-light">
      <rect x="0" y="0" width="380" height="42" rx="8" fill="#ffffff" stroke="#d63384" stroke-width="2"/>
      <text x="190" y="27" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="16" fill="#d63384" text-anchor="middle" letter-spacing="3">✦ KEEP CODING • KEEP GROWING ✦</text>
    </g>

    <!-- Tech Stack Pills -->
    <g transform="translate(50, 315)">
      <g transform="translate(0, 0)">
        <rect width="105" height="32" class="pill-bg-light"/>
        <text x="52" y="21" class="pill-text-light" text-anchor="middle">⚡ JavaScript</text>
      </g>
      <g transform="translate(115, 0)">
        <rect width="105" height="32" class="pill-bg-light"/>
        <text x="52" y="21" class="pill-text-light" text-anchor="middle">🔷 TypeScript</text>
      </g>
      <g transform="translate(230, 0)">
        <rect width="90" height="32" class="pill-bg-light"/>
        <text x="45" y="21" class="pill-text-light" text-anchor="middle">⚛️ React</text>
      </g>
      <g transform="translate(330, 0)">
        <rect width="95" height="32" class="pill-bg-light"/>
        <text x="47" y="21" class="pill-text-light" text-anchor="middle">🟢 Node.js</text>
      </g>
      <g transform="translate(435, 0)">
        <rect width="90" height="32" class="pill-bg-light"/>
        <text x="45" y="21" class="pill-text-light" text-anchor="middle">🐍 Python</text>
      </g>
      <g transform="translate(0, 44)">
        <rect width="95" height="32" class="pill-bg-light"/>
        <text x="47" y="21" class="pill-text-light" text-anchor="middle">🎨 HTML/CSS</text>
      </g>
      <g transform="translate(105, 44)">
        <rect width="80" height="32" class="pill-bg-light"/>
        <text x="40" y="21" class="pill-text-light" text-anchor="middle">🗄️ SQL</text>
      </g>
      <g transform="translate(195, 44)">
        <rect width="75" height="32" class="pill-bg-light"/>
        <text x="37" y="21" class="pill-text-light" text-anchor="middle">🔀 Git</text>
      </g>
      <g transform="translate(280, 44)">
        <rect width="115" height="32" class="pill-bg-light"/>
        <text x="57" y="21" class="pill-text-light" text-anchor="middle">🚀 REST APIs</text>
      </g>
      <g transform="translate(405, 44)">
        <rect width="120" height="32" class="pill-bg-light"/>
        <text x="60" y="21" class="pill-text-light" text-anchor="middle">✨ UI/UX Design</text>
      </g>
    </g>

    <!-- Code Editor Window -->
    <g transform="translate(50, 420)">
      <rect width="680" height="270" rx="14" fill="#ffffff" stroke="rgba(111, 66, 193, 0.3)" stroke-width="1.5" filter="drop-shadow(0 4px 12px rgba(0,0,0,0.05))"/>
      <path d="M0 14 Q0 0 14 0 H666 Q680 0 680 14 V38 H0 Z" fill="#f1f3f5"/>
      <circle cx="25" cy="19" r="5.5" fill="#ff5f56"/>
      <circle cx="42" cy="19" r="5.5" fill="#ffbd2e"/>
      <circle cx="59" cy="19" r="5.5" fill="#27c93f"/>
      <text x="340" y="24" font-family="'Fira Code', monospace" font-size="13" fill="#495057" text-anchor="middle">buildDreams.jsx</text>

      <g transform="translate(25, 65)">
        <text y="0" class="code-text-light"><tspan fill="#d63384">const</tspan> <tspan fill="#0d6efd">developer</tspan> = &#123;</text>
        <text y="28" class="code-text-light">&#160;&#160;name: <tspan fill="#198754">"{username}"</tspan>,</text>
        <text y="56" class="code-text-light">&#160;&#160;passion: <tspan fill="#198754">"Building slick interactive web apps"</tspan>,</text>
        <text y="84" class="code-text-light">&#160;&#160;currentGoal: <tspan fill="#6f42c1">"Mastering SVG animations &amp; AI"</tspan>,</text>
        <text y="112" class="code-text-light">&#160;&#160;buildDreams: () =&gt; &#123; <tspan fill="#d63384">return</tspan> <tspan fill="#198754">"Code. Learn. Build. Repeat."</tspan>; &#125;</text>
        <text y="140" class="code-text-light">&#125;;</text>
        <text y="172" class="code-text-light"><tspan fill="#d63384">export default</tspan> <tspan fill="#0d6efd">developer</tspan>;</text>
      </g>
    </g>

    <!-- RIGHT COLUMN: Character Image -->
    <g transform="translate(760, 30)">
      <rect x="10" y="10" width="470" height="670" rx="20" fill="none" stroke="url(#text-grad-light)" stroke-width="2" opacity="0.6"/>

      <g clip-path="url(#char-clip-light)">
        <clipPath id="char-clip-light">
          <rect x="15" y="15" width="460" height="660" rx="18"/>
        </clipPath>
        <image href="{char_b64}" xlink:href="{char_b64}" x="15" y="15" width="460" height="660" preserveAspectRatio="xMidYMid slice" />

        <g>
          <line x1="0" y1="0" x2="490" y2="0" stroke="#6f42c1" stroke-width="4" filter="url(#glow-light)">
            <animateTransform attributeName="transform" type="translate" from="0, 15" to="0, 675" dur="3.5s" repeatCount="indefinite"/>
          </line>
          <rect x="15" y="0" width="460" height="40" fill="url(#scan-grad-light)">
            <animateTransform attributeName="transform" type="translate" from="0, -15" to="0, 645" dur="3.5s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>
    </g>

    <rect width="1280" height="740" rx="24" ry="24" fill="none" stroke="#6f42c1" stroke-width="3" opacity="0.8"/>
  </g>
</svg>'''

with open(os.path.join(out_dir, "banner-light.svg"), "w", encoding="utf-8") as f:
    f.write(banner_light_svg_content)

print("Created valid XML banner-light.svg")
