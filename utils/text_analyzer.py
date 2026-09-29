import re

PATTERNS = [
    (r"\botp\b", "Requests or mentions an OTP."),
    (r"\bpin\b|\batm\b", "Mentions a PIN or ATM details."),
    (r"\bpassword\b", "Requests or mentions a password."),
    (r"\bpay\b|\bpayment\b|\bfee\b", "Requests a payment or fee."),
    (r"\burgent\b|\bimmediately\b|\btoday\b", "Uses urgency or pressure."),
    (r"\bprize\b|\blottery\b|\breward\b", "Mentions a prize, lottery, or reward."),
    (r"\bkyc\b|\bverify\b|\bsuspend(ed)?\b|\bblocked\b", "Uses account/KYC verification or threat language."),
]

def extract_urls(text):
    return re.findall(r"https?://[^\s<>'\"]+|www\.[^\s<>'\"]+", text)

def heuristic_warnings(text):
    warnings = []
    lower = text.lower()
    for pattern, message in PATTERNS:
        if re.search(pattern, lower):
            warnings.append(message)
    return warnings
