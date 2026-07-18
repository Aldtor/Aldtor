import os

out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

with open(os.path.join(out_dir, "char_b64.txt"), "r") as f:
    char_b64 = f.read().strip()

with open(os.path.join(out_dir, "face_b64.txt"), "r") as f:
    face_b64 = f.read().strip()

print(f"Loaded char_b64 len={len(char_b64)}, face_b64 len={len(face_b64)}")

username = "Aldtor"
display_name = "ALDTOR"

# 1. banner.svg (Dark Mode)
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
        <text y="28" class="code-text">&nbsp;&nbsp;name: <tspan fill="#f1fa8c">"{username}"</tspan>,</text>
        <text y="56" class="code-text">&nbsp;&nbsp;passion: <tspan fill="#f1fa8c">"Building slick interactive web apps"</tspan>,</text>
        <text y="84" class="code-text">&nbsp;&nbsp;currentGoal: <tspan fill="#bd93f9">"Mastering SVG animations &amp; AI"</tspan>,</text>
        <text y="112" class="code-text">&nbsp;&nbsp;buildDreams: () =&gt; &#123; <tspan fill="#ff79c6">return</tspan> <tspan fill="#f1fa8c">"Code. Learn. Build. Repeat."</tspan>; &#125;</text>
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
        <image href="{char_b64}" x="15" y="15" width="460" height="660" preserveAspectRatio="xMidYMid slice" />
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

print("Updated banner.svg for Aldtor")

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
        <text y="28" class="code-text-light">&nbsp;&nbsp;name: <tspan fill="#198754">"{username}"</tspan>,</text>
        <text y="56" class="code-text-light">&nbsp;&nbsp;passion: <tspan fill="#198754">"Building slick interactive web apps"</tspan>,</text>
        <text y="84" class="code-text-light">&nbsp;&nbsp;currentGoal: <tspan fill="#6f42c1">"Mastering SVG animations &amp; AI"</tspan>,</text>
        <text y="112" class="code-text-light">&nbsp;&nbsp;buildDreams: () =&gt; &#123; <tspan fill="#d63384">return</tspan> <tspan fill="#198754">"Code. Learn. Build. Repeat."</tspan>; &#125;</text>
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
        <image href="{char_b64}" x="15" y="15" width="460" height="660" preserveAspectRatio="xMidYMid slice" />

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

print("Updated banner-light.svg for Aldtor")

