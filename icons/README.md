### Create png files from the svgs

`find ./ -type f -name "*.svg" -exec inkscape -z -e {}.png -w 512 -h 512 {} \;`

`rename .svg.png .png *.svg.png`

### Cleanup
 - Remove Adobe comment
 - Remove ` style="enable-background:new 0 0 106 106;" xml:space="preserve"`
 - change `id=''` to the full EthOn URI