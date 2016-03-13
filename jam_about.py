# Copyright (C) 10se1ucgo 2016
# This file is part of pyjam.
#
# pyjam is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyjam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyjam.  If not, see <http://www.gnu.org/licenses/>.

# jam.py is cluttered enough as is.
import wx
import wx.lib.scrolledpanel as sp
import wx.adv

__version__ = "1.2.4"


def about_dialog(parent):
    license_text = """
    Copyright (C) 10se1ucgo 2016

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>."""

    about_info = wx.adv.AboutDialogInfo()
    about_info.SetName("pyjam")
    about_info.SetVersion("v{v}".format(v=__version__))
    about_info.SetCopyright("Copyright (C) 10se1ucgo 2016")
    about_info.SetDescription("An open source, cross-platform audio player for Source and GoldSrc engine based games.")
    about_info.SetWebSite("https://github.com/10se1ucgo/pyjam", "GitHub repository")
    about_info.AddDeveloper("10se1ucgo")
    about_info.AddDeveloper("Dx724")
    about_info.AddArtist("Dx724 - Icon")
    about_info.SetLicense(license_text)
    wx.adv.AboutBox(about_info, parent)


class Licenses(wx.Dialog):
    def __init__(self, parent):
        super(Licenses, self).__init__(parent, title="Licenses", style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.scrolled_panel = sp.ScrolledPanel(self)

        mono_font = wx.Font()
        mono_font.SetFamily(wx.FONTFAMILY_TELETYPE)

        info = wx.StaticText(self.scrolled_panel, label=("pyjam uses a number of open source software. The following "
                                                         "are the licenses for these software."))

        wxw = wx.StaticText(self.scrolled_panel, label=("pyjam uses wxWidgets and wxPython. Their licenses are below\n"
                                                        "More info at https://www.wxwidgets.org/about/"))
        wxw_license = """
                  wxWindows Library Licence, Version 3.1
                  ======================================

    Copyright (c) 1998-2005 Julian Smart, Robert Roebling et al

    Everyone is permitted to copy and distribute verbatim copies
    of this licence document, but changing it is not allowed.

                         WXWINDOWS LIBRARY LICENCE
       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

    This library is free software; you can redistribute it and/or modify it
    under the terms of the GNU Library General Public Licence as published by
    the Free Software Foundation; either version 2 of the Licence, or (at your
    option) any later version.

    This library is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
    Licence for more details.

    You should have received a copy of the GNU Library General Public Licence
    along with this software, usually in a file named COPYING.LIB.  If not,
    write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
    Floor, Boston, MA 02110-1301 USA.

    EXCEPTION NOTICE

    1. As a special exception, the copyright holders of this library give
    permission for additional uses of the text contained in this release of the
    library as licenced under the wxWindows Library Licence, applying either
    version 3.1 of the Licence, or (at your option) any later version of the
    Licence as published by the copyright holders of version 3.1 of the Licence
    document.

    2. The exception is that you may use, copy, link, modify and distribute
    under your own terms, binary object code versions of works based on the
    Library.

    3. If you copy code from files distributed under the terms of the GNU
    General Public Licence or the GNU Library General Public Licence into a
    copy of this library, as this licence permits, the exception does not apply
    to the code that you add in this way.  To avoid misleading anyone as to the
    status of such modified files, you must delete this exception notice from
    such code and/or adjust the licensing conditions notice accordingly.

    4. If you write modifications of your own for this library, it is your
    choice whether to permit this exception to apply to your modifications.  If
    you do not wish that, you must delete the exception notice from such code
    and/or adjust the licensing conditions notice accordingly."""
        wxw_text = wx.StaticText(self.scrolled_panel, label=wxw_license)
        wxw_text.SetFont(mono_font)

        seven = wx.StaticText(self.scrolled_panel, label=("pyjam bundles 7-zip Extra in binary form. "
                                                          "Its license is below.\n"
                                                          "Downloads and source: http://www.7zip.org"))
        seven_license = """
    7-Zip Extra
    ~~~~~~~~~~~
    License for use and distribution
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Copyright (C) 1999-2015 Igor Pavlov.

    7-Zip Extra files are under the GNU LGPL license.


    Notes:
    You can use 7-Zip Extra on any computer, including a computer in a commercial
    organization. You don't need to register or pay for 7-Zip.


    GNU LGPL information
    --------------------

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    Lesser General Public License for more details.

    You can receive a copy of the GNU Lesser General Public License from
    http://www.gnu.org/"""
        seven_text = wx.StaticText(self.scrolled_panel, label=seven_license)
        seven_text.SetFont(mono_font)

        ffmpeg = wx.StaticText(self.scrolled_panel, label=("pyjam uses FFmpeg in binary form. A note and "
                                                           "license info is below."))
        ffmpeg_info = """
    NOTE
    ----

    FFmpeg <https://ffmpeg.org> is downloaded upon the user's request (not bundled due to size).
    You can download binaries, including source and instructions, from https://ffmpeg.zeranoe.com/
    Builds from https://ffmpeg.zeranoe.com/ are licensed under the GNU GPL 3.0

    GNU GPL information
    -------------------

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>."""
        ffmpeg_text = wx.StaticText(self.scrolled_panel, label=ffmpeg_info)
        ffmpeg_text.SetFont(mono_font)

        yt_dl_text = wx.StaticText(self.scrolled_panel, label=("pyjam also uses youtube-dl. youtube-dl is released "
                                                               "under public domain"))

        meme_text = wx.StaticText(self.scrolled_panel, label=("Special 'drop dead' to my best friends s1zZLe && xioner "
                                                              "for their support and care <3"))

        self.top_sizer = wx.BoxSizer(wx.VERTICAL)
        self.scroll_sizer = wx.BoxSizer(wx.VERTICAL)

        self.scroll_sizer.Add(info, 0, wx.ALL, 2)
        self.scroll_sizer.Add(wxw, 0, wx.ALL, 2)
        self.scroll_sizer.Add(wxw_text, 0, wx.EXPAND | wx.ALL, 3)
        self.scroll_sizer.Add(seven, 0, wx.ALL, 2)
        self.scroll_sizer.Add(seven_text, 0, wx.EXPAND | wx.ALL, 3)
        self.scroll_sizer.Add(ffmpeg, 0, wx.ALL, 2)
        self.scroll_sizer.Add(ffmpeg_text, 0, wx.EXPAND | wx.ALL, 3)
        self.scroll_sizer.Add(yt_dl_text, 0, wx.ALL, 2)
        self.scroll_sizer.Add(meme_text, 0, wx.ALL, 2)
        self.top_sizer.Add(self.scrolled_panel, 1, wx.EXPAND)

        self.SetSizerAndFit(self.top_sizer)
        self.scrolled_panel.SetSizerAndFit(self.scroll_sizer)
        self.scrolled_panel.SetupScrolling()
        self.Show()
