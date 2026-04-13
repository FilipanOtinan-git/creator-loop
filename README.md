# creator-loop
<p align="center">
  <h1 align="center">CreatorLoop 🔁</h1>
  <p align="center">
    <strong>Automated YouTube scouting & CRM synchronization for Indie Comic outreach.</strong>
  </p>
  <p align="center">
    <a href="https://github.com/YOUR_USERNAME/creator-loop/issues">
      <img src="https://img.shields.io/github/issues/YOUR_USERNAME/creator-loop?style=flat-square" alt="Issues">
    </a>
    <a href="https://github.com/YOUR_USERNAME/creator-loop/network/members">
      <img src="https://img.shields.io/github/forks/YOUR_USERNAME/creator-loop?style=flat-square" alt="Forks">
    </a>
    <a href="https://github.com/YOUR_USERNAME/creator-loop/stargazers">
      <img src="https://img.shields.io/github/stars/YOUR_USERNAME/creator-loop?style=flat-square" alt="Stars">
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License">
    </a>
    <a href="https://www.python.org/downloads/">
      <img src="https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square" alt="Python 3.8+">
    </a>
  </p>
</p>

---

## 📖 Overview

**CreatorLoop** is a lightweight, Python-based CLI workflow designed to help independent creators, artists, and publishers find high-quality YouTube influencers for marketing campaigns. 

Instead of manually searching YouTube for hours, CreatorLoop automates the process: it "scouts" specific niches using boolean search logic, filters out corporate noise (e.g., Marvel/DC), identifies high-signal targets (e.g., reviewers, Kickstarter advocates), and pipes the vetted leads directly into your Google Sheets CRM.

## ✨ Key Features

- **🎯 Precision Scouting:** Built-in boolean logic to find niche creators (e.g., `"Indie Comics + Kickstarter -Marvel"`).
- **🧹 Smart Filtering:** Python-driven logic engine that evaluates creator descriptions and keywords to isolate high-value collaborators.
- **☁️ Seamless CRM Sync:** Native integration instructions for piping CSV output directly to Google Sheets via CLI.
- **🌍 Region Targeting:** Geolocate your influencer searches (e.g., strictly US or UK-based channels).
- **⚡ Zero API Costs:** Leverages headless CLI tools to bypass expensive third-party influencer platforms.

---

## 🏗️ Architecture

CreatorLoop operates on a simple 3-step pipeline:

1. **`scout.py` (The Engine):** Interfaces with YouTube to scrape raw channel data based on specific queries. Outputs to `raw_data.json`.
2. **`filter.py` (The Brain):** Parses the raw JSON, applies business logic (keyword matching, description length, etc.), and generates a clean `targets.csv`.
3. **Data Sync (The Push):** A bash one-liner utilizing Google CLI to append the CSV directly into a live Google Sheet.

---


### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/creator-loop.git](https://github.com/YOUR_USERNAME/creator-loop.git)
   cd creator-loop

### 🛠️ Prerequisites & APIs

Before running CreatorLoop, ensure you have the following installed on your system. 

**Core Languages:**
* **[Python 3.8+](https://www.python.org/downloads/)**
* **CLI Tools:**
* **[ytsearch](https://github.com/pndurette/ytsearch):** The primary headless scraper used in `scout.py` to pull YouTube JSON data.
* **[gogcli](https://github.com/fatih/gog):** The command-line tool used to pipe the final CSV data directly into your Google Sheets.

* **🦖 Legacy / Fallback APIs:**
* * **[The Caveman API](https://api.caveman.io/):** If you are adapting the older scraper workflow, or if the `ytsearch` CLI fails, you can route your `scout.py` requests through this legacy endpoint. (Note: Requires active API key injected into the request headers).

* 
  
