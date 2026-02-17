def classify_intent(message: str) -> str:
    text = message.lower()
    if any(k in text for k in ["login", "log in", "password", "otp", "signin", "sign in"]):
        return "login"
    if any(k in text for k in ["course", "enroll", "enrol", "access", "content", "module"]):
        return "course"
    if any(k in text for k in ["certificate", "cert", "completion", "badge"]):
        return "certificate"
    return "other"


def handle_login_issue(message: str) -> str:
    return (
        "Login help:\n"
        "1) Confirm your username and password are correct.\n"
        "2) Try resetting your password and login again.\n"
        "3) If OTP is not received, wait 2 minutes and request a new OTP."
    )


def handle_course_issue(message: str) -> str:
    return (
        "Course access help:\n"
        "1) Ensure you are enrolled in the course.\n"
        "2) Sign out and sign back in, then try again.\n"
        "3) Try opening the course in a new browser tab."
    )


def handle_certificate_issue(message: str) -> str:
    return (
        "Certificate help:\n"
        "1) Check that the course is marked as completed.\n"
        "2) Refresh the course page and look under Certificates.\n"
        "3) If it still doesn't appear, wait a few minutes and retry."
    )
