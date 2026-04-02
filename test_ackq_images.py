"""
Test: convert ACKQ DOCX files with Docling and extract figures as PNG files.

Images in DOCX are stored as base64 data URIs inside the DoclingDocument —
REFERENCED mode requires pre-existing file URIs so it produces only placeholders.
Instead: export markdown with PLACEHOLDER mode, then replace each placeholder in
order with a saved PNG reference built from doc.pictures[i].get_image().
"""

from pathlib import Path

from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode

RAW_DIR = Path("/home/rafael/data/vista-docs/raw/ACKQ")
OUT_DIR = Path("/home/rafael/data/vista-docs/markdown-image/ackq")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SKIP_PREFIXES = ("SF", "VBA")
PLACEHOLDER = "<!-- image -->"

converter = DocumentConverter()

docx_files = sorted(RAW_DIR.glob("*.docx"))
print(f"found {len(docx_files)} docx files in {RAW_DIR}")

for docx in docx_files:
    if any(docx.name.startswith(p) for p in SKIP_PREFIXES):
        print(f"  skip (noise): {docx.name}")
        continue

    slug = docx.stem
    md_path = OUT_DIR / f"{slug}.md"
    img_dir = OUT_DIR / f"{slug}_images"

    print(f"converting: {docx.name} ...", end=" ", flush=True)
    try:
        result = converter.convert(str(docx))
        doc = result.document

        # --- save each picture as PNG ---
        img_dir.mkdir(exist_ok=True)
        saved = []  # (rel_path, caption)
        for i, pic in enumerate(doc.pictures):
            img = pic.get_image(doc)
            if img is None:
                saved.append((None, ""))
                continue
            img_filename = f"image-{i:03d}.png"
            img_path = img_dir / img_filename
            img.save(img_path, format="PNG")
            caption = pic.caption_text(doc) or ""
            saved.append((img_dir.name + "/" + img_filename, caption))

        # --- export markdown with placeholders ---
        md = doc.export_to_markdown(
            image_mode=ImageRefMode.PLACEHOLDER,
            image_placeholder=PLACEHOLDER,
        )

        # --- replace placeholders in order ---
        for rel_path, caption in saved:
            if rel_path is None:
                # no image data — leave placeholder
                continue
            alt = caption.replace("\n", " ").strip() or "Figure"
            replacement = f"![{alt}]({rel_path})"
            md = md.replace(PLACEHOLDER, replacement, 1)

        md_path.write_text(md, encoding="utf-8")

        n_saved = sum(1 for p, _ in saved if p is not None)
        n_no_data = sum(1 for p, _ in saved if p is None)
        print(f"ok  ({n_saved} images saved, {n_no_data} no-data, {len(md):,} chars)")

    except Exception as e:
        import traceback

        print(f"ERROR: {e}")
        traceback.print_exc()

print("\ndone.")
