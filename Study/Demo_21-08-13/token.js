function i() {
            var r = ''
            for (var t = Math.round((new Date).getTime() / 1e3).toString(), e = arguments.length, r = new Array(e), i = 0; i < e; i++)
                r[i] = arguments[i];
            r.push(t);
            var o = n.SHA1(r.join(",")).toString(n.enc.Hex)
            , c = n.enc.Base64.stringify(n.enc.Utf8.parse([o, t].join(",")));
            return c
       }
function c(t) {
    if (r[t])
        return r[t].exports;
    var n = r[t] = {
        i: t,
        l: !1,
        exports: {}
    };
    return e[t].call(n.exports, n, n.exports, c),
    n.l = !0,
    n.exports
}