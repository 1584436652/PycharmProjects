import execjs


def key():
    with open('js_code.js', 'r', encoding='utf8') as f:
        file = f.read()
    ctx = execjs.compile(file)
    result = ctx.call('_0x5e920f', 0)
    print(result)


key()
