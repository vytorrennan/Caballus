import re
from datetime import datetime

from ..models import AnalysisFile, Sample, Element


def find_pattern_lines(text, pattern):
    match_lines = None

    for line_num, line in enumerate(text.splitlines(), start=1):
        if re.search(pattern, line):
            match_lines = line_num

    return match_lines


p_filename = r"Filename"
p_elements = r"Element"
p_date = r"Date"
p_calibration_mode = r"Calibration Mode"
p_sample_label = r"Sample Label"


def parse_data(content: str):
    content = content.replace("\r\n", "\n")
    analysis_list = []

    analysis_line_blocks = content.split("Analysis\n")[1:]

    for analysis in analysis_line_blocks:
        lines = analysis.split("\n")

        filename = lines[find_pattern_lines(analysis, p_filename) - 1].split("\t")[1]

        # Convert elements string into Element objects
        element_names = (
            lines[find_pattern_lines(analysis, p_elements) - 1]
            .split("\t")[1]
            .strip()
            .split(",")
        )

        element_objects = []
        for element_name in element_names:
            element_name = element_name.strip()
            element_obj, _ = Element.objects.get_or_create(name=element_name)
            element_objects.append(element_obj)

        # Parse date
        date = lines[find_pattern_lines(analysis, p_date) - 1].split("\t")[1]
        date_format = "%a %b %d %H:%M:%S %Y"
        parsed_date = datetime.strptime(date, date_format)

        # Get calibration mode
        calibration_mode = (
            lines[find_pattern_lines(analysis, p_calibration_mode) - 1].split("\t")[1]
            if p_calibration_mode in analysis
            else "Not identified"
        )

        # Process samples
        samples_list = []
        samples_index = find_pattern_lines(analysis, p_sample_label) + 1
        samples_lines = lines[samples_index:]

        for sample in samples_lines:
            fields = sample.split("\t")

            if len(fields) <= 1:
                continue  # Skip empty lines

            try:
                concentration_parsed = fields[1].replace(",", ".")
                concentration_parsed = float(concentration_parsed)
            except:
                concentration_parsed = fields[1]

            try:
                rsd_parsed = fields[2].replace(",", ".")
                rsd_parsed = float(rsd_parsed)
            except:
                rsd_parsed = fields[2]

            try:
                mean_abs_parsed = fields[3].replace(",", ".")
                mean_abs_parsed = float(mean_abs_parsed)
            except:
                mean_abs_parsed = fields[3]

            sample_obj = Sample.objects.create(
                label=fields[0],
                concentration=concentration_parsed,
                rsd_percentage=rsd_parsed,
                mean_abs=mean_abs_parsed,
            )
            samples_list.append(sample_obj)

        if not samples_list:
            continue  # Skip if no samples found

        # Create and save the AnalysisFile
        analysis_obj = AnalysisFile.objects.create(
            filename=filename,
            analysis_date=parsed_date,
            calibration_mode=calibration_mode,
        )

        # Associate elements and samples
        analysis_obj.elements.set(element_objects)
        analysis_obj.samples.set(samples_list)

        analysis_list.append(analysis_obj)

    return analysis_list