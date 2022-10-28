from astropy.io import fits
from astropy.wcs import WCS

COMPRESSION_TYPES = ["RICE_1", "RICE_ONE", "PLIO_1", "GZIP_1", "GZIP_2", "HCOMPRESS_1"]

hdu = fits.open("http://www.astropy.org/astropy-data/galactic_center/gc_2mass_k.fits")[0]

header = WCS(hdu.header).to_header()

for ct in COMPRESSION_TYPES:
    hdu = fits.CompImageHDU(
        hdu.data, header, compression_type=ct, tile_size=(100, 100)
    )
    hdu.writeto(f"gc_2mass_k_{ct}.fits", overwrite=True)
