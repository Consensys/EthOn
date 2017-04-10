### Create png files from the svgs

`find ./ -type f -name "*.svg" -exec inkscape -z -e {}.png -w 512 -h 512 {} \;`

`rename .svg.png .png *.svg.png`