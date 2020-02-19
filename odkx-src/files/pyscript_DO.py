import digitalocean
import sys

if len(sys.argv) != 4:
    print("Usage: python pyscript [TOKEN] [DESIRED DROPLET NAME] [REGION CODE]")
    quit()	

dtoken = sys.argv[1]
dname = sys.argv[2]
dregion = sys.argv[3]

script = open("cloud_init_DO.yml", "r")
scripttext = script.read()
script.close()

# create a droplet with arguments passed in 
droplet = digitalocean.Droplet(token = dtoken,
								name = dname,
								image = 'ubuntu-18-04-x64',
								region = dregion,
								size_slug = "4gb",
								user_data = scripttext,
								backups = False)
droplet.create()

print("Droplet created! Now log on to DigitalOcean and run the script on our droplet!")

