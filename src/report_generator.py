import os
from llm import LLM
class ReportGenerator:
    def __init__(self, llm):
        self.llm = llm

    def generate(self, updates):
        report = "Latest Release Information:\n\n"
        for repo, release in updates.items():
            report += f"Repository: {repo}\n"
            report += f"Latest Version: {release['tag_name']}\n"
            report += f"Release Name: {release['name']}\n"
            report += f"Published at: {release['published_at']}\n"
            report += f"Release Notes:\n{release['body']}\n"
            report += "-" * 40 + "\n"
        return report

    def generate_daily_report(self, markdown_file):
        with open(markdown_file, 'r') as f:
            content = f.read()

        issues = self.parse_section(content, "## Issues")
        pull_requests = self.parse_section(content, "## Pull Requests")

        summary = self.llm.summarize_issues_prs(issues, pull_requests)
        report_filename = markdown_file.replace('.md', '_report.md')

        with open(report_filename, 'w') as f:
            f.write("# Daily Report\n\n")
            f.write(summary)

        print(f"Generated daily report: {report_filename}")

    def parse_section(self, content, section):
        lines = content.split("\n")
        section_lines = []
        capture = False

        for line in lines:
            if line.strip() == section:
                capture = True
                continue
            if capture and line.startswith("##"):
                break
            if capture:
                section_lines.append(line.strip())

        return section_lines
