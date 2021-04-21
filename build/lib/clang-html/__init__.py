import sys
import argparse
import urllib.request
import re
from bs4 import BeautifulSoup
# You can also import custom clang checks from checks.py below.
# from checks import checks_list

# Each check will have its own node of information.
class checks:
    def __init__(self, dataval=None):
        self.name = ''
        self.count = 0
        self.data = ''

# Begin here.
def main():
    find_checks_list()
    checks_list.sort()

    # Updates the newest clang-tidy checks to your checks.py file.
    write_checks_file()

    # Process command line arguments.
    args = parse_command_line_options()
    external_link = ''
    external_name = ''
    if (args.button):
        external_link = input("What is the full link address?\n")
        external_name = input("What would you like to name the button to this link?\n")

    contents = args.file.readlines()

    checks_used = [0] * len(checks_list)

    # Increments each occurrence of a check.
    for line, content in enumerate(contents):
        content = content.replace('<', '&lt;')
        content = content.replace('>', '&gt;')
        for check_name in checks_list:
            if content.find(check_name) != -1:
                checks_used[checks_list.index(check_name)] += 1

    # Counts the max number of used checks in the log file.
    num_used_checks = 0
    for line, check in enumerate(checks_list):
        if checks_used[line] != 0:
            num_used_checks += 1

    names_of_used = [None] * num_used_checks
    names_of_usedL = [None] * num_used_checks

    # Creates new check classes for each used check.
    used_line = 0
    total_num_checks = 0
    for line, check in enumerate(checks_list):
        if checks_used[line] != 0:
            new_node = checks(check)
            new_node.name = check
            new_node.count = checks_used[line]
            total_num_checks += checks_used[line]
            names_of_used[used_line] = new_node

            names_of_usedL[used_line] = checks_list[line]
            used_line += 1

    # Adds details for each organized check.
    for line, content in enumerate(contents):
        # Goes through each used check.
        for initial_check in names_of_usedL:
            # Adds the lines that detail the warning message.
            if content.find(initial_check) != -1:
                content = content.replace('<', '&lt;')
                content = content.replace('>', '&gt;')
                names_of_used[names_of_usedL.index(
                    initial_check)].data += content
                details = line + 1
                finished = False
                while not finished:
                    # Ensure there is no overflow.
                    if details >= len(contents):
                        break
                    # If the line includes a used Clang-Tidy check name,
                    # continue to find the next.
                    for end_check in names_of_usedL:
                        if contents[details].find(end_check) != -1:
                            finished = True
                            break
                    # Otherwise, add the data to the specific used check
                    # name for the organization of checks in the HTML file.
                    if not finished:
                        names_of_used[names_of_usedL.index(
                            initial_check)].data += contents[details]
                        details += 1

    args.file.close()
    f = open("clang.html", "w")
    
    # Functions for writing to the clang.html file.
    writeHeader(f)
    writeList(f, num_used_checks, names_of_used, args,
              external_link, external_name, total_num_checks)
    sortLogs(f, contents, num_used_checks, names_of_used,
             args, external_link, external_name)
    writeScript(f, num_used_checks)

    # Close the file.
    f.close()
    sys.exit()

# Scrape data from clang-tidy's official list of current checks.
def find_checks_list():
    url = 'http://clang.llvm.org/extra/clang-tidy/checks/list.html'
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, "lxml")

    scrape_checks_list = []
    for link in soup.find_all('a', href=True):
        check = re.match("^([a-zA-Z0-9].*).html.*$", link['href'])
        if check:
            scrape_checks_list.append("[" + check.group(1) + "]")

    global checks_list
    checks_list = list(dict.fromkeys(scrape_checks_list))

# Optional: Update the checks.py file with the most recent checks.
def write_checks_file():
    with open('checks.py', 'w') as f:
        f.write('checks_list = [')
        for check, item in enumerate(checks_list):
            if check == len(checks_list) - 1:
                f.write("'{}']".format(item))
            else:
                f.write("'{}',".format(item))

