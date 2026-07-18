import os

out_dir = r"C:\Users\dell\.gemini\antigravity-ide\scratch\github-profile"

# 1. stats.svg (Exact replica of Megha Mittal's GitHub Stats card - 560x250)
stats_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 250" width="100%" height="auto">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14092b" />
      <stop offset="100%" stop-color="#0b0417" />
    </linearGradient>

    <linearGradient id="rank-ring" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff66cc" />
      <stop offset="100%" stop-color="#00f2fe" />
    </linearGradient>

    <filter id="glow-ring">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .card-border { fill: url(#card-bg); stroke: #ff66cc; stroke-width: 1.5; rx: 18; }
    .card-title { font-family: 'Segoe UI', sans-serif; font-size: 18px; font-weight: 800; fill: #ff66cc; }
    .stat-label { font-family: 'Segoe UI', sans-serif; font-size: 14px; font-weight: 600; fill: #e2d5f8; }
    .stat-val { font-family: 'Fira Code', monospace; font-size: 15px; font-weight: 800; fill: #00f2fe; text-anchor: end; }
    .rank-letter { font-family: 'Segoe UI', sans-serif; font-size: 44px; font-weight: 900; fill: #ffffff; text-anchor: middle; }
    .rank-sub { font-family: 'Fira Code', monospace; font-size: 11px; fill: #a090c0; text-anchor: middle; letter-spacing: 2px; }
  </style>

  <rect width="560" height="250" class="card-border" />

  <!-- Title -->
  <text x="25" y="38" class="card-title">🌸 DragoSatya~'s GitHub Stats</text>

  <!-- Left Stats List -->
  <g transform="translate(25, 75)">
    <!-- Star -->
    <g transform="translate(0, 0)">
      <text x="0" y="0" font-size="14" fill="#ffbd2e">★</text>
      <text x="20" y="0" class="stat-label">Total Stars Earned:</text>
      <text x="260" y="0" class="stat-val">50+</text>
    </g>

    <!-- Commits -->
    <g transform="translate(0, 32)">
      <text x="0" y="0" font-size="14" fill="#ff66cc">💻</text>
      <text x="20" y="0" class="stat-label">Total Commits:</text>
      <text x="260" y="0" class="stat-val">1,120+</text>
    </g>

    <!-- Repos -->
    <g transform="translate(0, 64)">
      <text x="0" y="0" font-size="14" fill="#00f2fe">📁</text>
      <text x="20" y="0" class="stat-label">Public Repos:</text>
      <text x="260" y="0" class="stat-val">36+</text>
    </g>

    <!-- Followers -->
    <g transform="translate(0, 96)">
      <text x="0" y="0" font-size="14" fill="#b55fe6">👥</text>
      <text x="20" y="0" class="stat-label">Followers:</text>
      <text x="260" y="0" class="stat-val">25+</text>
    </g>

    <!-- Real Apps Built -->
    <g transform="translate(0, 128)">
      <text x="0" y="0" font-size="14" fill="#00ffcc">⚡</text>
      <text x="20" y="0" class="stat-label">Real Apps Built:</text>
      <text x="260" y="0" class="stat-val">12+</text>
    </g>
  </g>

  <!-- Right Rank Circle -->
  <g transform="translate(440, 135)">
    <!-- Outer Glowing Ring -->
    <circle cx="0" cy="0" r="54" fill="none" stroke="rgba(255,102,204,0.2)" stroke-width="8"/>
    <circle cx="0" cy="0" r="54" fill="none" stroke="url(#rank-ring)" stroke-width="7" stroke-dasharray="310" stroke-dashoffset="35" filter="url(#glow-ring)"/>
    
    <text x="0" y="14" class="rank-letter">A+</text>
    <text x="0" y="74" class="rank-sub">RANK</text>
  </g>
</svg>'''

with open(os.path.join(out_dir, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(stats_svg_content)

print("Created exact stats.svg")


# 2. langs.svg (Exact replica of Megha Mittal's Top Languages card - 400x250)
langs_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 250" width="100%" height="auto">
  <defs>
    <linearGradient id="card-bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14092b" />
      <stop offset="100%" stop-color="#0b0417" />
    </linearGradient>
  </defs>

  <style>
    .card-border { fill: url(#card-bg2); stroke: #9b51e0; stroke-width: 1.5; rx: 18; }
    .card-title { font-family: 'Segoe UI', sans-serif; font-size: 17px; font-weight: 800; fill: #ffffff; }
    .lang-name { font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 700; fill: #ffffff; }
    .lang-pct { font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 700; fill: #ff66cc; text-anchor: end; }
  </style>

  <rect width="400" height="250" class="card-border" />

  <!-- Title -->
  <text x="25" y="38" class="card-title">📊 Top Languages</text>

  <!-- Multi-Color Progress Bar Stack -->
  <g transform="translate(25, 55)">
    <rect width="350" height="12" rx="6" fill="rgba(255,255,255,0.1)"/>
    <!-- Python 42% -->
    <rect x="0" y="0" width="147" height="12" rx="6" fill="#ff66cc"/>
    <!-- TypeScript 28% -->
    <rect x="147" y="0" width="98" height="12" fill="#00f2fe"/>
    <!-- C++ / IoT 18% -->
    <rect x="245" y="0" width="63" height="12" fill="#b55fe6"/>
    <!-- JavaScript 12% -->
    <rect x="308" y="0" width="42" height="12" rx="6" fill="#00ffcc"/>
  </g>

  <!-- Language Legend Rows -->
  <g transform="translate(25, 95)">
    <!-- Python -->
    <g transform="translate(0, 0)">
      <circle cx="6" cy="6" r="5" fill="#ff66cc"/>
      <text x="22" y="10" class="lang-name">Python</text>
      <text x="350" y="10" class="lang-pct">42.0%</text>
    </g>

    <!-- TypeScript -->
    <g transform="translate(0, 32)">
      <circle cx="6" cy="6" r="5" fill="#00f2fe"/>
      <text x="22" y="10" class="lang-name">TypeScript</text>
      <text x="350" y="10" class="lang-pct">28.0%</text>
    </g>

    <!-- C++ / Arduino -->
    <g transform="translate(0, 64)">
      <circle cx="6" cy="6" r="5" fill="#b55fe6"/>
      <text x="22" y="10" class="lang-name">C++ / IoT</text>
      <text x="350" y="10" class="lang-pct">18.0%</text>
    </g>

    <!-- JavaScript -->
    <g transform="translate(0, 96)">
      <circle cx="6" cy="6" r="5" fill="#00ffcc"/>
      <text x="22" y="10" class="lang-name">JavaScript</text>
      <text x="350" y="10" class="lang-pct">12.0%</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(out_dir, "langs.svg"), "w", encoding="utf-8") as f:
    f.write(langs_svg_content)

print("Created exact langs.svg")


# 3. streak.svg (Exact replica of Megha Mittal's GitHub Streak card - 960x180)
streak_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 180" width="100%" height="auto">
  <defs>
    <linearGradient id="card-bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14092b" />
      <stop offset="100%" stop-color="#0b0417" />
    </linearGradient>

    <linearGradient id="fire-ring" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff66cc" />
      <stop offset="100%" stop-color="#ff007f" />
    </linearGradient>

    <filter id="fire-glow">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .card-border { fill: url(#card-bg3); stroke: rgba(255, 102, 204, 0.4); stroke-width: 1.5; rx: 18; }
    .big-num { font-family: 'Fira Code', monospace; font-size: 38px; font-weight: 900; fill: #ff66cc; text-anchor: middle; }
    .label-title { font-family: 'Segoe UI', sans-serif; font-size: 14px; font-weight: 700; fill: #ffffff; text-anchor: middle; letter-spacing: 1px; }
    .sub-date { font-family: 'Segoe UI', sans-serif; font-size: 12px; fill: #a090c0; text-anchor: middle; }
    .divider-line { stroke: rgba(255, 102, 204, 0.25); stroke-width: 1.5; }
  </style>

  <rect width="960" height="180" class="card-border" />

  <!-- Vertical Dividers -->
  <line x1="320" y1="25" x2="320" y2="155" class="divider-line" />
  <line x1="640" y1="25" x2="640" y2="155" class="divider-line" />

  <!-- COLUMN 1: Total Contributions -->
  <g transform="translate(160, 60)">
    <text x="0" y="0" class="big-num">1,123</text>
    <text x="0" y="32" class="label-title">Total Contributions</text>
    <text x="0" y="52" class="sub-date">Aug 2022 - Present</text>
  </g>

  <!-- COLUMN 2: Current Streak (Center Fire Ring) -->
  <g transform="translate(480, 50)">
    <!-- Fire Ring Circle -->
    <circle cx="0" cy="-5" r="32" fill="none" stroke="url(#fire-ring)" stroke-width="4" filter="url(#fire-glow)"/>
    <text x="0" y="-14" font-size="16" text-anchor="middle">🔥</text>
    <text x="0" y="8" font-family="'Fira Code', monospace" font-size="20" font-weight="900" fill="#ffffff" text-anchor="middle">12</text>
    
    <text x="0" y="52" class="label-title">Current Streak</text>
    <text x="0" y="72" class="sub-date">Jul 18 - Active</text>
  </g>

  <!-- COLUMN 3: Longest Streak -->
  <g transform="translate(800, 60)">
    <text x="0" y="0" class="big-num">28</text>
    <text x="0" y="32" class="label-title">Longest Streak</text>
    <text x="0" y="52" class="sub-date">Jul 1 - Jul 28</text>
  </g>
</svg>'''

with open(os.path.join(out_dir, "streak.svg"), "w", encoding="utf-8") as f:
    f.write(streak_svg_content)

print("Created exact streak.svg")


# 4. README.md (Exact replica of Megha Mittal's GitHub Stats & Graphs section)
readme_md_content = f'''# 👋 Hi there, I'm Aldtor (DragoSatya~)!

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=22&pause=1000&color=FF66CC&center=true&vCenter=true&width=800&lines=Software+Engineer+%7C+Full+Stack+%26+Mobile;Android+Security+Researcher+%26+IoT+Developer;Creator+of+OFFLINE-PAY+%26+Sherlock+Android;The+rise+of+Kalki.+%E2%9C%A8" alt="Typing SVG" />
</p>

<p align="center">
  <img src="./banner.svg?v=15" alt="Aldtor Profile Banner" width="100%">
</p>

<br/>

<table border="0">
  <tr>
    <td width="35%" align="center" valign="top">
      <!-- Swinging Lanyard Badge -->
      <img src="./lanyard.svg?v=15" alt="Aldtor Lanyard Badge" width="100%" />
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

## 📊 GitHub Stats &amp; Graphs

<p align="center">
  <img src="./stats.svg?v=15" width="56%" alt="Aldtor GitHub Stats" />
  <img src="./langs.svg?v=15" width="41%" alt="Top Languages" />
</p>

<p align="center">
  <img src="./streak.svg?v=15" width="98%" alt="GitHub Streak Stats" />
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

print("Updated README.md v=15 with EXACT Megha Mittal Stats & Graphs section!")
