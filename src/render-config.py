from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("Usage: python render-config.py <Ubuntu/WSL2>")
    sys.exit(1)

# Access the command-line variables
os_conf_type = sys.argv[1]

config_files = []

# Ubuntu telegraf templates
if os_conf_type == "Ubuntu":
    config_files = [
            "Ubuntu/docker-compose.yml",
            "Ubuntu/conf/telegraf/telegraf.conf"
            ]

# Unsure if WSL2 is tested
if os_conf_type == "WSL2":
    config_files = [
            "Windows-WSL2/docker-compose.yml",
            "Windows-WSL2/conf/telegraf/telegraf.conf"
            ]

with open('config.yml', 'r') as file:
    loaded_config = yaml.safe_load(file)

jinja_env = Environment(loader=FileSystemLoader("templates/"))

# Iterate over each configuration file
for file_name in config_files:
    template = jinja_env.get_template(file_name)
    rendered_content = template.render(loaded_config)

    file_dest_path = Path(file_name)
    file_dest_path.parent.mkdir(exist_ok=True, parents=True)
    file_dest_path.write_text(rendered_content)