# Parses through the given command line options (-b, --button)
# and returns the given file's contents if read successfully.
def parse_command_line_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--button', action='store_true')
    parser.add_argument('file', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        usage()
        sys.exit()

    return args

# Prints usage information for the script.
def usage():
    print("""
***------------------------------------------ Clang HTML Visualizer -----------------------------------------***

    Generates an html file as a visual for clang-tidy checks. Additionally, it writes a checks.py file that
    informs you which checks have been scraped from http://clang.llvm.org/extra/clang-tidy/checks/list.html

    Arguments: python -m clang-html [logfile.log]

    Options:
        '-b', '--button': External link button for the html page. Asks for a hyperlink and name.
            -ex: python -m clang-html -b [logfile.log]
    
***----------------------------------------------------------------------------------------------------------***""")

# Header of the clang.html file.
def writeHeader(f):
    f.write("""
<!DOCTYPE html>
<html>
<head>
	<title>Clang-Tidy Visualizer</title>
	<meta charset="UTF-8">
	<meta name="author" content="Austin Hale">
	<meta name="description" content="Documentation tool for visualizing Clang-Tidy checks.">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
""")

# List the used checks found in the source code.
def writeList(f, num_used_checks, names_of_used, args, external_link, external_name, total_num_checks):
    f.write("""
<body style="background: rgb(220, 227, 230); width: 100%; height: 100%;">
    <div id="container" style="margin-left: 2%; margin-right: 2%;">
	    <div id="header" style="height: 55px; display: flex; justify-content: left; position: relative;">
		    <h3 style="text-align: center; color: #111; font-family: 'Helvetica Neue', sans-serif; font-weight: bold;     letter-spacing: 0.5px; line-height: 1;">Clang-Tidy Checks</h3>
		    <div class="btn-group" role="group" style="position: absolute; right: 0;">
			    <button type="button" class="btn btn-warning" onclick="highlightChecks(0)" style="outline: none; color: black">Warning</button>
			    <button type="button" class="btn btn-danger" onclick="highlightChecks(1)" style="outline: none; color: black">Danger</button>
			    <button type="button" class="btn btn-info" onclick="clearChecks()" style="outline: none; color: black">Clear All</button>
		    </div>
	    </div>
        <br>
	    <ul id="list" class="list-group" align="left" style="display: block; width: 25%; height: 0; margin-bottom: 0;">
""")

    # Iterates through each used check's details and organizes them into the given <pre> sections.
    f.write("""
            <a id=\"log\" href=\"#\" class=\"list-group-item list-group-item-success\" style=\"color: black; font-weight: bold; letter-spacing:0.4px;\"onclick=\"toggleLog()\">
                {} Original Log
            </a>
""".format(total_num_checks))

    for line in range(0, num_used_checks):
        f.write("""
            <a id=\"check{0}\" style=\"color: black\" href=\"#\" class=\"list-group-item list-group-item-action\"onclick=\"toggleInfo({0})\">
                {1} {2}
            </a>
""".format(line, names_of_used[line].count, names_of_used[line].name))

    f.write("""
        </ul>
        
        <div id="showLog" style="display: none; width: 75%; float: right;">
            <div style="display: flex; justify-content: left; position: relative;">
                <button id="collapse-btn0" type="button" class="btn nohover" onclick="collapseSidebar()" style="outline: none; background-color: lightgray" title="Collapse sidebar">
                <span id="collapse-img0" class="glyphicon glyphicon-menu-left"></button></span>
                <h4 style="margin-top: 0; color: #111; position: absolute; left: 50%; transform: translateX(-50%); margin-bottom: 10;">Original Log</h4>
""")

    # Insert the user-specified link for the button argument. Link opens in a new tab.
    if (args.button):
        f.write("""
                <button id=\"externalLink\" type=\"button\" class=\"btn\" onclick=\"window.open('{}','_blank')\"
                            style=\"outline: none; position: absolute; color: #111; right: 0; background-color: rgb(181, 215, 247)\">
                    {} 
                    <span class=\"glyphicon glyphicon-new-window\">
                </button></span>
""".format(external_link, external_name))

    f.write("""
            </div>
            <pre>
""")

# Sort through the used check logs for outputting the html.
def sortLogs(f, contents, num_used_checks, names_of_used, args, external_link, external_name):
    for line in contents:
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        f.write("{}".format(line))

    f.write("""
            </pre>
        </div>
""")

    for check_idx in range(0, num_used_checks):
        collapse_idx = check_idx + 1
        f.write("""
        <div id=\"show{0}\" style=\"display: none; width: 75%; float: right\">
            <div style=\"display: flex; justify-content: left; position: relative;\">
                <button id=\"collapse-btn{1}\" type=\"button\" class=\"btn nohover\" onclick=\"collapseSidebar()\"
                            style=\"outline: none; background-color: lightgray\" title=\"Collapse sidebar\">
                <span id=\"collapse-img{1}\" class=\"glyphicon glyphicon-menu-left\"></button></span>
                <h4 style=\"margin-top: 0; color: #111; position: absolute; left: 50%; transform: translateX(-50%); margin-bottom: 10px;\">
                    {2}
                </h4>
""".format(check_idx, collapse_idx, names_of_used[check_idx].name[1:-1]))

        if (args.button):
            f.write("""
                <button id=\"externalLink\" type=\"button\" class=\"btn\" onclick=\"window.open('{}','_blank')\"
                        style=\"outline: none; position: absolute; color: #111; right: 0; background-color: rgb(181, 215, 247)\">
                    {} 
                    <span class=\"glyphicon glyphicon-new-window\">
                </button></span>
""".format(external_link, external_name))

        f.write("""
            </div>
            <pre>
""")

        names_of_used[check_idx].data = names_of_used[check_idx].data.replace('<', '&lt;')
        names_of_used[check_idx].data = names_of_used[check_idx].data.replace('>', '&gt;')

        f.write("""
{}
            </pre>
        </div>
""".format(names_of_used[check_idx].data))

    f.write("""
    </div>
</body>
""")

# Writes Javascript and JQuery code to the html file for button and grouping functionalities.
def writeScript(f, num_used_checks):
    f.write("""
<script>
	var selected_idx;
	var checks_arr = [];
	var highlights = 'highlights';
	// Retrieves local storage data on document load for highlighted checks.
	$(document).ready(function () {{
		for (var all_checks = 0; all_checks < {0}; all_checks++) {{
			var check_hl = document.getElementById("check" + all_checks);
			switch (JSON.parse(localStorage.getItem(highlights))[all_checks]) {{
				case "warning":
					check_hl.classList.add('list-group-item-warning');
					checks_arr[all_checks] = "warning"; break;
				case "danger":
					check_hl.classList.add('list-group-item-danger');
					checks_arr[all_checks] = "danger"; break;
				default:
					checks_arr[all_checks] = "action";
					if (check_hl !== null) {{
						check_hl.classList.add('list-group-item-action');
					}} break;
			}}
		}}
		localStorage.setItem(highlights, JSON.stringify(checks_arr));
	}});

	function toggleLog() {{
		var log = document.getElementById("showLog");
		clearContent();
		if (log.style.display === "none") {{
			log.style.display = "block";
		}} else {{
			log.style.display = "none";
		}}
		selected_idx = undefined;
	}}

	function toggleInfo(check_position) {{
		selected_idx = check_position;
		clearContent();
		// Displays the chosen clang-tidy category.
		var category = document.getElementById("show" + check_position);
		if (category.style.display === "none") {{
			category.style.display = "block";
		}} else {{
			category.style.display = "none";
		}}
	}}

	// Clears document when choosing another selection.
	function clearContent() {{
		for (var all_checks = 0; all_checks < {0}; all_checks++) {{
			var clear = document.getElementById("show" + all_checks);
			if (clear.style.display === "block") {{
				clear.style.display = "none";
			}}
		}}
		var clearLog = document.getElementById("showLog");
		if (clearLog.style.display === "block") {{
			clearLog.style.display = "none";
		}}
	}}

	// Type 1 used for highlighting danger checks and 0 for warnings.
	function highlightChecks(type) {{
		if (selected_idx === undefined) return;
		var check_hl = document.getElementById("check" + selected_idx);
		if (check_hl !== null) {{
			if (check_hl.classList.contains('list-group-item-action')) {{
				check_hl.classList.remove('list-group-item-action');
				type == 1 ? check_hl.classList.add('list-group-item-danger') : check_hl.classList.add('list-group-item-warning');
				type == 1 ? checks_arr[selected_idx] = "danger" : checks_arr[selected_idx] = "warning";
			}} else if (check_hl.classList.contains('list-group-item-warning')) {{
				check_hl.classList.remove('list-group-item-warning');
				type == 1 ? check_hl.classList.add('list-group-item-danger') : check_hl.classList.add('list-group-item-action');
				type == 1 ? checks_arr[selected_idx] = "danger" : checks_arr[selected_idx] = "action";
			}} else {{
				check_hl.classList.remove('list-group-item-danger');
				type == 1 ? check_hl.classList.add('list-group-item-action') : check_hl.classList.add('list-group-item-warning');
				type == 1 ? checks_arr[selected_idx] = "action" : checks_arr[selected_idx] = "warning";
			}}
		}}
		// Sets local storage for each occurrence of a highlighted check.
		localStorage.setItem(highlights, JSON.stringify(checks_arr));
	}}

	function clearChecks(type) {{
		for (var all_checks = 0; all_checks < {0}; all_checks++) {{
			var clear = (document.getElementById("check" + all_checks));
			checks_arr[all_checks] = "action";
			if (clear !== null) {{
				if (clear.classList.contains('list-group-item-warning')) {{
					clear.classList.remove('list-group-item-warning');
				}} else if (clear.classList.contains('list-group-item-danger')) {{
					clear.classList.remove('list-group-item-danger');
				}}
				clear.classList.add('list-group-item-action');
			}}
		}}
		// Restores all checks to unhighlighted state on local storage.
		localStorage.removeItem(highlights);
	}}

	function collapseSidebar() {{
		var list = document.getElementById("list"); var hasExpanded;
		var log_details = document.getElementById("showLog");
		list.style.display === "block" ? hasSidebar = true : hasSidebar = false;
		hasSidebar ? list.style.display = "none" : list.style.display = "block";
		for (var all_checks = 0; all_checks <= {0}; all_checks++) {{
			var collapse_img = document.getElementById("collapse-img" + all_checks);
			var collapse_btn = document.getElementById("collapse-btn" + all_checks);
			var check_details = document.getElementById("show" + all_checks);
			if (collapse_img !== null) {{
				hasSidebar ? collapse_img.classList.remove('glyphicon-menu-left') : collapse_img.classList.remove('glyphicon-menu-right');
				hasSidebar ? collapse_img.classList.add('glyphicon-menu-right') : collapse_img.classList.add('glyphicon-menu-left');
				hasSidebar ? collapse_btn.title = "Expand sidebar" : collapse_btn.title = "Collapse sidebar";
			}}
			if (check_details !== null) {{ hasSidebar ? check_details.style.width = "100%" : check_details.style.width = "75%"; }}
		}}
		hasSidebar ? log_details.style.width = "100%" : log_details.style.width = "75%";
	}}
</script>
<style>
	pre {{
		white-space: pre-wrap;
		word-break: keep-all;
	}}

	#header {{
		border-bottom: 2px solid darkgray
	}}
</style>

</html>
""".format(num_used_checks))