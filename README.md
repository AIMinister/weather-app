# 🌦️ Weather CLI App

<p align="center">
  <b>A production-ready Python CLI for real-time weather data</b><br>
  Clean architecture • PyPI package • CLI tool
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/weather-app-vkyei?color=blue&label=PyPI">
  <img src="https://img.shields.io/pypi/pyversions/weather-app-vkyei">
  <img src="https://img.shields.io/github/stars/AIMinister/weather-app?style=social">
  <img src="https://img.shields.io/badge/status-production--ready-success">
</p>

---

## 🚀 Installation

```bash
pip install weather-app-vkyei
```

---

## ⚡ Usage

```bash
weather
```

---

## 🎬 Example Output

```
📍 Dallas
🌡️ Temp: 24.39°C
☁️ broken clouds
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Get your API key here: https://openweathermap.org/api

---

## 🧠 Features

- 🌍 Real-time weather lookup
- 💻 Command-line interface (CLI)
- 🔐 Secure API key handling via `.env`
- 🧩 Modular architecture (client + CLI separation)
- 📦 Packaged with `pyproject.toml`
- 🚀 Published to PyPI

---

## 📦 Project Structure

```
weather-app/
│
├── src/
│   └── weather_app_vkyei/
│       ├── __init__.py
│       ├── client.py        # API logic
│       └── cli.py           # CLI entry point
│
├── .env
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

- Python 3.14+
- requests
- python-dotenv
- uv (build + dependency management)

---

## 📦 PyPI Package

https://pypi.org/project/weather-app-vkyei/

---

## 🧪 Local Development

```bash
git clone https://github.com/AIMinister/weather-app.git
cd weather-app

uv venv
uv pip install -e .

python main.py
```

---

## 🚀 Build & Publish

```bash
uv build
uv run twine upload dist/*
```

---

## 🧩 Architecture

- `client.py` → Handles API communication  
- `cli.py` → User interaction (command line)  
- `.env` → Secure API key storage  
- `pyproject.toml` → Packaging & distribution  

---

## 🔮 Future Improvements

- Add forecast support (5-day / hourly)
- Add argument-based CLI (`weather Dallas`)
- Add caching for faster responses
- Build web UI (FastAPI + frontend)

---

## 👤 Author

**AIMinister**  
https://github.com/AIMinister

---

## ⭐ Support

If you found this useful:

⭐ Star the repo  
🍴 Fork it  
🚀 Build on top of it  

---

<p align="center">
  Built like a real-world Python package 📦
</p>