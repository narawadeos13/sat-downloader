# \# 🛰️ SatGrab — High-Res Satellite Raster Downloader

# 

# > \*\*Programmatically search, stitch, and export high-resolution satellite imagery from anywhere on Earth into 8-bit JPEGs — zero API keys required.\*\*

# 

# \*\*SatGrab\*\* (`sat-downloader`) is an interactive geospatial utility designed to bridge the gap between GIS satellite tile servers and Computer Vision (CV) pipelines.

# 

# By combining automated place-name geocoding with Web Mercator tile stitching, SatGrab converts a global landmark, lake, dam, or region into a high-quality JPEG ready for \*\*OpenCV, GeoAI, and image-processing workflows\*\*.

# 

# \---

# 

# \## 🔥 Features

# 

# \* 🌍 \*\*Natural Language Geocoding\*\*

# &#x20; Type any location name such as `"Mulshi Dam"`, `"Khadakwasla"`, or `"Pangong Tso"` and let the tool automatically locate it.

# 

# \* 🗺️ \*\*Esri ArcGIS World Imagery Integration\*\*

# &#x20; Retrieves high-resolution optical satellite imagery without requiring an API key or registration.

# 

# \* 🧩 \*\*Automated Tile Stitching\*\*

# &#x20; Dynamically calculates \*\*XYZ Web Mercator tile coordinates\*\* and stitches them into a seamless `1536 × 1536 px` composite image.

# 

# \* 🎚️ \*\*Prescriptive Zoom Control\*\*

# 

# &#x20; | Option                   | Zoom | Approx. Coverage | Best For                         |

# &#x20; | ------------------------ | ---: | ---------------: | -------------------------------- |

# &#x20; | High Detail / Local View |   16 |          \~1–2 km | Buildings, roads, local features |

# &#x20; | Balanced Regional View   |   14 |          \~5–8 km | Lakes, dams, surrounding areas   |

# &#x20; | Wide Regional View       |   12 |        \~15–20 km | Large landscapes and regions     |

# 

# \* 🖼️ \*\*OpenCV \& GeoAI Ready\*\*

# &#x20; Exports directly to \*\*8-bit JPEG at 95% quality\*\*, making the output suitable for:

# 

# &#x20; \* OpenCV

# &#x20; \* Image classification

# &#x20; \* Edge detection

# &#x20; \* HSV color masking

# &#x20; \* Morphological processing

# &#x20; \* GeoAI experiments

# &#x20; \* Computer vision pipelines

# 

# \---

# 

# \## 🏗️ Repository Architecture

# 

# ```text

# sat-downloader/

# │

# ├── data/                       # Target folder for output satellite images

# │   └── input\_image.jpg         # Stitched satellite JPEG

# │

# ├── download\_satellite\_img.py   # Core downloader \& tile stitching engine

# ├── requirements.txt            # Runtime dependencies

# ├── .gitignore                  # Prevents committing large images \& cache

# └── README.md                   # Project documentation

# ```

# 

# \---

# 

# \## 🚀 Quickstart

# 

# \### 1. Clone the Repository

# 

# ```bash

# git clone https://github.com/your-username/sat-downloader.git

# cd sat-downloader

# ```

# 

# \### 2. Install Dependencies

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \### 3. Run the Downloader

# 

# ```bash

# python download\_satellite\_img.py

# ```

# 

# \---

# 

# \## 🖥️ Interactive Walkthrough

# 

# The program provides an interactive terminal interface:

# 

# ```text

# ============================================================

# &#x20;SATELLITE RASTER IMAGE DOWNLOADER (GEOSPATIAL CV TOOL)

# ============================================================

# 

# Enter Place Name (e.g., 'Mulshi Dam', 'Khadakwasla', 'Pangong Tso'): Mulshi Dam

# 

# Match Found: Mulshi Dam, Pune, Maharashtra, India

# Coordinates: Lat 18.5032, Lon 73.5124

# 

# Select Coverage \& Resolution Level:

# &#x20; \[1] High Detail / Local View (Zoom 16, \~1-2 km coverage)

