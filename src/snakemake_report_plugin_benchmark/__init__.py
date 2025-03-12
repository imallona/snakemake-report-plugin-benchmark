from dataclasses import dataclass, field
from typing import Optional

from snakemake_interface_report_plugins.reporter import ReporterBase
from snakemake_interface_report_plugins.settings import ReportSettingsBase

# Raise errors that will not be handled within this plugin but thrown upwards to
# Snakemake and the user as WorkflowError.
from snakemake_interface_common.exceptions import WorkflowError  # noqa: F401


# Optional:
# Define additional settings for your reporter.
# They will occur in the Snakemake CLI as --report-<reporter-name>-<param-name>
# Omit this class if you don't need any.
# Make sure that all defined fields are Optional (or bool) and specify a default value
# of None (or False) or anything else that makes sense in your case.
@dataclass
class ReportSettings(ReportSettingsBase):
    flavour: Optional[int] = field(
        default="long",
        metadata={
            "help": "Report flavor (long, short, html, etc)",
            "env_var": False,
            "required": False,
        },
    )

    name: Optional[int] = field(
        default="report.txt",
        metadata={"help": "Report filename", "env_var": False, "required": False},
    )


# Required:
# Implementation of your reporter
class Reporter(ReporterBase):
    def __post_init__(self):
        # initialize additional attributes
        # Do not overwrite the __init__ method as this is kept in control of the base
        # class in order to simplify the update process.
        # See https://github.com/snakemake/snakemake-interface-report-plugins/snakemake_interface_report_plugins/reporter.py # noqa: E501
        # for attributes of the base class.
        # In particular, the settings of above ReportSettings class are accessible via
        # self.settings.
        print(self.settings.flavour)

    def render(self):
        # Render the report, using attributes of the base class.
        with open(self.settings.name, "w") as fh:
            fh.writelines("hey")
