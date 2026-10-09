"""Build the resume PDF from scratch.

Always regenerate the PDF with this script instead of patching the old file.
Overlaying edits on an existing PDF leaves the old text underneath, which ATS
parsers still read.

    pip install reportlab
    python tools/build_resume.py

Writes both assets/Anie_Ajamian_Sr_Product_Designer.pdf (linked from resume.html)
and assets/Anie-Ajamian-Resume.pdf (old URL, kept so existing links work).
Fonts: Karla static TTFs installed in ~/Library/Fonts.
"""
import os
import shutil

from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "Anie_Ajamian_Sr_Product_Designer.pdf")
OUT_OLD_URL = os.path.join(ROOT, "assets", "Anie-Ajamian-Resume.pdf")
FONT_DIR = os.path.expanduser("~/Library/Fonts")

for name in ("Regular", "Italic", "Bold", "ExtraBold"):
    pdfmetrics.registerFont(TTFont(f"Karla-{name}", os.path.join(FONT_DIR, f"Karla-{name}.ttf")))

INK = HexColor("#29282c")
BLUE = HexColor("#0383e6")
BLACK = HexColor("#000000")

PAGE_W, PAGE_H = 612, 792
LEFT, RIGHT = 48, 564
BULLET_X = 63
SEP = "  \u00b7  "

# ---------------------------------------------------------------- content

NAME = "ANIE AJAMIAN"
TITLE = "SENIOR PRODUCT DESIGNER · LOS ANGELES, CA"
CONTACT = [
    ("310.344.0086", None),
    ("aajamian203@gmail.com", "mailto:aajamian203@gmail.com"),
    ("anieajamian.com", "https://anieajamian.com"),
    ("linkedin.com/in/anieajamian", "https://www.linkedin.com/in/anieajamian"),
]
SUMMARY = (
    "Product designer with 15+ years fixing revenue-critical flows in consumer and marketplace "
    "products across hospitality, healthcare, fintech, and e-commerce. Led product strategy and "
    "design for 0 to 1 launches and high-traffic platforms serving millions, focused on growth and "
    "working across many teams and stakeholders."
)

PAGE1_JOBS = [
    ("Wyndham Hotels & Resorts", "Senior UI/UX Designer, Contract", "May 2024 – Present",
     "Global hotel company, booking and loyalty", [
         "Shaped the UX for Wyndham's booking and loyalty replatform across web and mobile with the design director, moving the business off legacy systems so it could ship features faster and add planned AI features",
         "Assigned as design lead for the replatform: delegated flows across a team of 4–6 designers and gave feedback on their work",
         "Redesigned Rooms & Rates, the main booking decision screen. After my first version cut mobile bookings 5% in an A/B test, designed a smaller, usability-tested update and staged bigger changes for post-launch tests",
         "Designed and tested tiered cash-plus-points rate options that increased points bookings by 4%",
         "Worked with product, research, brand leadership, and an outside engineering vendor to decide what shipped and in what order",
     ]),
    ("Joy", "Senior Product Designer", "Oct 2022 – Jul 2023",
     "Wedding website, registry, and gifting marketplace", [
         "Led product design for registry and checkout on Joy's gifting marketplace, making it easier for guests to find, pick, and buy gifts",
         "Rebuilt the cash gift flow so guests could tell when a gift was done and couples could trust it would arrive, cutting purchase-confusion support tickets by 75%",
         "Found where guests got stuck across registry and checkout using behavioral data, prototypes, usability tests, and A/B tests, then shipped UX and messaging fixes",
     ]),
    ("Medly Pharmacy", "Senior Product Designer", "May 2021 – Aug 2022",
     "Digital pharmacy with same-day prescription delivery", [
         "Led product strategy and design for Medly's patient web platform from first research through launch, covering prescription management, checkout, and delivery scheduling",
         "Moved delivery scheduling off the phone and into self-serve checkout, scaling deliveries from 20–30 to 250+ a day across all locations and freeing 65% of patient-support agents' time",
         "Owned product direction through three PMs in one year, working with the engineering lead to keep the roadmap moving between handoffs",
         "Designed patient flows on top of services built by the pharmacy, delivery, and support teams, and reviewed every new flow with compliance to keep it HIPAA compliant",
         "Set up the research approach and ran patient interviews that set roadmap priorities",
         "Built shared components with the iOS team to keep web and native consistent",
     ]),
]

