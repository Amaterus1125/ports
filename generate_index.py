import json
import os
import yaml

recipes_dir = "./recipes"
index = []

print("Crawling recipes directory...")
for filename in os.listdir(recipes_dir):
    if filename.endswith((".yml", ".yaml")):
        filepath = os.path.join(recipes_dir, filename)
        with open(filepath, "r") as f:
            try:
                data = yaml.safe_load(f)
                # Fallbacks in case a recipe is poorly written
                pkg_name = data.get("name", filename.rsplit(".", 1)[0])
                pkg_ver = str(data.get("version", "0.0.0"))
                pkg_desc = data.get("description", "No description provided.")

                index.append(
                    {
                        "name": pkg_name,
                        "version": pkg_ver,
                        "description": pkg_desc,
                    }
                )
                print(f"  -> Indexed: {pkg_name} ({pkg_ver})")
            except Exception as e:
                print(f"❌ Failed to parse {filename}: {e}")

# Save to the root of the repo
with open("index.json", "w") as out:
    json.dump(index, out, indent=2)

print(f"\n Success! index.json generated with {len(index)} packages.")
