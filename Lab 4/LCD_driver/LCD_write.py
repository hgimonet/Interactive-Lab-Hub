# cli.py
import click
import i2c_LCD_driver
from time import *

mylcd = i2c_LCD_driver.lcd()


@click.command()
@click.option('--message', '-m')
@click.option('--clear', '-c', default=False)
def main(message, clear):
    # click.echo("This is a CLI built with Click ✨")

    if message:
        mylcd.lcd_display_string(message, 1)

    if clear:
        mylcd.lcd_clear()

if __name__ == "__main__":
    main()