def on_forever():
    basic.show_string("RASTO")
    basic.show_icon(IconNames.GHOST)
    basic.show_icon(IconNames.GHOST)
    basic.pause(3000)
    basic.show_icon(IconNames.GIRAFFE)
basic.forever(on_forever)
