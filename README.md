# 🛰️SatGrab

**Type a place name. Get a stitched satellite image. No API key.**

SatGrab converts any location — a dam, a lake, a village, a mountain — into a high-resolution satellite image ready for OpenCV or Geo AI pipelines. It geocodes the name, works out which map tiles cover it, downloads them, and stitches them into a single JPEG.

Built as the data-acquisition layer for my Geo AI projects (Raireshwar Plateau, Sahyadri Ecosystem Research) — a reusable way to grab satellite context for any new site without manually hunting through a GIS tool each time.

---

## What it does

```
Place name  →  Geocoded to lat/lon (Nominatim)
            →  Converted to Web Mercator XYZ tile coordinates
            →  6×6 grid of 256×256 tiles downloaded (Esri ArcGIS World Imagery)
            →  Stitched into one 1536×1536 JPEG
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
Enter Place Name: Mulshi Dam

Match Found: Mulshi Dam, Pune, Maharashtra, India
Coordinates: Lat 18.5032, Lon 73.5124

Select Coverage & Resolution Level:
  [1] High Detail / Local View (Zoom 16, ~1-2 km)
  [2] Balanced Regional View (Zoom 14, ~5-8 km)
  [3] Wide Regional View (Zoom 12, ~15-20 km)

Fetching 6x6 tiles at Zoom Level 14...
Success! Image saved as 'input_image.jpg' (1536x1536 px)
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
- JPEG only — no GeoTIFF, so output isn't georeferenced for direct GIS re-import
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