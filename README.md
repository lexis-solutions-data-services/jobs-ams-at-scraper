# AMS Austria Jobs Scraper

![banner](https://i.imgur.com/ldfZdCO.png)

👋 Welcome to the AMS Austria Jobs Scraper! This actor extracts job listings and details from the Austrian public employment service portal (AMS). Use it to collect fresh postings including titles, company info, locations, and structured metadata such as employment relationship, working time, education levels, and more.

<p align="center">
  <img src="https://apify-image-uploads-prod.s3.us-east-1.amazonaws.com/DevbkY3adMTBuoECt-actor-AFMwLCeDTZuLrh4C5-TM52b84cIK-Screenshot_2025-10-07_at_9.59.06.png" alt="Jobs.ams.at Scraper" style="height: 60px; margin-right: 15px;" /><a href="https://apify.com/lexis-solutions/jobs-ams-at-scraper" target="_blank">
    <img src="https://img.shields.io/badge/Try%20it%20on-Apify-0066FF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjQwOCIgdmlld0JveD0iMCAwIDQwOCA0MDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8zNDFfNDE1NykiPgo8cGF0aCBkPSJNMjE4LjY5NSAxMDRIMzAwLjk3QzMwMi42NDMgMTA0IDMwNCAxMDUuMzU3IDMwNCAxMDcuMDNWMjMyLjc2NkMzMDQgMjM1Ljc3OCAzMDAuMDgzIDIzNi45NDUgMjk4LjQzNCAyMzQuNDI1TDIxNi4xNTkgMTA4LjY5QzIxNC44NDEgMTA2LjY3NCAyMTYuMjg3IDEwNCAyMTguNjk1IDEwNFoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xODkuMzA1IDEwNEgxMDcuMDNDMTA1LjM1NyAxMDQgMTA0IDEwNS4zNTcgMTA0IDEwNy4wM1YyMzIuNzY2QzEwNCAyMzUuNzc4IDEwNy45MTcgMjM2Ljk0NSAxMDkuNTY2IDIzNC40MjVMMTkxLjg0IDEwOC42OUMxOTMuMTU5IDEwNi42NzQgMTkxLjcxMyAxMDQgMTg5LjMwNSAxMDRaIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNMjAyLjU5MSAyMDQuNjY4TDEwOS4xMjcgMjk4LjgzNUMxMDcuMjI5IDMwMC43NDcgMTA4LjU4MyAzMDQgMTExLjI3OCAzMDRIMjk2LjhDMjk5LjQ4MyAzMDQgMzAwLjg0MiAzMDAuNzcgMjk4Ljk2NyAyOTguODUyTDIwNi45MDggMjA0LjY4NUMyMDUuNzI2IDIwMy40NzUgMjAzLjc4MiAyMDMuNDY4IDIwMi41OTEgMjA0LjY2OFoiIGZpbGw9IndoaXRlIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMzQxXzQxNTciPgo8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwNCAxMDQpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==&logoColor=white" alt="Try it on Apify" style="border-radius: 12px; height: 60px;" />
  </a>
</p>


## Introduction

## 📊 Actor Stats

| Stat | Value |
|------|-------|
| **Version** | `0.0.1` |
| **Last Update** | Dec 1, 2025 |

---



The AMS scraper crawls the public AMS jobs API endpoints behind the listings and detail pages. It paginates through results and saves a normalized dataset for each job.


## 💻 Integration Examples

This repository includes example code showing how to integrate the `jobs-ams-at-scraper` actor into your projects.

You can find example implementations in the [`examples/`](./examples) folder:
- **TypeScript/JavaScript**: See [`examples/typescript/`](./examples/typescript) for a complete TypeScript example
- **Python**: See [`examples/python/`](./examples/python) for a complete Python example

Each example includes:
- Ready-to-use code templates
- Setup instructions
- Documentation links

---


## Use Cases

- **Job Market Research**: Analyze roles, geographies, and employment types across Austria.
- **Recruitment Enrichment**: Feed ATS/CRMs with structured postings and metadata.
- **Competitor Monitoring**: Track company hiring activity by federal state or municipality.
- **Data Aggregation**: Build dashboards for trends by occupation, green-jobs, or working time.

## Input 📥

Provide any of the following fields:

- `startUrls` (array, optional): Direct list or API URLs to start from. Example: `{ "url": "https://jobs.ams.at/public/api/v1/jobs?query=engineer&state=wien" }`
- `query` (string, optional): Search keyword.
- `location` (string, optional): Human-readable location (e.g., `Wien`, `Klagenfurt`). The scraper will normalize this by taking the first suggestion if available.
- `radius` (string | number, optional): Search radius; only applies if the provided `location` resolves to a valid suggestion.
- `maxItems` (integer, optional): Maximum number of jobs to extract.
- `remoteWork` (boolean, optional): Filter for remote-friendly listings if applicable.
- `proxyConfiguration` (object, optional): Apify proxy configuration. Example: `{ "useApifyProxy": true }`

Notes:

- Either `startUrls` or `query` must be provided.
- The `location` you input will be normalized from the first suggestion when available.
- `radius` takes effect only when the `location` is valid.

Example input:

```json
{
  "query": "sales representative",
  "location": "Klagenfurt",
  "radius": "25",
  "maxItems": 100,
  "proxyConfiguration": { "useApifyProxy": true }
}
```

## Output 📤

Each dataset item contains fields like:

```json
{
  "url": "https://jobs.ams.at/public/emps/jobs/uuid/279a0faf-f84c-3989-b490-a883aade8e41",
  "title": "International Sales Reprsentative (m/w/d) for Europe (Klagenfurt / Remote)",
  "lastUpdatedAt": "2025-09-26T00:00:00Z",
  "companyName": "SET Sustainable Energy Technologies GmbH",
  "companyCountryCode": "AT",
  "companyFederalState": "Kärnten",
  "companyXipCode": "9020",
  "companyMunicipality": "Klagenfurt am Wörthersee",
  "companyTown": "Klagenfurt,15.Bez.:Hörtendorf",
  "companyStreet": "Ernst-Diez-Straße 6",
  "educationLevels": [
    {
      "code": "L*",
      "description": "Lehre/Lehre mit Meisterprüfung",
      "parent": null
    },
    {
      "code": "H*",
      "description": "Matura",
      "parent": null
    },
    {
      "code": "U*",
      "description": "Fachhochschule/Universität/pädagogische Hochschule",
      "parent": null
    }
  ],
  "jobOfferTypeCode": "AMS",
  "jobOfferTypeDescription": "Arbeitsmarktservice",
  "workingTimeCode": "V",
  "workingTimeDescription": "Vollzeit",
  "employmentRelationshipCode": "AA",
  "employmentRelationshipDescription": "ArbeiterInnen/Angestellte",
  "summaryHtml": "<p><br /><span class=\"fw-bold\">HAUPTAUFGABEN:</span><br />*Du unterstützt unseren Vertrieb mit deinem technischen Wissen bei internationalen Projekten in den Geschäftsbereichen Energie, Öl&amp;Gas und Industrie<br />* Du präsentierst unsere Produkte und Lösungen bei Kunden international<br />* Du bist Ansprechpartner/In für kaufmännische Fragen und technische Anfragen<br />* Du erstellst Angebote und begleitest sie bis zum Abschluss...",
  "summary": "HAUPTAUFGABEN: *Du unterstützt unseren Vertrieb mit deinem technischen Wissen bei internationalen Projekten in den Geschäftsbereichen Energie, Öl&Gas und Industrie * Du präsentierst unsere Produkte und Lösungen bei Kunden international * Du bist Ansprechpartner/In für kaufmännische Fragen und technische Anfragen * Du erstellst Angebote und begleitest sie bis zum Abschluss...",
  "occupations": "MaschinenbautechnikerIn; ElektrotechnikerIn für Anlagen- und Betriebstechnik",
  "workingLocationCountryCode": "AT",
  "workingLocationFederalState": "Kärnten",
  "workingLocationXipCode": "9020",
  "workingLocationMunicipality": "Klagenfurt am Wörthersee",
  "workingLocationTown": "Klagenfurt,15.Bez.:Hörtendorf",
  "workingLocationStreet": "Ernst-Diez-Straße 6",
  "isPreselection": false,
  "isBookmarked": null,
  "isGreenJob": true,
  "companyIntroductionHtml": "<p>SET entwickelt und fertigt als global agierendes Technologieunternehmen mit Sitz in Klagenfurt, Österreich unter dem Produktnamen SETCON einergieeffiziente elektro-mechanische Differenzantriebe für große Pumpen- und Kompressor-Antriebe. <br /><br />Zur Verstärkung unseres multidisziplinären Teams suchen wir zum ehest möglichen Eintritt eine(n)</p>",
  "companyIntroduction": "SET entwickelt und fertigt als global agierendes Technologieunternehmen mit Sitz in Klagenfurt, Österreich unter dem Produktnamen SETCON einergieeffiziente elektro-mechanische Differenzantriebe für große Pumpen- und Kompressor-Antriebe. Zur Verstärkung unseres multidisziplinären Teams suchen wir zum ehest möglichen Eintritt eine(n)",
  "generalEqualitiyInfoHtml": "Das Mindestentgelt für die Stelle als International Sales Reprsentative (m/w/d) for Europe (Klagenfurt / Remote) beträgt 65.000,00 EUR brutto pro Jahr auf Basis Vollzeitbeschäftigung. Bereitschaft zur Überzahlung.",
  "generalEqualitiyInfo": "Das Mindestentgelt für die Stelle als International Sales Reprsentative (m/w/d) for Europe (Klagenfurt / Remote) beträgt 65.000,00 EUR brutto pro Jahr auf Basis Vollzeitbeschäftigung. Bereitschaft zur Überzahlung.",
  "availableFrom": "ab sofort",
  "contact": null,
  "occupationExperience": [],
  "accessibility": null,
  "drivingLicence": null,
  "internationalExperience": null,
  "willingnessToTravel": null,
  "qualifications": [],
  "additionalBenefits": null,
  "educations": []
}
```

The scraper paginates list results and stops when there are no more jobs or when `maxItems` is reached.

## Why use the AMS Scraper?

- ⚡️ **Fast**: Uses API-backed pagination for efficiency.
- 🤙 **Easy to use**: Start from URLs or a simple `query` + `location`.
- ☑️ **Reliable**: Built on Apify Actors and Crawlee (Puppeteer).
- 🎯 **Flexible**: Supports location, radius, and max items limits.
- 🔍 **Comprehensive**: Collects key job and company fields from AMS.

## FAQ 💬

- **How many jobs can it extract?**  
  Set `maxItems` to limit results; a high value attempts to fetch all available.

- **What if the website changes?**  
  Site changes may require updates. Please report issues or request updates.

- **Does it support proxies?**  
  Yes. Provide `proxyConfiguration` (e.g., `{ "useApifyProxy": true }`).

## Need to scrape other job platforms?

Check out our other job scrapers on Apify:

- [Jobs.ch Scraper](https://apify.com/lexis-solutions/jobs-ch-scraper)
- [Jobs.cz Scraper](https://apify.com/lexis-solutions/jobs-cz-scraper)
- [VDAB.be Scraper](https://apify.com/lexis-solutions/vdab-be-scraper)
- [Austrian Jobs Scraper](https://apify.com/lexis-solutions/jobs-scraper-12Ycs0PX)

---

👀 **Need help or want a custom solution?**

Lexis Solutions is a certified Apify Partner. We can help with custom data extraction projects.

Contact us over [Email](mailto:scraping@lexis.solutions) or [LinkedIn](https://www.linkedin.com/company/lexis-solutions)

## Support Our Work 💝

If you're happy with our work and scrapers, you're welcome to leave us a company review [here](https://apify.com/partners/find/lexis-solutions/review) and leave a review for the scrapers you're subscribed to. It will take you less than a minute but it will mean a lot to us!
