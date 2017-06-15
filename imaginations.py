"""Get and process images."""
# import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random as rnd
import requests
from StringIO import StringIO


def get_twitpic(addr, user):
    """Get image from url."""
    path = "twits/imgs/" + user + "/"

    try:
        im = Image.open(path + user + "_profile.jpg")
        return im
    except Exception:
        r = requests.get(addr)
        im = Image.open(StringIO(r.content))
        im.save(path + user + "_profile.jpg")
        return im


def scooter(pix, xx, yy, twit):
    """Scoot some pixels to the right."""
    for ii in reversed(xrange(xx)):
        for jj in xrange(yy):
            tp0 = pix[ii, jj][0]
            tp1 = pix[ii, jj][1]
            tp2 = pix[ii, jj][2]
            if not tp0 & ~(ord(twit[70]) - 20):
                kk = ord(twit[72]) / 8
                while kk:
                    tpix = pix[(ii + kk) % xx, jj]
                    pix[(ii + kk) % xx, jj] = (tp0, tpix[1], tpix[2])
                    kk -= 1
            if not tp1 & ~(ord(twit[78]) - 20):
                kk = ord(twit[82]) / 8
                while kk:
                    tpix = pix[(ii + kk) % xx, jj]
                    pix[(ii + kk) % xx, jj] = (tpix[0], tp1, tpix[2])
                    kk -= 1
            if not tp2 & ~(ord(twit[88]) - 20):
                kk = ord(twit[96]) / 8
                while kk:
                    tpix = pix[(ii + kk) % xx, jj]
                    pix[(ii + kk) % xx, jj] = (tpix[0], tpix[1], tp2)
                    kk -= 1


def scootel(pix, xx, yy, twit):
    """Scoot some pixels to the left."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            tp0 = pix[ii, jj][0]
            tp1 = pix[ii, jj][1]
            tp2 = pix[ii, jj][2]
            if not tp0 & ~(ord(twit[40]) - 20):
                kk = ord(twit[42]) / 8
                while kk:
                    tpix = pix[abs(ii - kk), jj]
                    pix[abs(ii - kk), jj] = (tp0, tpix[1], tpix[2])
                    kk -= 1
            if not tp1 & ~(ord(twit[46]) - 20):
                kk = ord(twit[52]) / 8
                while kk:
                    tpix = pix[abs(ii - kk), jj]
                    pix[abs(ii - kk), jj] = (tpix[0], tp1, tpix[2])
                    kk -= 1
            if not tp2 & ~(ord(twit[60]) - 20):
                kk = ord(twit[66]) / 8
                while kk:
                    tpix = pix[abs(ii - kk), jj]
                    pix[abs(ii - kk), jj] = (tpix[0], tpix[1], tp2)
                    kk -= 1


def scooteu(pix, xx, yy, twit):
    """Scoot some pixels to the up."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            tp0 = pix[ii, jj][0]
            tp1 = pix[ii, jj][1]
            tp2 = pix[ii, jj][2]
            if not tp0 & ~(ord(twit[1]) - 20):
                kk = ord(twit[2]) / 8
                while kk:
                    tpix = pix[ii, abs(jj - kk)]
                    pix[ii, abs(jj - kk)] = (tp0, tpix[1], tpix[2])
                    kk -= 1
            if not tp1 & ~(ord(twit[4]) - 20):
                kk = ord(twit[6]) / 8
                while kk:
                    tpix = pix[ii, abs(jj - kk)]
                    pix[ii, abs(jj - kk)] = (tpix[0], tp1, tpix[2])
                    kk -= 1
            if not tp2 & ~(ord(twit[10]) - 20):
                kk = ord(twit[12]) / 8
                while kk:
                    tpix = pix[ii, abs(jj - kk)]
                    pix[ii, abs(jj - kk)] = (tpix[0], tpix[1], tp2)
                    kk -= 1


