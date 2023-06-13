import gspread


class GoogleSheets:
    def __init__(self, title, service_account_json_file="key.json"):
        self._client = gspread.service_account(service_account_json_file)
        self._spreadsheet = self._client.open(title)
        self._worksheet = self._spreadsheet.sheet1

    def select_worksheet(self, title):
        self._worksheet = self._spreadsheet.worksheet(title)

    def add_worksheet(self, title, rows, cols):
        self._worksheet = self._spreadsheet.add_worksheet(title, rows, cols)

    def delete_worksheet(self):
        if self._worksheet is self._spreadsheet.sheet1:
            raise RuntimeError("Cannot delete sheet 1")
        self._spreadsheet.del_worksheet(self._worksheet)
        self._worksheet = self._spreadsheet.sheet1

    def set_headers(self, headers=None):
        if not headers:
            raise ValueError("Headers are required")

        self._worksheet.update("A1:Z1", [headers])
        self._worksheet.format("A1:Z1", {
            "backgroundColor": {
                "red": 95,
                "green": 99,
                "blue": 104
            },
            "horizontalAlignment": "CENTER",
            "textFormat": {
                "foregroundColor": {
                    "red": 211,
                    "green": 211,
                    "blue": 211
                },
                "fontSize": 10,
                "bold": True
            }
        })

    def set_records(self, records):
        if not records:
            raise ValueError("Records are required")
        self._worksheet.update("A3", records, value_input_option="USER_ENTERED")

    def clear_records(self):
        self._worksheet.clear()

    def new_spreadsheet(self, title, email):
        self._spreadsheet = self._client.create(title)
        self._spreadsheet.share(email_address=email, perm_type="user", role="writer")
        self._worksheet = self._spreadsheet.sheet1
