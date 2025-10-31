import re
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_threat_report(text: str):
    doc = nlp(text)

    ips = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', text)
    domains = re.findall(r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', text)
    hashes = re.findall(r'\b[a-f0-9]{32,64}\b', text)
    cves = re.findall(r'CVE-\d{4}-\d{4,7}', text)
    orgs = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PERSON"]]

    queries = []
    if domains:
        queries.append(f'index=main ("{" OR ".join(domains)}")')
    if ips:
        queries.append(f'index=main ("{" OR ".join(ips)}")')
    if hashes:
        queries.append(f'index=main ("{" OR ".join(hashes)}")')
    if cves:
        queries.append(f'index=main ("{" OR ".join(cves)}")')
    if orgs:
        queries.append(f'index=main ("{" OR ".join(orgs)}")')

    entities = {
        "domains": domains,
        "ips": ips,
        "hashes": hashes,
        "cves": cves,
        "organizations": orgs,
        "queries": queries
    }
    return entities
