from PIL import Image, ImageDraw


def human(background_color: str, color_n: tuple, machtab: int, thick: int):
    img = Image.new("RGB", (16 * machtab, 21 * machtab), background_color)
    drawer = ImageDraw.Draw(img)

    drawer.ellipse(((6 * machtab, 1 * machtab), (10 * machtab, 5 * machtab)), 
                   outline=color_n, width=thick)
    drawer.ellipse(((7 * machtab - machtab // 5, 3 * machtab - machtab // 5), 
                    (7 * machtab + machtab // 5, 3 * machtab + machtab // 5)), color_n, width=thick)
    drawer.ellipse(((9 * machtab - machtab // 5, 3 * machtab - machtab // 5), 
                    (9 * machtab + machtab // 5, 3 * machtab + machtab // 5)), color_n, width=thick)
    drawer.ellipse(((7 * machtab - machtab // 5, 6 * machtab - machtab // 5), 
                    (7 * machtab + machtab // 5, 6 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((9 * machtab - machtab // 5, 6 * machtab - machtab // 5), 
                    (9 * machtab + machtab // 5, 6 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((4 * machtab - machtab // 5, 10 * machtab - machtab // 5), 
                    (4 * machtab + machtab // 5, 10 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((12 * machtab - machtab // 5, 10 * machtab - machtab // 5), 
                    (12 * machtab + machtab // 5, 10 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)    
    drawer.ellipse(((11 * machtab - machtab // 5, 10 * machtab - machtab // 5), 
                    (11 * machtab + machtab // 5, 10 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)    
    drawer.ellipse(((8 * machtab - machtab // 5, 11 * machtab - machtab // 5), 
                    (8 * machtab + machtab // 5, 11 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((6 * machtab - machtab // 5, 15 * machtab - machtab // 5), 
                    (6 * machtab + machtab // 5, 15 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((13 * machtab - machtab // 5, 15 * machtab - machtab // 5), 
                    (13 * machtab + machtab // 5, 15 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    drawer.ellipse(((5 * machtab - machtab // 5, 20 * machtab - machtab // 5), 
                    (5 * machtab + machtab // 5, 20 * machtab + machtab // 5)), 
                    outline=color_n, width=thick)
    
    drawer.arc((6 * machtab, 1 * machtab - machtab // 2, 10 * machtab, 5 * machtab - machtab // 2), 
               45, 45 + 90, width=thick, fill=color_n)

    drawer.line(((4 * machtab, 10 * machtab), (6 * machtab, 13 * machtab)), fill=color_n, width=thick)
    drawer.line(((4 * machtab, 10 * machtab), (7 * machtab, 6 * machtab)), fill=color_n, width=thick)
    drawer.line(((7 * machtab, 6 * machtab), (9 * machtab, 6 * machtab)), fill=color_n, width=thick)
    drawer.line(((9 * machtab, 6 * machtab), (12 * machtab, 10 * machtab)), fill=color_n, width=thick)
    drawer.line(((12 * machtab, 10 * machtab), (15 * machtab, 7 * machtab)), fill=color_n, width=thick)
    drawer.line(((8 * machtab, 5 * machtab), (8 * machtab, 11 * machtab)), fill=color_n, width=thick)
    drawer.line(((8 * machtab, 11 * machtab), (11 * machtab, 10 * machtab)), fill=color_n, width=thick)
    drawer.line(((8 * machtab, 11 * machtab), (6 * machtab, 15 * machtab)), fill=color_n, width=thick)
    drawer.line(((6 * machtab, 15 * machtab), (5 * machtab, 20 * machtab)), fill=color_n, width=thick)
    drawer.line(((5 * machtab, 20 * machtab), (7 * machtab, 20 * machtab)), fill=color_n, width=thick)
    drawer.line(((11 * machtab, 10 * machtab), (13 * machtab, 15 * machtab)), fill=color_n, width=thick)
    drawer.line(((13 * machtab, 15 * machtab), (15 * machtab, 14 * machtab)), fill=color_n, width=thick)
    
    img.save("human.png")

human('#00fAdc', (200, 0, 0), 50, 7)