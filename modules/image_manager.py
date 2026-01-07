"""
Image Manager for Fantasy Life Quest Tracker
Handles loading and caching of location thumbnails and regional maps
"""

import customtkinter as ctk
from PIL import Image
import os


class ImageManager:
    """Manages loading and caching of location/map images"""

    def __init__(self, image_dir="Images"):
        self.image_dir = image_dir
        self.cache = {}
        self.location_map = self._load_location_mapping()

    def _load_location_mapping(self):
        """Load mapping from placenames.txt and imagenames.txt"""
        mapping = {}

        try:
            # Read place names
            with open("placenames.txt", 'r', encoding='utf-8') as f:
                place_names = [line.strip() for line in f.readlines() if line.strip()]

            # Read image filenames
            with open("imagenames.txt", 'r', encoding='utf-8') as f:
                image_files = [line.strip() for line in f.readlines() if line.strip()]

            # Create mapping
            for place_name, image_file in zip(place_names, image_files):
                full_path = os.path.join(self.image_dir, image_file)
                if os.path.exists(full_path):
                    mapping[place_name] = full_path

        except FileNotFoundError as e:
            print(f"Warning: Could not load location mapping: {e}")

        return mapping

    def get_location_image(self, location_name, size=(80, 60)):
        """Get cached CTkImage for location thumbnail"""
        cache_key = f"{location_name}_{size[0]}x{size[1]}"

        # Return from cache if available
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Load image
        image_path = self.location_map.get(location_name)
        if not image_path or not os.path.exists(image_path):
            return None

        try:
            # Load with PIL
            pil_image = Image.open(image_path)

            # Convert GIF with transparency to RGB
            if pil_image.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', pil_image.size, (255, 255, 255))
                # Paste image on background
                if pil_image.mode == 'RGBA':
                    background.paste(pil_image, mask=pil_image.split()[-1])
                else:
                    background.paste(pil_image)
                pil_image = background

            # Resize to thumbnail
            pil_image = pil_image.resize(size, Image.Resampling.LANCZOS)

            # Create CTkImage
            ctk_image = ctk.CTkImage(
                light_image=pil_image,
                dark_image=pil_image,
                size=size
            )

            # Cache and return
            self.cache[cache_key] = ctk_image
            return ctk_image

        except Exception as e:
            print(f"Error loading image for {location_name}: {e}")
            return None

    def get_regional_map(self, region_name, size=(400, 300)):
        """Get larger regional map image"""
        from .region_mapping import REGIONAL_MAPS

        cache_key = f"map_{region_name}_{size[0]}x{size[1]}"

        # Return from cache if available
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Get map path
        map_path = REGIONAL_MAPS.get(region_name)
        if not map_path or not os.path.exists(map_path):
            return None

        try:
            # Load with PIL
            pil_image = Image.open(map_path)

            # Convert GIF with transparency
            if pil_image.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', pil_image.size, (255, 255, 255))
                if pil_image.mode == 'RGBA':
                    background.paste(pil_image, mask=pil_image.split()[-1])
                else:
                    background.paste(pil_image)
                pil_image = background

            # Resize
            pil_image = pil_image.resize(size, Image.Resampling.LANCZOS)

            # Create CTkImage
            ctk_image = ctk.CTkImage(
                light_image=pil_image,
                dark_image=pil_image,
                size=size
            )

            # Cache and return
            self.cache[cache_key] = ctk_image
            return ctk_image

        except Exception as e:
            print(f"Error loading regional map for {region_name}: {e}")
            return None

    def clear_cache(self):
        """Clear image cache"""
        self.cache.clear()
