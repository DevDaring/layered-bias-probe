# 📋 Publishing Checklist for layered-bias-probe

## ✅ Pre-Publishing Checklist

### 🔧 Setup Accounts
- [ ] Create PyPI account: https://pypi.org/account/register/
- [ ] Create TestPyPI account: https://test.pypi.org/account/register/
- [ ] Enable 2FA on both accounts
- [ ] Generate API tokens (recommended over passwords)

### 📝 Update Package Information
- [ ] Update `author` and `author_email` in `setup.py`
- [ ] Update `url` with your actual GitHub repository
- [ ] Update version number if needed
- [ ] Review and update `README.md`
- [ ] Ensure `LICENSE` file is correct

### 🛠️ Install Required Tools
```bash
pip install --upgrade pip
pip install --upgrade build twine
```

### 🧪 Test Locally
- [ ] Run `python install_and_test.py` successfully
- [ ] Run `python demo.py` successfully  
- [ ] Test example scripts work correctly
- [ ] Verify CLI works: `python -m layered_bias_probe.cli --help`

## 🚀 Publishing Steps

### 1️⃣ First-Time Setup
```bash
# Navigate to package directory
cd layered-bias-probe

# Verify you're in the right place
ls setup.py  # Should exist
```

### 2️⃣ Build Package
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Check what was created
ls dist/
```

You should see:
- `layered_bias_probe-1.0.0-py3-none-any.whl` (wheel)
- `layered-bias-probe-1.0.0.tar.gz` (source)

### 3️⃣ Check Package Quality
```bash
# Check package with twine
twine check dist/*
```

### 4️⃣ Test on TestPyPI (Recommended)
```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation (in a new environment)
pip install --index-url https://test.pypi.org/simple/ layered-bias-probe

# Test that it works
python -c "from layered_bias_probe import BiasProbe; print('Success!')"
```

### 5️⃣ Upload to Production PyPI
```bash
# Upload to PyPI (FINAL STEP!)
twine upload dist/*
```

### 6️⃣ Verify Public Installation
```bash
# Test public installation
pip install layered-bias-probe

# Verify it works
layered-bias-probe --help
```

## 🎉 Post-Publishing

### 📈 Monitor Your Package
- [ ] Check PyPI page: https://pypi.org/project/layered-bias-probe/
- [ ] Monitor download stats: https://pypistats.org/packages/layered-bias-probe
- [ ] Set up GitHub repository with the same code
- [ ] Add badges to README (PyPI version, downloads, etc.)

### 🔄 For Future Updates
1. Update version number in `setup.py`
2. Document changes in a CHANGELOG.md
3. Clean, build, and upload again
4. Note: You cannot delete or overwrite versions on PyPI

## 🛡️ Security Configuration

### API Token Setup (Recommended)
1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
3. Create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...your-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHl...your-testpypi-token-here
```

## 🚨 Common Issues & Solutions

### Package Name Already Exists
- Choose a different name (e.g., `layered-bias-probe-yourname`)
- Update name in `setup.py`

### Upload Fails
- Check credentials are correct
- Ensure 2FA is set up if required
- Try using API tokens instead of passwords

### Installation Issues
- Check dependencies in `requirements.txt` are correct
- Ensure Python version compatibility is right
- Test in a clean virtual environment

### Large Package Size
- Add files to `.gitignore` and exclude from `MANIFEST.in`
- Remove unnecessary data files
- Consider uploading large models separately

## 📞 Getting Help

- PyPI Help: https://pypi.org/help/
- Packaging Guide: https://packaging.python.org/
- TestPyPI: https://test.pypi.org/
- GitHub Issues: For package-specific problems

---

## 🎯 Quick Command Summary

```bash
# Complete publishing workflow
python publish.py

# Manual workflow
rm -rf build/ dist/ *.egg-info/
python -m build
twine check dist/*
twine upload --repository testpypi dist/*  # Test first
twine upload dist/*                        # Production
```

Good luck with your package! 🚀
