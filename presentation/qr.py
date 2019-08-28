import qrcode


def generateQR(name, url, fill_color="black", back_color="white"):
    """
    Generate a QR code from a url.
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=5,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save("qr-{}.png".format(name))


# %% binder
# https://mybinder.org/v2/gh/morganjwilliams/aegc2019/develop?urlpath=lab/tree/aegc2019/notebooks
generateQR("binder", "https://tinyurl.com/aegc2019williamsbinder", fill_color="#eda25a")
# %% github
# https://github.com/morganjwilliams/aegc2019/tree/develop
generateQR("github", "https://tinyurl.com/aegc2019williamsgithub")
# %% pyrolite docs
# pyrolite.readthedocs.io
generateQR("pyrolite", "https://pyrolite.readthedocs.io", fill_color="#5f9ed1")
# %% abstract
# https://github.com/morganjwilliams/aegc2019/raw/develop/presentation/abstract.pdf
generateQR("abstract", "https://tinyurl.com/aegc2019williamsabstract")