def scooted(pix, xx, yy, twit):
    """Scoot some pixels to the down."""
    for ii in xrange(xx):
        for jj in reversed(xrange(yy)):
            tp0 = pix[ii, jj][0]
            tp1 = pix[ii, jj][1]
            tp2 = pix[ii, jj][2]
            if not tp0 & ~(ord(twit[16]) - 20):
                kk = ord(twit[18]) / 8
                while kk:
                    tpix = pix[ii, (jj + kk) % yy]
                    pix[ii, (jj + kk) % yy] = (tp0, tpix[1], tpix[2])
                    kk -= 1
            if not tp1 & ~(ord(twit[22]) - 20):
                kk = ord(twit[28]) / 8
                while kk:
                    tpix = pix[ii, (jj + kk) % yy]
                    pix[ii, (jj + kk) % yy] = (tpix[0], tp1, tpix[2])
                    kk -= 1
            if not tp2 & ~(ord(twit[30]) - 20):
                kk = ord(twit[36]) / 8
                while kk:
                    tpix = pix[ii, (jj + kk) % yy]
                    pix[ii, (jj + kk) % yy] = (tpix[0], tpix[1], tp2)
                    kk -= 1


def scoots(pix, xx, yy, twit):
    """Scoot some pixels all over the place."""
    if len(twit) > 13:
        scooteu(pix, xx, yy, twit)
    if len(twit) > 37:
        scooted(pix, xx, yy, twit)
    if len(twit) > 67:
        scootel(pix, xx, yy, twit)
    if len(twit) > 97:
        scooter(pix, xx, yy, twit)


def scootxor(pix, xx, yy, twit):
    """Scoot some pixels all over the place."""
    tt = ""
    for c in reversed(twit):
        tt += c
    if len(twit) > 101:
        c = ord(twit[100])
        xor_c(pix, xx, yy, c)
        c = ord(tt[100])
        xor_c(pix, xx, yy, c)
    if len(twit) > 13:
        scooteu(pix, xx, yy, twit)
        scooteu(pix, xx, yy, tt)
    if len(twit) > 103:
        c = ord(twit[102])
        xor_m(pix, xx, yy, c)
        c = ord(tt[102])
        xor_m(pix, xx, yy, c)
    if len(twit) > 37:
        scooted(pix, xx, yy, twit)
        scooted(pix, xx, yy, tt)
    if len(twit) > 107:
        c = ord(twit[106])
        xor_y(pix, xx, yy, c)
        c = ord(tt[106])
        xor_y(pix, xx, yy, c)
    if len(twit) > 67:
        scootel(pix, xx, yy, twit)
        scooter(pix, xx, yy, tt)
    if len(twit) > 109:
        c = ord(twit[108])
        xor_k(pix, xx, yy, c)
        c = ord(tt[108])
        xor_k(pix, xx, yy, c)
    if len(twit) > 97:
        scootel(pix, xx, yy, tt)
        scooter(pix, xx, yy, twit)


def xorror(pix, xx, yy, twit):
    """Call the xor babbies."""
    if len(twit) > 101:
        c = ord(twit[100])
        xor_c(pix, xx, yy, c)
    if len(twit) > 103:
        c = ord(twit[102])
        xor_m(pix, xx, yy, c)
    if len(twit) > 107:
        c = ord(twit[106])
        xor_y(pix, xx, yy, c)
    if len(twit) > 109:
        c = ord(twit[108])
        xor_k(pix, xx, yy, c)


def xor_c(pix, xx, yy, tc):
    """Invert for cyan xors."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            t = ii ^ jj
            if 95 * t / 256 == tc:
                tp = pix[ii, jj]
                pix[ii, jj] = (~tp[0], tp[1], tp[2])


def xor_m(pix, xx, yy, tc):
    """Invert for magenta xors."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            t = (xx - ii) ^ jj
            if 95 * t / 256 == tc:
                tp = pix[ii, jj]
                pix[ii, jj] = (tp[0], ~tp[1], tp[2])