# 3. lanyard.svg (Swinging ID Badge with Pendulum Physics)
lanyard_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 450 680" width="100%" height="auto">
  <defs>
    <linearGradient id="strap-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff2a85" />
      <stop offset="50%" stop-color="#9b51e0" />
      <stop offset="100%" stop-color="#ff2a85" />
    </linearGradient>

    <linearGradient id="glass-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1f1137" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0a0518" stop-opacity="0.98" />
    </linearGradient>

    <linearGradient id="holo-shine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="45%" stop-color="#00f2fe" stop-opacity="0.0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="55%" stop-color="#ff00a0" stop-opacity="0.0"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <filter id="lanyard-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <style>
    .strap-text {{ font-family: 'Segoe UI', sans-serif; font-size: 11px; font-weight: 800; fill: #ffffff; letter-spacing: 2px; }}
    .badge-name {{ font-family: 'Segoe UI', sans-serif; font-size: 26px; font-weight: 900; fill: #ffffff; letter-spacing: 2px; }}
    .badge-handle {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #ff66cc; font-weight: 600; }}
    .badge-role {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; fill: #00f2fe; font-weight: 700; letter-spacing: 1px; }}
  </style>

  <circle cx="225" cy="0" r="14" fill="#333333"/>
  <circle cx="225" cy="0" r="7" fill="#111111"/>

  <g filter="url(#lanyard-shadow)">
    <animateTransform attributeName="transform" type="rotate" values="-4 225 0; 4 225 0; -4 225 0" dur="4.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>

    <path d="M 218 0 L 205 150 L 215 150 L 223 0 Z" fill="url(#strap-grad)"/>
    <path d="M 232 0 L 245 150 L 235 150 L 227 0 Z" fill="url(#strap-grad)"/>

    <text x="210" y="80" class="strap-text" transform="rotate(85 210 80)">DEVELOPER</text>
    <text x="240" y="80" class="strap-text" transform="rotate(-85 240 80)">{display_name}</text>

    <g transform="translate(225, 150)">
      <circle cx="0" cy="0" r="15" fill="none" stroke="#cccccc" stroke-width="4"/>
      <circle cx="0" cy="0" r="15" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.8"/>

      <rect x="-10" y="10" width="20" height="24" rx="4" fill="#999999"/>
      <rect x="-8" y="12" width="16" height="20" rx="3" fill="none" stroke="#ffffff" stroke-width="1.5"/>
    </g>

    <g transform="translate(75, 184)">
      <rect width="300" height="460" rx="20" fill="url(#glass-grad)" stroke="rgba(255, 42, 133, 0.6)" stroke-width="2"/>
      <rect x="125" y="12" width="50" height="12" rx="6" fill="#0c061a" stroke="#cccccc" stroke-width="2"/>

      <g transform="translate(150, 130)">
        <circle cx="0" cy="0" r="64" fill="none" stroke="url(#strap-grad)" stroke-width="4"/>
        <circle cx="0" cy="0" r="60" fill="#0d071b"/>

        <clipPath id="avatar-clip">
          <circle cx="0" cy="0" r="58"/>
        </clipPath>
        <image href="{face_b64}" x="-58" y="-58" width="116" height="116" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
      </g>

      <text x="150" y="232" class="badge-name" text-anchor="middle">{display_name}</text>
      <text x="150" y="258" class="badge-handle" text-anchor="middle">@{username}</text>
      <text x="150" y="284" class="badge-role" text-anchor="middle">FULL STACK DEVELOPER</text>

      <line x1="40" y1="308" x2="260" y2="308" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>

      <g transform="translate(45, 332)">
        <text font-family="'Segoe UI', sans-serif" font-size="11" fill="#a090c0">STATUS</text>
        <text y="18" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#00ffcc">● ACTIVE / BUILDING</text>

        <text x="130" font-family="'Segoe UI', sans-serif" font-size="11" fill="#a090c0">LOCATION</text>
        <text x="130" y="18" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" fill="#ffffff">GLOBAL 🌍</text>
      </g>

      <g transform="translate(50, 395)">
        <path d="M0 0 V30 M4 0 V30 M7 0 V30 M12 0 V30 M15 0 V30 M22 0 V30 M28 0 V30 M31 0 V30 M38 0 V30 M42 0 V30 M48 0 V30 M55 0 V30 M60 0 V30 M65 0 V30 M72 0 V30 M78 0 V30 M84 0 V30 M90 0 V30 M98 0 V30 M104 0 V30 M110 0 V30 M118 0 V30 M124 0 V30 M130 0 V30 M138 0 V30 M144 0 V30 M152 0 V30 M160 0 V30 M168 0 V30 M175 0 V30 M182 0 V30 M190 0 V30 M196 0 V30 M200 0 V30" stroke="#ffffff" stroke-width="2.5"/>
        <text x="100" y="44" font-family="'Fira Code', monospace" font-size="10" fill="#a090c0" text-anchor="middle">ID: ALDTOR-DEV-2026</text>
      </g>

      <rect width="300" height="460" rx="20" fill="url(#holo-shine)" pointer-events="none">
        <animateTransform attributeName="transform" type="translate" from="-300, -300" to="300, 300" dur="4s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(out_dir, "lanyard.svg"), "w", encoding="utf-8") as f:
    f.write(lanyard_svg_content)

print("Updated lanyard.svg for Aldtor")

# 4. stats.svg
stats_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 220" width="100%" height="auto">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140b29"/>
      <stop offset="100%" stop-color="#0a0518"/>
    </linearGradient>
    <linearGradient id="ring-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff2a85"/>
      <stop offset="100%" stop-color="#00f2fe"/>
    </linearGradient>
    <filter id="glow-stat">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .card-title {{ font-family: 'Segoe UI', sans-serif; font-size: 18px; font-weight: 800; fill: #ff4da6; letter-spacing: 1px; }}
    .stat-label {{ font-family: 'Segoe UI', sans-serif; font-size: 13px; fill: #a090c0; font-weight: 600; }}
    .stat-val {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: #ffffff; font-weight: 700; }}
    .rank-text {{ font-family: 'Segoe UI', sans-serif; font-size: 32px; font-weight: 900; fill: #ffffff; }}

    @keyframes ringSpin {{
      0% {{ stroke-dashoffset: 280; }}
      50% {{ stroke-dashoffset: 40; }}
      100% {{ stroke-dashoffset: 280; }}
    }}
    .progress-ring {{
      stroke-dasharray: 280;
      animation: ringSpin 4s ease-in-out infinite;
    }}
  </style>

  <rect width="480" height="220" rx="16" fill="url(#card-bg)" stroke="rgba(255,42,133,0.3)" stroke-width="1.5"/>

  <text x="30" y="40" class="card-title">⚡ {display_name}'S GITHUB STATS</text>
  <line x1="30" y1="52" x2="450" y2="52" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>

  <g transform="translate(85, 135)">
    <circle cx="0" cy="0" r="45" fill="none" stroke="#251545" stroke-width="8"/>
    <circle cx="0" cy="0" r="45" fill="none" stroke="url(#ring-grad)" stroke-width="8" stroke-linecap="round" class="progress-ring" transform="rotate(-90)"/>
    <text x="0" y="10" class="rank-text" text-anchor="middle" filter="url(#glow-stat)">S+</text>
  </g>

  <g transform="translate(180, 80)">
    <g transform="translate(0, 0)">
      <text class="stat-label">Total Commits (2026):</text>
      <text x="250" class="stat-val" text-anchor="end">1,480+</text>
      <rect y="10" width="250" height="6" rx="3" fill="#251545"/>
      <rect y="10" width="210" height="6" rx="3" fill="#ff2a85"/>
    </g>
    <g transform="translate(0, 32)">
      <text class="stat-label">Pull Requests:</text>
      <text x="250" class="stat-val" text-anchor="end">142</text>
      <rect y="10" width="250" height="6" rx="3" fill="#251545"/>
      <rect y="10" width="185" height="6" rx="3" fill="#9b51e0"/>
    </g>
    <g transform="translate(0, 64)">
      <text class="stat-label">Issues Closed:</text>
      <text x="250" class="stat-val" text-anchor="end">88</text>
      <rect y="10" width="250" height="6" rx="3" fill="#251545"/>
      <rect y="10" width="150" height="6" rx="3" fill="#00f2fe"/>
    </g>
    <g transform="translate(0, 96)">
      <text class="stat-label">Total Stars Earned:</text>
      <text x="250" class="stat-val" text-anchor="end">320+</text>
      <rect y="10" width="250" height="6" rx="3" fill="#251545"/>
      <rect y="10" width="230" height="6" rx="3" fill="#38ef7d"/>
    </g>
  </g>
</svg>'''

with open(os.path.join(out_dir, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(stats_svg_content)

print("Updated stats.svg for Aldtor")

# 7. README.md
readme_md_content = f'''# 👋 Hi there, I'm {username}!

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./banner.svg?v=1">
    <source media="(prefers-color-scheme: light)" srcset="./banner-light.svg?v=1">
    <img alt="{username} Profile Banner" src="./banner.svg?v=1" width="100%">
  </picture>
</p>

<br/>

<table border="0">
  <tr>
    <td width="40%" align="center" valign="top">
      <img src="./lanyard.svg?v=1" alt="{username} Lanyard Badge" width="100%" opacity="1" />
    </td>
    <td width="60%" valign="top">
      <h2>✨ About Me</h2>
      <p>
        I'm a passionate <b>Full Stack Developer</b> crafting sleek, high-performance web applications and interactive digital experiences.
      </p>
      <ul>
        <li>🔭 <b>Building:</b> Next-gen web apps with React, TypeScript &amp; SVG animations</li>
        <li>💻 <b>Core Tech:</b> JavaScript, TypeScript, React, Node.js, Python, SQL, Git</li>
        <li>🌱 <b>Learning:</b> Advanced AI prompts, WebGL &amp; SVG physics modeling</li>
        <li>⚡ <b>Fun Fact:</b> Powered by coffee, clean code &amp; continuous learning!</li>
      </ul>
      <br/>
      <h3>📫 Connect With Me</h3>
      <p>
        <a href="https://github.com/Aldtor"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
        <a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
      </p>
      <br/>
      <img src="https://komarev.com/ghpvc/?username=Aldtor&color=ff2a85&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile Views" />
    </td>
  </tr>
</table>

<br/>

## 📊 Performance & Statistics

<p align="center">
  <img src="./stats.svg?v=1" width="31%" alt="Stats Card" />
  <img src="./langs.svg?v=1" width="31%" alt="Languages Card" />
  <img src="./trophies.svg?v=1" width="31%" alt="Trophies Card" />
</p>

<br/>

## 🚀 Featured Projects

| Project | Description | Tech Stack | Link |
| :--- | :--- | :--- | :---: |
| **⚡ DreamCraft UI** | Interactive SVG & CSS animation components library | React, SVG, Tailwind | [View Code](https://github.com/Aldtor) |
| **🌐 DevFlow Hub** | Developer workflow & task management web application | TypeScript, Node.js | [View Code](https://github.com/Aldtor) |
| **🐍 Contribution Snake** | Custom colored snake animation generated via GitHub Actions | YAML, SVG, Canvas | [View Code](https://github.com/Aldtor/Aldtor) |

<br/>

## 🐍 Contribution Graph & Snake Game

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake.svg">
    <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake.svg" width="100%">
  </picture>
</p>

<hr/>

<p align="center">
  <sub><i>Designed with ❤️ for {username} • Keep Coding, Keep Growing!</i></sub>
</p>
'''

with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md_content)

print("Updated README.md for Aldtor")
