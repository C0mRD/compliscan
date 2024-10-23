import os

# Define the folder structure
folder_structure = {
    'backend': {
        'app': {
            'api': {
                'endpoints': ['compliance.py', 'organizations.py', 'policies.py', 'reports.py', 'standards.py'],
            },
            'core': ['auth.py', 'config.py', 'logging.py'],
            'models': ['database.py', 'schemas.py'],
            'services': ['compliance_service.py', 'vector_service.py', 'ml_service.py'],
            'workers': ['compliance_worker.py', 'document_worker.py'],
            'tests': {
                'api': [],
                'services': [],
                'workers': [],
            },
            'Dockerfile': None,
            'Dockerfile.worker': None,
            'requirements.txt': None,
        }
    },
    'frontend': {
        'components': {
            'Dashboard': None,
            'Compliance': None,
            'Reports': None,
            'Settings': None,
        },
        'pages': None,
        'public': None,
        'styles': None,
        'Dockerfile': None,
        'package.json': None,
    },
    'k8s': {
        'backend': None,
        'frontend': None,
        'databases': None,
    },
    'terraform': ['main.tf', 'variables.tf', 'outputs.tf'],
    '.github': {
        'workflows': None,
    },
    'docker-compose.yml': None,
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        # Construct the full path
        path = os.path.join(base_path, name)

        if isinstance(content, list):
            # If it's a list, create files
            for file_name in content:
                file_path = os.path.join(path, file_name)
                # Ensure the directory exists before creating the file
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                if not os.path.exists(file_path):
                    open(file_path, 'a').close()  # Create an empty file
                    print(f"Created file: {file_path}")
        elif isinstance(content, dict):
            # If it's a dictionary, create the directory and recurse
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)
        else:
            # If it's neither, assume it's a file name
            if not os.path.exists(path):
                open(path, 'a').close()  # Create an empty file
                print(f"Created file: {path}")

# Set the base path where you want to create the structure
base_path = '.'
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Create the folder structure
create_structure(base_path, folder_structure)
