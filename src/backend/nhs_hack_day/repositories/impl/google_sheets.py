import gspread
from oauth2client.service_account import ServiceAccountCredentials


SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]


def get_google_sheets_client():
    # Add your service account key file here
    creds = ServiceAccountCredentials.from_json_keyfile_name('config/secrets/credentials.json', SCOPE)

    # Authorize the gspread client
    client = gspread.authorize(creds)

    # Open the Google Sheet by name or URL
    spreadsheet = client.open("Ward jobs")  # Or use open_by_url('your_sheet_url')

    # Select the first sheet or use the specific sheet name
    sheet = spreadsheet.sheet1  # or spreadsheet.worksheet("Sheet Name")

    # Get all values in the sheet
    rows = sheet.get_all_values()

    return rows