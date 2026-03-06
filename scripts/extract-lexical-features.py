import json
import re
import tldextract
from dataclasses import dataclass, asdict
from urllib.parse import urlparse

@dataclass
class LexicalFeatures:
    URL: str
    Label: bool
    URLLength: int | None = None
    IsHTTPS: bool | None = None
    DomainLenght: int | None = None
    TLD: str | None = None
    NumberRatio: float | None = None
    SubDomainCount: int | None = None
    IPAddressExistsInURL: bool | None = None
    Paths: str | None = None
    Parameters: str | None = None

def get_domain_info(url):
    ext = tldextract.extract(url)
    host = ".".join(part for part in [ext.subdomain, ext.domain, ext.suffix] if part)
    return host, ext.suffix, ext.subdomain

def extractLexicalFeatures(inputPath: str, outputPath: str):
    print("Starting extraction...")
    extractedData = []

    ipv4_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
    ipv6_pattern = r"([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}"
    ip_regex = re.compile(f"({ipv4_pattern}|{ipv6_pattern})")

    try:
        with open(inputPath, mode="r") as f:
            raw_data = json.load(f)

        for row in raw_data:
            url = row["URL"]
            parse_url = url if url.lower().startswith(("http://", "https://")) else "http://" + url

            host, tld, subdomain = get_domain_info(url)
            
            try:
                parsed = urlparse(parse_url)
                path = parsed.path or None
                query = f"?{parsed.query}" if parsed.query else None
            except ValueError:
                path = None
                query = None

            feat = LexicalFeatures(
                URL=url,
                Label=row["Label"],
                URLLength=len(url),
                IsHTTPS=url.lower().startswith("https://") if "://" in url else None,
                DomainLenght=len(host),
                TLD=tld,
                NumberRatio=round(sum(c.isdigit() for c in url) / len(url), 2) if url else 0,
                SubDomainCount=len(subdomain.split('.')) if subdomain else 0,
                IPAddressExistsInURL=bool(ip_regex.search(url)),
                Paths=path,
                Parameters=query
            )
            extractedData.append(asdict(feat))

        with open(outputPath, mode="w") as f:
            json.dump(extractedData, f, indent=4)
        print(f"Success! Saved to {outputPath}")

    except Exception as e:
        print(f"Unexpected error: {e}")


extractLexicalFeatures("../datasets/harmonized-data.json", "../datasets/lexical-data.json")