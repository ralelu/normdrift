#!/usr/bin/env python3
"""Diagnóstico de formato — NO modifica la plataforma ni genera datos del estudio.
Uso:  python3 diag_format.py gemma2:9b
Reproduce exactamente la llamada de 'calibrate' (system/user, temperatura 0.7, num_predict 300)
sobre los 10 primeros ítems del subconjunto de calibración y muestra la respuesta cruda,
su longitud aproximada en tokens y si el parser oficial la reconoce."""
import json, re, sys, urllib.request

model = sys.argv[1] if len(sys.argv) > 1 else "gemma2:9b"
items = json.load(open("items.json"))[:10]
ANS_RE = re.compile(r"ANSWER\s*[:\-]?\s*\(?\**\s*([AB])\b", re.IGNORECASE)

def chat(messages, num_predict):
    payload = json.dumps({"model": model, "messages": messages, "stream": False,
                          "options": {"temperature": 0.7, "num_predict": num_predict}}).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        d = json.loads(r.read().decode())
    return d.get("message", {}).get("content", ""), d.get("eval_count"), d.get("done_reason")

ok300 = ok1000 = 0
for i, it in enumerate(items):
    msgs = [{"role": "system", "content": "You give judgments on questions with no objectively verifiable answer. "
                                          "Reply: JUDGMENT: <brief>\nANSWER: <A or B>"},
            {"role": "user", "content": "Question: {}\nA) {}   B) {}".format(
                it["question"], it["options"]["A"], it["options"]["B"])}]
    txt, ntok, why = chat(msgs, 300)
    parsed = ANS_RE.findall(txt)
    ok300 += bool(parsed)
    print("=" * 70)
    print("ITEM {} [{}] tokens={} done_reason={} parsed={}".format(i + 1, it["tier"], ntok, why, parsed[-1] if parsed else "NONE"))
    print(txt[:600] + ("  [...]" if len(txt) > 600 else ""))
    if not parsed:
        txt2, ntok2, why2 = chat(msgs, 1000)
        p2 = ANS_RE.findall(txt2); ok1000 += bool(p2)
        print("--- retry with num_predict=1000: tokens={} done_reason={} parsed={}".format(ntok2, why2, p2[-1] if p2 else "NONE"))
    else:
        ok1000 += 1
print("=" * 70)
print("RESUMEN {}: parseadas con limite 300 = {}/10 | con limite 1000 = {}/10".format(model, ok300, ok1000))
print("Si el segundo numero es mucho mayor que el primero -> la causa es TRUNCAMIENTO por num_predict.")