PAGE2_JOBS = [
    ("Contact Systems", "Senior Product Designer", "Sep 2019 – Jul 2020",
     "Web3 marketplace for digital gaming items", [
         "Only designer at the company. Launched Kalorian, a blockchain marketplace where players bought and sold digital gaming items, and owned its product design, UI, and branding",
         "Built the company's first design system",
         "Researched and redesigned inventory and selling so players could browse their full catalog instead of 6 items at a time, and list thousands of items in bulk instead of one by one",
     ]),
    ("Synacor", "UX Designer, promoted to Senior UX Designer", "Sep 2016 – Sep 2019",
     "White-label portal for AT&T's att.net, 45M+ users", [
         "Led UX for AT&T's att.net, an ad-funded news and content portal with 45M+ users and $41M+ a year in ad revenue",
         "Redesigned navigation and content discovery across the portal's main sections, adding a horizontal content nav and testing it through several rounds of live A/B tests",
         "Raised vertical page views 41%, article page views 13%, and dropdown engagement 25%, which meant more ad inventory",
         "Led and mentored 2 designers, and ran critiques on complex projects",
         "Worked with AT&T's product team to balance reader experience against ad revenue goals, and with Synacor's engineers to decide what to test and ship next",
     ]),
    ("Alchemy50", "Designer, promoted to Senior Designer", "Oct 2014 – Sep 2016",
     "Design agency for fintech and financial services clients", [
         "Designed two financial planning tools for advisors: one they used with clients to plan for retirement, a home, or college, and a denser one built for advisors only",
         "Worked on web and mobile apps for financial clients in data research, analytics, and asset management",
         "Designed branding, websites, and marketing materials that helped financial companies explain their services more clearly",
     ]),
]

SKILLS = [
    ("Core Expertise", ["Product strategy", "Conversion optimization", "Checkout and payments",
                            "UX research", "Usability and A/B testing", "Prototyping",
                            "Interaction and visual design", "Design systems",
                            "Native mobile (iOS and Android)"]),
    ("Tools", ["Figma", "Adobe CC", "UserTesting", "Zeroheight", "HTML/CSS"]),
    ("AI", ["Claude Code (built anieajamian.com)", "Claude",
                "Figma AI, for prototyping, research, and front-end builds"]),
]

# ---------------------------------------------------------------- layout


def width(text, font, size):
    return pdfmetrics.stringWidth(text, font, size)


def wrap_items(items, font, size, max_w, first_indent=0):
    """Wrap a dot-separated list, breaking only between items (the dot stays at the line end)."""
    lines, line = [], ""
    for item in items:
        trial = f"{line}{SEP}{item}" if line else item
        avail = max_w - (first_indent if not lines else 0)
        if line and width(trial, font, size) > avail:
            lines.append(line + SEP.rstrip())
            line = item
        else:
            line = trial
    lines.append(line)
    return lines


def wrap(text, font, size, max_w, first_indent=0):
    """Greedy word wrap. first_indent shrinks only the first line."""
    lines, line = [], ""
    for word in text.split(" "):
        trial = f"{line} {word}" if line else word
        avail = max_w - (first_indent if not lines else 0)
        if line and width(trial, font, size) > avail:
            lines.append(line)
            line = word
        else:
            line = trial
    lines.append(line)
    return lines


