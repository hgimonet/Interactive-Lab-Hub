# cli.py
import click
import i2c_LCD_driver
from time import *

mylcd = i2c_LCD_driver.lcd()


@click.command()
@click.option('text','t')
@click.option('--clear', '-c', default=False)
def main(text, clear):
    # click.echo("This is a CLI built with Click ✨")

    if text:
        mylcd.lcd_display_string(text, 1)

    if clear:
        mylcd.lcd_clear()

if __name__ == "__main__":
    main()