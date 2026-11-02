from django.shortcuts import render

# ---------- DATA ----------

HOTLINES = [
    {"name": "Emergency (Police/Ambulance)", "number": "999",
     "note": "Immediate danger. 24 hours."},
    {"name": "Talian Kasih (JKM)", "number": "15999",
     "note": "Counselling and referral. WhatsApp: 019-261 5999."},
    {"name": "WAO Hotline", "number": "03-3000 8858",
     "note": "Women's Aid Organisation. WhatsApp: 018-988 8058."},
    {"name": "Befrienders KL", "number": "03-7627 2929",
     "note": "Emotional support, 24 hours."},
]

ENFORCERS = [
    {"agency": "Royal Malaysia Police (PDRM) - D11",
     "role": "Receives reports, investigates, arrests offenders.",
     "how": "Go to any police station or call 999."},
    {"agency": "Department of Social Welfare (JKM)",
     "role": "Protection Officers, shelters, counselling, Interim Protection Orders.",
     "how": "Call Talian Kasih 15999 or visit the nearest JKM office."},
    {"agency": "Hospital One-Stop Crisis Centre (OSCC)",
     "role": "Medical care, forensic examination, police and welfare referral.",
     "how": "Go to the Emergency Department of a government hospital."},
    {"agency": "Courts",
     "role": "Issues Protection Orders and prosecutes offenders.",
     "how": "Through police, JKM, or a lawyer / legal aid."},
]

LAWS = [
    {"name": "Domestic Violence Act 1994 (Act 521)",
     "desc": "Protects family members from domestic violence; allows Protection Orders and Interim Protection Orders."},
    {"name": "Penal Code (Act 574)",
     "desc": "Criminal offences such as hurt, assault, rape and criminal intimidation."},
    {"name": "Sexual Offences Against Children Act 2017",
     "desc": "Protects minors from sexual offences."},
    {"name": "Anti-Sexual Harassment Act 2022 (Act 840)",
     "desc": "Provides redress through the Tribunal for Anti-Sexual Harassment."},
]


# ---------- VIEWS (controller actions) ----------

def home(request):
    # Hantar 2 hotline pertama sahaja untuk laman utama
    return render(request, 'support/home.html', {"hotlines": HOTLINES[:2]})


def what_is(request):
    return render(request, 'support/what_is.html')


def contact(request):
    sent = False
    if request.method == 'POST':
        # Demo sahaja. Projek sebenar akan simpan dalam database atau hantar email.
        name = request.POST.get('name')
        sent = True
    return render(request, 'support/contact.html', {"sent": sent})


def law_enforcement(request):
    return render(request, 'support/law_enforcement.html', {"laws": LAWS})


def enforcer(request):
    return render(request, 'support/enforcer.html', {"enforcers": ENFORCERS})


def hotline(request):
    return render(request, 'support/hotline.html', {"hotlines": HOTLINES})

def message(request):
    return render(request, 'support/message.html')