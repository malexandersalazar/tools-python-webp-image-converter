# WebP Image Converter

![alt text](/images/cover.png "WebP Image Converter")

A tool to convert to JPG or PNG all WebP files located in a folder.

## Installation

Just copy the `wic.py` script located in the dist folder.

## Getting Started

The default behaviour of the script will generate the images in JPEG format with the same file name and location of the target folder.

> python wic.py -t="C:\Users\AlexanderS\Downloads\WebPFolder"

We can also specify a format by setting the `-f` parameter with `png` or `jpeg`.

> python wic.py -t="C:\Users\AlexanderS\Downloads\WebPFolder" -f=png 

## Prerequisites

* Python (>= 3.8.5)
* PIL (>= 9.2.0)

## License

This project is licenced under the [MIT License][1].

[1]: https://opensource.org/licenses/mit-license.html "The MIT License | Open Source Initiative"