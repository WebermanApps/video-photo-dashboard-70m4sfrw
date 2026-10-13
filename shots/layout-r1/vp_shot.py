import sys
from playwright.sync_api import sync_playwright
url=sys.argv[1];tag=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in [(393,852),(1470,956),(2560,1440)]:
        pg=b.new_page(viewport={'width':w,'height':h});errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(url);pg.wait_for_timeout(800)
        sw=pg.evaluate('document.documentElement.scrollWidth')
        ov=pg.evaluate("[...document.querySelectorAll('.apps,.stats')].map(e=>e.scrollWidth-e.clientWidth)")
        pg.screenshot(path=f'shots/layout-r1/{tag}-{w}.png')
        print(w,'scrollW',sw,'inner',ov,'errs',errs)
    b.close()
