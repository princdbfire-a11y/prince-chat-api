"""
College info tool.
Answers questions about the college and about PRINCE itself.
Sourced from https://rjmcc.ac.in/ (official RJMCC website).
EDIT the COLLEGE_DATA dictionary below to keep adding more details (staff names, etc.).
"""

COLLEGE_DATA = {
    "prince": (
        "PRINCE is your college's own AI-powered campus assistant. It can help you "
        "with calculations, writing formal letters, navigating the campus, answering "
        "subject questions, and keeping you updated on college announcements."
    ),
    "founders": (
        "Our college was established in 1997 by Late Padmabhushan Dr. Jacob Cherian "
        "and Late Dr. (Mrs.) Mary Cherian, who were well known for their services to "
        "the local community. With a rare insight, they sought to supplement "
        "healthcare with education.\n\n"
        "In 1999, the President of India awarded Dr. Jacob Cherian the prestigious "
        "title of 'Padma Bhushan' in recognition of his laudable community services. "
        "The two societies he established are the Christian Fellowship Community "
        "Health Centre (CFCHC) and the Christian Education, Health and Development "
        "Society (CEHDS).\n\n"
        "The Cherians revolutionized the world of service and learning by offering "
        "medical and educational services at an affordable cost to severely "
        "disadvantaged groups. Their vision is now carried forward by a body of "
        "erudite academicians, doctors, judges, and corporate leaders.\n\n"
        "Join us in the mission to transform society.\n\n"
        "(These details are officially available on our college website: https://rjmcc.ac.in/our-founders/)"
    ),
    "history": (
        "Rev. Jacob Memorial Christian College (RJMCC), Ambilikkai, Oddanchathram "
        "(Taluk), is an Arts and Science, co-ed college founded in 1997 as the first "
        "self-financed college in Dindigul District. Built on Christian ideals of "
        "peace, goodwill, tolerance and service, the college is committed to "
        "imparting quality education with sound values, developing students into "
        "wholesome, responsible, and employable citizens.\n\n"
        "The college is named after the Founder's father, Rev. K.M. Jacob, who was "
        "recognized in the Guinness Book of Records for his long, outstanding "
        "service as a priest. The Founder, Late Dr. Jacob Cherian (a Padma Bhushan "
        "awardee), and his wife, Late Dr. Mary Cherian, are fondly remembered as "
        "'Ayya and Amma' by the local community for their service in the medical "
        "and educational fields.\n\n"
        "RJMCC is affiliated to Madurai Kamaraj University, recognized by the "
        "Government of Tamil Nadu, and has been granted 2(f) and 12(B) status by "
        "the UGC. It was the first self-financed college to be accredited by NAAC "
        "in 2007, and was reaccredited with a 'B' grade in 2022.\n\n"
        "Set in a serene rural location surrounded by the Palani Hills, about 7 km "
        "from Oddanchathram, the campus is easily accessible by road (Dindigul, "
        "Dharapuram, Coimbatore state highway) or rail. RJMCC is part of a larger "
        "group of institutions that also includes Christian College of Engineering "
        "and Christian Polytechnic College.\n\n"
        "(These details are officially available on our college website: https://rjmcc.ac.in/about-the-college/)"
    ),
    "departments": (
        "RJMCC offers the following UG/PG departments and courses:\n"
        "- Department of Tamil (BA Tamil)\n"
        "- Department of English (BA English, MA English)\n"
        "- Department of Business Administration (BBA - Digital Marketing)\n"
        "- Department of Biochemistry (B.Sc. Biochemistry, M.Sc. Biochemistry)\n"
        "- Department of Computer Science (BCA, B.Sc. CS - Digital Forensic Science "
        "and Cyber Security)\n"
        "- Department of Visual Communications (B.Sc. Visual Communication)\n"
        "- Department of Commerce (B.Com, B.Com CA, B.Com PA, M.Com CA)\n"
        "- Department of Library Science (B.LiSc, Certificate Course in Library and "
        "Information Science)\n\n"
        "There is also a One Year Diploma in Clinical Lab Sciences.\n\n"
        "(These details are officially available on our college website: https://rjmcc.ac.in/)"
    ),
    "staff": (
        "[Replace this with specific staff/HOD names per department. You can find the "
        "official list at https://rjmcc.ac.in/heads-of-departments/ and "
        "https://rjmcc.ac.in/principal/ — send me the names and I'll add them here.]"
    ),
    "contact": (
        "Rev. Jacob Memorial Christian College, Santhipuram, Ambilikkai, "
        "Oddanchatram (Tk), Dindigul (Dt), Tamil Nadu, India.\n"
        "Phone: 04553 249 330 / +91 84895 53839\n"
        "Email: info@rjmcc.ac.in\n\n"
        "(These details are officially available on our college website: https://rjmcc.ac.in/contact/ ) "
    ),
}


def handle_college_info(message: str) -> str:
    text = message.lower()

    if "prince" in text:
        return COLLEGE_DATA["prince"]
    if "founder" in text:
        return COLLEGE_DATA["founders"]
    if "history" in text:
        return COLLEGE_DATA["history"]
    if "department" in text or "course" in text:
        return COLLEGE_DATA["departments"]
    if "staff" in text or "hod" in text or "principal" in text:
        return COLLEGE_DATA["staff"]
    if "contact" in text or "address" in text or "phone" in text:
        return COLLEGE_DATA["contact"]

    return (
        "I can tell you about PRINCE, our founders, our college's history, "
        "departments, staff, or contact details. Could you clarify which one "
        "you'd like to know about?"
    )