# &#x20; \[2] Balanced Regional / Lake \& Mountain View (Zoom 14, \~5-8 km coverage)

# &#x20; \[3] Wide Regional View (Zoom 12, \~15-20 km coverage)

# 

# Enter choice (1, 2, or 3) \[Default: 2]: 2

# 

# Fetching 6x6 tiles at Zoom Level 14 for wider spatial coverage...

# 

# Success! Image saved as 'input\_image.jpg'

# Final Resolution: 1536x1536 pixels

# ```

# 

# \---

# 

# \## ⚙️ Technical Engine

# 

# SatGrab follows a simple geospatial image-processing pipeline:

# 

# ```text

# &#x20;             Place Name Input

# &#x20;                    │

# &#x20;                    ▼

# &#x20;            ┌───────────────┐

# &#x20;            │   Geocoding   │

# &#x20;            │               │

# &#x20;            │   Nominatim   │

# &#x20;            │   API         │

# &#x20;            └───────┬───────┘

# &#x20;                    │

# &#x20;                    ▼

# &#x20;            ┌───────────────┐

# &#x20;            │   Tile Math   │

# &#x20;            │               │

# &#x20;            │ Lat/Lon →     │

# &#x20;            │ XYZ Tile      │

# &#x20;            │ Coordinates   │

# &#x20;            └───────┬───────┘

# &#x20;                    │

# &#x20;                    ▼

# &#x20;            ┌───────────────┐

# &#x20;            │   Tile Grid   │

# &#x20;            │               │

# &#x20;            │ 6 × 6 tiles   │

# &#x20;            │ 256 × 256 px  │

# &#x20;            └───────┬───────┘

# &#x20;                    │

# &#x20;                    ▼

# &#x20;            ┌───────────────┐

# &#x20;            │   Stitching   │

# &#x20;            │               │

# &#x20;            │ Pillow / PIL  │

# &#x20;            │ RGB Canvas    │

# &#x20;            └───────┬───────┘

# &#x20;                    │

# &#x20;                    ▼

# &#x20;         ┌──────────────────────┐

# &#x20;         │   Output JPEG        │

# &#x20;         │                      │

# &#x20;         │   1536 × 1536 px     │

# &#x20;         │   8-bit RGB          │

# &#x20;         └──────────────────────┘

# &#x20;                    │

# &#x20;                    ▼

# &#x20;            OpenCV / GeoAI

# &#x20;            Processing Pipeline

# ```

# 

# \---

# 

# \## 🧠 How It Works

# 

# \### 1. Place Name → Coordinates

# 

# The user enters a natural-language location:

# 

# ```text

# Mulshi Dam

# ```

# 

# The application uses \*\*Nominatim geocoding\*\* to resolve the place name into geographic coordinates:

# 

# ```text

# Latitude:  18.5032

# Longitude: 73.5124

# ```

# 

# \---

# 

# \### 2. Coordinates → Web Mercator Tiles

# 

# The latitude and longitude are converted into \*\*Web Mercator XYZ tile coordinates\*\* based on the selected zoom level.

# 

# Conceptually:

# 

# ```text

# Latitude + Longitude

# &#x20;       ↓

# Web Mercator Projection

# &#x20;       ↓

# XYZ Tile Coordinates

# &#x20;       ↓

# Tile Grid

# ```

# 

# \---

# 

# \### 3. Download Satellite Tiles

# 

# SatGrab requests individual `256 × 256 px` satellite tiles from the configured ArcGIS imagery service.

# 

# For a `6 × 6` grid:

# 

# ```text

# 6 × 6 = 36 tiles

# 

# 36 × 256 × 256 px

# &#x20;       ↓

# 1536 × 1536 px

# ```

# 

# \---

# 

# \### 4. Stitch the Tiles

# 

# The downloaded tiles are placed onto a single Pillow image canvas:

# 

# ```text

# ┌────┬────┬────┬────┬────┬────┐

# │    │    │    │    │    │    │

# ├────┼────┼────┼────┼────┼────┤

# │    │    │    │    │    │    │

