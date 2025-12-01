"""
Example: How to call the jobs-ams-at-scraper actor using Apify API Client

For full documentation of the Apify Client for Python, see: https://docs.apify.com/api/client/python
For full documentation of the actor, see: https://apify.com/lexis-solutions/jobs-ams-at-scraper

Note: This example uses the Apify API Client (apify-client) to call actors from external code.
If you want to create Actors, use the Apify SDK (apify) instead:
https://docs.apify.com/sdk/python/docs/overview/introduction
"""

import os
from apify_client import ApifyClient


def run_actor():
    """Run the jobs-ams-at-scraper actor and retrieve results."""
    # Initialize the ApifyClient with your API token
    # Get your API token from https://console.apify.com/account/integrations
    client = ApifyClient(token=os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

    # Start the actor run and wait for it to finish
    # The .call() method starts the actor and waits for completion automatically
    actor_id = "lexis-solutions/jobs-ams-at-scraper"
    print(f"Starting actor: {actor_id}")

    run = client.actor(actor_id).call(
        run_input={
            "startUrls": [{"url":"https://jobs.ams.at/public/emps/jobs?page=3&query=sales&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&sortField=_SCORE"}],
            "maxItems": 10,
            "proxyConfiguration": {"useApifyProxy":False},
        }
    )

    # Get the dataset ID from the completed run
    dataset_id = run["defaultDatasetId"]
    print(f"Actor run completed! Dataset ID: {dataset_id}")

    # Get the results from the dataset
    dataset_items = client.dataset(dataset_id).list_items()
    items = dataset_items.items
    print(f"Retrieved {len(items)} items from the dataset.")
    print("Results:", items)
    return items


if __name__ == "__main__":
    run_actor()
