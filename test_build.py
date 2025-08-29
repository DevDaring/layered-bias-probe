"""
Simple test script to check if package can be built
"""

import os
import sys
import subprocess
import shutil

def test_setup():
    """Test if setup.py works correctly."""
    print("🔍 Testing setup.py...")
    
    try:
        # Test setup.py check
        result = subprocess.run([sys.executable, "setup.py", "check"], 
                              capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("✅ setup.py check passed")
        else:
            print(f"❌ setup.py check failed:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error running setup.py check: {e}")
        return False
    
    return True

def clean_build():
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    
    dirs_to_clean = ["build", "dist", "layered_bias_probe.egg-info"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  Removed {dir_name}/")

def test_build_wheel():
    """Test building wheel package."""
    print("🔨 Testing wheel build...")
    
    try:
        # Try building with setup.py
        result = subprocess.run([sys.executable, "setup.py", "bdist_wheel"], 
                              capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("✅ Wheel build successful with setup.py")
            return True
        else:
            print(f"❌ Wheel build failed with setup.py:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            
            # Try with pip wheel
            print("🔄 Trying with pip wheel...")
            result2 = subprocess.run([sys.executable, "-m", "pip", "wheel", ".", "--no-deps"], 
                                  capture_output=True, text=True, check=False)
            
            if result2.returncode == 0:
                print("✅ Wheel build successful with pip")
                return True
            else:
                print(f"❌ Wheel build failed with pip:")
                print(f"STDOUT: {result2.stdout}")
                print(f"STDERR: {result2.stderr}")
                return False
            
    except Exception as e:
        print(f"❌ Error building wheel: {e}")
        return False

def main():
    """Main test function."""
    print("🚀 Package Build Test")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("setup.py"):
        print("❌ setup.py not found. Please run from package directory.")
        return False
    
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Clean previous builds
    clean_build()
    
    # Test setup.py
    if not test_setup():
        return False
    
    # Test wheel build
    if not test_build_wheel():
        return False
    
    print("\n🎉 All tests passed! Package should build successfully.")
    
    # Show what was created
    if os.path.exists("dist"):
        dist_files = os.listdir("dist")
        print(f"\n📦 Created files:")
        for file in dist_files:
            print(f"  - {file}")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