# ├────┼────┼────┼────┼────┼────┤

# │    │    │    │    │    │    │

# ├────┼────┼────┼────┼────┼────┤

# │    │    │    │    │    │    │

# ├────┼────┼────┼────┼────┼────┤

# │    │    │    │    │    │    │

# ├────┼────┼────┼────┼────┼────┤

# │    │    │    │    │    │    │

# └────┴────┴────┴────┴────┴────┘

# 

# &#x20;       6 × 6 Tiles

# 

# &#x20;       ↓

# 

# &#x20;  1536 × 1536 px

# ```

# 

# \---

# 

# \### 5. Export

# 

# The final image is converted into an RGB image and exported as:

# 

# ```text

# data/input\_image.jpg

# ```

# 

# with:

# 

# ```text

# Format:      JPEG

# Color:       RGB / 8-bit

# Resolution:  1536 × 1536 px

# Quality:     95%

# ```

# 

# \---

# 

# \## 🛠️ Technology Stack

# 

# | Technology               | Purpose                      |

# | ------------------------ | ---------------------------- |

# | \*\*Python 3.8+\*\*          | Core application             |

# | \*\*GeoPy\*\*                | Geocoding                    |

# | \*\*Nominatim\*\*            | Place-name → coordinates     |

# | \*\*Requests\*\*             | HTTP tile downloading        |

# | \*\*Pillow\*\*               | Image processing \& stitching |

# | \*\*ArcGIS World Imagery\*\* | Satellite imagery source     |

# | \*\*Web Mercator / XYZ\*\*   | Tile addressing system       |

# 

# \---

# 

# \## 📦 Dependencies

# 

# The project intentionally keeps its dependency footprint small.

# 

# Example `requirements.txt`:

# 

# ```text

# geopy

# Pillow

# requests

# ```

# 

# Install them with:

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \---

# 

# \## 🌐 Data \& Imagery Sources

# 

# SatGrab uses:

# 

# \* \*\*Nominatim / OpenStreetMap\*\* for geocoding

# \* \*\*Esri ArcGIS World Imagery\*\* for satellite imagery

# \* \*\*Web Mercator XYZ tile scheme\*\* for spatial tile addressing

# 

# > \*\*Important:\*\* Availability, resolution, usage limits, attribution requirements, and licensing terms are controlled by the respective data/service providers. Check the applicable provider terms before using downloaded imagery in commercial or public-facing applications.

# 

# \---

# 

# \## 🎯 Use Cases

# 

# SatGrab can be used as a preprocessing tool for several geospatial and computer-vision applications.

# 

# \### 🛰️ GeoAI

# 

# \* Land-cover analysis

# \* Water-body detection

# \* Geographic feature extraction

# \* Remote-sensing experiments

# \* Spatial AI datasets

# 

# \### 👁️ Computer Vision

# 

# \* Edge detection

# \* Segmentation

# \* Object detection

# \* HSV-based feature extraction

# \* Morphological image processing

# \* Image classification

# 

# \### 🌊 Environmental Analysis

# 

# Example workflow:

# 

# ```text

# Satellite Image

# &#x20;     ↓

# Water Detection

# &#x20;     ↓

# HSV / RGB Mask

# &#x20;     ↓

# Morphological Cleaning

# &#x20;     ↓

# Contour Detection

# &#x20;     ↓

# Water-body Analysis

# ```

# 

# \### 🏔️ Geographic Exploration

# 

# Useful for downloading imagery around:

# 

# \* Lakes

# \* Dams

# \* Mountains

# \* Forts

# \* Cities

# \* Roads

# \* Villages

# \* Rivers

# \* Agricultural regions

# 

# \---

# 

# \## 🔬 Example GeoAI Workflow

# 

# SatGrab can act as the \*\*data acquisition layer\*\* of a larger GeoAI pipeline:

# 

# ```text

# &#x20;            Location Name

# &#x20;                  │

# &#x20;                  ▼

# &#x20;         ┌─────────────────┐

# &#x20;         │    SatGrab      │

# &#x20;         │                 │

# &#x20;         │ Geocoding       │

