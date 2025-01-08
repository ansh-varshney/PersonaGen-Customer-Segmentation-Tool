import pickle
import pathlib

# Determine the absolute path of the current script
current_path = pathlib.Path(__file__).resolve().parent

# Construct the path for the pickle file
pickle_file = current_path / 'model.pkl'

# Load the model from the pickle file
with pickle_file.open('rb') as model_file:
    model = pickle.load(model_file)
