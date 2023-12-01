import os
import argparse
import subprocess
from time import time

def run_script(script_name, script_nb):
    if script_nb < 10:
        day_name = f'day0{str(script_nb)}.in'
    else:
        day_name = f'day{str(script_nb)}.in'
    if os.path.exists(f'../in/{day_name}'):
        with open(f'../in/{day_name}','r') as day:
            start = time()
            r = subprocess.Popen(
                ['python3', script_name],                               
                stdin=day,
                stdout=subprocess.PIPE,               
                stderr=subprocess.PIPE, 
                text=True
                )
            stdout, errors = r.communicate()
            end = time()
            elapsed = end - start

            if r.returncode != 0:
                err_msg = errors
                print(f'{day_name} error: \n {err_msg}')  

            else:
                output = stdout
                print(elapsed)   
                print(output)
                with open(f'../out/{day_name.replace("in", "out")}', 'w') as out_file:
                    out_file.write(output)



if __name__ == '__main__':
    ap = argparse.ArgumentParser()    
    ap.add_argument("-script", "--script", required=True,
    help="python script to test")
    ap.add_argument("-script_nb", "--script_nb", required=True,
    help="Which test to execute..")
    args = vars(ap.parse_args())

    script_name = args["script"]
    script_nb = int(args['script_nb'])
    run_script(script_name, script_nb)