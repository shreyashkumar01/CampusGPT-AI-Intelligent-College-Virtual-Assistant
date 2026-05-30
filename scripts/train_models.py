import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / '..' / 'backend'))
from app.services.ml_pipeline import train_models

if __name__ == '__main__':
    sample_file = Path(__file__).resolve().parent.parent / 'data' / 'sample' / 'admissions.csv'
    if not sample_file.exists():
        raise FileNotFoundError('Sample dataset not found.')
    results = train_models(str(sample_file))
    print('Model training results:')
    for model_name, metrics in results.items():
        print(f"{model_name}: {metrics}")
