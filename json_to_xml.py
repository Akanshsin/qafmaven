import xml.etree.ElementTree as ET
import json
import time

def convert_result_to_junit_status(result):
    if result == "pass":
        return "passed"
    elif result == "fail":
        return "failed"
    elif result == "skip":
        return "skipped"
    else:
        return "unknown"

def convert_to_junit_xml(json_file, output_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    methods = json_data.get("methods", [])
    if not methods:
        raise ValueError("No methods found in JSON data")

    testsuite = ET.Element("testsuite")
    testsuite.set("name", "com.qmetry.qaf.automation.step.client.Scenario")
    testsuite.set("tests", str(len(methods)))

    total_duration = sum(method.get("duration", 0) for method in methods)
    testsuite.set("time", str(total_duration / 1000.0))  # Convert total duration to seconds

    # Extract timestamp from startTime field in epoch format
    timestamp_epoch = methods[0].get("startTime", 0)
    timestamp = time.strftime("%d %b %Y %H:%M:%S GMT", time.gmtime(timestamp_epoch / 1000))
    testsuite.set("timestamp", timestamp)

    hostname = json_data.get("hostname", "Unknown Hostname")
    testsuite.set("hostname", hostname)

    failures = len([method for method in methods if method.get("result") == "fail"])
    testsuite.set("failures", str(failures))

    errors = len([method for method in methods if method.get("result") == "error"])
    testsuite.set("errors", str(errors))

    skipped = len([method for method in methods if method.get("result") == "skip"])
    testsuite.set("skipped", str(skipped))

    for method in methods:
        testcase = ET.SubElement(testsuite, "testcase")
        testcase.set("name", method.get("metaData", {}).get("name", "UnknownTest"))
        testcase.set("time", str(method.get("duration", 0) / 1000.0))  # Convert duration to seconds
        testcase.set("classname", "com.qmetry.qaf.automation.step.client.Scenario")

        result_status = convert_result_to_junit_status(method.get("result"))
        if result_status != "passed":
            skipped_element = ET.SubElement(testcase, "skipped")

    tree = ET.ElementTree(testsuite)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    json_file = "test-results/25_Apr_2024_02_03_PM/json/QAFDemo/BDDTest/scenarios/suite1.feature/meta-info.json"  # Change this to the path of your JSON file
    output_file = "junit_output.xml"
    convert_to_junit_xml(json_file, output_file)
    print(f"JUnit XML file '{output_file}' created successfully.")
