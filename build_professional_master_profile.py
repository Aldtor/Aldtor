import os

out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

with open(os.path.join(out_dir, "char_nobg_b64.txt"), "r") as f:
    char_b64 = f.read().strip()

with open(os.path.join(out_dir, "face_b64.txt"), "r") as f:
    face_b64 = f.read().strip()

print(f"Loaded char_b64 len={len(char_b64)}, face_b64 len={len(face_b64)}")

username = "Aldtor"
display_name = "DragoSatya~"

# ==============================================================================
# 1. banner.svg (Ultra-Professional Sleek Dark Mode Banner)
# ==============================================================================
banner_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <!-- Dark Background Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b0518" />
      <stop offset="50%" stop-color="#14092b" />
      <stop offset="100%" stop-color="#06020c" />
    </linearGradient>

    <!-- Animated Glowing Script Name Gradient -->
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

    <!-- Scanner Beam Gradient -->
    <linearGradient id="scan-line-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff00a0" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f2fe" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#ff00a0" stop-opacity="0"/>
    </linearGradient>

    <filter id="glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <clipPath id="banner-clip">
      <rect x="0" y="0" width="1280" height="740" rx="22" ry="22" />
    </clipPath>
  </defs>

  <style>
    .term-prompt {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: #00ffcc; font-weight: 700; }}
    .hi-title {{ font-family: 'Segoe UI', sans-serif; font-size: 30px; font-weight: 800; fill: #ffffff; }}
    .name-main {{ font-family: 'Segoe UI', 'Brush Script MT', cursive, sans-serif; font-size: 54px; font-weight: 900; fill: url(#name-grad); letter-spacing: 2px; filter: drop-shadow(0 0 10px rgba(255,102,204,0.4)); }}
    .role-sub {{ font-family: 'Segoe UI', sans-serif; font-size: 19px; font-weight: 700; fill: #d699ff; }}
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

    <!-- LEFT COLUMN -->
    <g transform="translate(45, 42)">
      <text x="0" y="0" class="term-prompt">aldtor@developer:~$ cat README.md<tspan class="blink-cursor">_</tspan></text>

      <text x="0" y="45" class="hi-title">Hi, I'm 👋</text>
      <text x="0" y="106" class="name-main">{display_name} ❗️</text>
      <text x="0" y="144" class="role-sub">⚡ Full Stack &amp; Mobile Systems Developer</text>

      <!-- Tagline Box -->
      <g transform="translate(0, 168)">
        <rect width="360" height="42" rx="10" fill="rgba(0, 242, 254, 0.08)" stroke="#00f2fe" stroke-width="1.5"/>
        <text x="18" y="26" class="quote-box-text">"The rise of Kalki. ✨"</text>
      </g>

      <!-- Horizontal Divider -->
      <line x1="0" y1="225" x2="450" y2="225" stroke="rgba(255,102,204,0.25)" stroke-width="1.5"/>

      <!-- Tech Stack -->
      <g transform="translate(0, 245)">
        <text x="0" y="0" class="section-head">⚡ Tech Stack &amp; Tools</text>
        <g transform="translate(0, 15)">
          <g transform="translate(0,0)"><rect width="70" height="26" class="pill-bg"/><text x="35" y="17" class="pill-txt" text-anchor="middle">Python</text></g>
          <g transform="translate(78,0)"><rect width="65" height="26" class="pill-bg"/><text x="32" y="17" class="pill-txt" text-anchor="middle">Android</text></g>
          <g transform="translate(151,0)"><rect width="90" height="26" class="pill-bg"/><text x="45" y="17" class="pill-txt" text-anchor="middle">JavaScript</text></g>
          <g transform="translate(249,0)"><rect width="90" height="26" class="pill-bg"/><text x="45" y="17" class="pill-txt" text-anchor="middle">TypeScript</text></g>
          <g transform="translate(347,0)"><rect width="70" height="26" class="pill-bg"/><text x="35" y="17" class="pill-txt" text-anchor="middle">React</text></g>
          
          <g transform="translate(0,34)"><rect width="75" height="26" class="pill-bg"/><text x="37" y="17" class="pill-txt" text-anchor="middle">Node.js</text></g>
          <g transform="translate(83,34)"><rect width="95" height="26" class="pill-bg"/><text x="47" y="17" class="pill-txt" text-anchor="middle">C++ / IoT</text></g>
          <g transform="translate(186,34)"><rect width="55" height="26" class="pill-bg"/><text x="27" y="17" class="pill-txt" text-anchor="middle">SQL</text></g>
          <g transform="translate(249,34)"><rect width="115" height="26" class="pill-bg"/><text x="57" y="17" class="pill-txt" text-anchor="middle">Mobile &amp; Web</text></g>
        </g>
      </g>

      <!-- About Me -->
      <g transform="translate(0, 348)">
        <text x="0" y="0" class="section-head">💖 About Me</text>
        <text x="0" y="24" class="about-line">📌 Building offline payment systems, mobile tools &amp; web experiences.</text>
        <text x="0" y="46" class="about-line">💡 Creator of OFFLINE-PAY &amp; Android diagnostic toolkits.</text>
        <text x="0" y="68" class="about-line">✨ Always innovating, always building real-world solutions.</text>
      </g>

      <!-- Stats Bar Row -->
      <g transform="translate(0, 452)">
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
      <g transform="translate(0, 542)">
        <text x="0" y="0" font-family="'Fira Code', monospace" font-size="12" fill="#a090c0">🐱 github.com/Aldtor &#160;•&#160; 📧 aldtor.in@gmail.com &#160;•&#160; 🟢 open to collaborate</text>
        <text x="0" y="24" font-family="'Segoe UI', sans-serif" font-size="13" font-style="italic" fill="#ff66cc">"Code is my art, Logic is my superpower. 💕"</text>
      </g>
    </g>

    <!-- RIGHT COLUMN -->
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

    <g transform="translate(950, 42)" class="neon-sign">
      <rect width="280" height="90" rx="14" fill="rgba(255, 0, 127, 0.08)" stroke="#ff007f" stroke-width="2"/>
      <text x="140" y="36" font-family="'Fira Code', monospace" font-weight="900" font-size="22" fill="#ff66cc" text-anchor="middle" letter-spacing="2">&lt;/&gt;</text>
      <text x="140" y="58" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#ffffff" text-anchor="middle" letter-spacing="2">KEEP CODING</text>
      <text x="140" y="74" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="13" fill="#ff66cc" text-anchor="middle" letter-spacing="2">KEEP GROWING</text>
    </g>

    <!-- Character Image Overlay -->
    <g transform="translate(780, 150)">
      <image href="{char_b64}" xlink:href="{char_b64}" x="0" y="0" width="460" height="570" preserveAspectRatio="xMidYMin meet" />
    </g>

    <!-- Full Banner 1280px Laser Hologram Scanner Line -->
    <g>
      <line x1="0" y1="0" x2="1280" y2="0" stroke="#00f2fe" stroke-width="3.5" opacity="0.85" filter="url(#glow-filter)">
        <animateTransform attributeName="transform" type="translate" from="0, 0" to="0, 740" dur="4s" repeatCount="indefinite"/>
      </line>
      <rect x="0" y="0" width="1280" height="45" fill="url(#scan-line-grad)">
        <animateTransform attributeName="transform" type="translate" from="0, -45" to="0, 695" dur="4s" repeatCount="indefinite"/>
      </rect>
    </g>

    <rect width="1280" height="740" rx="22" ry="22" fill="none" stroke="#9b51e0" stroke-width="3" opacity="0.8"/>
  </g>
</svg>'''

with open(os.path.join(out_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(banner_svg_content)

# ==============================================================================
# 2. README.md (Ultra Professional Developer Portfolio & Specs)
# ==============================================================================
readme_md_content = f'''# 👋 Hi there, I'm {username} ({display_name})!

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=22&pause=1000&color=FF66cc&center=true&vCenter=true&width=800&lines=Software+Engineer+%7C+Full+Stack+%26+Mobile;Android+Security+Researcher+%26+IoT+Developer;Creator+of+OFFLINE-PAY+%26+Sherlock+Android;The+rise+of+Kalki.+%E2%9C%A8" alt="Typing SVG" />
</p>

<p align="center">
  <img src="./banner.svg?v=14" alt="Aldtor Profile Banner" width="100%">
</p>

<br/>

<table border="0">
  <tr>
    <td width="35%" align="center" valign="top">
      <!-- Swinging Lanyard Badge -->
      <img src="./lanyard.svg?v=14" alt="Aldtor Lanyard Badge" width="100%" />
    </td>
    <td width="65%" valign="top">
      <h2>🚀 Featured Repositories &amp; Core Projects</h2>
      <table width="100%">
        <thead>
          <tr>
            <th align="left">Project &amp; Focus</th>
            <th align="center">💻 Stack</th>
            <th align="center">🔗 Link</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>💳 OFFLINE-PAY</b><br/><sub>Offline mesh transaction payment protocol</sub></td>
            <td align="center"><code>Python</code> <code>Android</code></td>
            <td align="center"><a href="https://github.com/Aldtor/OFFLINE-PAY"><b>View Code</b></a></td>
          </tr>
          <tr>
            <td><b>🔍 Sherlock Android</b><br/><sub>Android security analysis &amp; diagnostics</sub></td>
            <td align="center"><code>Kotlin</code> <code>Android</code></td>
            <td align="center"><a href="https://github.com/Aldtor/sherlock-android"><b>View Code</b></a></td>
          </tr>
          <tr>
            <td><b>📡 ESP8266 Toolkit</b><br/><sub>IoT microcontroller &amp; wireless firmware suite</sub></td>
            <td align="center"><code>C++</code> <code>Arduino</code></td>
            <td align="center"><a href="https://github.com/Aldtor/esp8266-toolkit"><b>View Code</b></a></td>
          </tr>
          <tr>
            <td><b>🌐 Aldtor Web App</b><br/><sub>Interactive high-performance developer portfolio</sub></td>
            <td align="center"><code>React</code> <code>TypeScript</code></td>
            <td align="center"><a href="https://aldtor.vercel.app"><b>Visit Live</b></a></td>
          </tr>
          <tr>
            <td><b>🎮 Calc Rush Showcase</b><br/><sub>Arcade math puzzle web application</sub></td>
            <td align="center"><code>JavaScript</code> <code>HTML5</code></td>
            <td align="center"><a href="https://github.com/Aldtor/calc-rush-showcase"><b>View Code</b></a></td>
          </tr>
        </tbody>
      </table>
      <br/>
      <p align="center">
        <i>"The rise of Kalki. • Ship > Perfect ✨"</i>
      </p>
    </td>
  </tr>
</table>

<br/>

## 🛠️ Technical Skillset Matrix

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> &#160;
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/> &#160;
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/> &#160;
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin"/> &#160;
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++"/> &#160;
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js"/> &#160;
  <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white" alt="Android"/> &#160;
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/> &#160;
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/> &#160;
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/> &#160;
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel"/>
</p>

<br/>

## 📊 GitHub Stats &amp; Performance

<p align="center">
  <img src="./stats.svg?v=14" width="31%" alt="Aldtor GitHub Stats" />
  <img src="./langs.svg?v=14" width="31%" alt="Top Languages" />
  <img src="./trophies.svg?v=14" width="31%" alt="Achievements &amp; Trophies" />
</p>

<br/>

## 📈 Contribution Graph ⚡

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Aldtor&theme=tokyonight&bg_color=0b0518&color=ff66cc&line=ff66cc&point=00f2fe&area=true&hide_border=false" width="100%" alt="Contribution Graph" />
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
  <a href="https://in.linkedin.com/in/aldtor"><img src="https://img.shields.io/badge/LINKEDIN-00f2fe?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a> &#160;
  <a href="https://aldtor.vercel.app"><img src="https://img.shields.io/badge/WEBSITE-00ffcc?style=for-the-badge&logo=vercel&logoColor=black" alt="Website" /></a>
</p>

<br/>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Aldtor&color=ff66cc&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile Views" />
</p>

<hr/>

<p align="center">
  <sub><i>★ Always learning, always building. ✨</i></sub>
</p>
'''

with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md_content)

print("Updated README.md v=13 with professional badge suite and typing SVG!")
