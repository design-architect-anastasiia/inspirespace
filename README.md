# InspireSpace 🏛️

**InspireSpace** is a web-based gallery for architectural inspiration, where you can upload, view, and share 3D renders of interiors, moods, and material concepts.

Created by [@design-architect-anastasiia](https://github.com/design-architect-anastasiia)

---

📁 Project Structure

inspirespace/
├── app.py
├── gallery_data.json
├── requirements.txt
├── static/
│   ├── style.css
│   └── uploads/
│       ├── example_render1.jpg
│       └── example_render2.jpg
├── templates/
│   ├── index.html
│   └── upload.html


## 💡 Features

- Upload 3D render images with titles, descriptions, and moods
- View a gallery of inspirational architecture
- Store metadata in a simple JSON format
- Beautiful responsive layout

---

## 🛠️ Tech Stack

- `Python` + `Flask` (backend)
- `HTML`, `CSS` (frontend)
- 3D visualization via `Daz3D` or `3DMax` (external, optional)
- `JSON` storage (no database required for MVP)

---

## 🚀 Getting Started

### 1. Clone the project

```
git clone https://github.com/design-architect-anastasiia/inspirespace.git
cd inspirespace
```

### 2. Set up virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

Open http://localhost:5000 in your browser.
