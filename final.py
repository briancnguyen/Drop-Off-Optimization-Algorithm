from solver import solve_all
import argparse
import os
import sys
import shutil

def copy_outputs(df, output_dir_old, output_dir_new):
    if not os.path.exists(output_dir_new):
        os.makedirs(output_dir_new)
    for file in df['file'].tolist():
        file_code = file.split("/")[1].split('.in')[0]
        shutil.copy2(str(output_dir_old) + str(file_code) + '.out', str(output_dir_new))
        
def merge_best_outputs(ant_file, tsp_file, ant_out_dir, tsp_out_dir, final_out_dir):
    if ant_file and tsp_file:
        ant_data = output_data(ant_file, 'ant')
        tsp_data = output_data(tsp_file, 'tsp')
        merged_tsp_ant = pd.merge(ant_data, tsp_data, left_on='file', right_on='file', suffixes=('_ant', '_tsp'))
        ant_better = merged_tsp_ant[merged_tsp_ant['cost_ant'] < merged_tsp_ant['cost_tsp']]
        tsp_better = merged_tsp_ant[merged_tsp_ant['cost_ant'] >= merged_tsp_ant['cost_tsp']]
        copy_outputs(ant_better, ant_out_dir, final_out_dir)
        copy_outputs(tsp_better, tsp_out_dir, final_out_dir)
    elif tsp_file and not ant_file:
        tsp_data = output_data(tsp_file, 'tsp')
        copy_outputs(tsp_data, tsp_out_dir, final_out_dir)

def final(output_directory):
    print(output_directory)
    solve_all('inputs', 'outputs_ant_50_best', ['ANT', '50'])
    solve_all('inputs', 'outputs_tsp_50_best', ['TSP', '50'])
    solve_all('inputs', 'outputs_tsp_100_best', ['TSP', '100'])
    solve_all('inputs', 'outputs_tsp_200_best', ['TSP', '200'])
    merge_best_outputs('best_ant_50.txt', 'best_tsp_50.txt', 'outputs_ant_50/', 'outputs_tsp_50/', output_directory + '/')
    merge_best_outputs('best_ant_100.txt', 'best_tsp_100.txt', 'outputs_ant_100/', 'outputs_tsp_100/', output_directory + '/')
    merge_best_outputs(None, 'best_tsp_100.txt', None, 'outputs_tsp_200/', output_directory + '/'))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    args = parser.parse_args()
    output_directory = args.output_directory
    final(output_directory)