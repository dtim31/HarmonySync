import json
import HarmonySync

json_structure = {
    "app_path": str(HarmonySync.app_path),
    "app_version": HarmonySync.app_version,
    "profiles": [],
    "settings": {}
}
save_data = open(HarmonySync.app_path + "/save_data.json", "w")

save_data.write(json.dumps(json_structure, indent=3))
save_data.close()

