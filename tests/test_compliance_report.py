import unittest
from report_generation import generate_compliance_report

class TestComplianceReport(unittest.TestCase):
    def test_report_generation(self):
        # ...
        self.assertIn("Compliance Overview", report)
        self.assertTrue(os.path.exists("reports/compliance_overview.png"))
