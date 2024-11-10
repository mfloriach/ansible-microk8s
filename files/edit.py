import yaml
import argparse  

parser = argparse.ArgumentParser(description='Parse and edit kube config') 

parser.add_argument('--ip', help="Hostname IP address", required=True) 
parser.add_argument('--kube_config', help="Kube config path", required=True)   
args = parser.parse_args()   

with open(args.kube_config, 'r') as f:
    valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
    valuesYaml['clusters'][0]["cluster"]["server"] = "https://"+args.ip+":16443"
    
with open(args.kube_config, 'w') as yaml_file:
    yaml_file.write( yaml.dump(valuesYaml, default_flow_style=False))