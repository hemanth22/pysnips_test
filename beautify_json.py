import json

def beautify_json(input_file, output_file):
    """
    Beautify a JSON file by formatting it with proper indentation.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to save the beautified JSON file.

    Returns:
        None
    """
    try:
        # Read the input JSON file
        with open(input_file, 'r') as infile:
            data = json.load(infile)
        
        # Write the formatted JSON to the output file
        with open(output_file, 'w') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

        print(f"Beautified JSON has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# beautify_json("input.json", "output.json")
