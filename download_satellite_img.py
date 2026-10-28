from datetime import datetime
from io import BytesIO
import math
from geopy.geocoders import Nominatim
from PIL import Image
import requests


def get_coordinates(place_name):
    """Geocodes a place name string to latitude and longitude coordinates with fallbacks."""
    geolocator = Nominatim(user_agent="geospatial_cv_downloader")

    # Try searching with increasing regional detail
    search_queries = [
        place_name,
        f"{place_name}, Maharashtra",
        f"{place_name}, India",
    ]

    for query in search_queries:
        location = geolocator.geocode(query)
        if location:
            print(f"\nMatch Found: {location.address}")
            print(
                f"Coordinates: Lat {location.latitude:.4f}, Lon {location.longitude:.4f}"
            )
            return location.latitude, location.longitude

    raise ValueError(
        f"Could not locate '{place_name}'. Try entering a nearby major town or district name."
    )


def latlon_to_tile(lat, lon, zoom):
    """Converts (lat, lon) coordinates to Web Mercator XYZ Tile indices."""
    lat_rad = math.radians(lat)
    n = 2.0**zoom
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int(
        (1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi)
        / 2.0
        * n
    )
    return xtile, ytile


def download_satellite_image(
    place_name, zoom=14, grid_size=6, output_filename="input_image.jpg", pil_format="JPEG"
):
    """Downloads satellite imagery tiles for any user-entered location and stitches them into the selected format."""
    # 1. Geocode location from user input
    lat, lon = get_coordinates(place_name)

    # 2. Get central tile coordinates
    center_x, center_y = latlon_to_tile(lat, lon, zoom)

    tile_url_template = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    tile_pixels = 256
    half_grid = grid_size // 2

    # Canvas dimensions = grid_size * 256 pixels
    stitched_image = Image.new(
        "RGB", (grid_size * tile_pixels, grid_size * tile_pixels)
    )
    headers = {"User-Agent": "Mozilla/5.0"}

    print(
        f"\nFetching {grid_size}x{grid_size} tiles at Zoom Level {zoom} for wider spatial coverage..."
    )

    for i, dx in enumerate(range(-half_grid, half_grid + (grid_size % 2))):
        for j, dy in enumerate(range(-half_grid, half_grid + (grid_size % 2))):
            x, y = center_x + dx, center_y + dy
            response = requests.get(
                tile_url_template.format(z=zoom, x=x, y=y), headers=headers
            )

            if response.status_code == 200:
                tile_img = Image.open(BytesIO(response.content))
                stitched_image.paste(
                    tile_img, (i * tile_pixels, j * tile_pixels)
                )

    # Save format-specific configurations
    save_kwargs = {}
    if pil_format == "JPEG":
        save_kwargs["quality"] = 95
    elif pil_format == "TIFF":
        save_kwargs["compression"] = "tiff_lzw"  # Optional compression for GIS TIFFs

    stitched_image.save(output_filename, pil_format, **save_kwargs)
    print(f"\nSuccess! Image saved as '{output_filename}'")
    print(f"Final Resolution: {stitched_image.width}x{stitched_image.height} pixels")


# --- INTERACTIVE USER INPUTS ---
if __name__ == "__main__":
    print("=" * 60)
    print(" SATELLITE RASTER IMAGE DOWNLOADER (GEOSPATIAL CV TOOL)")
    print("=" * 60)

    # 1. Place name input
    place = input(
        "\nEnter Place Name (e.g., 'Mulshi Dam', 'Khadakwasla', 'Pangong Tso'): "
    ).strip()

    # 2. Coverage Preset Choice
    print("\nSelect Coverage & Resolution Level:")
    print("  [1] High Detail / Local View (Zoom 16, ~1-2 km coverage)")
    print(
        "  [2] Balanced Regional / Lake & Mountain View (Zoom 14, ~5-8 km coverage)"
    )
    print("  [3] Wide Regional View (Zoom 12, ~15-20 km coverage)")

    choice = input("Enter choice (1, 2, or 3) [Default: 2]: ").strip()

    # Preset configurations
    if choice == "1":
        selected_zoom = 16
        selected_grid = 6
    elif choice == "3":
        selected_zoom = 12
        selected_grid = 6
    else:
        selected_zoom = 14
        selected_grid = 6

    # 3. Output Format Choice
    print("\nSelect Output Format:")
    print("  [1] JPEG (smaller file, default)")
    print("  [2] PNG  (lossless)")
    print("  [3] TIFF (for GIS use)")

    fmt_choice = input("Enter choice (1/2/3) [Default: 1]: ").strip()

    format_map = {
        "1": ("JPEG", "jpg"),
        "2": ("PNG", "png"),
        "3": ("TIFF", "tif"),
    }
    pil_format, extension = format_map.get(fmt_choice, ("JPEG", "jpg"))

    # Generate dynamic filename using timestamp and safe place name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    safe_name = place.lower().replace(" ", "_")
    output_file = f"{safe_name}_{timestamp}.{extension}"

    # Pass everything cleanly to the download function
    download_satellite_image(
        place_name=place,
        zoom=selected_zoom,
        grid_size=selected_grid,
        output_filename=output_file,
        pil_format=pil_format,
    )