class Resume:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))
        self.c.setTitle("Anie Ajamian, Senior Product Designer")
        self.c.setAuthor("Anie Ajamian")
        self.c.setSubject("Resume")
        self.y = 0  # baseline, measured from the top of the page

    def runs(self, x, y, parts):
        """Draw one visual line made of (text, font, size, color) runs as a single text object,
        so text extraction reads it as one line."""
        t = self.c.beginText(x, PAGE_H - y)
        for text, font, size, color in parts:
            t.setFont(font, size)
            t.setFillColor(color)
            t.textOut(text)
        self.c.drawText(t)

    def text(self, x, y, s, font="Karla-Regular", size=10, color=INK):
        self.runs(x, y, [(s, font, size, color)])

    def right(self, y, s, font="Karla-Regular", size=10, color=INK):
        self.text(RIGHT - width(s, font, size), y, s, font, size, color)

    def heading(self, label, gap_before):
        self.y += gap_before
        self.text(LEFT, self.y, label, "Karla-ExtraBold", 10)

    def job(self, company, role, dates, desc, bullets, gap_before):
        self.y += gap_before
        self.runs(LEFT, self.y, [(company, "Karla-Bold", 10, BLUE),
                                 ("  |  ", "Karla-Bold", 10, BLUE),
                                 (role, "Karla-Bold", 10, BLACK)])
        self.right(self.y, dates)
        self.y += 16
        self.text(LEFT, self.y, desc, "Karla-Italic", 10)
        gap = 18
        for b in bullets:
            self.y += gap
            self.c.setFillColor(INK)
            self.c.circle(55.3, PAGE_H - (self.y - 2.6), 0.85, stroke=0, fill=1)
            for i, line in enumerate(wrap(b, "Karla-Regular", 10, RIGHT - BULLET_X)):
                if i:
                    self.y += 14
                self.text(BULLET_X, self.y, line)
            gap = 18

    def link(self, x, y, text, url, font, size):
        w = width(text, font, size)
        self.c.linkURL(url, (x, PAGE_H - y - 3, x + w, PAGE_H - y + size), relative=0, thickness=0)

    def page_one(self):
        c = self.c
        self.text(LEFT, 64.2, NAME, "Karla-Bold", 24, BLUE)
        self.text(LEFT, 85, TITLE, "Karla-ExtraBold", 10)
        sep = SEP
        self.text(LEFT, 109.6, sep.join(t for t, _ in CONTACT), "Karla-Regular", 12)
        x = LEFT
        for t, url in CONTACT:
            if url:
                self.link(x, 109.6, t, url, "Karla-Regular", 12)
            x += width(t + sep, "Karla-Regular", 12)
        self.y = 136.6
        for i, line in enumerate(wrap(SUMMARY, "Karla-Regular", 12, RIGHT - LEFT)):
            if i:
                self.y += 16
            self.text(LEFT, self.y, line, "Karla-Regular", 12)
        self.heading("EXPERIENCE", 26.4)
        gap = 22
        for j in PAGE1_JOBS:
            self.job(*j, gap_before=gap)
            gap = 30
        assert self.y < PAGE_H - 36, f"page 1 overflows (last baseline {self.y})"
        c.showPage()

    def page_two(self):
        c = self.c
        self.text(LEFT, 53, NAME, "Karla-ExtraBold", 10, BLUE)
        self.right(53, "PAGE 2", "Karla-ExtraBold", 10)
        self.y = 53
        for j in PAGE2_JOBS:
            self.job(*j, gap_before=30)

        self.y += 30
        self.runs(LEFT, self.y, [
            ("Earlier Experience:  ", "Karla-Bold", 10, INK),
            ("Ogilvy & Mather", "Karla-Bold", 10, BLUE),
            (" (Art Director)  ·  ", "Karla-Regular", 10, INK),
            ("InMotion Hosting", "Karla-Bold", 10, BLUE),
            (" (Graphic/Web Designer)", "Karla-Regular", 10, INK),
        ])
        self.right(self.y, "2011 – 2014")

        self.heading("SKILLS", 30)
        gap = 22
        for label, items in SKILLS:
            self.y += gap
            lead = f"{label}:  "
            lead_w = width(lead, "Karla-Bold", 10)
            lines = wrap_items(items, "Karla-Regular", 10, RIGHT - LEFT, first_indent=lead_w)
            self.runs(LEFT, self.y, [(lead, "Karla-Bold", 10, INK), (lines[0], "Karla-Regular", 10, INK)])
            for line in lines[1:]:
                self.y += 14
                self.text(LEFT, self.y, line)
            gap = 18

        self.heading("EDUCATION", 30)
        self.y += 22
        self.runs(LEFT, self.y, [
            ("California State University, Long Beach", "Karla-Bold", 10, BLUE),
            ("  ·  B.A. Studio Art (Graphic Design), Minor in Marketing", "Karla-Regular", 10, INK),
        ])
        assert self.y < PAGE_H - 36, f"page 2 overflows (last baseline {self.y})"
        c.showPage()

    def save(self):
        self.page_one()
        self.page_two()
        self.c.save()


if __name__ == "__main__":
    Resume(OUT).save()
    shutil.copyfile(OUT, OUT_OLD_URL)
    print(f"wrote {OUT}\nwrote {OUT_OLD_URL}")
