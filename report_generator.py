from datetime import datetime

def create_markdown_report(sector, analysis):

    report = f"""
# Trade Opportunity Report

# Sector: {sector}

# Generated: {datetime.now()}

{analysis}
"""

    return report