import qrcode


def generateQR(name, url, fill_color="black", back_color="white", box_size=12):
    """
    Generate a QR code from a url.
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save("qr-{}.png".format(name))


midday_blue = "#00a8ce"  # should be 0aafde
midnight_blue = "#041b2b"
teal = "#007582"

bg = "white"
# %% binder
# https://mybinder.org/v2/gh/morganjwilliams/aegc2019/develop?filepath=/notebooks/1_StartHere.ipynb
generateQR(
    "binder", "https://tinyurl.com/aegc19MWlive", fill_color="#E27B19", back_color=bg
)
# %% github
# https://github.com/morganjwilliams/aegc2019
generateQR(
    "github", "https://tinyurl.com/aegc2019MWgithub", fill_color=midnight_blue, back_color=bg
)
# %% pyrolite docs
# pyrolite.readthedocs.io
generateQR(
    "pyrolite", "https://pyrolite.readthedocs.io", fill_color="#5f9ed1", back_color=bg
)
# %% abstract
# https://github.com/morganjwilliams/aegc2019/raw/develop/presentation/abstract.pdf
generateQR(
    "abstract",
    "https://tinyurl.com/aegc2019MWabstract",
    fill_color="black",
    back_color=bg,
)
