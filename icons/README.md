## EthOn icon set
![Some of the icons](overview.jpg)

The above is an excerpt of the icon set. There are some more icons in this folder. 

The icons were designed by @VladTod. Thank you!

Like the rest of EthOn they are licensed CC-BY

[![CC-BY](https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png)](https://creativecommons.org/licenses/by/4.0/)

## Post-processing

### Create png files from the svgs

`find ./ -type f -name "*.svg" -exec inkscape -z -e {}.png -w 512 -h 512 {} \;`

`rename .svg.png .png *.svg.png`

### Cleanup
 - Remove Adobe comment
 - Remove ` style="enable-background:new 0 0 106 106;" xml:space="preserve"`
 - change `id=''` to the full EthOn URI
