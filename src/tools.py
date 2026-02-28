from typing import Optional
import uuid

# ========== REGISTRATION ISSUES ==========

def registration_unable_tool(email: str) -> str:
    """User is unable to register on the platform. Provide this when they face general registration failure."""
    return (
        "Registration Issue: Unable to register.\n"
        "Please ensure:\n"
        "• You are using a valid government email\n"
        "• Parichay authentication is successful\n"
        "• Try again after clearing browser cache"
    )

def registration_email_exists_tool(email: str) -> str:
    """Use this when a user gets 'email already exists' during registration. Requires the email address."""
    return (
        f"The email **{email}** is already registered.\n"
        "Please try logging in instead or use the 'Forgot Password' option."
    )

def registration_parichay_error_tool() -> str:
    """Use this when a Parichay error occurs during registration."""
    return (
        "Parichay Registration Error detected.\n"
        "Please ensure:\n"
        "• Aadhaar is linked correctly\n"
        "• Parichay services are accessible\n"
        "• Try again after some time"
    )

# ========== LOGIN ISSUES ==========

def login_unable_tool(user_id: Optional[str] = None) -> str:
    """Use this when a user is unable to login to their account."""
    return (
        "Login failed.\n"
        "Please verify your credentials and try again.\n"
        "If the issue persists, reset your password."
    )

def login_otp_not_received_tool(email: str) -> str:
    """Use this when a user reports they have not received their login OTP. Requires the email."""
    return (
        f"OTP not received for **{email}**.\n"
        "Please wait 5–10 minutes and retry. Also check your spam/junk folder."
    )

def login_parichay_error_tool() -> str:
    """Use this for Parichay authentication errors during the login process."""
    return (
        "Parichay Login Error.\n"
        "Please retry logging in via Parichay.\n"
        "If the issue persists, Parichay services may be temporarily unavailable."
    )

def login_invalid_credentials_tool() -> str:
    """Use this when the user provided an invalid username or password."""
    return (
        "Invalid credentials.\n"
        "Please use 'Forgot Password' to reset your password."
    )

# ========== COURSE ISSUES ==========

def course_not_visible_tool(course_name: Optional[str] = None) -> str:
    """Use this when a course is not visible after enrollment."""
    return (
        f"Course **{course_name or ''}** is not visible.\n"
        "Please log out and log in again.\n"
        "If still not visible, syncing may be pending."
    )

def course_progress_stuck_tool(course_name: str) -> str:
    """Use this when a user's course progress appears stuck or not moving."""
    return (
        f"Progress for **{course_name}** appears stuck.\n"
        "Please complete all modules fully and refresh the page."
    )

def course_completion_not_updated_tool(course_name: str) -> str:
    """Use this when a course completion status is not updating."""
    return (
        f"Completion not updated for **{course_name}**.\n"
        "Completion sync can take up to 24 hours."
    )

# ========== CERTIFICATE ISSUES ==========

def certificate_not_generated_tool(course_name: str) -> str:
    """Use this when a certificate is not generated after course completion."""
    return (
        f"Certificate not yet generated for **{course_name}**.\n"
        "Certificates are issued within 24 hours after completion."
    )

def certificate_name_incorrect_tool(correct_name: str) -> str:
    """Use this to request a name correction on a certificate. Requires the correct name."""
    return (
        f"Certificate name correction requested.\n"
        f"Correct name: **{correct_name}**.\n"
        "Our team will process this shortly."
    )

def certificate_download_failed_tool() -> str:
    """Use this when a user fails to download their certificate."""
    return (
        "Certificate download failed.\n"
        "Please try using a different browser or device."
    )

# ========== PROFILE & DASHBOARD ISSUES ==========

def profile_not_visible_tool() -> str:
    """Use this when a user's profile is not visible."""
    return (
        "If your profile is not visible:\n"
        "1. Log out and log back in.\n"
        "2. Check if your profile verification is pending.\n"
        "3. Ensure you are logged in with the correct email ID.\n"
        "4. Try clearing browser cache and refreshing the page."
    )

def dashboard_karma_points_missing_tool() -> str:
    """Use this when Karma points are missing from the dashboard."""
    return (
        "Your Karma points are missing from the dashboard.\n"
        "Steps to resolve:\n"
        "1. Karma points sync can take up to 24 hours.\n"
        "2. Refresh the dashboard after some time."
    )

# ========== FINAL ESCALATION ==========

def create_support_ticket(
    email: str, 
    phone_number: str, 
    issue_type: str, 
    issue_description: str
) -> str:
    """
    Creates a support ticket. This is the final escalation step when troubleshooting fails.
    Requires: email, phone_number, issue_type, and issue_description.
    """
    ticket_id = f"IGOT-{uuid.uuid4().hex[:8].upper()}"
    return (
        " Your support request has been successfully recorded.\n\n"
        f"Ticket ID: {ticket_id}\n"
        f"Issue Type: {issue_type}\n\n"
        "Our support team will review this and get back to you."
    )

# List of all tools to be passed to the ADK Agent
TOOLS = [
    registration_unable_tool, registration_email_exists_tool, registration_parichay_error_tool,
    login_unable_tool, login_otp_not_received_tool, login_parichay_error_tool, login_invalid_credentials_tool,
    course_not_visible_tool, course_progress_stuck_tool, course_completion_not_updated_tool,
    certificate_not_generated_tool, certificate_name_incorrect_tool, certificate_download_failed_tool,
    profile_not_visible_tool, dashboard_karma_points_missing_tool, create_support_ticket
]