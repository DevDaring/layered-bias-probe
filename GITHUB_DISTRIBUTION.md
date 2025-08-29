# Alternative: GitHub-Based Distribution

## 🎯 GitHub Installation Method

If you prefer not to use PyPI initially, you can distribute via GitHub:

### Users can install directly from GitHub:
```bash
pip install git+https://github.com/yourusername/layered-bias-probe.git
```

### Or from a specific branch/tag:
```bash
pip install git+https://github.com/yourusername/layered-bias-probe.git@main
pip install git+https://github.com/yourusername/layered-bias-probe.git@v1.0.0
```

## 🔧 GitHub Setup Steps

### 1. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `layered-bias-probe`
3. Description: "Layer-wise bias analysis and fine-tuning for large language models"
4. Set to Public
5. Add README, .gitignore (Python), MIT License

### 2. Upload Your Code
```bash
# In your package directory
git init
git add .
git commit -m "Initial commit: layered-bias-probe package"
git branch -M main
git remote add origin https://github.com/yourusername/layered-bias-probe.git
git push -u origin main
```

### 3. Create Releases
1. Go to your repo → Releases → Create a new release
2. Tag version: `v1.0.0`
3. Release title: `v1.0.0 - Initial Release`
4. Describe features
5. Attach built files from `dist/` folder

### 4. Automated PyPI Publishing with GitHub Actions

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: "3.9"
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Add `PYPI_API_TOKEN` to GitHub secrets (Settings → Secrets → Actions).

## 🎯 Conda-Forge (Advanced)

For wider distribution, consider Conda-Forge:
1. First publish to PyPI
2. Submit to conda-forge: https://github.com/conda-forge/staged-recipes

## 📊 Comparison of Methods

| Method | Ease | Reach | Maintenance |
|--------|------|-------|-------------|
| PyPI | Medium | High | Medium |
| GitHub | Easy | Medium | Low |
| Conda-Forge | Hard | High | High |

**Recommendation**: Start with GitHub, then PyPI, then consider Conda-Forge.
