# cli.py
import click
import i2c_LCD_driver
from time import *

mylcd = i2c_LCD_driver.lcd()


@click.command()
@click.option('--message', '-m')
@click.option('--line', '-l', default=1)
@click.option('--position', '-p', default=0)
@click.option('--clear', '-c', default=False, is_flag=True)
@click.option('--backlight', '-b', default=0)
def main(message, line, position, clear, backlight):
    # click.echo("This is a CLI built with Click ✨")

    mylcd.backlight(backlight)

    if message:
        mylcd.lcd_display_string(message, line, position)

    if clear:
        mylcd.lcd_clear()

if __name__ == "__main__":
    main()
