import os

out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

with open(os.path.join(out_dir, "char_nobg_b64.txt"), "r") as f:
    char_b64 = f.read().strip()

with open(os.path.join(out_dir, "face_b64.txt"), "r") as f:
    face_b64 = f.read().strip()

print(f"Loaded char_b64 len={len(char_b64)}, face_b64 len={len(face_b64)}")

username = "Aldtor"
display_name = "Aldtor"

# 1. banner.svg (Full Body Character - Top Hair Not Cut Off!)
banner_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110722" />
      <stop offset="50%" stop-color="#1c0d38" />
      <stop offset="100%" stop-color="#0a0314" />
    </linearGradient>

    <!-- Animated Cursive Name Gradient -->
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff66cc">
        <animate attributeName="stop-color" values="#ff66cc; #b55fe6; #00f2fe; #ff66cc" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#b55fe6">
        <animate attributeName="stop-color" values="#b55fe6; #00f2fe; #ff66cc; #b55fe6" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe; #ff66cc; #b55fe6; #00f2fe" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Hologram Scanner Beam Gradient -->
    <linearGradient id="scan-line-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff00a0" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ff00a0" stop-opacity="0"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <clipPath id="banner-clip">
      <rect x="0" y="0" width="1280" height="740" rx="22" ry="22" />
    </clipPath>
  </defs>

  <style>
    .term-prompt {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: #00ffcc; }}
    .hi-title {{ font-family: 'Segoe UI', sans-serif; font-size: 32px; font-weight: 800; fill: #ffffff; }}
    .name-main {{ font-family: 'Segoe UI', 'Brush Script MT', cursive, sans-serif; font-size: 58px; font-weight: 900; fill: url(#name-grad); letter-spacing: 2px; filter: drop-shadow(0 0 10px rgba(255,102,204,0.4)); }}
    .role-sub {{ font-family: 'Segoe UI', sans-serif; font-size: 20px; font-weight: 700; fill: #d699ff; }}
    .quote-box-text {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #ff99dd; font-style: italic; }}
    .section-head {{ font-family: 'Segoe UI', sans-serif; font-size: 15px; font-weight: 800; fill: #ffffff; letter-spacing: 1px; }}
    .about-line {{ font-family: 'Segoe UI', sans-serif; font-size: 14px; fill: #e2d5f8; }}
    .stat-num {{ font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 800; fill: #ff66cc; }}
    .stat-lbl {{ font-family: 'Segoe UI', sans-serif; font-size: 12px; fill: #a090c0; }}
    .code-editor-text {{ font-family: 'Consolas', monospace; font-size: 13px; fill: #f8f8f2; }}
    .pill-bg {{ fill: rgba(255, 255, 255, 0.08); stroke: rgba(181, 95, 230, 0.5); stroke-width: 1.5; rx: 12; }}
    .pill-txt {{ font-family: 'Segoe UI', sans-serif; font-size: 12px; font-weight: 700; fill: #ffffff; }}

    @keyframes cursorBlink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .blink-cursor {{ animation: cursorBlink 1s infinite; fill: #00ffcc; }}

    @keyframes neonBoxPulse {{ 0%, 100% {{ opacity: 1; filter: drop-shadow(0 0 8px #ff007f); }} 50% {{ opacity: 0.5; filter: drop-shadow(0 0 2px #ff007f); }} }}
    .neon-sign {{ animation: neonBoxPulse 2.5s infinite; }}
  </style>

  <g clip-path="url(#banner-clip)">
    <!-- Base Background -->
    <rect width="1280" height="740" fill="url(#bg-grad)" stroke="#9b51e0" stroke-width="2" rx="22"/>

    <!-- Ambient Glowing Orbs -->
    <circle cx="180" cy="180" r="220" fill="#9b51e0" opacity="0.14" filter="url(#glow-filter)"/>
    <circle cx="1100" cy="550" r="260" fill="#ff2a85" opacity="0.12" filter="url(#glow-filter)"/>
    <circle cx="640" cy="370" r="200" fill="#00f2fe" opacity="0.08" filter="url(#glow-filter)"/>

    <!-- Floating Sparkles & Hearts -->
    <text x="680" y="310" font-size="20" fill="#ff66cc" opacity="0.8">✦</text>
    <text x="1200" y="190" font-size="18" fill="#00f2fe" opacity="0.7">✨</text>
    <text x="740" y="680" font-size="16" fill="#ff4da6" opacity="0.8">💕</text>

    <!-- LEFT COLUMN: Content (x=45 to x=540) -->
    <g transform="translate(45, 42)">
      <!-- Terminal Prompt -->
      <text x="0" y="0" class="term-prompt">aldtor@developer:~$ cat README.md<tspan class="blink-cursor">_</tspan></text>

      <!-- Hi Greeting -->
      <text x="0" y="45" class="hi-title">Hi, I'm 👋</text>

      <!-- Large Cursive Name -->
      <text x="0" y="106" class="name-main">{display_name} 💕</text>

      <!-- Subtitle Role -->
      <text x="0" y="144" class="role-sub">⚡ Full Stack Developer &amp; Software Engineer</text>

      <!-- Quote Box -->
      <g transform="translate(0, 168)">
        <rect width="360" height="42" rx="10" fill="rgba(255, 102, 204, 0.08)" stroke="#ff66cc" stroke-width="1.5"/>
        <text x="18" y="26" class="quote-box-text">"I don't watch anime, I code anime. ✨"</text>
      </g>

      <!-- Tech I Know -->
      <g transform="translate(0, 238)">
        <text x="0" y="0" class="section-head">⚡ Tech I Know</text>
        <g transform="translate(0, 15)">
          <g transform="translate(0,0)"><rect width="65" height="26" class="pill-bg"/><text x="32" y="17" class="pill-txt" text-anchor="middle">HTML</text></g>
          <g transform="translate(73,0)"><rect width="55" height="26" class="pill-bg"/><text x="27" y="17" class="pill-txt" text-anchor="middle">CSS</text></g>
          <g transform="translate(136,0)"><rect width="90" height="26" class="pill-bg"/><text x="45" y="17" class="pill-txt" text-anchor="middle">JavaScript</text></g>
          <g transform="translate(234,0)"><rect width="90" height="26" class="pill-bg"/><text x="45" y="17" class="pill-txt" text-anchor="middle">TypeScript</text></g>
          <g transform="translate(332,0)"><rect width="70" height="26" class="pill-bg"/><text x="35" y="17" class="pill-txt" text-anchor="middle">React</text></g>
          
          <g transform="translate(0,34)"><rect width="75" height="26" class="pill-bg"/><text x="37" y="17" class="pill-txt" text-anchor="middle">Node.js</text></g>
          <g transform="translate(83,34)"><rect width="70" height="26" class="pill-bg"/><text x="35" y="17" class="pill-txt" text-anchor="middle">Python</text></g>
          <g transform="translate(160,34)"><rect width="55" height="26" class="pill-bg"/><text x="27" y="17" class="pill-txt" text-anchor="middle">SQL</text></g>
          <g transform="translate(223,34)"><rect width="115" height="26" class="pill-bg"/><text x="57" y="17" class="pill-txt" text-anchor="middle">Responsive UI</text></g>
        </g>
      </g>

      <!-- About Me -->
      <g transform="translate(0, 342)">
        <text x="0" y="0" class="section-head">💖 About Me</text>
        <text x="0" y="24" class="about-line">📌 I build responsive, user-friendly and impactful web experiences.</text>
        <text x="0" y="46" class="about-line">💡 Always learning, always building.</text>
        <text x="0" y="68" class="about-line">✨ Turning ideas into real-world solutions.</text>
      </g>

      <!-- Stats Bar Row -->
      <g transform="translate(0, 448)">
        <rect width="450" height="65" rx="14" fill="rgba(15, 7, 30, 0.85)" stroke="rgba(255, 102, 204, 0.3)" stroke-width="1.5"/>
        
        <g transform="translate(35, 23)">
          <text x="0" y="0" class="stat-num">36+</text>
          <text x="0" y="18" class="stat-lbl">Repos</text>
        </g>
        <g transform="translate(140, 23)">
          <text x="0" y="0" class="stat-num">1,120+</text>
          <text x="0" y="18" class="stat-lbl">Commits</text>
        </g>
        <g transform="translate(260, 23)">
          <text x="0" y="0" class="stat-num">50+</text>
          <text x="0" y="18" class="stat-lbl">Stars</text>
        </g>
        <g transform="translate(365, 23)">
          <text x="0" y="0" class="stat-num">25+</text>
          <text x="0" y="18" class="stat-lbl">Followers</text>
        </g>
      </g>

      <!-- Footer Bar -->
      <g transform="translate(0, 538)">
        <text x="0" y="0" font-family="'Fira Code', monospace" font-size="12" fill="#a090c0">🐱 github.com/Aldtor &#160;•&#160; 📧 aldtor.in@gmail.com &#160;•&#160; 🟢 open to collaborate</text>
        <text x="0" y="24" font-family="'Segoe UI', sans-serif" font-size="13" font-style="italic" fill="#ff66cc">"Code is my art, Logic is my superpower. 💕"</text>
      </g>
    </g>

    <!-- RIGHT COLUMN: Dreams.jsx Snippet + Neon Box + Full Body Character Art (x=530 to x=1240) -->
    <!-- dreams.jsx Code Card -->
    <g transform="translate(530, 42)">
      <rect width="400" height="210" rx="14" fill="#0c061a" stroke="rgba(181, 95, 230, 0.4)" stroke-width="1.5"/>
      <path d="M0 12 Q0 0 12 0 H388 Q400 0 400 12 V28 H0 Z" fill="#170c33"/>
      <circle cx="16" cy="14" r="4" fill="#ff5f56"/>
      <circle cx="28" cy="14" r="4" fill="#ffbd2e"/>
      <circle cx="40" cy="14" r="4" fill="#27c93f"/>
      <text x="200" y="18" font-family="'Fira Code', monospace" font-size="11" fill="#a090c0" text-anchor="middle">dreams.jsx</text>

      <g transform="translate(18, 48)">
        <text y="0" class="code-editor-text"><tspan fill="#ff79c6">function</tspan> <tspan fill="#50fa7b">buildDreams</tspan>() &#123;</text>
        <text y="18" class="code-editor-text">&#160;&#160;<tspan fill="#ff79c6">return</tspan> (</text>
        <text y="36" class="code-editor-text">&#160;&#160;&#160;&#160;&lt;<tspan fill="#8be9fd">div</tspan> className=<tspan fill="#f1fa8c">"dreams"</tspan>&gt;</text>
        <text y="54" class="code-editor-text">&#160;&#160;&#160;&#160;&#160;&#160;&lt;<tspan fill="#ffb86c">Code</tspan> /&gt;</text>
        <text y="72" class="code-editor-text">&#160;&#160;&#160;&#160;&#160;&#160;&lt;<tspan fill="#ffb86c">Coffee</tspan> /&gt;</text>
        <text y="90" class="code-editor-text">&#160;&#160;&#160;&#160;&#160;&#160;&lt;<tspan fill="#ffb86c">Repeat</tspan> /&gt;</text>
        <text y="108" class="code-editor-text">&#160;&#160;&#160;&#160;&#160;&#160;&lt;<tspan fill="#ffb86c">Success</tspan> /&gt;</text>
        <text y="126" class="code-editor-text">&#160;&#160;&#160;&#160;&lt;/<tspan fill="#8be9fd">div</tspan>&gt;</text>
        <text y="144" class="code-editor-text">&#160;&#160;);</text>
        <text y="160" class="code-editor-text">&#125; <tspan fill="#6272a4">// export default</tspan></text>
      </g>
    </g>

    <!-- Neon Tagline Box Top Right -->
    <g transform="translate(950, 42)" class="neon-sign">
      <rect width="280" height="90" rx="14" fill="rgba(255, 0, 127, 0.08)" stroke="#ff007f" stroke-width="2"/>
      <text x="140" y="36" font-family="'Fira Code', monospace" font-weight="900" font-size="22" fill="#ff66cc" text-anchor="middle" letter-spacing="2">&lt;/&gt;</text>
      <text x="140" y="58" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#ffffff" text-anchor="middle" letter-spacing="2">KEEP CODING</text>
      <text x="140" y="74" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#ff66cc" text-anchor="middle" letter-spacing="2">KEEP GROWING</text>
    </g>

    <!-- Transparent Character Full Body Image Overlay (preserveAspectRatio="xMidYMin meet" so upper hair is 100% visible!) -->
    <g transform="translate(760, 140)">
      <image href="{char_b64}" xlink:href="{char_b64}" x="0" y="0" width="480" height="580" preserveAspectRatio="xMidYMin meet" />

      <!-- Continuous Full-Width Horizontal Scanner Line Sweeping Top to Bottom -->
      <g>
        <line x1="0" y1="0" x2="480" y2="0" stroke="#00f2fe" stroke-width="4" filter="url(#glow-filter)">
          <animateTransform attributeName="transform" type="translate" from="0, 0" to="0, 580" dur="3.5s" repeatCount="indefinite"/>
        </line>
        <rect x="0" y="0" width="480" height="40" fill="url(#scan-line-grad)">
          <animateTransform attributeName="transform" type="translate" from="0, -40" to="0, 540" dur="3.5s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>

    <!-- Outer Border -->
    <rect width="1280" height="740" rx="22" ry="22" fill="none" stroke="#9b51e0" stroke-width="3" opacity="0.8"/>
  </g>
</svg>'''

with open(os.path.join(out_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(banner_svg_content)

print("Created full body banner.svg with no hair cut off!")

# 2. lanyard.svg (With NEW attached cosmic alien avatar image!)
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
    <text x="240" y="80" class="strap-text" transform="rotate(-85 240 80)">{display_name.upper()}</text>

    <g transform="translate(225, 150)">
      <circle cx="0" cy="0" r="15" fill="none" stroke="#cccccc" stroke-width="4"/>
      <circle cx="0" cy="0" r="15" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.8"/>

      <rect x="-10" y="10" width="20" height="24" rx="4" fill="#999999"/>
      <rect x="-8" y="12" width="16" height="20" rx="3" fill="none" stroke="#ffffff" stroke-width="1.5"/>
    </g>

    <g transform="translate(75, 184)">
      <rect width="300" height="460" rx="20" fill="url(#glass-grad)" stroke="rgba(255, 42, 133, 0.6)" stroke-width="2"/>
      <rect x="125" y="12" width="50" height="12" rx="6" fill="#0c061a" stroke="#cccccc" stroke-width="2"/>

      <!-- Glowing Avatar Frame with NEW attached Cosmic Alien avatar image -->
      <g transform="translate(150, 130)">
        <circle cx="0" cy="0" r="64" fill="none" stroke="url(#strap-grad)" stroke-width="4"/>
        <circle cx="0" cy="0" r="60" fill="#0d071b"/>

        <clipPath id="avatar-clip">
          <circle cx="0" cy="0" r="58"/>
        </clipPath>
        <image href="{face_b64}" xlink:href="{face_b64}" x="-58" y="-58" width="116" height="116" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
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

# 3. README.md (Bump version query to v=9 for cache purge)
readme_md_content = f'''# 👋 Hi there, I'm {username}!

<p align="center">
  <img src="./banner.svg?v=9" alt="Aldtor Profile Banner" width="100%">
</p>

<br/>

<table border="0">
  <tr>
    <td width="36%" align="center" valign="top">
      <!-- Swinging Lanyard Badge -->
      <img src="./lanyard.svg?v=9" alt="Aldtor Lanyard Badge" width="100%" />
    </td>
    <td width="64%" valign="top">
      <h2>🌸 My Anime &amp; Web Creations</h2>
      <table width="100%">
        <thead>
          <tr>
            <th align="left">Project</th>
            <th align="center">💻 Tech</th>
            <th align="center">★ Stars</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>⚡ Naruto — Sage Mode</b></td>
            <td align="center"><code>HTML</code> <code>CSS</code> <code>JS</code></td>
            <td align="center">25</td>
          </tr>
          <tr>
            <td><b>⚔️ Zoro — King of Hell</b></td>
            <td align="center"><code>HTML</code> <code>CSS</code> <code>JS</code></td>
            <td align="center">14</td>
          </tr>
          <tr>
            <td><b>🔥 Demon Slayer — Web App</b></td>
            <td align="center"><code>HTML</code> <code>CSS</code> <code>JS</code></td>
            <td align="center">12</td>
          </tr>
          <tr>
            <td><b>👁️ JJK — Sukuna Domain</b></td>
            <td align="center"><code>HTML</code> <code>CSS</code> <code>JS</code></td>
            <td align="center">10</td>
          </tr>
          <tr>
            <td><b>🌊 One Piece 3D Experience</b></td>
            <td align="center"><code>TypeScript</code> <code>Three.js</code></td>
            <td align="center">8</td>
          </tr>
        </tbody>
      </table>
      <br/>
      <p align="center">
        <i>"I don't watch anime, I code anime. 💕"</i>
      </p>
    </td>
  </tr>
</table>

<br/>

## 📊 GitHub Stats &amp; Performance

<p align="center">
  <img src="./stats.svg?v=9" width="31%" alt="Aldtor GitHub Stats" />
  <img src="./langs.svg?v=9" width="31%" alt="Top Languages" />
  <img src="./trophies.svg?v=9" width="31%" alt="Achievements &amp; Trophies" />
</p>

<br/>

## 📈 Contribution Graph 💕

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Aldtor&theme=tokyonight&bg_color=110722&color=ff66cc&line=ff66cc&point=00f2fe&area=true&hide_border=false" width="100%" alt="Contribution Graph" />
</p>

<br/>

## 🐍 Watch the snake eat my contributions

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake.svg">
    <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/Aldtor/Aldtor/output/github-contribution-grid-snake.svg" width="100%">
  </picture>
</p>

<br/>

## 🚩 Let's Connect

<p align="center">
  <a href="mailto:aldtor.in@gmail.com"><img src="https://img.shields.io/badge/M_EMAIL-ff66cc?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> &#160;
  <a href="https://github.com/Aldtor"><img src="https://img.shields.io/badge/GH_GITHUB-9b51e0?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a> &#160;
  <a href="https://in.linkedin.com/in/aldtor"><img src="https://img.shields.io/badge/LINKEDIN-00f2fe?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
</p>

<br/>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Aldtor&color=ff66cc&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile Views" />
</p>

<hr/>

<p align="center">
  <sub><i>★ Always learning, always building. 💕</i></sub>
</p>
'''

with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md_content)

print("Updated README.md v=9 and lanyard.svg with new avatar image!")
