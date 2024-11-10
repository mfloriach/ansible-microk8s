import yaml
import argparse 

parser = argparse.ArgumentParser(description='Parse and edit kube config for read only') 

parser.add_argument('--ip', help="Hostname IP address", required=True) 
parser.add_argument('--name', help="Username", required=True) 
parser.add_argument('--kube_config', help="Kube config path", required=True) 
parser.add_argument('--output', help="output path", required=True)   
args = parser.parse_args()   

with open(args.output+"/kube-config-admin", 'r') as f:
    valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
    ca = valuesYaml['clusters'][0]["cluster"]["certificate-authority-data"]

with open(args.kube_config, 'r') as f:
    valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
    
    valuesYaml['clusters'][0]["cluster"]["certificate-authority-data"] = ca
    valuesYaml['clusters'][0]["cluster"]["server"] = "https://"+args.ip+":16443"
    valuesYaml['contexts'][0]['context']['user'] = args.name
    valuesYaml['users'][0]['name'] = args.name
    valuesYaml['users'][0]['user']['client-certificate'] = args.output+"/"+args.name+".crt"
    valuesYaml['users'][0]['user']['client-key'] = args.output+"/"+args.name+".key"
    del valuesYaml['users'][0]['user']['client-certificate-data']
    del valuesYaml['users'][0]['user']['client-key-data']
    
with open(args.output+"/kube-config-"+args.name, 'w') as yaml_file:
    yaml_file.write( yaml.dump(valuesYaml, default_flow_style=False))