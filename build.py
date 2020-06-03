#!/usr/bin/env python3
# coding: utf-8
import os
import sys
import shutil
import datetime as dt
import PyInstaller.__main__
from zipfile import ZipFile, ZIP_DEFLATED

def main():
    platform_name = {'win32': 'Windows', 'linux': 'Linux', 'darwin': 'MacOS'}[sys.platform]
    exec_name = 'gti' + ('.exe' if sys.platform == 'win32' else '')

    bin_dir = './bin'
    build_dir = './build'
    dist_dir = './dist/'
    release_dir = './release'
    target_dir = 'GTI'

    shutil.rmtree(build_dir, ignore_errors=True)
    shutil.rmtree(dist_dir, ignore_errors=True)
    os.makedirs(release_dir, exist_ok=True)

    dists = {
        'Chrome81': (f'chromedriver81_{sys.platform}', 'chromedriver'),
        'Chrome83': (f'chromedriver83_{sys.platform}', 'chromedriver'),
        'Chrome84': (f'chromedriver84_{sys.platform}', 'chromedriver'),
        'Firefox26': (f'geckodriver26_{sys.platform}', 'geckodriver'),
    }
    date = dt.datetime.now().strftime('%Y%m%d')

    os.makedirs(dist_dir, exist_ok=True)
    PyInstaller.__main__.run(['--onefile', '--clean', '-i', 'form.ico', '-n', 'gti', 'main.py'])
    for dist in dists:
        release_name = f'GTI_{platform_name}_{dist}_{date}'
        release_path = os.path.join(release_dir, f'{release_name}.zip')
        with ZipFile(release_path, mode='w', compression=ZIP_DEFLATED) as zipfile:
            print(f'Archiving {release_path}')
            exec_path = os.path.join(dist_dir, exec_name)
            driver_bin = os.path.join(bin_dir, dists[dist][0])
            zip_exec_path = os.path.join(target_dir, exec_name)
            zip_driver_path = os.path.join(target_dir, dists[dist][1])
            for src, target in [(exec_path, zip_exec_path), (driver_bin, zip_driver_path)]:
                zipfile.write(src, target)

if __name__ == '__main__':
    main()
