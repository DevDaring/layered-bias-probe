"""
Publishing Script for layered-bias-probe

This script helps you publish the package to PyPI.
Run this after updating the version and testing locally.
"""

import subprocess
import sys
import os
import shutil
from datetime import datetime

def run_command(command, description, check=True):
    """Run a command and return success status."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=check, 
                              capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr and not check:
            print(f"Warning: {result.stderr}")
        print(f"✅ {description} completed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def check_requirements():
    """Check if required tools are installed."""
    print("🔍 Checking requirements...")
    
    # Check if build and twine are installed
    try:
        import build
        print("✅ build package is available")
    except ImportError:
        print("❌ build package not found. Installing...")
        run_command(f"{sys.executable} -m pip install build", "Installing build")
    
    try:
        subprocess.run(["twine", "--version"], check=True, capture_output=True)
        print("✅ twine is available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ twine not found. Installing...")
        run_command(f"{sys.executable} -m pip install twine", "Installing twine")

def clean_build():
    """Clean previous build artifacts."""
    print("\n🧹 Cleaning previous builds...")
    
    dirs_to_clean = ["build", "dist", "layered_bias_probe.egg-info"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  Removed {dir_name}/")
    
    print("✅ Build artifacts cleaned!")

def validate_package():
    """Validate package structure."""
    print("\n✅ Validating package structure...")
    
    required_files = [
        "setup.py",
        "requirements.txt",
        "README.md",
        "LICENSE",
        "MANIFEST.in",
        "layered_bias_probe/__init__.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files present!")
    return True

def build_package():
    """Build the package."""
    print("\n🔨 Building package...")
    
    success = run_command(
        f"{sys.executable} -m build",
        "Building wheel and source distribution"
    )
    
    if success and os.path.exists("dist"):
        dist_files = os.listdir("dist")
        print(f"\n📦 Created distribution files:")
        for file in dist_files:
            print(f"  - {file}")
        return True
    
    return False

def check_package():
    """Check the built package."""
    print("\n🔍 Checking package with twine...")
    
    return run_command("twine check dist/*", "Checking package")

def upload_to_testpypi():
    """Upload to TestPyPI for testing."""
    print("\n🧪 Uploading to TestPyPI...")
    print("📝 You'll need to enter your TestPyPI credentials.")
    
    success = run_command(
        "twine upload --repository testpypi dist/*",
        "Uploading to TestPyPI",
        check=False
    )
    
    if success:
        print("\n✅ Package uploaded to TestPyPI!")
        print("🔗 Check: https://test.pypi.org/project/layered-bias-probe/")
        print("\n📥 Test installation with:")
        print("pip install --index-url https://test.pypi.org/simple/ layered-bias-probe")
    
    return success

def upload_to_pypi():
    """Upload to production PyPI."""
    print("\n🚀 Uploading to PyPI...")
    print("📝 You'll need to enter your PyPI credentials.")
    print("⚠️  This will make the package publicly available!")
    
    confirm = input("\nAre you sure you want to upload to PyPI? (yes/no): ")
    if confirm.lower() != 'yes':
        print("❌ Upload cancelled.")
        return False
    
    success = run_command(
        "twine upload dist/*",
        "Uploading to PyPI",
        check=False
    )
    
    if success:
        print("\n🎉 Package uploaded to PyPI!")
        print("🔗 Check: https://pypi.org/project/layered-bias-probe/")
        print("\n📥 Anyone can now install with:")
        print("pip install layered-bias-probe")
    
    return success

def main():
    """Main publishing workflow."""
    print("🚀 layered-bias-probe Publishing Script")
    print("=" * 50)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check current directory
    if not os.path.exists("setup.py"):
        print("❌ setup.py not found. Please run from the package root directory.")
        return False
    
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Step 1: Check requirements
    check_requirements()
    
    # Step 2: Validate package
    if not validate_package():
        return False
    
    # Step 3: Clean previous builds
    clean_build()
    
    # Step 4: Build package
    if not build_package():
        return False
    
    # Step 5: Check package
    if not check_package():
        print("⚠️  Package check failed, but continuing...")
    
    # Step 6: Choose upload option
    print("\n📤 Upload Options:")
    print("1. Upload to TestPyPI (recommended first)")
    print("2. Upload to PyPI (production)")
    print("3. Skip upload")
    
    choice = input("\nChoose option (1/2/3): ").strip()
    
    if choice == "1":
        upload_to_testpypi()
    elif choice == "2":
        upload_to_pypi()
    elif choice == "3":
        print("📦 Package built successfully. Upload skipped.")
    else:
        print("❌ Invalid choice. Upload skipped.")
    
    print(f"\n✅ Publishing workflow completed!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
