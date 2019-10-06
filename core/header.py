from core import info
from core import colors
from core.moduleop import count

arissploit = r"""

            .----.   @   @                  
           / .-.-.`.  \v/                            
           | | '\ \ \_/ )                      
          ,-\ `-.' /.'  /           
          '---`----'----'    
"""

def print_info():
	count()

	print("\t" + colors.bold + "Arissploit Framework\n" + colors.end)
	print("\t" + colors.bold + "Core "+colors.end+"\t[ "+info.version+" "+info.codename+" ]" + colors.end)
	print("\t" + colors.bold + "API"+colors.end+"\t[ "+info.apiversion+" ]"+colors.end)
	print("\t" + colors.bold + "Date"+colors.end+"\t[ "+info.update_date+" ]"+colors.end)
	print("\t" + colors.bold + "Modules "+colors.end+"[ "+count.mod+" modules"+" ]"+colors.end)
	print("\n")
