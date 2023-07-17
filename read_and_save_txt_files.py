import os

def read_txt_files_and_save():
    folder_path = os.getcwd()  # Get the current working directory
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    if not txt_files:
        print("No .txt files found in the current folder.")
        return

    combined_output = ''
    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            combined_output += f"Content of {file_name}:\n{content}\n-----------------------\n"

    output_file = os.path.join(folder_path, 'output.txt')
    with open(output_file, 'w') as output:
        output.write(combined_output)

if __name__ == "__main__":
    read_txt_files_and_save()