def xor_y(pix, xx, yy, tc):
    """Invert for yellow xors."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            t = ii ^ (yy - jj)
            if 95 * t / 256 == tc:
                tp = pix[ii, jj]
                pix[ii, jj] = (tp[0], tp[1], ~tp[2])


def xor_k(pix, xx, yy, tc):
    """Invert for blackish xors."""
    for ii in xrange(xx):
        for jj in xrange(yy):
            t = (xx - ii) ^ (yy - jj)
            if 95 * t / 256 == tc:
                tp = pix[ii, jj]
                pix[ii, jj] = (~tp[0], ~tp[1], ~tp[2])


def shapes(pix, xx, yy, twit, count):
    """Do something in a shape."""
    n = count
    while n > 0:
        t1 = rnd.randint(0, len(twit) - 1)
        t2 = rnd.randint(0, len(twit) - 1)
        t3 = rnd.randint(0, len(twit) - 1)
        t4 = rnd.randint(0, len(twit) - 1)
        t5 = rnd.randint(0, len(twit) - 1)
        t6 = rnd.randint(0, len(twit) - 1)
        t7 = rnd.randint(0, len(twit) - 1)
        cx = xx / 2 + ord(twit[t1]) - ord(twit[t2])
        cy = yy / 2 + ord(twit[t3]) - ord(twit[t4])
        r1 = ord(twit[t5]) - 20
        r2 = ord(twit[t6]) + 20
        tc = ord(twit[t7]) - 20
        not_circler(pix, xx, yy, cx, cy, r1, r2 * 3, tc)
        n -= 1


def circler(pix, xx, yy, cx, cy, r1, r2, tc):
    """Do a donut."""
    if r1 > r2:
        temp = r1
        r1 = r2
        r2 = temp
    if r1 == r2:
        r2 += tc

    for ii in xrange(xx):
        for jj in xrange(yy):
            if ((ii - cx) ** 2) + ((jj - cy) ** 2) > r1 ** 2\
               and ((ii - cx) ** 2) + ((jj - cy) ** 2) < r2 ** 2:
                t = pix[ii, jj]
                pix[ii, jj] = (t[0] ^ tc,
                               t[1] ^ tc,
                               t[2] ^ tc)


def trangler(pix, xx, yy, x0, x1, x2, y0, y1, y2, w, tc):
    """Make a trangle."""
    pass


def not_circler(pix, xx, yy, cx, cy, r1, r2, tc):
    """Do not a donut."""
    if r1 > r2:
        temp = r1
        r1 = r2
        r2 = temp
    if r1 == r2:
        r2 += tc

    for ii in xrange(xx):
        for jj in xrange(yy):
            if r1 <= abs(cx - ii) <= r2\
                    and r1 <= abs(cy - jj) <= r2:
                t = pix[ii, jj]
                pix[ii, jj] = (t[0] ^ tc,
                               t[1] ^ tc,
                               t[2] ^ tc)


def wordler(img, l1, l2, l3):
    """Make some words."""
    t = [(ord(l1[0]) - 20) / 16,
         (ord(l2[1]) - 20) / 8,
         (ord(l3[1]) - 20) / 8,
         (ord(l1[2]) - 20) / 8,
         (ord(l2[3]) - 20) / 4,
         (ord(l3[5]) - 20) / 4,
         (ord(l1[8]) - 20) / 4]

    draw = ImageDraw.Draw(img)
    font_path = "/usr/share/fonts/truetype/"\
                + "liberation/LiberationMono-Regular.ttf"
    font = ImageFont.truetype(font_path, 40 + t[0])
    draw.text((t[1], 0 + t[4]), l1, (255, 255, 255), font=font)
    draw.text((t[2], 48 + t[5]), l2, (255, 255, 255), font=font)
    draw.text((t[3], 96 + t[6]), l3, (255, 255, 255), font=font)
