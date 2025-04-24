import os

def get_file_names_to_notepad(folder_path, notepad_path):
    """
    Retrieves all file names from a folder and saves them to a Notepad file.

    Args:
        folder_path: The path to the folder.
        notepad_path: The path to the Notepad file.
    """
    try:
        file_names = os.listdir(folder_path)
        with open(notepad_path, "w") as f:
            for name in file_names:
                f.write(name + "\n")
        print(f"File names saved to {notepad_path}")
    except FileNotFoundError:
        print(f"Error: Folder not found at {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
folder_path = "./" # Replace with the actual path
notepad_path = "./filenames.txt" # Replace with the desired path and filename

get_file_names_to_notepad(folder_path, notepad_path)