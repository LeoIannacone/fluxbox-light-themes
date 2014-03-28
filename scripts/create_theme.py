#!/usr/bin/python


template  ="""

! about

style.name:             %(name)s
style.author:           Leo Iannacone <l3on@ubuntu.com>
style.date:             Mar 30, 2014
style.license:          GPL-3
style.credits:          http://leoiannacone.com
style.comment:          Based on ubuntu-light themes

! fonts

*.font:                 Ubuntu Light-10
window.*.font:          Ubuntu-10
menu.title.font:        Ubuntu-10
*.textColor:            %(foreground)s

! menu

menu.frame:                         Raised
menu.title:                         Raised
menu.*.color:                       %(menu_color)s
menu.title.justify:                 Center
menu.titleHeight:                   21
menu.itemHeight:                    21
menu.hilite:                        Raised Gradient Vertical
menu.hilite.color:                  %(menu_hilite_color)s
menu.hilite.colorTo:                %(menu_hilite_colorTo)s
menu.hilite.textColor:              %(menu_hilite_foreground)s

! toolbar

toolbar.*.borderWidth:              0
toolbar.height:                     21
toolbar.*.pixmap:                   window_focused.png
toolbar.iconbar.focused.pixmap:     none
toolbar.iconbar.focused:            Sunken Gradient Vertical
toolbar.iconbar.focused.color:      %(toolbar_focus_color)s
toolbar.iconbar.focused.colorTo:    %(toolbar_focus_colorTo)s

! window

window.borderWidth:                 1
window.borderColor:                 %(window_border_color)s
window.title.height:                25
window.roundCorners:                TopLeft TopRight
window.label.*.pixmap:              window_focused.png
window.label.unfocus.pixmap:        window_unfocused.png
window.handleWidth:                 2
window.handle.*:                    Flat
window.handle.*.color:              %(window_border_color)s
window.grip.*:                      Flat
window.grip.*.color:                %(window_border_color)s

! buttons

window.maximize.pixmap:             maximize.png
window.maximize.pressed.pixmap:     maximize_focused_pressed.png
window.maximize.unfocus.pixmap:     maximize_unfocused.png
window.iconify.pixmap:              minimize.png
window.iconify.pressed.pixmap:      minimize_focused_pressed.png
window.iconify.unfocus.pixmap:      minimize_unfocused.png
window.close.pixmap:                close.png
window.close.pressed.pixmap:        close_focused_pressed.png
window.close.unfocus.pixmap:        close_unfocused.png
"""


ambiance = {}
ambiance["name"]                     = 'Ambiance'
ambiance["foreground"]               = '#FFFFFF'
ambiance["window_border_color"]      = '#3c3b37'
ambiance["menu_color"]               = '#43423e'
ambiance["menu_hilite_color"]        = '#fd845d'
ambiance["menu_hilite_colorTo"]      = '#e9673e'
ambiance["menu_hilite_foreground"]   = '#FFFFF'
ambiance["toolbar_focus_color"]      = '#373633'
ambiance["toolbar_focus_colorTo"]    = '#2b2b2a'

##########

radiance = {}
radiance["name"]                     = 'Radiance'
radiance["foreground"]               = '#404040'
radiance["window_border_color"]      = '#baac9f'
radiance["menu_color"]               = '#eee9e4'
radiance["menu_hilite_color"]        = '#f88759'
radiance["menu_hilite_colorTo"]      = '#e56936'
radiance["menu_hilite_foreground"]   = '#FFFFFF'
radiance["toolbar_focus_color"]      = '#e0d9d1'
radiance["toolbar_focus_colorTo"]    = '#d9d0c7'




def make_theme(name, args):
    with open("%s/theme.cfg" % name, 'w') as theme:
        theme.write(template % args)

make_theme('Ambiance', ambiance)
make_theme('Radiance', radiance)
