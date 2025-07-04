import os

def read_last_lines(file_path: str, num_lines: int = 50):
    if not os.path.isfile(file_path):
        return {"error": f"File not found: {file_path}"}

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return {
                "file": file_path,
                "last_lines": lines[-num_lines:]
            }
    except Exception as e:
        return {"error": str(e)}