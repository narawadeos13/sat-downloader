# 🛰️SatGrab

**Type a place name. Get a stitched satellite image. No API key.**

SatGrab converts any location — a dam, a lake, a village, a mountain — into a high-resolution satellite image ready for OpenCV or Geo AI pipelines. It geocodes the name, works out which map tiles cover it, downloads them, and stitches them into a single JPEG/PNG/TIF.

Built as the data-acquisition layer for my Geo AI projects (Raireshwar Plateau, Sahyadri Ecosystem Research) — a reusable way to grab satellite context for any new site without manually hunting through a GIS tool each time.

---

## What it does

```
Place name  →  Geocoded to lat/lon (Nominatim)
            →  Converted to Web Mercator XYZ tile coordinates
            →  6×6 grid of 256×256 tiles downloaded (Esri ArcGIS World Imagery)
            →  Stitched into one 1536×1536 JPEG/PNG/TIF
```

No registration, no API key — uses Esri's public World Imagery tile endpoint.

---

## Quickstart

```bash
git clone https://github.com/narawadeos13/satgrab.git
cd satgrab
pip install -r requirements.txt
python download_satellite_img.py
```

```
============================================================
 SATELLITE RASTER IMAGE DOWNLOADER (GEOSPATIAL CV TOOL)
============================================================

Enter Place Name (e.g., 'Mulshi Dam', 'Khadakwasla', 'Pangong Tso'): mulshi dam

Select Coverage & Resolution Level:
  [1] High Detail / Local View (Zoom 16, ~1-2 km coverage)
  [2] Balanced Regional / Lake & Mountain View (Zoom 14, ~5-8 km coverage)
  [3] Wide Regional View (Zoom 12, ~15-20 km coverage)
Enter choice (1, 2, or 3) [Default: 2]: 2

Select Output Format:
  [1] JPEG (smaller file, default)
  [2] PNG  (lossless)
  [3] TIFF (for GIS use)
Enter choice (1/2/3) [Default: 1]: 3

Match Found: Mulshi Dam, Sambhave, Mulshi Subdistrict, Pune, Maharashtra, 412108, India
Coordinates: Lat 18.5265, Lon 73.5111

Fetching 6x6 tiles at Zoom Level 14 for wider spatial coverage...

Success! Image saved as 'mulshi_dam_20261028_0952.tif'
Final Resolution: 1536x1536 pixels
```

---

## Geocoding fallback

A place name alone often isn't specific enough for the geocoder. SatGrab retries automatically with increasing regional context before giving up:

```
"Mulshi Dam"
      ↓ not found?
"Mulshi Dam, Maharashtra"
      ↓ not found?
"Mulshi Dam, India"
```

---

## Zoom presets

| Option | Zoom | Coverage | Good for |
|---|---|---|---|
| 1 | 16 | ~1–2 km | Buildings, roads, fine detail |
| 2 (default) | 14 | ~5–8 km | Lakes, dams, plateaus |
| 3 | 12 | ~15–20 km | Full regions, mountain ranges |

All presets output the same 6×6 grid → 1536×1536 px frame; zoom changes what fits inside it, not the pixel size.

---

## Dependencies

```
geopy
Pillow
requests
```

```bash
pip install -r requirements.txt
```

---

## Project structure

```
satgrab/
├── download_satellite_img.py   # geocoding, tile math, download, stitching
├── requirements.txt
├── data/
│   └── input_image.jpg         # output lands here
└── README.md
```

---

## Use cases

- **Geo AI field prep** — pull satellite context for a new site before a field visit (how this tool is actually used in my own Raireshwar/Sahyadri work)
- **Computer vision input** — edge detection, HSV water-body masking, segmentation on real terrain
- **Quick geographic exploration** — dams, forts, rivers, agricultural land, anywhere Esri has coverage

---

## Known limitations

- Fixed 6×6 grid / 1536×1536 output — no custom dimensions yet
- Single imagery source (Esri World Imagery) — no cloud filtering, no date selection
- Sequential tile downloads — a 6×6 grid means 36 requests, not parallelized

---

## Possible next steps

- [ ] GeoTIFF export with georeferencing
- [ ] Custom grid size / output dimensions
- [ ] Parallel tile downloads
- [ ] NDVI / multispectral source option
- [ ] CLI arguments (skip the interactive prompts)

---

## License

MIT — see [LICENSE](LICENSE)

---

## Author

**Om Narawade** — [GitHub](https://github.com/narawadeos13) · [LinkedIn](https://www.linkedin.com/in/om-narawade-0a992a248)
