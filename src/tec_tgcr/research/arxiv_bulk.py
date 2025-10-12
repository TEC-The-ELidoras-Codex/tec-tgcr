from __future__ import annotations

from typing import Optional

import httpx


ARXIV_PDF_MANIFEST = "https://arxiv.s3.amazonaws.com/pdf/arXiv_pdf_manifest.xml"
ARXIV_SRC_MANIFEST = "https://arxiv.s3.amazonaws.com/src/arXiv_src_manifest.xml"


def fetch_manifest(kind: str = "pdf", client: Optional[httpx.Client] = None) -> str:
    """Fetch arXiv S3 bulk manifest (pdf or src) as XML text.

    Note: These are requester-pays S3 buckets; fetching the manifest is free over HTTPS.
    """
    url = ARXIV_PDF_MANIFEST if kind == "pdf" else ARXIV_SRC_MANIFEST
    cl = client or httpx.Client(timeout=60.0)
    r = cl.get(url)
    r.raise_for_status()
    return r.text
