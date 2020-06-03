import os
import shutil
import datetime as dt
import subprocess as sp
import PyInstaller.__main__ # pylint: disable=unresolved-import

def main():
    shutil.rmtree('./build')
    shutil.rmtree('./dist')
    shutil.rmtree('./release')
    dists = {
        'Chrome81': ('chromedriver81_linux', 'chromedriver'),
        'Chrome83': ('chromedriver83_linux', 'chromedriver'),
        'Chrome84': ('chromedriver84_linux', 'chromedriver'),
        'Firefox26': ('geckodriver26_linux', 'geckodriver'),
    }
    date = dt.datetime.now().strftime('%Y%m%d')

    os.makedirs('./release', exist_ok=True)
    PyInstaller.__main__.run(['--onefile', '--clean', 'main.py'])
    for dist in dists:
        out_subdir = f'TranslationImprover_{dist}_{date}'
        out_dir = os.path.join('./dist', out_subdir)
        os.makedirs(out_dir, exist_ok=True)
        shutil.copy('./dist/main', os.path.join(f'{out_dir}', 'main.exe'))
        shutil.copy(os.path.join('./bin', dists[dist][0]), os.path.join(out_dir, dists[dist][1]))
        sp.call(['7z', 'a', f'./release/{out_subdir}.zip', out_dir])

if __name__ == '__main__':
    main()
