import os
import shutil
import datetime as dt
import subprocess as sp
import PyInstaller.__main__ # pylint: disable=unresolved-import

def main():
    shutil.rmtree('./build')
    shutil.rmtree('./dist')
    shutil.rmtree('./release')
    dist = {
        'Chrome81': ('chromedriver81.exe', 'chromedriver.exe'),
        'Chrome83': ('chromedriver83.exe', 'chromedriver.exe'),
        'Chrome84': ('chromedriver84.exe', 'chromedriver.exe'),
        'Firefox26': ('geckodriver26.exe', 'geckodriver.exe'),
    }
    date = dt.datetime.now().strftime('%Y%m%d')

    os.makedirs('./release', exist_ok=True)
    PyInstaller.__main__.run(['--onefile', '--clean', 'main.py'])
    for d in dist:
        out_subdir = f'TranslationImprover_{d}_{date}'
        out_dir = os.path.join('./dist', out_subdir)
        os.makedirs(out_dir, exist_ok=True)
        shutil.copy('./dist/main.exe', os.path.join(f'{out_dir}', 'main.exe'))
        shutil.copy(os.path.join('./bin', dist[d][0]), os.path.join(out_dir, dist[d][1]))
        sp.call(['7z', 'a', f'./release/{out_subdir}.zip', out_dir])

if __name__ == '__main__':
    main()
