"""Verify DOIs and fetch metadata/abstract/affiliations.
Usage: py lit.py dois.txt out.json   (one DOI per line; '#' comments allowed)
Sources: Crossref (metadata, affiliations, sometimes abstract), Semantic Scholar batch (abstract, citations, affiliations).
"""
import json, re, sys, time, urllib.request, urllib.parse, html

UA = {"User-Agent": "lit-review-script/0.1 (academic use)"}

def get(url, data=None, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={**UA, **({"Content-Type": "application/json"} if data else {})})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            err = e
            time.sleep(3 * (k + 1))
    return {"_error": str(err)}

def clean(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

def crossref(doi):
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if "_error" in d:
        return {"cr_error": d["_error"]}
    m = d["message"]
    auth = m.get("author", [])
    affs = []
    for a in auth:
        for af in a.get("affiliation", []):
            n = af.get("name", "")
            if n and n not in affs:
                affs.append(n)
    yr = (m.get("published-print") or m.get("published-online") or m.get("issued") or {}).get("date-parts", [[None]])[0][0]
    return {
        "doi": m.get("DOI"),
        "title": clean((m.get("title") or [""])[0]),
        "first_author": (auth[0].get("family", "") + ", " + auth[0].get("given", "")) if auth else "",
        "last_author": (auth[-1].get("family", "") + ", " + auth[-1].get("given", "")) if auth else "",
        "n_auth": len(auth),
        "year": yr,
        "journal": (m.get("container-title") or [""])[0],
        "type": m.get("type"),
        "cr_affs": affs[:12],
        "cr_abstract": clean(m.get("abstract", ""))[:3000],
        "refs": m.get("reference-count"),
        "cited_cr": m.get("is-referenced-by-count"),
    }

def s2_batch(dois):
    out = {}
    for i in range(0, len(dois), 100):
        chunk = dois[i:i + 100]
        body = json.dumps({"ids": ["DOI:" + x for x in chunk]}).encode()
        d = get("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,abstract,tldr,citationCount,authors.affiliations,authors.name,externalIds", data=body)
        if isinstance(d, dict) and "_error" in d:
            for x in chunk:
                out[x.lower()] = {"s2_error": d["_error"]}
            continue
        for x, p in zip(chunk, d):
            if not p:
                out[x.lower()] = {}
                continue
            affs = []
            for a in p.get("authors") or []:
                for af in a.get("affiliations") or []:
                    if af not in affs:
                        affs.append(af)
            out[x.lower()] = {
                "s2_abstract": clean(p.get("abstract") or "")[:3000],
                "tldr": (p.get("tldr") or {}).get("text", "") if p.get("tldr") else "",
                "cited_s2": p.get("citationCount"),
                "s2_affs": affs[:12],
            }
        time.sleep(2)
    return out

if __name__ == "__main__":
    dois = [l.split("#")[0].strip() for l in open(sys.argv[1], encoding="utf-8")]
    dois = [x for x in dois if x]
    s2 = s2_batch(dois)
    res = []
    for x in dois:
        r = {"query_doi": x, **crossref(x), **s2.get(x.lower(), {})}
        res.append(r)
        time.sleep(0.3)
    json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in res:
        print(r.get("query_doi"), "|", r.get("year"), "|", r.get("first_author"), "|", r.get("journal"), "|", (r.get("title") or r.get("cr_error", ""))[:70],
              "| abs:", "CR" if r.get("cr_abstract") else "-", "S2" if r.get("s2_abstract") else "-", "| affs:", len(r.get("cr_affs", [])), len(r.get("s2_affs", [])))
