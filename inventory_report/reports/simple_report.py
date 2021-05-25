from inventory_report.reports.utils import ReportsUtils


class SimpleReport:
    @classmethod
    def generate(cls, report_list):
        oldest = ReportsUtils.get_oldest(report_list)
        next_to_expire = ReportsUtils.get_next_to_expire(report_list)
        largest = ReportsUtils.get_largest_stock(report_list)
        simple_report = (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {next_to_expire}\n"
            f"Empresa com maior quantidade de produtos estocados: {largest}\n"
        )
        return simple_report
