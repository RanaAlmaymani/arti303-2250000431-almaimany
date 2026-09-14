"""Utilities for cleaning text."""

def clean_name(raw):
    """Clean a name by collapsing spaces and converting to title case."""
    return " ".join(raw.split()).title()