# &#x20;         │ Tile Download   │

# &#x20;         │ Tile Stitching  │

# &#x20;         └────────┬────────┘

# &#x20;                  │

# &#x20;                  ▼

# &#x20;         Satellite Raster

# &#x20;         1536 × 1536 JPEG

# &#x20;                  │

# &#x20;                  ▼

# &#x20;         ┌─────────────────┐

# &#x20;         │     OpenCV      │

# &#x20;         ├─────────────────┤

# &#x20;         │ Preprocessing   │

# &#x20;         │ Segmentation    │

# &#x20;         │ Feature Extract │

# &#x20;         └────────┬────────┘

# &#x20;                  │

# &#x20;                  ▼

# &#x20;         ┌─────────────────┐

# &#x20;         │      GeoAI      │

# &#x20;         ├─────────────────┤

# &#x20;         │ Classification  │

# &#x20;         │ Detection       │

# &#x20;         │ Prediction      │

# &#x20;         └─────────────────┘

# ```

# 

# \---

# 

# \## 📁 Output

# 

# After execution, the downloaded image is stored in:

# 

# ```text

# data/

# └── input\_image.jpg

# ```

# 

# Example:

# 

# ```text

# Input:

# &#x20;   Mulshi Dam

# 

# Output:

# &#x20;   data/input\_image.jpg

# ```

# 

# \---

# 

# \## ⚡ Design Goals

# 

# SatGrab was designed around four principles:

# 

# \### 1. Simple

# 

# No complicated GIS software or manual tile downloading.

# 

# \### 2. Accessible

# 

# No API key is required for the configured public imagery endpoint.

# 

# \### 3. Programmable

# 

# The downloaded imagery can immediately enter Python/CV workflows.

# 

# \### 4. GeoAI Ready

# 

# The tool can serve as the first stage of a larger remote-sensing or computer-vision pipeline.

# 

# \---

# 

# \## 🚧 Future Improvements

# 

# Potential improvements include:

# 

# \* \[ ] GeoTIFF export

# \* \[ ] Automatic image georeferencing

# \* \[ ] Bounding-box based downloads

# \* \[ ] Custom image dimensions

# \* \[ ] Parallel tile downloading

# \* \[ ] Automatic retry handling

# \* \[ ] Multiple satellite imagery providers

# \* \[ ] Cloud/quality filtering

# \* \[ ] NDVI and multispectral imagery support

# \* \[ ] Interactive map preview

# \* \[ ] CLI arguments instead of interactive input

# \* \[ ] Automatic water-body detection

# \* \[ ] GPU-accelerated image processing

# \* \[ ] Direct integration with ML/GeoAI models

# 

# \---

# 

# \## 📜 License

# 

# This project is distributed under the \*\*MIT License\*\*.

# 

# See the \[`LICENSE`](LICENSE) file for details.

# 

# \---

# 

# \## 👨‍💻 Author

# 

# \*\*Om Narawade\*\*

# 

# Built as a geospatial computer-vision utility for experimenting with \*\*Satellite Imagery, GeoAI, Remote Sensing, and Computer Vision\*\*.

# 

# \---

# 

# \## ⭐ Support

# 

# If you find this project useful:

# 

# ⭐ \*\*Star the repository\*\*

# 🍴 \*\*Fork the project\*\*

# 🐛 \*\*Report issues\*\*

# 💡 \*\*Suggest improvements\*\*

# 

# \---

# 

# \## 📌 Project Summary

# 

# > \*\*SatGrab converts a place name into a stitched satellite raster image, creating a simple bridge between online GIS imagery and Python-based GeoAI / Computer Vision workflows.\*\*

# 

# ```text

# Place Name

# &#x20;   ↓

# Geocoding

# &#x20;   ↓

# Lat / Lon

# &#x20;   ↓

# Web Mercator Tile Math

# &#x20;   ↓

# Satellite Tiles

# &#x20;   ↓

# Tile Stitching

# &#x20;   ↓

# 1536 × 1536 JPEG

# &#x20;   ↓

# OpenCV / GeoAI

# ```



